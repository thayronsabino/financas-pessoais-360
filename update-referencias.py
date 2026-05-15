#!/usr/bin/env python3
"""
update-referencias.py — Atualiza automaticamente REFERENCIAS-BRASIL-2026.md
com dados da API pública do Banco Central do Brasil.

Uso:     python update-referencias.py
Requer:  Python 3.8+ e biblioteca 'requests'  →  pip install requests

Automação via GitHub Actions: ver .github/workflows/update-referencias.yml
Automação local (Windows Task Scheduler / cron):
    - Windows: schtasks /create /sc weekly /tn "MordomIA BCB" /tr "python C:\\...\\update-referencias.py"
    - Linux/Mac: crontab -e → 0 8 * * 1 python /path/to/update-referencias.py
"""

import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ Biblioteca 'requests' não encontrada.")
    print("   Execute: pip install requests")
    sys.exit(1)

# ──────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÃO
# ──────────────────────────────────────────────────────────────────────────────

REFS_FILE = Path(__file__).parent / "docs" / "REFERENCIAS-BRASIL-2026.md"
TIMEOUT = 10  # segundos por requisição

# API SGS do Banco Central — séries numéricas, sem autenticação
# Resposta: [{"data": "DD/MM/YYYY", "valor": "X.XX"}]
BCB_SGS = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{serie}/dados/ultimos/1?formato=json"

# API Olinda do Banco Central — taxas por modalidade de crédito
BCB_TAXAS_CREDITO = (
    "https://olinda.bcb.gov.br/olinda/servico/taxaJuros/versao/v2/odata/"
    "TaxasJuros?$top=300&$format=json&$orderby=DataEmissao%20desc"
    "&$select=Modalidade,TaxaJurosMes,TaxaJurosAno,DataEmissao"
)

# Séries SGS a buscar
SERIES_SGS = {
    "selic_meta": 432,   # Selic Meta % a.a. (fixada pelo Copom, base 252)
    "ipca_mes":   433,   # IPCA % a.m. (último mês disponível)
    "cdi_ano":    12,    # CDI % a.a.
    "tr_mes":     226,   # TR % a.m.
    "igpm_mes":   189,   # IGP-M % a.m.
}

# Mapeamento de modalidades de crédito (nome na API → chave interna)
MODALIDADES_MAP = {
    "cartão de crédito - rotativo total":                "rotativo",
    "cartão de crédito - parcelado":                     "parcelado",
    "cheque especial":                                   "cheque_especial",
    "crédito pessoal não consignado":                    "pessoal_nao_consig",
    "crédito consignado - setor privado":                "consignado_privado",
    "crédito consignado - setor público":                "consignado_publico",
    "financiamento imobiliário com taxas de mercado":    "imobiliario_sbpe",
}


# ──────────────────────────────────────────────────────────────────────────────
# FUNÇÕES DE BUSCA
# ──────────────────────────────────────────────────────────────────────────────

def fetch_sgs(serie: int) -> float | None:
    """Busca o último valor de uma série do BCB SGS."""
    try:
        r = requests.get(BCB_SGS.format(serie=serie), timeout=TIMEOUT)
        r.raise_for_status()
        data = r.json()
        if data:
            return float(str(data[-1]["valor"]).replace(",", "."))
    except Exception as e:
        print(f"    ⚠️  Série {serie}: {e}")
    return None


def fetch_taxas_credito() -> dict:
    """Busca taxas de crédito por modalidade via API Olinda do BCB."""
    resultado = {}
    try:
        r = requests.get(BCB_TAXAS_CREDITO, timeout=TIMEOUT)
        r.raise_for_status()
        items = r.json().get("value", [])

        for item in items:
            modalidade_api = (item.get("Modalidade") or "").lower().strip()
            for nome_chave, chave in MODALIDADES_MAP.items():
                if nome_chave in modalidade_api and chave not in resultado:
                    taxa_mes = item.get("TaxaJurosMes")
                    taxa_ano = item.get("TaxaJurosAno")
                    if taxa_mes is not None:
                        resultado[chave] = {
                            "mes": float(taxa_mes),
                            "ano": float(taxa_ano) if taxa_ano else None,
                        }
    except Exception as e:
        print(f"    ⚠️  API Olinda (taxas crédito): {e}")
    return resultado


# ──────────────────────────────────────────────────────────────────────────────
# FUNÇÕES DE ATUALIZAÇÃO DO MARKDOWN
# ──────────────────────────────────────────────────────────────────────────────

def substituir(padrao: str, substituto: str, conteudo: str) -> tuple[str, bool]:
    """Aplica substituição regex e retorna (conteudo, houve_mudanca)."""
    novo = re.sub(padrao, substituto, conteudo)
    return novo, novo != conteudo


def atualizar_cabecalho(conteudo: str, hoje: str, proxima: str) -> tuple[str, list]:
    """Atualiza datas no cabeçalho do arquivo."""
    alteracoes = []

    conteudo, mudou = substituir(
        r"(\*\*Última atualização:\*\* )[\d\-]+",
        f"\\g<1>{hoje}",
        conteudo,
    )
    if mudou:
        alteracoes.append(f"Última atualização → {hoje}")

    conteudo, mudou = substituir(
        r"(\*\*Próxima revisão obrigatória:\*\* )[\d\-]+[^\n]*",
        f"\\g<1>{proxima} (45 dias — ciclo Copom)",
        conteudo,
    )
    if mudou:
        alteracoes.append(f"Próxima revisão → {proxima}")

    return conteudo, alteracoes


def atualizar_selic(conteudo: str, selic: float, ipca_mes: float | None) -> tuple[str, list]:
    """Atualiza Selic Meta, juros real e Selic líquida."""
    alteracoes = []

    conteudo, mudou = substituir(
        r"(\*\*Selic Meta\*\* \| )[\d,\.]+(% a\.a\.)",
        f"\\g<1>{selic:.2f}\\2",
        conteudo,
    )
    if mudou:
        alteracoes.append(f"Selic Meta → {selic:.2f}% a.a.")

    if ipca_mes is not None:
        ipca_12m = round(((1 + ipca_mes / 100) ** 12 - 1) * 100, 2)
        juros_real = round(selic - ipca_12m, 1)
        conteudo, mudou = substituir(
            r"(\*\*Juros real \(Selic − IPCA 12m\):\*\* ~)[\d,\.]+(% a\.a\.)",
            f"\\g<1>{juros_real:.1f}\\2",
            conteudo,
        )
        if mudou:
            alteracoes.append(f"Juros real → {juros_real:.1f}% a.a.")

    selic_liq = round(selic * 0.85, 1)  # após IR 15% (aplicação > 720 dias)
    conteudo, mudou = substituir(
        r"(\*\*Selic líquida \d{4}:\*\* ~)[\d,\.]+(% \(após IR 15%\))",
        f"\\g<1>{selic_liq:.1f}\\2",
        conteudo,
    )
    if mudou:
        alteracoes.append(f"Selic líquida → {selic_liq:.1f}%")

    return conteudo, alteracoes


def atualizar_cdi(conteudo: str, cdi: float) -> tuple[str, list]:
    alteracoes = []
    conteudo, mudou = substituir(
        r"(\*\*CDI\*\* \| ~)[\d,\.]+(% a\.a\.)",
        f"\\g<1>{cdi:.2f}\\2",
        conteudo,
    )
    if mudou:
        alteracoes.append(f"CDI → {cdi:.2f}% a.a.")
    return conteudo, alteracoes


def atualizar_ipca(conteudo: str, ipca: float) -> tuple[str, list]:
    alteracoes = []
    ipca_12m = round(((1 + ipca / 100) ** 12 - 1) * 100, 2)
    conteudo, mudou = substituir(
        r"(\*\*IPCA \(oficial\)\*\* \| )[\d,\.]+(% a\.m\.)",
        f"\\g<1>{ipca:.2f}\\2",
        conteudo,
    )
    if mudou:
        alteracoes.append(f"IPCA → {ipca:.2f}% a.m. (≈{ipca_12m:.2f}% a.a.)")
    return conteudo, alteracoes


def atualizar_tr(conteudo: str, tr: float) -> tuple[str, list]:
    alteracoes = []
    conteudo, mudou = substituir(
        r"(\*\*TR \(Taxa Referencial\)\*\* \| ~)[\d,\.]+(% a\.m\.)",
        f"\\g<1>{tr:.4f}\\2",
        conteudo,
    )
    if mudou:
        alteracoes.append(f"TR → {tr:.4f}% a.m.")
    return conteudo, alteracoes


def atualizar_igpm(conteudo: str, igpm: float) -> tuple[str, list]:
    alteracoes = []
    conteudo, mudou = substituir(
        r"(\*\*IGP-M\*\* \| )[\d,\.]+(% a\.m\.)",
        f"\\g<1>{igpm:.2f}\\2",
        conteudo,
    )
    if mudou:
        alteracoes.append(f"IGP-M → {igpm:.2f}% a.m.")
    return conteudo, alteracoes


def atualizar_taxas_credito(conteudo: str, taxas: dict) -> tuple[str, list]:
    """Atualiza tabela de taxas por modalidade."""
    alteracoes = []

    mapa_regex = {
        "rotativo":          r"(\*\*Rotativo do cartão de crédito\*\* \| ~)[\d,\.]+(%)",
        "cheque_especial":   r"(\*\*Cheque especial\*\* \| ~)[\d,\.]+(%)",
        "pessoal_nao_consig": r"(\*\*Crédito pessoal não consignado\*\* \| ~)[\d,\.]+(%)",
        "consignado_privado": r"(\*\*Crédito consignado privado\*\* \| ~)[\d,\.]+(%)",
        "consignado_publico": r"(\*\*Crédito consignado público\*\* \| ~)[\d,\.]+(%)",
        "imobiliario_sbpe":   r"(\*\*Financiamento imobiliário \(SBPE\)\*\* \| ~)[\d,\.]+(%)",
    }

    for chave, padrao in mapa_regex.items():
        if chave in taxas:
            t = taxas[chave]
            conteudo, mudou = substituir(padrao, f"\\g<1>{t['mes']:.1f}\\2", conteudo)
            if mudou:
                alteracoes.append(f"{chave.replace('_', ' ')} → {t['mes']:.1f}%/mês")

    return conteudo, alteracoes


# ──────────────────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  MordomIA — Atualização de Referências Brasil (BCB API)")
    print("=" * 60)

    if not REFS_FILE.exists():
        print(f"\n❌ Arquivo não encontrado: {REFS_FILE}")
        sys.exit(1)

    hoje = datetime.now().strftime("%Y-%m-%d")
    proxima = (datetime.now() + timedelta(days=45)).strftime("%Y-%m-%d")

    # ── 1. Buscar dados da API ─────────────────────────────────────
    print("\n📡 Buscando dados da API do Banco Central...\n")

    dados: dict[str, float | None] = {}
    for nome, serie in SERIES_SGS.items():
        val = fetch_sgs(serie)
        dados[nome] = val
        status = f"{val:.4f}" if val is not None else "❌ falhou"
        print(f"  {nome:<20} {status}")

    print()
    taxas = fetch_taxas_credito()
    print(f"  taxas_crédito          {len(taxas)} modalidades obtidas")

    # ── 2. Ler arquivo ────────────────────────────────────────────
    conteudo = REFS_FILE.read_text(encoding="utf-8")
    todas_alteracoes: list[str] = []

    # ── 3. Aplicar atualizações ───────────────────────────────────
    print("\n✏️  Aplicando atualizações...\n")

    conteudo, alt = atualizar_cabecalho(conteudo, hoje, proxima)
    todas_alteracoes.extend(alt)

    if dados.get("selic_meta"):
        conteudo, alt = atualizar_selic(conteudo, dados["selic_meta"], dados.get("ipca_mes"))
        todas_alteracoes.extend(alt)

    if dados.get("cdi_ano"):
        conteudo, alt = atualizar_cdi(conteudo, dados["cdi_ano"])
        todas_alteracoes.extend(alt)

    if dados.get("ipca_mes"):
        conteudo, alt = atualizar_ipca(conteudo, dados["ipca_mes"])
        todas_alteracoes.extend(alt)

    if dados.get("tr_mes"):
        conteudo, alt = atualizar_tr(conteudo, dados["tr_mes"])
        todas_alteracoes.extend(alt)

    if dados.get("igpm_mes"):
        conteudo, alt = atualizar_igpm(conteudo, dados["igpm_mes"])
        todas_alteracoes.extend(alt)

    if taxas:
        conteudo, alt = atualizar_taxas_credito(conteudo, taxas)
        todas_alteracoes.extend(alt)

    # ── 4. Gravar ─────────────────────────────────────────────────
    if todas_alteracoes:
        REFS_FILE.write_text(conteudo, encoding="utf-8")
        print(f"✅ {len(todas_alteracoes)} alteração(ões) gravadas em {REFS_FILE.name}:\n")
        for a in todas_alteracoes:
            print(f"   • {a}")
    else:
        print("✓ Nenhuma alteração necessária — dados já atualizados.")

    falhas = [k for k, v in dados.items() if v is None]
    if falhas:
        print(f"\n⚠️  Séries que falharam (verifique manualmente em bcb.gov.br):")
        for f in falhas:
            print(f"   • {f}")

    print(f"\n📅 Atualizado em: {hoje}")
    print(f"📅 Próxima revisão: {proxima}")
    print("\n✔ Concluído.")


if __name__ == "__main__":
    main()

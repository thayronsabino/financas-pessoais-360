#!/usr/bin/env python3
"""
install.py - Instalador do pacote MordomIA
Repositorio: https://github.com/thayronsabino/mordomia

Uso:
  python install.py                          # Instala tudo em ./mordomia
  python install.py --destino /caminho       # Instala em pasta especifica
  python install.py --skills-only            # Apenas as 7 skills
  python install.py --quiet                  # Modo silencioso
  python install.py --branch main            # Branch especifica (default: main)
"""
import sys
import argparse
from pathlib import Path
from urllib.request import urlretrieve
from urllib.error import URLError, HTTPError

REPO    = "thayronsabino/mordomia"
BRANCH  = "main"
VERSAO  = "2.1.0"

SKILLS = [
    "gestor-financeiro",
    "pessoal-diagnostico-financeiro",
    "pessoal-orcamento-domestico",
    "pessoal-plano-dividas-reserva",
    "pessoal-estrategia-investimentos",
    "pessoal-rotina-financeira-mensal",
    "pessoal-investimento-reino",
]

ARQUIVOS_CENTRAIS = [
    "docs/REFERENCIAS-BRASIL-2026.md",
    "docs/GLOSSARIO.md",
    "docs/MEMORY-SYSTEM.md",
    "docs/PRINCIPIOS-BIBLICOS-EXPANDIDOS.md",
    "docs/PROTOCOLO-CRISE-ESPIRITUAL.md",
    "docs/EDUCACAO-FINANCEIRA-BASICA.md",
]

PLAYBOOKS = [
    "recuperacao-90-dias.md",
    "estruturacao-familiar.md",
    "casal-e-financas.md",
    "transicao-clt-pj.md",
    "generosidade-sustentavel.md",
    "idoso-aposentadoria-insuficiente.md",
    "informal-sem-cnpj.md",
    "endividamento-por-saude.md",
]

FRAMEWORKS = [
    "investir-vs-quitar-divida.md",
    "clt-vs-pj.md",
    "casa-vs-aluguel.md",
    "priorizacao-financeira.md",
    "comprar-a-vista-vs-parcelado.md",
]

DOCUMENTACAO = [
    "README.md",
    "PACOTE.md",
    "INSTALAR.md",
    "ROADMAP.md",
    "DESIGN.md",
    "LICENSE",
]


def log(msg: str, quiet: bool = False) -> None:
    if not quiet:
        print(msg)


def baixar(url: str, destino: Path, quiet: bool = False) -> bool:
    try:
        urlretrieve(url, destino)
        return True
    except HTTPError as e:
        log(f"    HTTP {e.code}: {url}", quiet)
        return False
    except URLError as e:
        log(f"    Erro de rede: {e.reason}", quiet)
        return False
    except Exception as e:
        log(f"    Erro inesperado: {e}", quiet)
        return False


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Instala o pacote MordomIA a partir do GitHub.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemplos:\n"
            "  python install.py\n"
            "  python install.py --destino ~/projetos/mordomia\n"
            "  python install.py --skills-only\n"
            "  python install.py --quiet\n"
        ),
    )
    parser.add_argument(
        "--destino",
        default="mordomia",
        help="Diretorio de destino (padrao: ./mordomia)",
    )
    parser.add_argument(
        "--branch",
        default=BRANCH,
        help=f"Branch do repositorio (padrao: {BRANCH})",
    )
    parser.add_argument(
        "--skills-only",
        action="store_true",
        help="Instala apenas as 7 skills (sem playbooks, frameworks ou arquivos centrais)",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Modo silencioso (sem prompts ou logs detalhados)",
    )
    args = parser.parse_args()

    base_url = f"https://raw.githubusercontent.com/{REPO}/{args.branch}"
    destino = Path(args.destino)
    quiet = args.quiet

    log("=" * 60, quiet)
    log(f"  MordomIA v{VERSAO} — Instalador", quiet)
    log(f"  Repositorio: github.com/{REPO}", quiet)
    log(f"  Destino:     {destino.resolve()}", quiet)
    log("=" * 60, quiet)
    log("", quiet)

    erros = []
    instalados = 0

    # 1. SKILLS (sempre instaladas)
    log(">>> Instalando skills (7 arquivos)...", quiet)
    for skill in SKILLS:
        skill_dir = destino / skill
        skill_dir.mkdir(parents=True, exist_ok=True)
        url = f"{base_url}/{skill}/SKILL.md"
        ok = baixar(url, skill_dir / "SKILL.md", quiet)
        status = "OK  " if ok else "ERRO"
        log(f"  [{status}] {skill}/SKILL.md", quiet)
        if ok:
            instalados += 1
        else:
            erros.append(f"{skill}/SKILL.md")
    log("", quiet)

    if not args.skills_only:
        # 2. ARQUIVOS CENTRAIS (alma do pacote)
        log(">>> Instalando arquivos centrais (6 arquivos)...", quiet)
        for arquivo in ARQUIVOS_CENTRAIS:
            url = f"{base_url}/{arquivo}"
            ok = baixar(url, destino / arquivo, quiet)
            status = "OK  " if ok else "ERRO"
            log(f"  [{status}] {arquivo}", quiet)
            if ok:
                instalados += 1
            else:
                erros.append(arquivo)
        log("", quiet)

        # 3. PLAYBOOKS (cronogramas premium)
        log(">>> Instalando playbooks (8 arquivos)...", quiet)
        playbooks_dir = destino / "playbooks"
        playbooks_dir.mkdir(parents=True, exist_ok=True)
        for playbook in PLAYBOOKS:
            url = f"{base_url}/playbooks/{playbook}"
            ok = baixar(url, playbooks_dir / playbook, quiet)
            status = "OK  " if ok else "ERRO"
            log(f"  [{status}] playbooks/{playbook}", quiet)
            if ok:
                instalados += 1
            else:
                erros.append(f"playbooks/{playbook}")
        log("", quiet)

        # 4. FRAMEWORKS (engines de decisao)
        log(">>> Instalando frameworks (5 arquivos)...", quiet)
        frameworks_dir = destino / "frameworks"
        frameworks_dir.mkdir(parents=True, exist_ok=True)
        for framework in FRAMEWORKS:
            url = f"{base_url}/frameworks/{framework}"
            ok = baixar(url, frameworks_dir / framework, quiet)
            status = "OK  " if ok else "ERRO"
            log(f"  [{status}] frameworks/{framework}", quiet)
            if ok:
                instalados += 1
            else:
                erros.append(f"frameworks/{framework}")
        log("", quiet)

        # 5. DOCUMENTACAO
        log(">>> Instalando documentacao (6 arquivos)...", quiet)
        for doc in DOCUMENTACAO:
            url = f"{base_url}/{doc}"
            ok = baixar(url, destino / doc, quiet)
            status = "OK  " if ok else "ERRO"
            log(f"  [{status}] {doc}", quiet)
            if ok:
                instalados += 1
            else:
                erros.append(doc)
        log("", quiet)

    # Relatorio final
    log("=" * 60, quiet)
    if erros:
        log(f"Instalacao concluida com {len(erros)} erro(s):", quiet)
        for e in erros:
            log(f"  - {e}", quiet)
        log("", quiet)
        log("Tente novamente ou clone manualmente:", quiet)
        log(f"  git clone https://github.com/{REPO}.git", quiet)
        log("=" * 60, quiet)
        sys.exit(1)

    log(f"  Instalacao concluida com sucesso!", quiet)
    log(f"  {instalados} arquivos instalados em: {destino.resolve()}", quiet)
    log("=" * 60, quiet)
    log("", quiet)
    log("Para comecar, invoque o orquestrador no seu agente:", quiet)
    log("", quiet)
    log("  /gestor-financeiro", quiet)
    log("", quiet)
    log("Documentacao:", quiet)
    log(f"  {destino}/README.md     - Visao geral", quiet)
    log(f"  {destino}/PACOTE.md     - Indice completo", quiet)
    log(f"  {destino}/ROADMAP.md    - Visao de longo prazo", quiet)
    log("", quiet)


if __name__ == "__main__":
    main()

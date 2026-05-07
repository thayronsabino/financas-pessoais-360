#!/usr/bin/env python3
"""
install.py - Instalador do pacote Financas Pessoais 360
Uso: python install.py [--destino <caminho>]
"""
import sys
import argparse
from pathlib import Path
from urllib.request import urlretrieve
from urllib.error import URLError, HTTPError

REPO    = "thayronsabino/financas-pessoais-360"
BRANCH  = "main"
BASE_URL = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"

SKILLS = [
    "gestor-financeiro",
    "pessoal-diagnostico-financeiro",
    "pessoal-orcamento-domestico",
    "pessoal-plano-dividas-reserva",
    "pessoal-estrategia-investimentos",
    "pessoal-rotina-financeira-mensal",
    "pessoal-investimento-reino",
]

EXTRAS = ["PACOTE.md", "INSTALAR.md"]


def baixar(url: str, destino: Path) -> bool:
    try:
        urlretrieve(url, destino)
        return True
    except HTTPError as e:
        print(f"    HTTP {e.code}: {url}")
        return False
    except URLError as e:
        print(f"    Erro de rede: {e.reason}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Instala o pacote Financas Pessoais 360 a partir do GitHub."
    )
    parser.add_argument(
        "--destino",
        default="financas-pessoais-360",
        help="Diretorio de destino (padrao: ./financas-pessoais-360)",
    )
    args = parser.parse_args()

    destino = Path(args.destino)
    print(f"Financas Pessoais 360 — instalando em: {destino.resolve()}")
    print()

    erros = []

    for skill in SKILLS:
        skill_dir = destino / skill
        skill_dir.mkdir(parents=True, exist_ok=True)
        url = f"{BASE_URL}/{skill}/SKILL.md"
        ok = baixar(url, skill_dir / "SKILL.md")
        status = "OK  " if ok else "ERRO"
        print(f"  [{status}] {skill}")
        if not ok:
            erros.append(skill)

    print()
    for nome in EXTRAS:
        url = f"{BASE_URL}/{nome}"
        ok = baixar(url, destino / nome)
        status = "OK  " if ok else "ERRO"
        print(f"  [{status}] {nome}")
        if not ok:
            erros.append(nome)

    print()
    if erros:
        print(f"Instalacao concluida com {len(erros)} erro(s):")
        for e in erros:
            print(f"  - {e}")
        sys.exit(1)

    total = len(SKILLS)
    print(f"Instalacao concluida. {total} skills instaladas em: {destino.resolve()}")
    print()
    print("Para comecar, invoque o orquestrador:")
    print("  /gestor-financeiro")


if __name__ == "__main__":
    main()

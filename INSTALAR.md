# Instalação — Finanças Pessoais 360

**Repositório:** https://github.com/thayronsabino/financas-pessoais-360

Escolha o método de instalação conforme seu ambiente.

---

## Método A — npx skills (recomendado)

Compatível com Claude Code, Codex, Cursor e 55+ agentes. Requer Node.js.

```bash
# Instalar o pacote completo
npx skills add thayronsabino/financas-pessoais-360

# Instalar skill específica
npx skills add thayronsabino/financas-pessoais-360 --skill gestor-financeiro

# Instalar todas as skills explicitamente
npx skills add thayronsabino/financas-pessoais-360 --skill '*'
```

---

## Método B — Upload via Habilidades (Claude.ai)

Não requer repositório nem terminal. Faça upload direto pela interface do Claude.

1. Abra **Configurações → Habilidades**
2. Faça upload dos 7 arquivos `SKILL.md` abaixo (um por vez):

| Arquivo | Skill |
|---------|-------|
| `gestor-financeiro/SKILL.md` | Orquestrador — instale primeiro |
| `pessoal-diagnostico-financeiro/SKILL.md` | Raio-X financeiro |
| `pessoal-orcamento-domestico/SKILL.md` | Orçamento doméstico |
| `pessoal-plano-dividas-reserva/SKILL.md` | Dívidas e reserva |
| `pessoal-estrategia-investimentos/SKILL.md` | Investimentos |
| `pessoal-rotina-financeira-mensal/SKILL.md` | Rotina mensal |
| `pessoal-investimento-reino/SKILL.md` | Contribuições do reino |

3. Após o upload de todas, invoque o orquestrador:

```
/gestor-financeiro
```

> Todas as 7 skills precisam estar instaladas. O `gestor-financeiro` roteia para as demais automaticamente.

---

## Método B — Instalação via terminal (Python)

Requer Python 3.6+ e conexão com a internet. Funciona em Windows, Mac e Linux.

```bash
curl -O https://raw.githubusercontent.com/thayronsabino/financas-pessoais-360/main/install.py
python install.py
```

Por padrão, instala na pasta `./financas-pessoais-360`. Para escolher outro destino:

```bash
python install.py --destino /caminho/desejado
```

---

## Método C — Clone do repositório

```bash
git clone https://github.com/thayronsabino/financas-pessoais-360.git
```

---

## Estrutura instalada

```
financas-pessoais-360/
├── gestor-financeiro/SKILL.md
├── pessoal-diagnostico-financeiro/SKILL.md
├── pessoal-orcamento-domestico/SKILL.md
├── pessoal-plano-dividas-reserva/SKILL.md
├── pessoal-estrategia-investimentos/SKILL.md
├── pessoal-rotina-financeira-mensal/SKILL.md
└── pessoal-investimento-reino/SKILL.md
```

## Dependências entre skills

```
gestor-financeiro (entrada)
├── pessoal-diagnostico-financeiro  →  pessoal-orcamento-domestico
│                                   →  pessoal-plano-dividas-reserva
├── pessoal-orcamento-domestico     →  pessoal-plano-dividas-reserva
│                                   →  pessoal-investimento-reino
│                                   →  pessoal-rotina-financeira-mensal
├── pessoal-plano-dividas-reserva   →  pessoal-rotina-financeira-mensal
│                                   →  pessoal-estrategia-investimentos
├── pessoal-estrategia-investimentos →  pessoal-rotina-financeira-mensal
├── pessoal-investimento-reino       (integrada em toda cadeia)
└── pessoal-rotina-financeira-mensal (hub de manutenção mensal)
```

## Arquivos de apoio

- `PACOTE.md` — visão geral e ordem recomendada de execução

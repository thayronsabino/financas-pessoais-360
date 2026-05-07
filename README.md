# Finanças Pessoais 360

Pacote de skills para orientação financeira pessoal com base em mordomia cristã.
Funciona com Claude, Codex e qualquer agente compatível com o sistema de skills.

---

## Como instalar

### Método A — Upload via Habilidades (Claude.ai)

Sem terminal. Direto pela interface do Claude:

1. Abra **Configurações → Habilidades**
2. Faça upload dos 7 arquivos `SKILL.md` (baixe cada um pelo link abaixo ou clone o repositório)
3. Invoque: `/gestor-financeiro`

### Método B — Terminal (Python 3.6+)

```bash
curl -O https://raw.githubusercontent.com/thayronsabino/financas-pessoais-360/main/install.py
python install.py
```

Destino customizado:

```bash
python install.py --destino /caminho/desejado
```

### Método C — Clone completo

```bash
git clone https://github.com/thayronsabino/financas-pessoais-360.git
```

---

## Como usar

Invoque sempre pelo orquestrador:

```
/gestor-financeiro
```

O `gestor-financeiro` faz a triagem da sua situação financeira e decide automaticamente qual skill acionar, em que ordem e quantas por sessão. Não é necessário chamar as skills individuais diretamente.

---

## Skills incluídas

| Skill | Função |
|-------|--------|
| `gestor-financeiro` | Orquestrador — ponto de entrada do pacote |
| `pessoal-diagnostico-financeiro` | Raio-X financeiro: para onde vai o dinheiro, risco de inadimplência |
| `pessoal-orcamento-domestico` | Orçamento doméstico com categorias, tetos e ritual semanal |
| `pessoal-plano-dividas-reserva` | Quitação de dívidas (avalanche/bola de neve) + reserva de emergência |
| `pessoal-estrategia-investimentos` | Carteira por perfil de risco, horizonte e objetivos |
| `pessoal-rotina-financeira-mensal` | Fechamento mensal, análise de desvios e recalibração |
| `pessoal-investimento-reino` | Planejamento de dízimo, ofertas e projetos ministeriais |

---

## Como funciona a orquestração

O `gestor-financeiro` coleta o contexto do usuário (renda, dívidas, reserva, objetivos) e classifica a urgência da situação:

- **Alta** — Modo Consultoria: cadeia de 2 a 5 skills em sequência
- **Baixa** — Modo Direto: 1 skill específica

As skills se encadeiam naturalmente: o diagnóstico aponta para o orçamento, o orçamento para o plano de dívidas, e assim por diante. Cada skill indica a próxima ao final da execução.

```
gestor-financeiro
├── pessoal-diagnostico-financeiro
│   └── pessoal-orcamento-domestico  ou  pessoal-plano-dividas-reserva
├── pessoal-orcamento-domestico
│   └── pessoal-plano-dividas-reserva  /  pessoal-investimento-reino  /  pessoal-rotina-financeira-mensal
├── pessoal-plano-dividas-reserva
│   └── pessoal-rotina-financeira-mensal  /  pessoal-estrategia-investimentos
├── pessoal-estrategia-investimentos
│   └── pessoal-rotina-financeira-mensal
└── pessoal-investimento-reino  (presente em toda cadeia)
```

---

## Filosofia

O pacote integra **mordomia cristã** em todas as orientações: recursos financeiros são tratados como bens confiados para administração fiel, não como fins em si mesmos. Dízimo, ofertas e contribuições missionárias fazem parte do planejamento — não como obrigação, mas como prioridade planejada.

> "Ganhe tudo o que puder, economize tudo o que puder, dê tudo o que puder." — John Wesley

---

## Licença

Distribuído sob a **Apache License 2.0**. Veja o arquivo [`LICENSE`](LICENSE) para o texto completo.

**Em resumo — você pode:**
- Usar livremente para fins pessoais
- Usar comercialmente (consultorias financeiras, assessorias de investimento, planejamento com clientes)
- Modificar e redistribuir

**Condição obrigatória:**
- Sempre referencie a fonte original: `github.com/thayronsabino/financas-pessoais-360`

---

## Arquivos de apoio

- `PACOTE.md` — ordem recomendada de execução
- `INSTALAR.md` — guia completo de instalação
- `Instruções - Gestão Financeira Pessoal e Economia do Reino.txt` — contexto e filosofia detalhada
- `Finanças Pessoais 360.xlsx` — planilha complementar de controle financeiro

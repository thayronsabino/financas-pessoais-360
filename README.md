# MordomIA — Sistema Operacional Financeiro com Mordomia Cristã

> *Transformar ansiedade em clareza, improviso em direção, consumo em consciência, e recursos em propósito.*

[![Licença](https://img.shields.io/badge/licença-Apache%202.0-blue)](LICENSE)
[![Versão](https://img.shields.io/badge/versão-2.1.0-green)]()
[![Status](https://img.shields.io/badge/status-em%20produção-success)]()
[![Idioma](https://img.shields.io/badge/idioma-português--BR-yellow)]()

**Repositório oficial:** https://github.com/thayronsabino/mordomia

---

## O Que É o MordomIA

O **MordomIA** é um sistema completo de inteligência consultiva para finanças pessoais, fundamentado em **princípios de mordomia cristã**. Funciona com Claude, Codex, Cursor e qualquer agente compatível com o sistema de skills.

Não é um app de orçamento. Não é uma calculadora. Não é uma planilha sofisticada.

É um **sistema operacional financeiro** que combina:

```
🧠 Inteligência consultiva (engines de decisão, classificação por estado)
📊 Capacidade analítica (frameworks, simulações, painéis operacionais)
✝️ Profundidade pastoral (princípios bíblicos, cuidado em crise)
🇧🇷 Adaptação ao Brasil (taxas, leis, casos específicos)
🤝 Acessibilidade real (educação financeira para iniciantes absolutos)
```

> *"Dinheiro sem direção gera ansiedade. Mordomia com propósito gera liberdade."* — Manifesto MordomIA

---

## 🚀 Instalação Rápida

### Método A — npx skills (recomendado)

Compatível com Claude Code, Codex, Cursor e 55+ agentes. Requer Node.js.

```bash
# Instalar o pacote completo
npx skills add thayronsabino/mordomia

# Instalar skill específica
npx skills add thayronsabino/mordomia --skill gestor-financeiro

# Instalar todas as skills explicitamente
npx skills add thayronsabino/mordomia --skill '*'
```

### Método B — Upload via Habilidades (Claude.ai)

Sem terminal. Direto pela interface do Claude:

1. Acesse **Configurações → Habilidades**
2. Faça upload dos 7 arquivos `SKILL.md` (um por vez)
3. Invoque: `/gestor-financeiro`

### Método C — Clone do repositório

```bash
git clone https://github.com/thayronsabino/mordomia.git
cd mordomia
```

### Método D — Script Python (fallback)

Para ambientes sem Node.js. Requer Python 3.6+:

```bash
curl -O https://raw.githubusercontent.com/thayronsabino/mordomia/main/install.py
python install.py
```

📖 **Guia completo de instalação:** [`INSTALAR.md`](INSTALAR.md)

---

## 🎯 Como Usar

Invoque sempre pelo orquestrador:

```
/gestor-financeiro
```

O `gestor-financeiro` faz a triagem, classifica seu **Estado Financeiro** (Sobrevivência → Legado), ativa o **Protocolo Operacional** correto e decide automaticamente entre modo direto ou cadeia consultiva. Não é necessário chamar as skills individuais diretamente.

**Exemplos de invocação real:**

```
"Estou com dívida no rotativo do cartão e não sei o que fazer"
→ gestor-financeiro classifica como SOBREVIVÊNCIA
→ ativa Protocolo Estancar Sangria
→ encadeia: diagnóstico → orçamento → plano-dívidas

"Recebi proposta de R$ 14k PJ — vale a pena vs. meu CLT de R$ 9k?"
→ gestor-financeiro detecta gatilho CLT-PJ
→ aciona framework clt-vs-pj.md
→ se decisão = aceitar, ativa playbook transicao-clt-pj.md

"Estou com 65 anos e a aposentadoria não está dando"
→ gestor-financeiro detecta perfil idoso
→ ativa playbook idoso-aposentadoria-insuficiente.md
→ mapeia direitos não acessados (BPC, isenção IR, Carteira do Idoso)
```

---

## 🏗️ Arquitetura do Sistema

### Camada 1 — Skills (7 arquivos `SKILL.md`)

| Skill | Função |
|-------|--------|
| `gestor-financeiro` | Orquestrador — ponto de entrada, classifica estado e ativa protocolos |
| `pessoal-diagnostico-financeiro` | Sistema de Mapeamento de Fluxo Financeiro |
| `pessoal-orcamento-domestico` | Sistema de Orçamento Doméstico (4 blocos) |
| `pessoal-plano-dividas-reserva` | Plano de Quitação + Camada de Proteção Financeira |
| `pessoal-estrategia-investimentos` | Estratégia de Crescimento Patrimonial |
| `pessoal-rotina-financeira-mensal` | Ciclo de Recalibração Financeira |
| `pessoal-investimento-reino` | Plano de Generosidade Sustentável (dízimos, ofertas, projetos) |

### Camada 2 — Playbooks Premium (8 arquivos em `playbooks/`)

Cronogramas operacionais para situações específicas:

| Playbook | Situação |
|----------|----------|
| `recuperacao-90-dias.md` | Sair do Estado Sobrevivência em 90 dias |
| `estruturacao-familiar.md` | Família sem sistema → Sistema operacional |
| `casal-e-financas.md` | Conflito ou desalinhamento conjugal |
| `transicao-clt-pj.md` | Migração CLT → PJ com cálculo real |
| `generosidade-sustentavel.md` | Crescimento progressivo de contribuições |
| `idoso-aposentadoria-insuficiente.md` | 60+ com aposentadoria que não cobre necessidades |
| `informal-sem-cnpj.md` | Trabalhador informal sem proteção formal |
| `endividamento-por-saude.md` | Família em crise por doença grave |

### Camada 3 — Frameworks de Decisão (5 arquivos em `frameworks/`)

Engines de decisão para perguntas específicas:

| Framework | Resolve |
|-----------|---------|
| `investir-vs-quitar-divida.md` | Quando quitar e quando investir |
| `clt-vs-pj.md` | Cálculo real de equivalência entre regimes |
| `casa-vs-aluguel.md` | Análise de 30 anos com custo total |
| `priorizacao-financeira.md` | Ordem correta entre 8 níveis financeiros |
| `comprar-a-vista-vs-parcelado.md` | "Sem juros" embutido + custo de oportunidade |

### Camada 4 — Arquivos Centrais (a alma do pacote)

| Arquivo | Função |
|---------|--------|
| `REFERENCIAS-BRASIL-2026.md` | Dados macroeconômicos, tributários e legislativos atualizados |
| `GLOSSARIO.md` | Terminologia proprietária centralizada |
| `MEMORY-SYSTEM.md` | Especificação do Mecanismo de Memória Financeira |
| `PRINCIPIOS-BIBLICOS-EXPANDIDOS.md` | **A alma do pacote** — idolatria, ansiedade, contentamento, generosidade radical, riqueza como teste, honestidade, confiança em escassez, hospitalidade |
| `PROTOCOLO-CRISE-ESPIRITUAL.md` | **Crítico** — quando ativar e como conduzir situações que transcendem finanças (vício, violência, crise emocional, risco à vida) |
| `EDUCACAO-FINANCEIRA-BASICA.md` | Glossário e conceitos básicos para usuários iniciantes absolutos |

---

## 🌟 Estados Financeiros (5)

O sistema classifica o usuário em um destes 5 estados — a classificação determina o protocolo ativo:

```
SOBREVIVÊNCIA → ORGANIZAÇÃO → ESTABILIZAÇÃO → EXPANSÃO → LEGADO
```

| Estado | Indicadores | Protocolo |
|--------|-------------|-----------|
| Sobrevivência | Déficit, rotativo ativo, inadimplência | Estancar Sangria |
| Organização | Orçamento funcional, dívidas reduzindo | Construção de Base |
| Estabilização | Reserva ativa, consistência mensal | Proteção Ativa |
| Expansão | Investimentos, patrimônio crescendo | Multiplicação Responsável |
| Legado | Patrimônio sustentável, planejamento sucessório | Legado Vivo |

---

## 📁 Estrutura de Diretórios

```
mordomia/
├── README.md                            ← Este arquivo
├── PACOTE.md                            ← Índice do pacote
├── INSTALAR.md                          ← Guia completo de instalação
├── ROADMAP.md                           ← Visão de longo prazo
├── DESIGN.md                            ← Design system
├── LICENSE                              ← Apache 2.0
├── install.py                           ← Script de instalação
│
├── REFERENCIAS-BRASIL-2026.md           ← Dados dinâmicos
├── GLOSSARIO.md                         ← Terminologia proprietária
├── MEMORY-SYSTEM.md                     ← Persistência entre sessões
├── PRINCIPIOS-BIBLICOS-EXPANDIDOS.md    ← Alma pastoral
├── PROTOCOLO-CRISE-ESPIRITUAL.md        ← Cuidado em crise
├── EDUCACAO-FINANCEIRA-BASICA.md        ← Para iniciantes absolutos
│
├── gestor-financeiro/SKILL.md
├── pessoal-diagnostico-financeiro/SKILL.md
├── pessoal-orcamento-domestico/SKILL.md
├── pessoal-plano-dividas-reserva/SKILL.md
├── pessoal-estrategia-investimentos/SKILL.md
├── pessoal-rotina-financeira-mensal/SKILL.md
├── pessoal-investimento-reino/SKILL.md
│
├── playbooks/
│   ├── recuperacao-90-dias.md
│   ├── estruturacao-familiar.md
│   ├── casal-e-financas.md
│   ├── transicao-clt-pj.md
│   ├── generosidade-sustentavel.md
│   ├── idoso-aposentadoria-insuficiente.md
│   ├── informal-sem-cnpj.md
│   └── endividamento-por-saude.md
│
├── frameworks/
│   ├── investir-vs-quitar-divida.md
│   ├── clt-vs-pj.md
│   ├── casa-vs-aluguel.md
│   ├── priorizacao-financeira.md
│   └── comprar-a-vista-vs-parcelado.md
│
└── landing-page/
    ├── index.html
    ├── style.css
    ├── main.js
    ├── Manifesto — MordomIA.md
    ├── SISTEMA.md
    └── Landing Page da MordomIA Fin.md
```

---

## 🌍 Filosofia

O MordomIA integra **mordomia cristã** em todas as orientações: recursos financeiros são tratados como bens confiados para administração fiel. Dízimo (10% inviolável), ofertas, contribuições missionárias e projetos do Reino fazem parte do planejamento — não como obrigação, mas como **prioridade planejada**.

**Princípios inegociáveis:**

1. **Acolhimento antes de números** — toda primeira interação começa com escuta empática
2. **Dízimo é piso (10%) — nunca alvo** — não negociável em qualquer estado financeiro
3. **Camada de Proteção Financeira antes de investimentos** de longo prazo
4. **Quitar dívida com taxa > Selic líquida antes de investir**
5. **O sistema decide; não lista opções** — autoridade consultiva
6. **Estado real, não estado desejado** — não dar orientação de Expansão para usuário em Sobrevivência
7. **Mordomia inclui cuidar da própria casa** (1 Tm 5:8) — generosidade sustentável
8. **Sistema reconhece limites** — quando o problema transcende finanças, encaminhar
9. **Mordomia operacional + mordomia espiritual** — os dois juntos, sempre
10. **Linguagem serve ao usuário** — em crise ou início, simplificar; em maturidade, usar termos proprietários

---

## 🤝 Para Quem é o MordomIA

```
✅ Cristãos buscando integrar fé e finanças com profundidade
✅ Famílias querendo organizar finanças com base em princípios bíblicos
✅ Pastores e conselheiros que precisam de ferramenta estruturada
✅ Profissionais financeiros (CFP, contadores) que querem perspectiva pastoral
✅ Igrejas usando para discipulado financeiro
✅ Iniciantes absolutos que precisam de educação financeira acessível
✅ Quem está em crise (sobrevivência) e precisa de mapa claro
✅ Quem está em expansão e precisa de cuidado para não se perder na riqueza
```

**Não é apenas para:**
- Pessoas ricas querendo otimizar tributação
- Investidores em busca de "dicas quentes"
- Quem busca enriquecimento rápido

---

## 📜 Licença

Distribuído sob a **Apache License 2.0**. Veja [`LICENSE`](LICENSE) para o texto completo.

**Em resumo — você pode:**
- ✅ Usar livremente para fins pessoais
- ✅ Usar comercialmente (consultorias, assessorias, planejamento com clientes)
- ✅ Modificar e redistribuir
- ✅ Integrar com seus próprios sistemas

**Condição obrigatória:**
- 📌 Sempre referenciar a fonte: `github.com/thayronsabino/mordomia`

---

## 🛣️ Roadmap

O MordomIA é um sistema vivo. Próximas versões planejadas:

| Versão | Data | Foco |
|--------|------|------|
| v2.2 | Jun/2026 | Ajustes Incrementais |
| v3.0 | Set/2026 | Simulation Layer (scripts executáveis) |
| v3.5 | Dez/2026 | Web Integration (taxas em tempo real) |
| v4.0 | Mar/2027 | Operational Layer (CLI, dashboard) |
| v4.5 | Jun/2027 | Multi-Idioma (en, es) |
| v5.0 | 2028+ | Platform (SaaS opcional) |

📖 **Roadmap completo:** [`ROADMAP.md`](ROADMAP.md)

---

## 🤲 Contribuições

Contribuições são bem-vindas:

- 🐛 **Bugs:** abra uma issue em https://github.com/thayronsabino/mordomia/issues
- 📊 **Atualização de taxas:** PRs com `REFERENCIAS-BRASIL-2026.md` atualizado (citando fonte oficial)
- 📖 **Novos playbooks:** casos brasileiros não cobertos
- 🌐 **Tradução:** versões em outros idiomas
- ✍️ **Casos de uso reais:** transcrições anonimizadas

📖 **Detalhes em:** [`ROADMAP.md`](ROADMAP.md) (seção "Como Contribuir")

---

## 📚 Documentação Complementar

| Documento | Conteúdo |
|-----------|----------|
| [`PACOTE.md`](PACOTE.md) | Índice completo e ordem de execução |
| [`INSTALAR.md`](INSTALAR.md) | Guia detalhado de instalação |
| [`ROADMAP.md`](ROADMAP.md) | Visão de longo prazo e próximas versões |
| [`DESIGN.md`](DESIGN.md) | Design system (Stripe-inspired) |
| [`PRINCIPIOS-BIBLICOS-EXPANDIDOS.md`](PRINCIPIOS-BIBLICOS-EXPANDIDOS.md) | Fundamentação teológica |
| [`PROTOCOLO-CRISE-ESPIRITUAL.md`](PROTOCOLO-CRISE-ESPIRITUAL.md) | Cuidado em crise emocional/espiritual |
| [`EDUCACAO-FINANCEIRA-BASICA.md`](EDUCACAO-FINANCEIRA-BASICA.md) | Para iniciantes absolutos |
| [`landing-page/Manifesto — MordomIA.md`](landing-page/Manifesto%20—%20MordomIA.md) | Manifesto do projeto |

---

## 💬 Contato e Comunidade

- **GitHub:** https://github.com/thayronsabino/mordomia
- **Issues:** https://github.com/thayronsabino/mordomia/issues
- **Discussões:** https://github.com/thayronsabino/mordomia/discussions

---

## 🙏 Agradecimentos

> *"Ganhe tudo o que puder, economize tudo o que puder, dê tudo o que puder."* — John Wesley
>
> *"Bem está com o homem que se compadece, e empresta; disporá os seus negócios com juízo."* — Salmo 112:5
>
> *"Honra ao Senhor com a tua fazenda, e com as primícias de toda a tua renda."* — Provérbios 3:9

O MordomIA é dedicado a todos que buscam administrar fielmente o que foi confiado a eles — não como conquistadores de riqueza, mas como **mordomos do Reino**.

---

**Versão:** 2.1.0 | **Última atualização:** 2026-05-08

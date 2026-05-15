# MordomIA — Sistema Operacional Financeiro com Mordomia Cristã

> *Transformar ansiedade em clareza, improviso em direção, consumo em consciência, e recursos em propósito.*

[![Licença](https://img.shields.io/badge/licença-Apache%202.0-blue)](LICENSE)
[![Versão](https://img.shields.io/badge/versão-2.2.0-green)]()
[![Status](https://img.shields.io/badge/status-em%20produção-success)]()
[![Idioma](https://img.shields.io/badge/idioma-português--BR-yellow)]()
[![BCB API](https://img.shields.io/badge/BCB%20API-live-red)]()

**Repositório oficial:** https://github.com/thayronsabino/mordomia

---

## O Que É o MordomIA

O **MordomIA** é um sistema completo de inteligência consultiva para finanças pessoais, fundamentado em **princípios de mordomia cristã**. Funciona com Claude, Codex, Cursor e qualquer agente compatível com o sistema de skills.

Não é um app de orçamento. Não é uma calculadora. Não é uma planilha sofisticada.

É um **sistema operacional financeiro** que combina:

```
🧠 Inteligência consultiva (engines de decisão, classificação por estado)
📊 Capacidade analítica (frameworks, simulações, gráficos sob demanda)
✝️  Profundidade pastoral (princípios bíblicos, cuidado em crise)
🇧🇷 Adaptação ao Brasil (taxas ao vivo via BCB API, leis vigentes)
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

"Mostre um gráfico de pizza da minha carteira de investimentos"
→ gestor-financeiro ativa VISUALIZACAO.md tipo 3 (pizza)
→ gera Mermaid + fallback ASCII automaticamente
```

---

## 🏗️ Arquitetura do Sistema

📐 **Orquestração visual interativa:** [`docs/organograma.html`](docs/organograma.html)

### Camada 1 — Skills (7 arquivos `SKILL.md`)

| Skill | Função | Destaques v2.2 |
|-------|--------|----------------|
| `gestor-financeiro` | Orquestrador — ponto de entrada, classifica estado e ativa protocolos | Pergunta medo financeiro, protocolo recorrente, guia de encaminhamento |
| `pessoal-diagnostico-financeiro` | Sistema de Mapeamento de Fluxo Financeiro | Regime de trabalho + dependentes, estimador gastos invisíveis, lacunas de proteção |
| `pessoal-orcamento-domestico` | Sistema de Orçamento Doméstico (4 blocos) | Calendário sazonal, zona cinzenta, gestão cartão, guia de apps |
| `pessoal-plano-dividas-reserva` | Plano de Quitação + Camada de Proteção Financeira | Calculadora de perigo, portabilidade, Lei 14.181/2021, recuperação de score |
| `pessoal-estrategia-investimentos` | Estratégia de Crescimento Patrimonial | BCB API live, PGBL/VGBL engine, IR regressivo, encaminhamento AAI/CFP |
| `pessoal-rotina-financeira-mensal` | Ciclo de Recalibração Financeira | BCB IPCA live, revisão trimestral, planejamento anual, protocolo IR |
| `pessoal-investimento-reino` | Plano de Generosidade Sustentável | Calculadora bruto vs. líquido, IRPF deduções, automação dízimo |

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

### Camada 4 — Documentos Centrais

| Arquivo | Função |
|---------|--------|
| [`docs/REFERENCIAS-BRASIL-2026.md`](docs/REFERENCIAS-BRASIL-2026.md) | Dados macroeconômicos, tributários e legislativos atualizados |
| [`docs/VISUALIZACAO.md`](docs/VISUALIZACAO.md) | **NOVO** — Biblioteca de 10 tipos de gráficos (Mermaid + ASCII) |
| [`docs/organograma.html`](docs/organograma.html) | **NOVO** — Orquestração animada dos agentes e skills |
| [`docs/GLOSSARIO.md`](docs/GLOSSARIO.md) | Terminologia proprietária centralizada |
| [`docs/MEMORY-SYSTEM.md`](docs/MEMORY-SYSTEM.md) | Especificação do Mecanismo de Memória Financeira |
| [`docs/PRINCIPIOS-BIBLICOS-EXPANDIDOS.md`](docs/PRINCIPIOS-BIBLICOS-EXPANDIDOS.md) | **A alma do pacote** — idolatria, ansiedade, contentamento, riqueza como teste |
| [`docs/PROTOCOLO-CRISE-ESPIRITUAL.md`](docs/PROTOCOLO-CRISE-ESPIRITUAL.md) | **Crítico** — quando ativar e como conduzir crises (vício, violência, risco à vida) |
| [`docs/EDUCACAO-FINANCEIRA-BASICA.md`](docs/EDUCACAO-FINANCEIRA-BASICA.md) | Glossário e conceitos básicos para iniciantes absolutos |

---

## 🔴 BCB API — Taxas em Tempo Real

O MordomIA conecta diretamente à **API pública do Banco Central do Brasil** — sem autenticação, sem custo, atualizada a cada Copom (≈45 dias). Toda orientação usa a taxa vigente, não estimativas desatualizadas.

### Série SGS (dados históricos)
```
Selic:  https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/1?formato=json
IPCA:   https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados/ultimos/1?formato=json
CDI:    https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados/ultimos/1?formato=json
TR:     https://api.bcb.gov.br/dados/serie/bcdata.sgs.226/dados/ultimos/1?formato=json
IGP-M:  https://api.bcb.gov.br/dados/serie/bcdata.sgs.189/dados/ultimos/1?formato=json
```

### Taxas de crédito (Olinda API)
```
https://olinda.bcb.gov.br/olinda/servico/taxas_juros/versao/v2/odata/
```

### Uso automático nas skills
- `gestor-financeiro` → Selic (comparação benchmark)
- `pessoal-estrategia-investimentos` → Selic, IPCA, CDI (todo cálculo de rendimento)
- `pessoal-rotina-financeira-mensal` → IPCA (ajuste anualizado)
- `pessoal-plano-dividas-reserva` → Selic (teste custo da dívida vs. benchmark)
- `pessoal-diagnostico-financeiro` → Selic (benchmark rápido)

---

## 📊 Recursos Visuais (Novo em v2.2)

O MordomIA agora gera **gráficos e visualizações sob demanda** — o usuário pode pedir qualquer tipo de visual durante a consulta.

### 10 Tipos de Visualização disponíveis

| Tipo | Formato | Uso típico |
|------|---------|-----------|
| Barras | Mermaid xychart-beta | Distribuição orçamento, ranking dívidas |
| Linha | Mermaid xychart-beta | Crescimento patrimonial, evolução reserva |
| Pizza | Mermaid pie | Composição orçamento, alocação carteira |
| Gantt | Mermaid gantt | Cronograma quitação, roadmap de metas |
| Fluxograma | Mermaid graph | Jornada financeira, árvores de decisão |
| Tabela amortização | Markdown | Mês a mês: saldo, juros, principal |
| Comparativo A vs B | Markdown | Mínimo vs. agressivo, produto X vs. Y |
| Barra de progresso | ASCII | % de meta atingida |
| Termômetro comprometimento | ASCII | Zonas saudável/atenção/risco/crítico |
| Sparkline | ASCII | Tendência 6 meses por categoria |

> Fallback ASCII automático para ambientes sem suporte a Mermaid (terminal, Notion, WhatsApp).

**Exemplos de solicitação:**
```
"mostre minha carteira em pizza"
"quero ver o gráfico de evolução da minha reserva"
"crie a tabela de amortização do meu financiamento"
"compare pagar o mínimo vs. pagar R$600/mês no cartão"
"mostre em barras como está meu orçamento"
```

📖 **Referência completa:** [`docs/VISUALIZACAO.md`](docs/VISUALIZACAO.md)

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
├── update-referencias.py                ← Atualização automática de taxas BCB
│
├── docs/
│   ├── REFERENCIAS-BRASIL-2026.md       ← Dados dinâmicos
│   ├── VISUALIZACAO.md                  ← ✨ NOVO — Biblioteca de gráficos
│   ├── organograma.html                 ← ✨ NOVO — Orquestração animada
│   ├── GLOSSARIO.md                     ← Terminologia proprietária
│   ├── MEMORY-SYSTEM.md                 ← Persistência entre sessões
│   ├── PRINCIPIOS-BIBLICOS-EXPANDIDOS.md ← Alma pastoral
│   ├── PROTOCOLO-CRISE-ESPIRITUAL.md    ← Cuidado em crise
│   └── EDUCACAO-FINANCEIRA-BASICA.md    ← Para iniciantes absolutos
│
├── gestor-financeiro/SKILL.md           ← Orquestrador
├── pessoal-diagnostico-financeiro/SKILL.md
├── pessoal-orcamento-domestico/SKILL.md
├── pessoal-plano-dividas-reserva/SKILL.md
├── pessoal-estrategia-investimentos/SKILL.md
├── pessoal-rotina-financeira-mensal/SKILL.md
├── pessoal-investimento-reino/SKILL.md
│
├── playbooks/                           ← 8 cronogramas operacionais
├── frameworks/                          ← 5 engines de decisão
└── landing-page/                        ← Página do projeto
```

---

## ✨ Novidades da v2.2.0

### 🔴 BCB API em todas as skills relevantes
Selic, IPCA e CDI em tempo real com protocolo explícito de URL — sem estimativas hardcoded.

### 📊 VISUALIZACAO.md — Biblioteca de Gráficos
10 tipos de visualização com Mermaid + fallback ASCII. O usuário pode solicitar qualquer gráfico durante a consulta com linguagem natural.

### 🎨 Organograma Animado
[`docs/organograma.html`](docs/organograma.html) — representação visual interativa da orquestração do sistema com animações CSS e conexões SVG dinâmicas.

### 🧠 Auditoria de Qualidade — Skills Nível Consultor

Cada skill recebeu adições que a elevam ao nível de um especialista humano:

| Skill | Principal adição |
|-------|-----------------|
| `diagnóstico` | Regime de trabalho + dependentes no input; estimador de gastos invisíveis; lacunas de proteção (saúde, vida, INSS) |
| `orçamento` | Calendário sazonal mês a mês com provisão; zona cinzenta (Netflix, academia, carro) com respostas explícitas; gestão de cartão |
| `dívidas e reserva` | Calculadora de perigo (custo real do mínimo); portabilidade de crédito (Lei Circular BCB 3.419/2008); Lei do Superendividamento 14.181/2021 |
| `investimentos` | PGBL/VGBL engine completo; IR regressivo com tabela; quando encaminhar para AAI/CFP |
| `rotina mensal` | Revisão trimestral completa (março/junho/setembro/dezembro); planejamento anual familiar; protocolo de emergência mid-month; protocolo época de IR |
| `investimento reino` | Calculadora dízimo bruto vs. líquido (a pergunta mais frequente); IRPF deduções (FCA/FUMCAD vs. igrejas); automação passo a passo |
| `gestor` | Pergunta medo financeiro na abertura; protocolo para usuário recorrente; guia de encaminhamento para especialista humano (7 situações) |

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

| Versão | Data | Status | Foco |
|--------|------|--------|------|
| v2.1.0 | Mai/2026 | ✅ Entregue | Sistema operacional financeiro base |
| v2.2.0 | Mai/2026 | ✅ Entregue | BCB API live, VISUALIZACAO.md, auditoria de qualidade, organograma |
| v3.0 | Set/2026 | 🔲 Planejado | Simulation Layer (scripts executáveis) |
| v3.5 | Dez/2026 | 🔲 Planejado | Web Integration (dashboard em tempo real) |
| v4.0 | Mar/2027 | 🔲 Planejado | Operational Layer (CLI, alertas automáticos) |
| v4.5 | Jun/2027 | 🔲 Planejado | Multi-Idioma (en, es) |
| v5.0 | 2028+ | 🔲 Planejado | Platform (SaaS opcional) |

📖 **Roadmap completo:** [`ROADMAP.md`](ROADMAP.md)

---

## 🤲 Contribuições

Contribuições são bem-vindas:

- 🐛 **Bugs:** abra uma issue em https://github.com/thayronsabino/mordomia/issues
- 📊 **Atualização de taxas:** PRs com `docs/REFERENCIAS-BRASIL-2026.md` atualizado (citando fonte oficial)
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
| [`docs/VISUALIZACAO.md`](docs/VISUALIZACAO.md) | **NOVO** — Biblioteca de gráficos e visualizações |
| [`docs/organograma.html`](docs/organograma.html) | **NOVO** — Orquestração animada interativa |
| [`docs/PRINCIPIOS-BIBLICOS-EXPANDIDOS.md`](docs/PRINCIPIOS-BIBLICOS-EXPANDIDOS.md) | Fundamentação teológica |
| [`docs/PROTOCOLO-CRISE-ESPIRITUAL.md`](docs/PROTOCOLO-CRISE-ESPIRITUAL.md) | Cuidado em crise emocional/espiritual |
| [`docs/EDUCACAO-FINANCEIRA-BASICA.md`](docs/EDUCACAO-FINANCEIRA-BASICA.md) | Para iniciantes absolutos |
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

**Versão:** 2.2.0 | **Última atualização:** 2026-05-15

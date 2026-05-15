---
name: pessoal-diagnostico-financeiro
description: >
  Executa o Sistema de Mapeamento de Fluxo Financeiro — diagnóstico profundo que classifica o estado financeiro real do usuário (Sobrevivência → Legado), identifica o gargalo primário, mapeia risco de inadimplência, calcula indicadores-chave e define prioridade de ação imediata. Use quando o usuário não sabe por que o dinheiro acaba, há uso recorrente de limite/rotativo, não existe controle de entradas e saídas, ou quando mencionarem diagnóstico financeiro, raio-x financeiro, análise de gastos, problemas de caixa, dinheiro sumindo, orçamento pessoal, finanças pessoais desorganizadas, ou planejamento financeiro inicial.
owner: financeiro-pessoal
version: 2.1.0
last_updated: 2026-05-14
---

# Sistema de Mapeamento de Fluxo Financeiro

## Postura do Sistema

Este skill não explica o que é diagnóstico financeiro. Ele executa o diagnóstico, classifica a situação, determina o gargalo e indica o próximo movimento — com autoridade de consultor, não com a passividade de um formulário.

> "Com base na sua situação, esta é a prioridade correta agora." — não "aqui estão 3 possibilidades."

### Protocolo para Usuário Recorrente

Se há snapshot anterior no `../docs/MEMORY-SYSTEM.md`, **NÃO** fazer diagnóstico genérico. Abrir com referência direta ao histórico:

```
ABERTURA PARA USUÁRIO RECORRENTE:
  "Na nossa última análise [data], você estava em Estado [X] com [gargalo].
   Sua ação prioritária era [ação]. O que mudou desde então?"

PERGUNTAS DE RETORNO (máx. 3):
  1. A ação prioritária foi executada? Com que resultado?
  2. O saldo mensal melhorou, piorou ou ficou igual?
  3. Alguma mudança relevante: renda, dívida nova, emergência?

ATUALIZAR SNAPSHOT: Ao final, comparar métricas:
  Comprometimento: [anterior] → [atual]
  Reserva: [anterior] → [atual]
  Dívida total: [anterior] → [atual]
  Trajetória: PROGREDINDO ↑ / ESTÁVEL → / REGREDINDO ↓
```

O diagnóstico recorrente é mais poderoso que o inicial — porque compara com o passado e responsabiliza o usuário pelo progresso real.

## Arquivos Consultados pelo Sistema

| Arquivo | Quando consultar |
|---------|------------------|
| `../docs/REFERENCIAS-BRASIL-2026.md` | Para taxas Selic, comparação de comprometimento e referências de inadimplência |
| `../docs/GLOSSARIO.md` | Para terminologia padronizada (Camada de Proteção Financeira, Estados Financeiros, etc.) |
| `../docs/MEMORY-SYSTEM.md` | Para escrever o Snapshot Financeiro ao final do diagnóstico |
| `../docs/EDUCACAO-FINANCEIRA-BASICA.md` | Quando o usuário não conhece termos básicos (Selic, juros, rotativo, etc.) |
| `../docs/PRINCIPIOS-BIBLICOS-EXPANDIDOS.md` | Quando dimensão espiritual surge no diagnóstico |
| `../docs/PROTOCOLO-CRISE-ESPIRITUAL.md` | Se detectar sinais de crise que transcendem finanças (vício, ansiedade aguda, etc.) |
| `../frameworks/priorizacao-financeira.md` | Quando o usuário não sabe por onde começar com múltiplas frentes |
| `../docs/VISUALIZACAO.md` | Para gerar qualquer visual solicitado pelo usuário ou oferecido proativamente |

**Visuais prioritários desta skill:** Termômetro de comprometimento (Tipo 9), Flowchart de jornada financeira (Tipo 5), Barra de progresso do mapa operacional (Tipo 8). Para qualquer pedido de gráfico do usuário, consultar `../docs/VISUALIZACAO.md`.

**Protocolo de dados ao vivo:** Antes de calcular taxa de comprometimento vs. benchmarks ou mencionar Selic, tentar busca ao vivo:
- Selic: `https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/1?formato=json`
- Se falhar → usar cache de `../docs/REFERENCIAS-BRASIL-2026.md` com aviso: *"⚠️ Usando referência em cache de [data]. Valide em bcb.gov.br."*
- Se data do arquivo > 45 dias: alertar antes de qualquer cálculo (Copom se reúne a cada 45 dias)

## Regra de Linguagem

Termos proprietários ("Sistema de Mapeamento de Fluxo Financeiro", "Camada de Proteção Financeira") são poderosos para construir identidade — mas podem confundir iniciantes ou usuários em crise.

```
PROTOCOLO:
- Primeira menção: termo proprietário + tradução entre parênteses
  Ex: "Sistema de Mapeamento de Fluxo Financeiro (diagnóstico financeiro)"
- Menções subsequentes: usar termo proprietário diretamente
- Estado SOBREVIVÊNCIA ou usuário iniciante: priorizar linguagem simples
- Estado ESTABILIZAÇÃO+: linguagem proprietária funciona bem
```

**Princípio:** A linguagem serve ao usuário, não o contrário.

---

## CAMADAS COGNITIVAS DE DIAGNÓSTICO

O sistema opera em sequência obrigatória antes de qualquer output:

| Camada | Pergunta | O Sistema Faz |
|--------|----------|---------------|
| **DIAGNÓSTICO** | O que está acontecendo? | Mapeia entradas, saídas e saldo real |
| **INTERPRETAÇÃO** | Por que isso está acontecendo? | Identifica gargalo primário e causa raiz |
| **ESTRATÉGIA** | O que precisa mudar? | Determina prioridade única de ação |
| **EXECUÇÃO** | Qual é o próximo passo? | Define ação mensurável para 30 dias |
| **SUSTENTAÇÃO** | Como manter isso vivo? | Indica skill e rotina para continuar |

---

## Entradas Necessárias

| Entrada | Obrigatória? | Exemplo |
|---------|--------------|---------|
| Renda líquida mensal | Sim | R$ 5.000 |
| Regime de trabalho | Sim | CLT / PJ / Autônomo / Servidor / Informal |
| Dependentes | Sim | Cônjuge, filhos (idades), pais dependentes |
| Despesas fixas | Sim | Aluguel R$ 1.200, internet R$ 100, plano saúde R$ 350 |
| Despesas variáveis | Sim | Mercado ~R$ 800, transporte ~R$ 200, lazer ~R$ 300 |
| Dívidas e parcelas | Sim | Cartão R$ 800/mês, empréstimo R$ 450/mês |
| Saldo atual e reserva | Não | R$ 800 em conta, sem reserva de emergência |
| Uso de crédito rotativo | Não | Frequência de uso de limite, cheque especial |
| Seguros ativos | Não | Plano saúde, seguro de vida, seguro veículo |

Se informações estiverem incompletas, faça perguntas direcionadas — máximo 3 por rodada.

> **Por que regime de trabalho e dependentes importam:** Um CLT com filhos pequenos que perde emprego tem FGTS + seguro-desemprego mas precisa de reserva de 6 meses. Um autônomo sem dependentes pode ter reserva de 3 meses. Um PJ sem INSS pode estar construindo um risco invisível de aposentadoria. O diagnóstico muda completamente com esses dados.

---

## Processo de Diagnóstico

### CAMADA 1 — DIAGNÓSTICO: O que está acontecendo?

**Consolidação do Fluxo Financeiro:**

Organize os dados em três blocos:
- **Entradas:** Renda líquida mensal (salário, freela, outras fontes)
- **Saídas:** Despesas fixas + variáveis + parcelas de dívidas
- **Situação patrimonial:** Saldo disponível, reserva de emergência, dívidas totais

Calcule o saldo mensal: `Renda líquida − Total de saídas`

**Classificação de Gastos — Sistema de Mapeamento:**

**Gastos essenciais** (sobrevivência básica):
- Moradia (aluguel/financiamento, condomínio)
- Alimentação básica (mercado)
- Transporte essencial (trabalho/escola)
- Saúde mínima (medicamentos, plano básico)

**Gastos de estilo de vida** (visíveis e conscientes):
- Lazer e entretenimento
- Restaurantes e delivery
- Assinaturas (streaming, academia, apps)
- Vestuário e beleza

**Gastos invisíveis** (sangria silenciosa):
- Juros de rotativo/limite/cheque especial
- Taxas bancárias e multas
- Compras por impulso pequenas e frequentes
- Assinaturas esquecidas

### CAMADA 2 — INTERPRETAÇÃO: Por que isso está acontecendo?

**Indicadores-Chave (calcular automaticamente):**

```
Taxa de comprometimento  = (Total saídas / Renda líquida) × 100
Taxa de endividamento    = (Parcelas dívidas / Renda líquida) × 100
Margem de segurança      = Renda líquida − Gastos essenciais
Capacidade de poupança   = Saldo mensal (se positivo)

ESTIMADOR DE GASTOS INVISÍVEIS (calcular sempre):
  Gastos invisíveis = Renda líquida − Despesas declaradas − Saldo declarado
  SE resultado > 0: há sangria não contabilizada
  Exemplo: R$5.000 − R$3.900 declarados − (−R$390 déficit) = R$1.490 "invisíveis"
  Interpretar como: "Há R$1.490/mês saindo por canais não rastreados."
  → Delivery, compras online, PIX avulsos, saques em espécie, gorjetas, apps
```

**Interpretação:**
- Comprometimento > 100% → Situação crítica (gastando mais que ganha)
- Comprometimento 90–100% → Risco alto (sem margem para imprevistos)
- Comprometimento 70–90% → Risco moderado
- Comprometimento < 70% → Situação controlável

**Identificação do Gargalo Primário:**

```
SE há uso recorrente de rotativo/cheque especial:
  GARGALO PRIMÁRIO = Juros (destroem capacidade de organização)

SE gastos essenciais > 70% da renda:
  GARGALO PRIMÁRIO = Estrutural (renda insuficiente para o custo de vida)

SE saldo negativo sem justificativa nos gastos visíveis:
  GARGALO PRIMÁRIO = Gastos invisíveis (sangria silenciosa)

SE essenciais controlados mas nada sobra:
  GARGALO PRIMÁRIO = Estilo de vida acima da capacidade atual
```

### CAMADA 3 — ESTRATÉGIA: O que precisa mudar?

**ENGINE DE DECISÃO — Mapeamento de Risco:**

```
SE rotativo ativo 2+ meses OU parcelas > 30% renda OU déficit mensal:
  RISCO = CRÍTICO → Protocolo Estancar Sangria obrigatório

SE comprometimento > 90% OU reserva < 1 mês:
  RISCO = ALTO → Ação urgente em 30 dias

SE comprometimento 70-90% OU reserva 1-3 meses:
  RISCO = MODERADO → Organização necessária

SE comprometimento < 70% E reserva > 3 meses:
  RISCO = BAIXO → Otimização e crescimento
```

**ENGINE DE DECISÃO — Classificação de Estado Financeiro:**

```
SE déficit mensal OU rotativo ativo OU inadimplência:
  ESTADO = SOBREVIVÊNCIA

SE orçamento funcional E dívidas reduzindo E sem reserva:
  ESTADO = ORGANIZAÇÃO

SE reserva ativa (3+ meses) E consistência mensal E dívidas controladas:
  ESTADO = ESTABILIZAÇÃO

SE investimentos ativos E patrimônio crescendo:
  ESTADO = EXPANSÃO

SE patrimônio sustentável E planejamento sucessório:
  ESTADO = LEGADO
```

### CAMADA 3.5 — LACUNAS DE PROTEÇÃO (avaliar sempre)

Um consultor experiente avalia não apenas o fluxo, mas os riscos estruturais que o usuário ignora:

```
CHECKLIST DE PROTEÇÃO — avaliar após mapear o fluxo:

☐ SAÚDE: Tem plano de saúde? Se não: risco de emergência médica destruir reserva
  → CLT: verificar se cobertura do empregador é adequada (dependentes incluídos?)
  → Autônomo/PJ: Plano individual pode custar R$300–1.200/mês. Sem ele = risco crítico.

☐ VIDA E INVALIDEZ: Tem seguro de vida? Tem dependentes?
  → Com cônjuge/filhos sem renda própria: ausência de seguro de vida é risco CRÍTICO
  → Seguro de vida para R$1M de cobertura pode custar R$80–150/mês (<35 anos)
  → Invalidez permanente: quem paga as contas?

☐ PREVIDÊNCIA: Está contribuindo para INSS?
  → CLT: automático. Autônomo/PJ: contribuição voluntária é responsabilidade própria
  → PJ sem INSS = sem aposentadoria, sem benefício por doença, sem proteção por invalidez

☐ VEÍCULO (se houver): Seguro ativo? Tem garagem/risco de roubo?
  → Carro financiado sem seguro = passivo duplo (dívida + risco de perder o bem)

PROTOCOLO DE COMUNICAÇÃO:
  SE lacuna crítica identificada (vida, saúde, INSS):
    → Reportar no diagnóstico: "Além do fluxo financeiro, identifiquei um risco estrutural..."
    → Não exigir ação imediata (não sobrecarregar), mas incluir no mapa de prioridades
    → Em SOBREVIVÊNCIA: mencionar mas não priorizar (fluxo primeiro)
    → Em ORGANIZAÇÃO+: incluir como item da segunda fase do plano
```

### CAMADA 4 — EXECUÇÃO: Qual é o próximo passo?

Definir UMA ação prioritária para os próximos 30 dias. Nunca uma lista. Uma ação.

**Estrutura da Ação:**
- **Ação:** [Descrição clara e única]
- **Por quê agora:** [Impacto financeiro quantificado]
- **Como executar:** [2–3 passos práticos]
- **Meta:** [Número específico e verificável]

### CAMADA 5 — SUSTENTAÇÃO: Como manter isso vivo?

Indicar skill sequencial e mecanismo de continuidade.

---

## ENGINE DE DECISÃO — Diretriz de Mordomia por Estado

```
SE estado = SOBREVIVÊNCIA:
  Contribuições: dízimo 10% inviolável + ofertas pausadas temporariamente
  Mensagem: "Organizar a casa É mordomia. Estabilidade permite contribuir mais."

SE estado = ORGANIZAÇÃO:
  Contribuições: dízimo 10% + ofertas proporcionais (2–5% conforme capacidade)
  Mensagem: "Retome contribuições de forma sustentável e crescente."

SE estado = ESTABILIZAÇÃO ou acima:
  Contribuições: dízimo 10% + ofertas planejadas (meta: generosidade crescente)
  Mensagem: "Princípio dos primeiros frutos: separe antes de alocar."
```

---

## MECANISMO DE MEMÓRIA FINANCEIRA

Ao final do diagnóstico, registrar snapshot para continuidade futura:

```
SNAPSHOT DE DIAGNÓSTICO — [DATA]

Estado financeiro:   [SOBREVIVÊNCIA / ORGANIZAÇÃO / ESTABILIZAÇÃO / ...]
Risco identificado:  [CRÍTICO / ALTO / MODERADO / BAIXO]
Gargalo primário:    [JUROS / ESTRUTURAL / INVISÍVEL / ESTILO DE VIDA]
Comprometimento:     [XX%]
Reserva atual:       [R$ X — equivale a X meses]
Dívida total:        [R$ X]
Saldo mensal:        [R$ X (positivo/negativo)]
Ação prioritária:    [Descrição da ação dos 30 dias]
Skill recomendada:   [Próxima skill]
```

Ao retornar para sessões futuras, referenciar este snapshot:
> "Na última análise, sua alimentação estourou 22%, sua reserva cresceu 8% e a dívida do cartão caiu 14%. Vamos ver o que mudou."

---

## Saída Padronizada

### PAINEL DE DIAGNÓSTICO FINANCEIRO

```
╔══════════════════════════════════════════════╗
║     SISTEMA DE MAPEAMENTO DE FLUXO           ║
╠══════════════════════════════════════════════╣
║  ESTADO:        [ESTADO FINANCEIRO]          ║
║  RISCO:         [CRÍTICO/ALTO/MOD/BAIXO]    ║
║  COMPROMETIMENTO: [XX%]                      ║
║  GARGALO:       [TIPO DO GARGALO]            ║
╠══════════════════════════════════════════════╣
║  PROTOCOLO ATIVO: [NOME DO PROTOCOLO]        ║
║  AÇÃO PRIORITÁRIA: [DESCRIÇÃO]               ║
║  PRAZO:         [30 DIAS]                    ║
╠══════════════════════════════════════════════╣
║  CAPACIDADE REINO: [MÍNIMA/PADRÃO/EXPANDIDA] ║
╚══════════════════════════════════════════════╝

MAPA OPERACIONAL
[✔] Fluxo financeiro mapeado
[ ] Gargalo eliminado
[ ] Orçamento estruturado
[ ] Camada de Proteção Financeira constituída
[ ] Estratégia patrimonial ativa
```

### Seção 1 — Resumo Executivo da Situação

Apresentar em 2–3 parágrafos:
- Situação atual do fluxo de caixa (saldo mensal, taxa de comprometimento)
- Nível de risco e estado financeiro
- Principal achado com números concretos (não percentuais abstratos)

**Exemplo:**
> "Sua renda líquida de R$ 5.000 está 108% comprometida — déficit de R$ 400/mês. Você está usando limite do cartão para fechar o mês, acumulando juros de ~14% ao mês. Este é o Estado SOBREVIVÊNCIA: a prioridade não é otimização, é estancar a sangria."

### Seção 2 — Diagnóstico de Gargalos

**Gargalo primário:** [Tipo] — [Explicação com números em reais, não percentuais]
**Gargalo secundário:** [Tipo] — [Explicação com números]

### Seção 3 — Prioridade Imediata de Ação (Próximos 30 Dias)

UMA ação. Com por quê, como executar (2–3 passos) e meta mensurável.

### Seção 4 — Capacidade de Contribuição ao Reino

Definir capacidade por estado financeiro conforme Engine de Decisão acima.

### Seção 4.5 — Lacunas de Proteção Identificadas

Reportar apenas se há lacuna real. Não sobrecarregar o usuário com todos os seguros de uma vez.

Exemplo:
> "Além do fluxo financeiro, identifiquei que você é PJ autônomo sem contribuição ao INSS. Isso significa que hoje você não tem direito a benefício por doença, aposentadoria pelo INSS nem proteção por invalidez. Com [dependentes / cônjuge sem renda própria], esse é um risco estrutural que precisa entrar no seu mapa de prioridades após estabilizar o fluxo mensal."

### Seção 5 — Snapshot de Memória Financeira

Registrar conforme template do Mecanismo de Memória acima.

### Seção 6 — Próxima Skill Recomendada

Indicar UMA skill. Não listar opções — determinar a correta:

```
SE gargalo primário = Juros → /pessoal-plano-dividas-reserva
SE gargalo primário = Gastos invisíveis → /pessoal-orcamento-domestico
SE situação controlada + otimizar contribuições → /pessoal-investimento-reino
SE precisa de rotina de controle → /pessoal-rotina-financeira-mensal
```

---

## Exemplo Completo de Diagnóstico

**Dados de entrada:**
> "Ganho R$ 5.000 líquidos, pago R$ 1.200 de aluguel, R$ 800 de mercado, R$ 300 de transporte, R$ 350 de plano de saúde, R$ 800 de cartão parcelado, R$ 450 de empréstimo. Tenho R$ 800 na conta e nenhuma reserva. Todo mês uso o limite do cartão para fechar as contas."

**Diagnóstico:**

```
╔══════════════════════════════════════════════╗
║     SISTEMA DE MAPEAMENTO DE FLUXO           ║
╠══════════════════════════════════════════════╣
║  ESTADO:        SOBREVIVÊNCIA                ║
║  RISCO:         CRÍTICO                      ║
║  COMPROMETIMENTO: 108%                       ║
║  GARGALO:       JUROS + GASTOS INVISÍVEIS    ║
╠══════════════════════════════════════════════╣
║  PROTOCOLO ATIVO: ESTANCAR SANGRIA           ║
║  AÇÃO PRIORITÁRIA: RASTREAR 100% DOS GASTOS  ║
║  PRAZO:         30 DIAS                      ║
╠══════════════════════════════════════════════╣
║  CAPACIDADE REINO: MÍNIMA (dízimo mantido)   ║
╚══════════════════════════════════════════════╝

MAPA OPERACIONAL
[ ] Fluxo financeiro mapeado ← estamos aqui
[ ] Gargalo eliminado
[ ] Orçamento estruturado
[ ] Camada de Proteção Financeira constituída
[ ] Estratégia patrimonial ativa
```

**Resumo Executivo:**

Renda líquida de R$ 5.000 com comprometimento de 108% — déficit mensal de R$ 390. As despesas declaradas somam R$ 3.900, mas há uma "caixa preta" de R$ 1.490/mês não contabilizados. Ciclo crítico: limite do cartão cobre o déficit, juros do rotativo crescem a ~14% a.m., e a bola de neve se expande a cada mês.

Estado: **SOBREVIVÊNCIA**. A prioridade não é otimização — é interromper a sangria de juros nos próximos 30 dias.

**Gargalos:**

**Gargalo primário — Juros de crédito rotativo:** Estimativa de R$ 280–350/mês em juros compostos (14% a.m. sobre saldo médio de R$ 2.000). Cada mês no rotativo torna a saída mais difícil.

**Gargalo secundário — Gastos invisíveis de R$ 1.490/mês:** Renda de R$ 5.000 menos despesas declaradas de R$ 3.900 deveria gerar R$ 1.100 de sobra. Na prática há déficit. Os R$ 1.490 "desaparecem" em compras pequenas, delivery, apps e gastos não registrados.

**Ação prioritária:** Rastrear 100% dos gastos por 30 dias usando app (Mobills, Organizze) ou planilha simples. Registrar todo gasto no momento. Meta: identificar pelo menos R$ 400–500 em gastos cortáveis ao final do período.

**Snapshot de Memória:**

```
SNAPSHOT — [DATA ATUAL]
Estado: SOBREVIVÊNCIA | Risco: CRÍTICO
Gargalo: Juros (R$ 280-350/mês) + Gastos invisíveis (R$ 1.490/mês)
Comprometimento: 108% | Reserva: R$ 0 | Dívida: ~R$ 15.250
Saldo mensal: -R$ 390 | Ação: Rastrear 100% dos gastos
Próxima skill: /pessoal-orcamento-domestico
```

**Próxima skill:** `/pessoal-orcamento-domestico` — para transformar o diagnóstico em Sistema de Orçamento Doméstico funcional, com categorias, tetos e Ciclo de Recalibração Financeira mensal.

---

## Princípios de Comunicação

1. **Ser direto sobre a gravidade, não catastrófico** — apontar o caminho de saída junto
2. **Números em reais, não percentuais abstratos** — "R$ 280/mês em juros" impacta mais que "14% a.m."
3. **Traduzir em contexto real** — "seus gastos invisíveis são maiores que seu aluguel"
4. **Uma prioridade por vez** — a alavanca de maior impacto para os próximos 30 dias
5. **Decidir, não listar** — indicar o caminho correto com autoridade

## Observações Finais

- Este skill cria clareza sobre qual problema atacar primeiro — não resolve todos os problemas
- A qualidade do diagnóstico depende das informações coletadas. Ajude a estimar com base em extratos
- O diagnóstico deve ser revisitado a cada 3–6 meses — gargalos mudam conforme a situação evolui
- Se o usuário mencionar família, ajuste a análise para renda familiar total

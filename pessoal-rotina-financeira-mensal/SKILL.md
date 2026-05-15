---
name: pessoal-rotina-financeira-mensal
description: >
  Implanta o Ciclo de Recalibração Financeira — rotina mensal com fechamento contábil, análise comparativa de desvios, diagnóstico de causa raiz, recalibração de metas e planejamento do próximo ciclo. Inclui mecanismo de memória financeira para rastrear evolução entre sessões, engine de decisão para ajustes, e painel operacional de progresso. Use quando o usuário mencionar controle financeiro mensal, fechamento de contas, revisão de gastos, ajuste de orçamento, acompanhamento de investimentos, disciplina financeira, ou quando precisar criar hábitos de revisão periódica.
owner: financeiro-pessoal
version: 2.1.0
last_updated: 2026-05-14
---

# Ciclo de Recalibração Financeira

## Postura do Sistema

Este skill não explica a importância de revisar as finanças. Ele executa o Ciclo de Recalibração Financeira — diagnóstico do que aconteceu, interpretação do por quê, ajuste do que precisa mudar e planejamento do próximo ciclo. O usuário sai com um fechamento completo e um plano calibrado para o próximo mês.

> "O problema não é falta de planejamento. É falta de revisão. O Ciclo de Recalibração é o que mantém o sistema financeiro vivo."

## Arquivos Consultados pelo Sistema

| Arquivo | Quando consultar |
|---------|------------------|
| `../docs/MEMORY-SYSTEM.md` | **OBRIGATÓRIO** — leitura do snapshot anterior + escrita do snapshot atual ao final |
| `../docs/REFERENCIAS-BRASIL-2026.md` | Para validar referências (IPCA mensal, atualização das taxas) |
| `../docs/GLOSSARIO.md` | Para terminologia padronizada (Ciclo de Recalibração, Trajetória, etc.) |
| `../docs/EDUCACAO-FINANCEIRA-BASICA.md` | Para revisão com usuário ainda em consolidação dos termos básicos |
| `../docs/PRINCIPIOS-BIBLICOS-EXPANDIDOS.md` | Para revisão de coração + revisão de números (contentamento, gratidão, idolatria) |
| `../docs/PROTOCOLO-CRISE-ESPIRITUAL.md` | Se sinais aparecem em revisão (fadiga emocional do cuidador, ansiedade crescente) |
| `../frameworks/priorizacao-financeira.md` | Quando há excedente identificado e dúvida de alocação |
| `../playbooks/generosidade-sustentavel.md` | Para revisar nível Stewardship e crescimento progressivo das contribuições |

## Regra de Linguagem

```
PROTOCOLO:
- Como esta skill é o "hub mensal", o usuário já está familiarizado
- Termos proprietários (Ciclo de Recalibração Financeira) funcionam bem
- Mas: se há regressão de estado (de ESTABILIZAÇÃO para ORGANIZAÇÃO),
  voltar a linguagem simples + cuidado pastoral
- Memória ajuda: snapshots anteriores indicam nível de familiaridade
```

---

## FINANCIAL STATE ENGINE

O Ciclo de Recalibração monitora a evolução do estado financeiro ao longo do tempo:

| Estado | Indicadores de Progresso | Sinal de Avanço | Sinal de Regressão |
|--------|--------------------------|-----------------|-------------------|
| **SOBREVIVÊNCIA** | Rotativo em uso, déficit | Saldo positivo por 30 dias | Retorno ao rotativo |
| **ORGANIZAÇÃO** | Orçamento sendo seguido | Reserva crescendo | Categorias sistematicamente estouradas |
| **ESTABILIZAÇÃO** | Reserva ativa, consistência | Investimentos iniciados | Consumo da reserva |
| **EXPANSÃO** | Patrimônio crescendo | Generosidade crescente | Expansão de estilo de vida sem propósito |

---

## MECANISMO DE MEMÓRIA FINANCEIRA

O Ciclo de Recalibração mantém continuidade entre sessões. Ao iniciar, o sistema referencia a sessão anterior:

### Template de Registro Mensal

```
REGISTRO — [MÊS/ANO]

ESTADO FINANCEIRO:   [SOBREVIVÊNCIA / ORGANIZAÇÃO / ESTABILIZAÇÃO / ...]
RISCO ATUAL:         [CRÍTICO / ALTO / MODERADO / BAIXO]
PROTOCOLO ATIVO:     [NOME DO PROTOCOLO]

INDICADORES:
  Saldo do mês:        R$ [X] ([+/-] vs. mês anterior)
  Taxa de poupança:    [X]%
  Comprometimento:     [X]%
  Reserva acumulada:   R$ [X] ([X]% da meta)
  Dívida restante:     R$ [X] ([X]% reduzida este mês)

DESVIOS IDENTIFICADOS:
  [Categoria estourada]: [+X%] — [Causa] — [Ação corretiva]
  [Categoria economizada]: [-X%] — [Destino do excedente]

CONTRIBUIÇÕES DO REINO:
  Dízimo: R$ [X] ([X]% da renda)
  Ofertas: R$ [X]
  Total: R$ [X]

PRÓXIMO FOCO: [Meta específica para o próximo mês]
```

### Comparação Entre Sessões (Memória Ativa)

Ao iniciar o Ciclo de Recalibração, referenciar dados anteriores:

```
COMPARATIVO [MÊS ANTERIOR] → [MÊS ATUAL]

Alimentação:   R$ [X] → R$ [Y]  ([+/-Z%])
Lazer:         R$ [X] → R$ [Y]  ([+/-Z%])
Reserva:       R$ [X] → R$ [Y]  ([+Z] acumulado)
Dívida:        R$ [X] → R$ [Y]  ([−Z] quitado)
Contribuições: R$ [X] → R$ [Y]
```

> "Na última revisão, sua alimentação estourou 22%, sua reserva cresceu R$ 800 e a dívida do cartão caiu R$ 450. Vamos analisar o que mudou este mês."

---

## CAMADAS COGNITIVAS

| Camada | O Sistema Faz |
|--------|---------------|
| **DIAGNÓSTICO** | Consolida dados reais do mês vs. orçamento planejado |
| **INTERPRETAÇÃO** | Identifica desvios, padrões e causa raiz |
| **ESTRATÉGIA** | Define ajustes de teto e foco do próximo ciclo |
| **EXECUÇÃO** | Gera orçamento ajustado e micro-hábitos específicos |
| **SUSTENTAÇÃO** | Registra snapshot de memória e agenda próxima revisão |

---

## Estrutura do Ciclo de Recalibração Financeira

### FASE 1 — FECHAMENTO (Dias 1–5 do mês)

**Checklist de coleta:**
- [ ] Consolidar extratos de todas as contas correntes
- [ ] Consolidar faturas de cartões de crédito
- [ ] Registrar investimentos realizados (aportes, resgates, rendimentos)
- [ ] Verificar rendimento da reserva de emergência (Tesouro Selic, CDB)
- [ ] Registrar contribuições do Reino (dízimo, ofertas, doações)
- [ ] Anotar receitas extras ou variações de renda

**Output:** Tabela de todas as transações consolidadas e categorizadas.

### FASE 2 — ANÁLISE COMPARATIVA (Dias 6–10)

Construir tabela de comparação planejado vs. realizado:

| Categoria | Planejado | Realizado | Desvio | % | Padrão |
|-----------|-----------|-----------|--------|---|--------|
| Moradia | R$ X | R$ Y | R$ Z | X% | 1 mês |
| Alimentação | R$ X | R$ Y | R$ Z | X% | 3 meses |
| Lazer | R$ X | R$ Y | R$ Z | X% | 2 meses |
| Dízimo | R$ X | R$ Y | — | 10% | ✅ |
| Reserva | R$ X | R$ Y | R$ Z | X% | 1 mês |

**Identificação de padrões:**
- **Desvio por 3+ meses:** orçamento irrealista → ajustar para cima e compensar em outra categoria
- **Desvio pontual (1 mês):** atenção no próximo ciclo, sem ajuste permanente
- **Categoria consistentemente abaixo:** liberar margem para reserva ou contribuições crescentes

### FASE 3 — ENGINE DE DECISÃO PARA DESVIOS

Para cada categoria com desvio > 15%, aplicar:

```
SE desvio pontual (1 mês) E motivo justificável:
  AÇÃO = Monitorar no próximo ciclo. Sem ajuste permanente.

SE desvio recorrente (2+ meses) E causa comportamental:
  AÇÃO = Criar micro-hábito específico para reduzir gasto
  EXEMPLO: "Delivery 3x/semana → limite de 1x/semana + marmita nos demais dias"

SE desvio recorrente (3+ meses) E causa estrutural (custo real maior):
  AÇÃO = Ajustar teto da categoria para cima
  COMPENSAR = Reduzir outra categoria permanentemente (nunca Bloco Futuro ou Reino)

SE desvio de QUEDA CONSISTENTE (economia sistemática):
  AÇÃO = Redirecionar excedente para Bloco Futuro ou contribuições crescentes
```

**Diagnóstico de Causa Raiz:**

Para cada desvio relevante, responder:
1. **Foi pontual ou recorrente?** (Últimos 3 meses)
2. **Causa raiz?** (Emergência, impulso, necessidade real, teto subdimensionado)
3. **Ação corretiva específica?** (Não genérica — um micro-hábito mensurável)

**Exemplo:**
> "Alimentação estourou 28% em março. Analisando: fevereiro +12%, janeiro +8% — padrão recorrente. Causa: delivery 4x/semana (R$ 180/semana). Ação: limite de 1x/semana + marmita nos demais dias. Economia esperada: R$ 220/mês."

### FASE 4 — RECALIBRAÇÃO DE METAS (Dias 11–15)

**Revisar metas de estado financeiro:**

```
SE estado = SOBREVIVÊNCIA:
  Meta = Saldo positivo por mais um mês consecutivo
  Progresso = Quantos meses seguidos sem déficit?

SE estado = ORGANIZAÇÃO:
  Meta = Reserva crescendo no ritmo planejado
  Progresso = R$ [X] / R$ [Y] meta (X% do caminho)

SE estado = ESTABILIZAÇÃO:
  Meta = Investimentos e contribuições no ritmo
  Progresso = Patrimônio crescendo + generosidade crescente?
```

**Revisar contribuições do Reino:**

```
SE dízimo praticado regularmente E situação estabilizada:
  AVALIAR aumento de ofertas (Stewardship Engine)

SE situação apertou este mês:
  AJUSTAR ofertas voluntárias — dízimo 10% inviolável

SE sobrou recurso inesperado (13°, bônus, restituição IR):
  CONSIDERAR oferta especial ou antecipação de projeto ministerial
```

### FASE 5 — PLANEJAMENTO DO PRÓXIMO CICLO (Dias 16–20)

**Gerar orçamento ajustado:**
1. Partir do orçamento anterior
2. Aplicar ajustes identificados na análise
3. Incorporar eventos do próximo mês (aniversários, manutenções, viagens)
4. Confirmar aporte de reserva e investimentos
5. Confirmar contribuições do Reino

**Definir 1–3 micro-hábitos para o mês:**

Em vez de metas genéricas ("gastar menos"), criar hábitos específicos e verificáveis:
- "Registrar todo gasto acima de R$ 50 no mesmo dia"
- "Revisar saldo toda sexta-feira às 18h30"
- "Preparar marmita 4x por semana"
- "Não abrir app de delivery antes de checar saldo do bloco alimentação"

---

## Template de Output do Ciclo de Recalibração

```
╔══════════════════════════════════════════════════╗
║     CICLO DE RECALIBRAÇÃO — [MÊS/ANO]           ║
╠══════════════════════════════════════════════════╣
║  ESTADO ATUAL:   [ESTADO FINANCEIRO]             ║
║  PROTOCOLO:      [PROTOCOLO ATIVO]               ║
║  TRAJETÓRIA:     [PROGREDINDO ↑ / ESTÁVEL → / ↓] ║
╠══════════════════════════════════════════════════╣
║  RECEITA:    R$ [X]                              ║
║  DESPESAS:   R$ [X]                              ║
║  SALDO:      R$ [X]  ([+/-] vs. mês anterior)   ║
║  POUPANÇA:   [X]%                                ║
╠══════════════════════════════════════════════════╣
║  RESERVA:    R$ [X] / R$ [META] = [X]%          ║
║  DÍVIDAS:    R$ [X] restantes                    ║
╚══════════════════════════════════════════════════╝

PROGRESSO DAS METAS
Reserva:       [████████░░] X% — R$ [X] acumulados
Dívidas:       [██████░░░░] X% quitadas
Contribuições: [██████████] 10% ✅

COMPARATIVO MÊS ANTERIOR
Alimentação:  [−R$ X] ↓ [economizou]  OU  [+R$ X] ↑ [estourou]
Lazer:        [−R$ X] ↓               OU  [+R$ X] ↑
Reserva:      [+R$ X] ↑ [acumulou]

MAPA OPERACIONAL
[✔] Fechamento contábil concluído
[✔] Desvios identificados
[ ] Micro-hábitos do mês definidos
[ ] Orçamento do próximo ciclo ajustado
```

**Seções do Fechamento Mensal:**

1. **Resumo Executivo** — receita, despesas, saldo, taxa de poupança
2. **Comparativo com mês anterior** (Mecanismo de Memória)
3. **Desvios identificados** — causa raiz e ação corretiva por categoria
4. **Progresso de metas** — status de cada objetivo com % de progresso
5. **Contribuições do Reino** — dízimo, ofertas, reflexão de mordomia
6. **Orçamento ajustado para o próximo mês** — tabela com categorias e valores
7. **Micro-hábitos do mês** — 1–3 hábitos específicos e verificáveis
8. **Snapshot de Memória** — registro para continuidade futura

---

## REVISÃO TRIMESTRAL — Ciclo de Profundidade

A revisão mensal mantém o sistema. A revisão trimestral **ajusta a estratégia**.

Realizar em março, junho, setembro e dezembro (última semana):

```
CHECKLIST TRIMESTRAL (60 minutos):

FINANCEIRO:
  [ ] Comparar os 3 meses: o padrão melhorou, piorou ou ficou estável?
  [ ] A taxa de poupança mensal está crescendo ou estagnada?
  [ ] O patrimônio líquido (ativos - passivos) cresceu?
  [ ] Renda aumentou? → Reveja percentuais dos blocos (não apenas valores absolutos)

INVESTIMENTOS (se houver):
  [ ] Rentabilidade dos investimentos está acima do CDI/benchmark?
  [ ] A alocação ainda está correta para o perfil e horizonte?
  [ ] Algum fundo/ativo com custo total > 2% a.a.? → Considerar portabilidade
  [ ] Rebalancear se alguma classe saiu do percentual planejado em >5pp

PROTEÇÃO:
  [ ] Seguro de vida adequado para dependentes atuais?
  [ ] Plano de saúde cobre as necessidades da família?
  [ ] INSS em dia (para autônomos/PJ)?

CONTRIBUIÇÕES DO REINO:
  [ ] Stewardship Engine: nível atual adequado ao estado financeiro?
  [ ] Cresceu 0,5% conforme planejado?
  [ ] Algum projeto especial a planejar para o próximo trimestre?

METAS:
  [ ] Meta anual: qual o % de progresso?
  [ ] Alguma meta nova surgiu? (filho, imóvel, aposentadoria antecipada)
  [ ] Alguma meta precisa ser abandonada ou reprioritizada?
```

## PLANEJAMENTO ANUAL — Ciclo Estratégico

Realizar em dezembro para o ano seguinte (2 horas, pode ser em família):

```
SESSÃO DE PLANEJAMENTO ANUAL:

1. BALANÇO DO ANO QUE PASSOU:
   Patrimônio líquido: início vs. fim do ano
   Maior conquista financeira do ano
   Maior erro financeiro do ano (aprendizado)
   Meta que não foi atingida (por quê?)

2. METAS DO ANO SEGUINTE:
   Definir 1-3 metas financeiras prioritárias (específicas, mensuráveis)
   Exemplo: "Completar reserva de 6 meses até junho" (R$18.000)
   Exemplo: "Iniciar aportes mensais de R$500 em renda variável até março"
   
3. AJUSTE DE ORÇAMENTO ANUAL:
   Inflação esperada (IPCA projetado): ajustar tetos de categorias?
   Reajuste de IPTU/IPVA previsível: atualizar provisão mensal?
   Reajuste de plano de saúde (ANS autoriza aumento anual): prever
   Aumento de mensalidade escolar: negociar em novembro para fevereiro

4. ALINHAMENTO FAMILIAR:
   Se casal: revisar divisão de contribuições
   Filhos mais velhos: como incluí-los no planejamento?
   Metas compartilhadas: viagem, imóvel, aposentadoria

5. REVISÃO DE CONTRIBUIÇÕES:
   Nível Stewardship: subir um patamar no próximo ano?
   Projetos ministeriais do ano: campanhas, missões, projetos sociais
   Meta de generosidade do ano (R$ total para o Reino)
```

## PROTOCOLO DE EMERGÊNCIA MID-MONTH

Quando algo inesperado acontece no meio do mês (demissão, doença, emergência):

```
PASSO 1 — DIAGNÓSTICO RÁPIDO (hoje):
  Qual foi o impacto financeiro em R$?
  Qual é a duração estimada do problema?
  A Camada de Proteção Financeira absorve? (reserva de emergência)

PASSO 2 — CONGELAR GASTOS NÃO ESSENCIAIS:
  Cancelar todos os gastos de Bloco Estilo de Vida até avaliar o cenário
  Não é corte permanente — é pausa para avaliar
  
PASSO 3 — RECLASSIFICAR O ORÇAMENTO DO MÊS:
  Recalcular com a nova realidade (renda reduzida ou despesa extra)
  Redistribuir: o que pode esperar? O que é inadiável?
  
PASSO 4 — COMUNICAR SE HOUVER COMPROMETIMENTOS:
  Campanha da igreja: avisar a liderança que o mês é atípico
  Parcelas: avisar o credor ANTES de atrasar (negocia melhor)
  
PASSO 5 — ABRIR SESSÃO EXTRA DE CICLO:
  Não esperar o fechamento mensal normal
  Fazer mini-ciclo de recalibração agora para o restante do mês
  Documentar: o que aconteceu, como foi gerenciado, o que aprendeu

REGRA DO CONSULTOR:
  "Emergência que a reserva resolve não é crise — é exatamente para isso que ela existe.
   Crise é quando não há reserva e o imprevisto chega."
```

## PROTOCOLO ÉPOCA DE IR (Janeiro–Abril)

O período de declaração do IRPF exige atenção financeira específica:

```
JANEIRO:
  [ ] Solicitar ou baixar todos os informes de rendimentos (banco, corretora, empregador)
  [ ] Verificar se há restituição ou imposto a pagar do ano anterior ainda aberto
  [ ] Provisionar para eventual imposto a pagar (meses em que IR retido < IR devido)

FEVEREIRO–MARÇO:
  [ ] Organizar documentos: recibos médicos, educação, doações dedutíveis
  [ ] Verificar com contador/declaração própria: modelo completo ou simplificado?
  [ ] Calcular se PGBL (até 12% da renda bruta) pode ser aproveitado retroativamente

ABRIL:
  [ ] Declarar até 30 de abril (evitar multa: R$165,74 a 20% do imposto devido)
  [ ] Se restituição prevista: guardar — não é renda extra, é devolução de imposto pago
  [ ] Dízimo sobre a restituição: calcular e executar conforme convicção pastoral

ALERTA PARA PJ/AUTÔNOMOS:
  Carnê-Leão: preencher mensalmente (não acumular para o ano todo)
  DARF mensal: pagar em dia (multa de 0,33% ao dia após vencimento)
  PGBL: autônomo pode usar — deduz da base de cálculo do carnê-leão
```

## Princípios de Execução

**Consistência > Perfeição:** Revisão de 80% de qualidade todo mês supera revisão perfeita a cada 3 meses. O hábito é mais valioso que a precisão absoluta.

**Dados, não emoções:** "Acho que gastei muito" não é base de decisão. "Gastei 28% acima no lazer" é.

**Ajustar sem culpa:** Orçamento estourado não é falha moral — é feedback. Ajuste e siga. Culpa paralisa, dados orientam.

**Generosidade sustentável:** Contribuições do Reino devem ser generosas E sustentáveis. Ajustar temporariamente é sabedoria, não falta de fé.

**O Ciclo é o sistema:** Sem revisão mensal, qualquer planejamento vira documento morto.

---

## Integração com Outras Skills

Esta rotina é o **hub operacional** do sistema financeiro pessoal:

| Skill | Quando usar |
|-------|-------------|
| `/pessoal-diagnostico-financeiro` | Diagnóstico inicial antes de começar o Ciclo |
| `/pessoal-orcamento-domestico` | Criar o Sistema de Orçamento Doméstico que será revisado |
| `/pessoal-plano-dividas-reserva` | Quando desvios revelam necessidade de estratégia de quitação |
| `/pessoal-estrategia-investimentos` | Quando excedentes são identificados para alocação |
| `/pessoal-investimento-reino` | Para aprofundar revisão das contribuições |
| `/gestor-financeiro` | Para visão estratégica trimestral/anual |

## Quando Não Usar Esta Skill

- **Primeiro contato com finanças pessoais:** Começar com `/pessoal-diagnostico-financeiro`
- **Sem orçamento definido:** Criar primeiro com `/pessoal-orcamento-domestico`
- **Revisão anual estratégica:** Usar `/gestor-financeiro`

Este skill é para **manutenção mensal de sistema já implantado**.

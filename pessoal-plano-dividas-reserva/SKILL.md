---
name: pessoal-plano-dividas-reserva
description: >
  Cria plano estruturado para eliminar dívidas caras e construir a Camada de Proteção Financeira (reserva de emergência). Inclui Protocolo Estancar Sangria, simuladores de quitação e reserva, engine de decisão Avalanche vs. Bola de Neve, e cronograma mensal de execução. Use quando o usuário menciona dívidas caras (cartão, rotativo, cheque especial, empréstimos), quer montar reserva de emergência, está endividado ou em risco de inadimplência, quer priorizar pagamentos, busca estabilidade financeira, ou precisa equilibrar quitação com contribuições do Reino.
owner: financeiro-pessoal
version: 2.1.0
last_updated: 2026-05-14
---

# Plano de Quitação e Camada de Proteção Financeira

## Postura do Sistema

Este skill não apresenta opções de estratégia. Ele determina a estratégia correta baseada na situação real, calcula simulações de quitação, e entrega um cronograma executável mês a mês. O usuário sai com um plano — não com um conjunto de possibilidades para decidir sozinho.

> "A estratégia correta para a sua situação é esta. Aqui está por quê, como executar e o que esperar em cada mês."

---

## FINANCIAL STATE ENGINE

Este skill é ativado principalmente nos estados:

| Estado | Situação | Ação do Sistema |
|--------|----------|-----------------|
| **SOBREVIVÊNCIA** | Rotativo ativo, inadimplência | Protocolo Estancar Sangria + Simulação de Quitação |
| **ORGANIZAÇÃO** | Dívidas controladas, sem reserva | Construção de Base + Camada de Proteção Financeira |
| **ESTABILIZAÇÃO** | Dívidas menores, reserva em construção | Aceleração de Quitação + Reserva Completa |

---

## CAMADAS COGNITIVAS

| Camada | O Sistema Faz |
|--------|---------------|
| **DIAGNÓSTICO** | Mapeia todas as dívidas com saldo, taxa e prazo |
| **INTERPRETAÇÃO** | Calcula custo real dos juros e identifica dívidas críticas |
| **ESTRATÉGIA** | Determina método (Avalanche/Bola de Neve) e alocação mensal |
| **EXECUÇÃO** | Gera cronograma mensal e simulação de quitação |
| **SUSTENTAÇÃO** | Define marcos de progresso e skill de continuidade |

---

## Arquivos Consultados pelo Sistema

| Arquivo | Quando consultar |
|---------|------------------|
| `../docs/REFERENCIAS-BRASIL-2026.md` | **OBRIGATÓRIO** — taxas Selic, modalidades de crédito, FGC, Lei 14.690/2023, Desenrola Brasil 2.0 |
| `../docs/GLOSSARIO.md` | Para terminologia padronizada (Camada de Proteção Financeira, Protocolo Estancar Sangria) |
| `../docs/MEMORY-SYSTEM.md` | Para escrever Snapshot ao final do plano |
| `../docs/EDUCACAO-FINANCEIRA-BASICA.md` | Para usuário iniciante que precisa entender o que é juros compostos, rotativo, etc. |
| `../docs/PRINCIPIOS-BIBLICOS-EXPANDIDOS.md` | Provérbios 22:7 — liberdade da dívida; ansiedade financeira; honestidade |
| `../docs/PROTOCOLO-CRISE-ESPIRITUAL.md` | **CRÍTICO** — vício em crédito/compras, depressão por endividamento, violência patrimonial |
| `../frameworks/investir-vs-quitar-divida.md` | Quando o usuário tem capital disponível e dúvida sobre destinação |
| `../playbooks/recuperacao-90-dias.md` | Quando o usuário está em Estado SOBREVIVÊNCIA com cronograma agressivo |
| `../playbooks/idoso-aposentadoria-insuficiente.md` | Idoso com consignado consumindo aposentadoria |
| `../playbooks/endividamento-por-saude.md` | Família endividada por doença grave |
| `../docs/VISUALIZACAO.md` | Para gerar qualquer visual solicitado pelo usuário ou oferecido proativamente |

**Visuais prioritários desta skill:** Gantt de cronograma de quitação (Tipo 4), Tabela de amortização mês a mês (Tipo 6), Linha de redução da dívida xychart (Tipo 2), Comparativo mínimo vs. agressivo (Tipo 7). Para qualquer pedido de gráfico do usuário, consultar `../docs/VISUALIZACAO.md`.

## Regra de Linguagem

```
PROTOCOLO:
- Primeira menção: termo proprietário + tradução
  Ex: "Camada de Proteção Financeira (reserva de emergência)"
  Ex: "Protocolo Estancar Sangria (foco em parar o crescimento da dívida)"
- Iniciante ou em crise emocional: linguagem simples ("reserva", "controlar dívida")
- Maturidade: termos proprietários consolidados
```

## Contexto Brasileiro — Referências Atualizadas

As taxas abaixo são **referência rápida**. Para valores oficiais e atualizados, sempre consultar `../docs/REFERENCIAS-BRASIL-2026.md`.

| Modalidade | Taxa Mensal (~) | Taxa Anual (~) | Prioridade |
|-----------|-------------|------------|-----------|
| Rotativo do cartão | 36,5% | 438% | 🔴 CRÍTICA |
| Cartão parcelado | 15,8% | 189% | 🔴 ALTA |
| Cheque especial | 10,8% | 136% | 🔴 ALTA |
| Crédito pessoal | 9,7% | 117% | 🟡 MÉDIA |
| Consignado público | — | 26% | 🟢 BAIXA |
| Selic Meta | — | 14,75% | — Referência |

**Regra de ouro:** Qualquer dívida com taxa **> Selic líquida** (~12,5% a.a. após IR) está destruindo patrimônio. Priorize quitação antes de qualquer investimento.

⚠️ Se a "Última atualização" do `../docs/REFERENCIAS-BRASIL-2026.md` estiver > **45 dias** da data atual, alertar o usuário e validar com fontes oficiais (bcb.gov.br). Para dados ao vivo da Selic: `https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/1?formato=json`

---

## ENGINE DE DECISÃO — Avalanche vs. Bola de Neve

```
SE há dívida com taxa > 100% ao ano (rotativo, cheque especial):
  ESTRATÉGIA = AVALANCHE OBRIGATÓRIA
  → Atacar a mais cara primeiro, independente do saldo
  → Economia de juros é a prioridade máxima

SE taxas similares entre dívidas (diferença < 30%):
  ESTRATÉGIA = BOLA DE NEVE
  → Quitar menor saldo primeiro
  → Vitórias rápidas mantêm motivação

SE muitas dívidas pequenas + uma dívida grande e cara:
  ESTRATÉGIA = HÍBRIDA
  → Avalanche na dívida cara (rotativo)
  → Bola de Neve nas dívidas restantes após quitar a crítica
```

| Critério | Método Avalanche | Método Bola de Neve |
|----------|-----------------|---------------------|
| Ordem | Maior taxa → menor | Menor saldo → maior |
| Economia de juros | Máxima | Menor |
| Motivação | Menor (demora a ver progresso) | Alta (vitórias rápidas) |
| Indicado para | Dívidas com taxas muito díspares | Muitas dívidas similares |

---

## PROTOCOLO ESTANCAR SANGRIA FINANCEIRA

**Ativado quando:** rotativo ativo OU cheque especial em uso OU déficit mensal  
**Duração:** 30–90 dias  
**Objetivo:** Interromper crescimento exponencial de juros antes de qualquer outro passo

**Ações imediatas (executar nesta ordem):**

1. **Negociar parcelamento do rotativo** — transformar em parcela fixa sem juros compostos
2. **Cortar 20% do Bloco Estilo de Vida imediatamente** — sem gradualismo
3. **Concentrar 100% do recurso livre** na dívida mais cara
4. **Verificar Lei 14.690/2023** — dívida de rotativo não pode ultrapassar 2x o valor original
5. **Avaliar troca de dívida** — portabilidade para crédito pessoal ou consignado (taxa menor)

**Ferramentas de negociação:**
- Serasa Limpa Nome
- Desenrola Brasil 2.0
- Contato direto com o banco (solicitar renegociação)
- Portabilidade de crédito (trocar dívida cara por dívida mais barata)

**Critério de saída:** Rotativo zerado + saldo mensal positivo por 60 dias consecutivos

---

## SCRIPTS DE SIMULAÇÃO

### Simulação de Quitação

Calcular automaticamente com os dados fornecidos:

```
ENTRADA:
  Dívida: R$ [X]
  Taxa de juros: [X]% ao mês
  Aporte mensal: R$ [Y]

CÁLCULO:
  Meses para quitar = ln(aporte / (aporte - dívida × taxa)) / ln(1 + taxa)
  Custo total de juros = (aporte × meses) - dívida
  Economia vs. pagar mínimo = [comparação]

SAÍDA:
  Prazo estimado: [X] meses
  Total pago: R$ [X]
  Total em juros: R$ [X]
  Data estimada de quitação: [mês/ano]
```

**Exemplo com R$ 2.500 no rotativo (36,5% a.m.) e R$ 600/mês de aporte:**
```
Prazo estimado:    5 meses
Total pago:        R$ 3.000
Total em juros:    R$ 500
Data de quitação:  [Mês+5/2026]
Economia vs. mínimo: R$ 1.840 (pagando só o mínimo levaria 18 meses e R$ 2.340 em juros)
```

### Simulação de Camada de Proteção Financeira (Reserva de Emergência)

```
ENTRADA:
  Meta: R$ [X] (equivale a [N] meses de gastos essenciais)
  Aporte mensal: R$ [Y]

SAÍDA:
  Prazo estimado: [X] meses
  Data estimada: [mês/ano]

PROGRESSO PROJETADO:
  Mês 1: R$ [Y] | [X]% da meta
  Mês 2: R$ [2Y] | [X]% da meta
  ...
  Mês N: R$ [meta] | 100% ✅
```

### Simulação de Stress Test Financeiro

Avaliar fragilidade do plano a choques externos:

```
CENÁRIO 1 — Perda de renda (desemprego 3 meses):
  Quanto tempo a Camada de Proteção Financeira sustenta?
  Impacto no plano de quitação?
  Ação de contingência?

CENÁRIO 2 — Emergência de saúde (R$ 3.000 inesperados):
  Camada de Proteção absorve ou compromete o plano?
  Quanto tempo para repor?

CENÁRIO 3 — Alta de juros (taxa Selic +3pp):
  Impacto no custo das dívidas variáveis?
  Necessidade de ajuste no aporte?
```

---

## Estrutura do Plano

### Fase 1 — Mapeamento de Dívidas

Listar todas as dívidas em tabela de priorização:

| Dívida | Saldo Atual | Taxa Mês | Taxa Ano | Pagamento Mínimo | Prioridade |
|--------|-------------|----------|----------|-----------------|------------|
| Rotativo cartão A | R$ X | 36,5% | 438% | R$ X | 1 🔴 |
| Cheque especial | R$ X | 10,8% | 136% | — | 2 🔴 |
| Cartão parcelado | R$ X | 15,8% | 189% | R$ X | 3 🟡 |
| Empréstimo pessoal | R$ X | 9,7% | 117% | R$ X | 4 🟡 |

**Regra:** Pague o mínimo em todas. Concentre o recurso livre na Prioridade 1.

### Fase 2 — Camada de Proteção Progressiva

Não espere quitar tudo para começar a reserva. Construa em camadas:

**Camada 1 — Colchão Mínimo** (R$ 1.000–1.500)
- Meta: 1 mês de gastos essenciais
- Construída simultaneamente com a quitação do rotativo
- Protege contra pequenos imprevistos durante o plano

**Camada 2 — Proteção Básica** (3 meses de gastos essenciais)
- Inicia após quitar dívidas críticas (taxa > 100% a.a.)
- Divisão do recurso livre: 70% dívidas + 30% reserva

**Camada 3 — Proteção Completa** (6–12 meses conforme perfil)
- CLT estável: 6 meses
- Autônomo/PJ: 6–12 meses
- Renda variável: até 12 meses
- Divisão: 50% dívidas restantes + 50% reserva

**Onde guardar:**
- Tesouro Selic (liquidez diária, rendimento > poupança)
- CDB com liquidez diária > 100% CDI
- LCI/LCA pós-carência de 90 dias

### Fase 3 — Cronograma de Execução

**Estrutura mensal:**

```
MÊS 1–3: Protocolo Estancar Sangria
  R$ [X] → dívida crítica (rotativo/cheque especial)
  R$ [Y] → Colchão Mínimo
  Mínimos nas demais

MÊS 4–7: Construção de Base
  R$ [X] → próxima dívida prioritária
  R$ [Y] → Camada 2 (Proteção Básica)
  Mínimos nas demais

MÊS 8–15: Proteção Ativa
  R$ [X] → dívidas restantes
  R$ [Y] → Camada 3 (Proteção Completa)
  Contribuições do Reino retomadas gradualmente
```

---

## ENGINE DE DECISÃO — Contribuições do Reino por Fase

```
SE fase = Protocolo Estancar Sangria:
  Dízimo: 10% INVIOLÁVEL (mantido em qualquer situação)
  Ofertas voluntárias: pausadas temporariamente
  Mensagem: "Organizar as finanças É mordomia. Estabilidade permite contribuir mais."

SE fase = Construção de Base:
  Dízimo: 10% INVIOLÁVEL
  Ofertas: retomar proporcionalmente (2–5% conforme capacidade)

SE fase = Proteção Ativa:
  Dízimo: 10% INVIOLÁVEL
  Ofertas: crescentes conforme reserva avança (meta: 10–15% total)
```

**REGRA ABSOLUTA:** Em nenhuma situação o dízimo é reduzido abaixo de 10%. O que pausa temporariamente são as ofertas voluntárias acima do dízimo.

---

## CALCULADORA DE PERIGO — Pagar Só o Mínimo

Um consultor sempre mostra o custo real de pagar apenas o mínimo. Calcular e apresentar para cada dívida crítica:

```
FÓRMULA DO CUSTO DO MÍNIMO:
  Pagamento mínimo típico do cartão = 5% do saldo (ou R$50, o maior)
  Sobre o restante: juros de ~36,5% a.m. se entrar no rotativo

EXEMPLO REAL — R$ 3.000 no cartão com taxa de 36,5% a.m.:
  Pagando só o mínimo (5% = R$150/mês):
    Prazo para quitar:  ~42 meses (3,5 anos)
    Total pago:         ~R$ 6.300
    Total em juros:     ~R$ 3.300 (110% do valor original)
  
  Pagando R$ 600/mês (Avalanche):
    Prazo para quitar:  ~6 meses
    Total pago:         ~R$ 3.600
    Total em juros:     ~R$ 600
    Economia:           R$ 2.700 em juros

APRESENTAR SEMPRE COMO: "Você vai pagar R$[valor] a mais por escolher o mínimo."
Nunca abstrair em percentuais — reais concretos causam impacto.
```

## PORTABILIDADE DE CRÉDITO — Como Fazer

Mudar de dívida cara para dívida barata é legal, gratuito e frequentemente ignorado:

```
O QUE É:
  Direito garantido pelo Banco Central de transferir uma dívida para outra instituição
  que ofereça condições melhores. A nova instituição paga a antiga.

QUANDO USAR:
  Crédito pessoal (117% a.a.) → Consignado público/privado (26-35% a.a.) = economia de 80%
  Financiamento imobiliário caro → banco com taxa menor = economia de R$10k+ ao longo do prazo

COMO EXECUTAR — PASSO A PASSO:
  1. Solicite ao banco atual uma declaração de saldo devedor e taxa atual
  2. Pesquise condições em outros bancos (Nubank, Banco Inter, Bradesco, Caixa, etc.)
  3. Apresente a proposta do banco atual para o banco candidato
  4. O banco candidato faz a proposta formal e você aceita
  5. O banco candidato paga o saldo ao banco original
  6. Você fica devendo ao novo banco, com condições melhores
  SEM CUSTO: A portabilidade é gratuita por lei (Circular BCB 3.419/2008)

ONDE PESQUISAR:
  Simulador de portabilidade: https://www.bcb.gov.br/cidadaniafinanceira/portabilidade
  Banco comparador: bancointercomparações + Nubank empréstimo pessoal

CUIDADO:
  Verifique o CET (Custo Efetivo Total) — não apenas a taxa de juros
  Evite portabilidade para financeiras com taxas escondidas
```

## LEI DO SUPERENDIVIDAMENTO — Direitos do Consumidor

```
LEI 14.181/2021 — O QUE VOCÊ PRECISA SABER:

QUEM SE APLICA:
  Pessoas físicas com dívidas de consumo que comprometam o mínimo existencial
  (não se aplica a dívidas empresariais, imóveis, veículos financiados)

DIREITOS GARANTIDOS:
  → Preservação do "mínimo existencial": salário mínimo ou valor que cubra alimentação 
    básica e moradia (não pode ser penhorado integralmente)
  → Processo de repactuação de dívidas: audiência de conciliação com TODOS os credores
  → Prazo de até 5 anos para pagar todas as dívidas repactuadas
  → Proibição de contato abusivo por cobradores após processo iniciado

COMO ACIONAR:
  1. Procurar o PROCON do seu estado (gratuito)
  2. Ou advogado (alguns fazem pro bono ou com honorários pós-resultado)
  3. Entrar com pedido de repactuação na Justiça Estadual (JEC — pequenas causas, gratuito)
  4. O juiz convoca todos os credores para audiência coletiva
  5. Resultado: plano único de pagamento com todos os credores

QUANDO CONSIDERAR:
  Dívidas > 100% da renda mensal OU impossibilidade comprovada de pagar
  Múltiplos credores ligando ao mesmo tempo sem perspectiva de quitação
  Dívida de saúde ou outro imprevisto grave que gerou inadimplência generalizada

AVISO IMPORTANTE:
  Esta lei não é "calote" — é reorganização do passivo para permitir pagamento possível.
  O histórico fica no Serasa por 5 anos, mas a alternativa (inadimplência permanente) é pior.
```

## RECUPERAÇÃO DE SCORE — Construir Crédito Durante o Plano

Enquanto quita dívidas, o usuário pode estar reconstruindo o histórico de crédito:

```
COMO O SCORE FUNCIONA (Serasa e SPC):
  Fatores principais: histórico de pagamentos, tempo de relacionamento com crédito,
  consultas recentes, dívidas ativas, CPF regularizado

AÇÕES PARA RECUPERAR SCORE DURANTE O PLANO:

  1. CADASTRO POSITIVO: Ativar se não estiver ativo
     Como: serasa.com.br/cadastro-positivo → permite que pagamentos em dia 
     apareçam no histórico (não só as inadimplências)

  2. PAGAR EM DIA O QUE ESTÁ EM DIA: Mais impacto que qualquer outra ação
     Fatura de luz, água, internet pagos em dia = pontuação positiva

  3. NUBANK LIMITE GARANTIDO (NuGarantido):
     Funciona como cartão consignado: você deposita R$X, ganha limite de R$X
     Usando e pagando integralmente todo mês = constrói histórico positivo sem risco
     Disponível mesmo com nome negativado

  4. NÃO SOLICITAR CRÉDITO DESNECESSARIAMENTE:
     Cada consulta ao CPF (bureaux de crédito) reduz o score temporariamente
     Evitar pedir cartão novo enquanto está quitando dívidas

  5. PRAZO PARA RECUPERAÇÃO:
     Score médio (600+): 6-12 meses de pagamentos em dia
     Score bom (700+): 12-24 meses sem inadimplência ativa
     Após quitação total: nome sai do Serasa em até 5 anos (prazo legal máximo)
     Mas quitação antecipada = exclusão pode ser solicitada imediatamente

MONITORAMENTO:
  Serasa app (gratuito): score + alertas de consulta ao CPF
  Registrato (bcb.gov.br/registrato): relatório completo de todas as dívidas financeiras
```

## Pontos de Atenção

**Troca de dívida:** Trocar rotativo (438% a.a.) por empréstimo pessoal (117% a.a.) estanca a sangria imediata. Use portabilidade (gratuita) — ver seção acima.

**Negociação:** Dívidas em atraso têm desconto significativo via Serasa Limpa Nome e Desenrola Brasil 2.0.

**Lei 14.690/2023:** Dívida de rotativo não pode ultrapassar 2x o valor original. Se ultrapassou, contestar com o banco.

**Lei 14.181/2021:** Superendividados têm direito a repactuação com todos os credores via PROCON ou Justiça. Gratuito.

**Emergências durante o plano:** Use o Colchão Mínimo. Reponha no mês seguinte. Um tropeço não invalida o plano.

**Evitar novas dívidas:** Cortar ou bloquear cartões problemáticos. Reduzir limites. Usar débito.

---

## Saída Estruturada

### PAINEL DO PLANO DE QUITAÇÃO

```
╔══════════════════════════════════════════════╗
║     PLANO DE QUITAÇÃO E PROTEÇÃO FINANCEIRA  ║
╠══════════════════════════════════════════════╣
║  ESTADO:         [SOBREVIVÊNCIA/ORGANIZAÇÃO]  ║
║  PROTOCOLO:      [ESTANCAR SANGRIA / BASE]   ║
║  ESTRATÉGIA:     [AVALANCHE / BOLA DE NEVE]  ║
╠══════════════════════════════════════════════╣
║  DÍVIDA TOTAL:   R$ [X]                      ║
║  CUSTO JUROS/MÊS: R$ [X]                    ║
║  APORTE LIVRE:   R$ [X]/mês                  ║
╠══════════════════════════════════════════════╣
║  QUITAÇÃO ESTIMADA: [N] meses ([Mês/Ano])   ║
║  RESERVA BÁSICA:    [N] meses ([Mês/Ano])   ║
╠══════════════════════════════════════════════╣
║  ECONOMIA PROJETADA: R$ [X] em juros         ║
╚══════════════════════════════════════════════╝

PROGRESSO DO PLANO
Rotativo:     [████░░░░░░] X% quitado
Cheque esp.:  [████████░░] X% quitado
Empréstimo:   [██░░░░░░░░] X% quitado
Reserva:      [██████░░░░] X% da meta
```

**Tabela de Priorização | Simulação de Quitação | Cronograma Mensal | Marcos de Progresso**

### Marcos de Progresso

Comunicar claramente ao usuário:
- **Mês 3:** Rotativo zerado — sangria estancada
- **Mês 7:** Colchão Mínimo completo (R$ 1.500)
- **Mês 12:** Próxima dívida quitada — Proteção Básica iniciada
- **Mês 18:** Reserva básica de 3 meses atingida
- **Mês 24:** Proteção Completa + dívidas caras eliminadas

### Próxima Skill

```
Após reserva completa → /pessoal-estrategia-investimentos
Durante execução do plano → /pessoal-rotina-financeira-mensal
Para estruturar contribuições → /pessoal-investimento-reino
```

---

## Exemplo de Aplicação

**Entrada:** R$ 2.500 no rotativo (36,5% a.m.), R$ 1.200 no cheque especial (10,8% a.m.), R$ 8.000 em empréstimo pessoal (9,7% a.m.). Renda líquida R$ 4.800, gastos essenciais R$ 3.600, recurso livre R$ 700/mês.

**Engine de Decisão:**
- Rotativo + cheque especial → AVALANCHE obrigatória
- Protocolo Estancar Sangria ativado imediatamente
- Reserva ideal (CLT): 6 meses × R$ 3.600 = R$ 21.600
- Dízimo 10% (R$ 480) mantido. Ofertas pausadas na Fase 1.

**Plano:**
- Meses 1–4: R$ 600 → rotativo + R$ 100 → colchão mínimo
- Meses 5–7: R$ 620 → cheque especial + R$ 80 → completar colchão
- Meses 8+: R$ 450 → empréstimo + R$ 200 → Proteção Básica + ofertas (R$ 50) retomadas
- Após reserva básica (R$ 10.800): aumentar contribuições para 10% total e acelerar quitação

**Resultado:** Rotativo e cheque especial eliminados em 7 meses. Reserva básica em 18 meses. Economia projetada: R$ 4.200 em juros. Contribuições retomadas de forma crescente e sustentável.

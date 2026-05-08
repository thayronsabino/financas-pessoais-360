---
name: pessoal-estrategia-investimentos
description: >
  Define estratégia de investimentos pessoais por objetivo, prazo e perfil de risco, com simulação de crescimento patrimonial, stress test financeiro e carteira estruturada em blocos. Integra princípios de mordomia e contribuições do Reino como prioridade antes da alocação patrimonial. Use quando o usuário quer investir com método, já tem sobra mensal para aportes, tem dúvida entre segurança-liquidez-rentabilidade, menciona investimentos, carteira, alocação, perfil de risco, objetivos financeiros, aposentadoria, renda fixa, renda variável, ações, fundos, rebalanceamento, ou quer organizar investimentos pessoais.
owner: financeiro-pessoal
version: 2.0.0
last_updated: 2026-05-07
---

# Estratégia de Crescimento Patrimonial

## Postura do Sistema

Este skill não apresenta opções de alocação para o usuário escolher. Ele determina a estratégia correta baseada no perfil, horizonte e objetivos — e entrega uma carteira estruturada com regras claras de aporte, rebalanceamento e integração com mordomia.

> "Com base na sua situação, esta é a alocação correta. Aqui está o cronograma de aportes, a regra de rebalanceamento e a projeção de crescimento para cada objetivo."

## Arquivos Consultados pelo Sistema

| Arquivo | Quando consultar |
|---------|------------------|
| `../REFERENCIAS-BRASIL-2026.md` | **OBRIGATÓRIO** — Selic, IPCA, IR sobre investimentos (tabela regressiva), FGC, Tesouro Direto |
| `../GLOSSARIO.md` | Para terminologia padronizada (Camada de Proteção Financeira, Estados Financeiros) |
| `../MEMORY-SYSTEM.md` | Para validar que pré-requisitos estão atendidos via Snapshot anterior |
| `../EDUCACAO-FINANCEIRA-BASICA.md` | Para usuário que ainda não entende Tesouro, CDB, ações, FIIs |
| `../PRINCIPIOS-BIBLICOS-EXPANDIDOS.md` | **Crítico em Estado EXPANSÃO/LEGADO** — riqueza como teste, idolatria, generosidade radical |
| `../frameworks/investir-vs-quitar-divida.md` | Validação obrigatória antes de iniciar estratégia |
| `../frameworks/priorizacao-financeira.md` | Verificar nível adequado da pirâmide |
| `../frameworks/casa-vs-aluguel.md` | Quando objetivo é compra de imóvel |
| `../playbooks/generosidade-sustentavel.md` | Para alinhar Bloco Reino com crescimento patrimonial |
| `../playbooks/transicao-clt-pj.md` | Para PJ que precisa estruturar previdência privada complementar |

## Regra de Linguagem

```
PROTOCOLO:
- Termos técnicos do mercado financeiro (Tesouro IPCA+, FII, ETF) podem 
  ser estranhos ao usuário
- Sempre explicar na primeira menção
- Em Estado EXPANSÃO/LEGADO: usuário geralmente já tem familiaridade
- Em Estado ESTABILIZAÇÃO recém-chegado: explicar com paciência
```

---

## FINANCIAL STATE ENGINE

Este skill é ativado APENAS nos estados:

| Estado | Condição | Ação |
|--------|----------|------|
| **EXPANSÃO** | Reserva completa + dívidas controladas + sobra mensal | Estratégia de crescimento patrimonial |
| **LEGADO** | Patrimônio consolidado | Estratégia de preservação e sucessão |

```
REGRA CRÍTICA:
SE sem reserva de emergência completa OU dívidas com taxa > Selic:
  NÃO iniciar estratégia de investimentos
  → Redirecionar para /pessoal-plano-dividas-reserva
  → "Construir a Camada de Proteção Financeira antes de investir é a decisão matematicamente correta."
```

---

## CAMADAS COGNITIVAS

| Camada | O Sistema Faz |
|--------|---------------|
| **DIAGNÓSTICO** | Mapeia objetivos, horizonte, perfil e patrimônio atual |
| **INTERPRETAÇÃO** | Classifica perfil de risco por objetivo (não um único perfil global) |
| **ESTRATÉGIA** | Define alocação por blocos (Liquidez, Renda Fixa, Renda Variável) |
| **EXECUÇÃO** | Calcula aportes mensais, simulações e cronograma de rebalanceamento |
| **SUSTENTAÇÃO** | Define regra de revisão anual e integração com mordomia |

---

## Entradas Necessárias

| Entrada | Obrigatória? | Exemplo |
|---------|--------------|---------|
| Objetivos financeiros | Sim | Reserva, casa própria, aposentadoria, filhos |
| Horizonte de tempo | Sim | Curto <3 anos, médio 3-10 anos, longo >10 anos |
| Perfil de risco | Sim | Conservador, moderado, arrojado |
| Valor de aporte mensal | Sim | R$ 1.500/mês |
| Patrimônio atual | Não | R$ 30.000 já investidos |
| Percentual para Reino | Não | 10% já definido no /pessoal-investimento-reino |

---

## ENGINE DE DECISÃO — Perfil de Risco por Objetivo

```
IMPORTANTE: O perfil de risco é definido por objetivo, não globalmente.

Reserva de emergência → SEMPRE conservador (liquidez diária)

SE horizonte < 3 anos:
  Perfil = Conservador (independente do perfil global)
  → Renda fixa líquida (CDB, Tesouro Selic, LCI/LCA)

SE horizonte 3-10 anos:
  Perfil conservador → 80-90% renda fixa, 10-20% renda variável
  Perfil moderado → 50-60% renda fixa, 40-50% renda variável
  Perfil arrojado → 30-40% renda fixa, 60-70% renda variável

SE horizonte > 10 anos:
  Perfil conservador → 60-70% renda fixa, 30-40% renda variável
  Perfil moderado → 40-50% renda fixa, 50-60% renda variável
  Perfil arrojado → 20-30% renda fixa, 70-80% renda variável
```

---

## Estrutura da Carteira por Blocos

### Bloco 1 — Liquidez e Segurança (curto prazo)
- Reserva de emergência completa (liquidez diária)
- Objetivos com prazo < 3 anos
- **Produtos:** Tesouro Selic, CDB liquidez diária, LCI/LCA pós-carência
- **Rentabilidade alvo:** 100-105% CDI

### Bloco 2 — Renda Fixa Estruturada (médio prazo)
- Objetivos de 3–10 anos
- Proteção contra inflação e previsibilidade
- **Produtos:** Tesouro IPCA+, CDBs de bancos médios, Debêntures incentivadas, CRI/CRA
- **Rentabilidade alvo:** IPCA + 5-7% a.a.

### Bloco 3 — Renda Variável e Crescimento (longo prazo)
- Objetivos com horizonte > 10 anos
- Aceita volatilidade de curto prazo em troca de crescimento de longo prazo
- **Produtos:** Ações (BDRs, ETFs), FIIs, Fundos multimercado
- **Rentabilidade alvo:** CDI + 4-8% a.a. (histórico de mercado, sem garantia)

---

## SCRIPTS DE SIMULAÇÃO

### Simulação de Crescimento Patrimonial (Juros Compostos)

```
FÓRMULA: VP × (1+r)^n + PMT × [(1+r)^n - 1] / r

ENTRADA:
  Patrimônio inicial: R$ [VP]
  Aporte mensal: R$ [PMT]
  Taxa de retorno mensal: [r]% (CDI atual: ~1,21% a.m.)
  Horizonte: [n] meses

SAÍDA:
  Patrimônio projetado em [n] meses: R$ [X]
  Total aportado: R$ [X]
  Total de rendimentos: R$ [X]
  Multiplicador: [X]x o capital investido

PROJEÇÃO ANUAL:
  Ano 1:   R$ [X]
  Ano 5:   R$ [X]
  Ano 10:  R$ [X]
  Ano 20:  R$ [X] (aposentadoria)
```

**Exemplo — R$ 1.500/mês por 20 anos a 8% a.a. real:**
```
Ano 5:   R$ 110.000
Ano 10:  R$ 275.000
Ano 20:  R$ 890.000
Total aportado: R$ 360.000
Total rendimentos: R$ 530.000
```

### Simulação de Stress Test de Carteira

Avaliar a robustez da estratégia a choques de mercado:

```
CENÁRIO 1 — Queda de 30% na renda variável:
  Impacto no patrimônio total: R$ [X] (X% da carteira)
  Tempo estimado de recuperação histórico: [N] meses
  Ação recomendada: [manter / rebalancear / aportar mais]

CENÁRIO 2 — Inflação 10% ao ano:
  Impacto no poder de compra da carteira?
  Bloco de Renda Fixa cobre? (Tesouro IPCA+ protege)
  Ajuste necessário?

CENÁRIO 3 — Necessidade de resgate emergencial (20% da carteira):
  Qual bloco resgatar primeiro? (Liquidez → Renda Fixa → Variável)
  Impacto no horizonte dos objetivos?
```

### Simulação de Objetivo Específico

```
OBJETIVO: [Nome] (ex: Entrada de imóvel)
META: R$ [X]
PRAZO: [N] meses
PATRIMÔNIO ATUAL: R$ [Y]

CÁLCULO DO APORTE NECESSÁRIO:
  Aporte = [Meta - PV × (1+r)^n] / [(1+r)^n - 1] / r
  Aporte mensal necessário: R$ [X]
  Viável com aporte atual? [SIM / NÃO — ajuste necessário]
```

---

## ENGINE DE DECISÃO — Alocação e Rebalanceamento

### Regra de Aporte Mensal

```
SE objetivo = reserva de emergência incompleta:
  100% do aporte → Bloco Liquidez (Tesouro Selic)

SE objetivos de curto prazo < 3 anos:
  Aportes direcionados para Bloco 1 (100% Liquidez)

SE carteira equilibrada em dia:
  Distribuir aportes conforme peso-alvo de cada bloco

SE bloco específico abaixo do peso-alvo em >10%:
  Concentrar aporte nesse bloco até reequilibrar
```

### Regra de Rebalanceamento

```
Frequência: Semestral ou anual (evita IR excessivo e custos)

Gatilho: Quando bloco desviar > 10% do peso-alvo
  Ex: Alvo 40% renda variável → atual 50% (ações subiram)
  → Rebalancear usando novos aportes (vender ativos como último recurso)

NUNCA rebalancear por notícia ou emoção de mercado
SEMPRE rebalancear por critério definido (calendário ou desvio de peso)
```

---

## Mapeamento de Objetivos

Organizar objetivos por prazo e prioridade:

| Objetivo | Prazo | Valor Necessário | Aporte Mensal | Bloco |
|----------|-------|-----------------|--------------|-------|
| Reserva emergência | Curto | R$ [6×gastos] | R$ [X] | Liquidez |
| [Objetivo 2] | [Prazo] | R$ [X] | R$ [X] | [Bloco] |
| Aposentadoria | Longo | R$ [X] | R$ [X] | Variável |

---

## Integração com Contribuições do Reino

```
Aportes mensais = Renda disponível - Contribuições do Reino - Gastos

ORDEM DE PRIORIDADE:
1. Dízimo (10% da renda) — SEMPRE primeiro
2. Gastos essenciais e de vida
3. Camada de Proteção Financeira (se incompleta)
4. Aportes para investimentos pessoais
5. Ofertas voluntárias crescentes (conforme Stewardship Engine)
```

> O objetivo de crescimento patrimonial e o investimento no Reino não competem — ambos refletem mordomia: crescer para servir mais.

---

## Saída Estruturada

### PAINEL DE CRESCIMENTO PATRIMONIAL

```
╔══════════════════════════════════════════════╗
║     ESTRATÉGIA DE CRESCIMENTO PATRIMONIAL    ║
╠══════════════════════════════════════════════╣
║  ESTADO:      EXPANSÃO                       ║
║  PROTOCOLO:   MULTIPLICAÇÃO RESPONSÁVEL      ║
╠══════════════════════════════════════════════╣
║  PERFIL:      [CONSERVADOR/MOD/ARROJADO]     ║
║  APORTE:      R$ [X]/mês                     ║
╠══════════════════════════════════════════════╣
║  BLOCO LIQUIDEZ:   [X]% — R$ [X]             ║
║  BLOCO RENDA FIXA: [X]% — R$ [X]             ║
║  BLOCO VARIÁVEL:   [X]% — R$ [X]             ║
╠══════════════════════════════════════════════╣
║  PATRIMÔNIO EM 5 ANOS:  R$ [X]               ║
║  PATRIMÔNIO EM 10 ANOS: R$ [X]               ║
║  PATRIMÔNIO EM 20 ANOS: R$ [X]               ║
╚══════════════════════════════════════════════╝

PROGRESSO DOS OBJETIVOS
Reserva:        [██████████] 100% ✅
[Objetivo 2]:   [████░░░░░░] X%
Aposentadoria:  [████████░░] X%
```

### Componentes do Output

1. **Mapa de Objetivos e Prazos** — tabela com objetivo, prazo, valor necessário, aporte
2. **Alocação por Bloco** — percentuais justificados pelo perfil e horizonte
3. **Simulação de Crescimento Patrimonial** — projeção com juros compostos
4. **Stress Test de Carteira** — cenários de queda e ação recomendada
5. **Produtos por Bloco** — sugestões concretas sem recomendação específica regulada
6. **Regra de Aporte** — valor fixo, distribuição, automação
7. **Regra de Rebalanceamento** — frequência, gatilho, método
8. **Integração com Reino** — como a mordomia molda a estratégia

### Próxima Skill

```
Para manter disciplina de execução → /pessoal-rotina-financeira-mensal
Para estruturar contribuições → /pessoal-investimento-reino
Para visão integrada → /gestor-financeiro
```

---

## Alertas e Disclaimers

- Esta skill é **educacional** e não substitui recomendação de investimento regulada (CNPI, agente autônomo, CFP)
- Rentabilidade passada não garante resultados futuros
- Evite produtos complexos (COE, derivativos, estruturados) sem entender completamente risco e custo
- Renda variável pode ter perdas temporárias — só invista valores que não precisará no curto prazo
- Considere impostos (IR sobre renda fixa e ganho de capital) e taxas (custódia, administração)
- Revise anualmente ou quando houver mudanças significativas de vida

## Princípios Orientadores

**Simplicidade:** Três blocos funcionais, poucos produtos, fácil de acompanhar.

**Disciplina:** Aportes regulares e rebalanceamento planejado superam tentativas de timing de mercado.

**Alinhamento:** Perfil de risco e horizonte determinam alocação — não modismos ou notícias do dia.

**Integração:** Crescimento patrimonial e generosidade crescente refletem mordomia fiel e intencional.

---
name: pessoal-estrategia-investimentos
description: >
  Define estratégia de investimentos pessoais por objetivo, prazo e perfil de risco, com simulação de crescimento patrimonial, stress test financeiro e carteira estruturada em blocos. Integra princípios de mordomia e contribuições do Reino como prioridade antes da alocação patrimonial. Use quando o usuário quer investir com método, já tem sobra mensal para aportes, tem dúvida entre segurança-liquidez-rentabilidade, menciona investimentos, carteira, alocação, perfil de risco, objetivos financeiros, aposentadoria, renda fixa, renda variável, ações, fundos, rebalanceamento, ou quer organizar investimentos pessoais.
owner: financeiro-pessoal
version: 3.0.0
last_updated: 2026-05-14
---

# Estratégia de Crescimento Patrimonial

## Postura do Sistema

Este skill não apresenta opções de alocação para o usuário escolher. Ele determina a estratégia correta baseada no perfil, horizonte e objetivos — e entrega uma carteira estruturada com regras claras de aporte, rebalanceamento e integração com mordomia.

> "Com base na sua situação, esta é a alocação correta. Aqui está o cronograma de aportes, a regra de rebalanceamento e a projeção de crescimento para cada objetivo."

## Arquivos Consultados pelo Sistema

| Arquivo | Quando consultar |
|---------|------------------|
| `../docs/REFERENCIAS-BRASIL-2026.md` | **OBRIGATÓRIO** — Selic, IPCA, IR sobre investimentos (tabela regressiva), FGC, Tesouro Direto |
| `../docs/GLOSSARIO.md` | Para terminologia padronizada (Camada de Proteção Financeira, Estados Financeiros) |
| `../docs/MEMORY-SYSTEM.md` | Para validar que pré-requisitos estão atendidos via Snapshot anterior |
| `../docs/EDUCACAO-FINANCEIRA-BASICA.md` | Para usuário que ainda não entende Tesouro, CDB, ações, FIIs |
| `../docs/PRINCIPIOS-BIBLICOS-EXPANDIDOS.md` | **Crítico em Estado EXPANSÃO/LEGADO** — riqueza como teste, idolatria, generosidade radical |
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
| Perfil de risco | Sim | Avaliado via teste comportamental (não autodeclarado) |
| Valor de aporte mensal | Sim | R$ 1.500/mês |
| Tipo de declaração IR | Sim | Completo ou simplificado (define elegibilidade ao PGBL) |
| Renda bruta anual tributável | Sim | R$ 96.000/ano (base para cálculo do benefício PGBL) |
| Patrimônio atual | Não | R$ 30.000 já investidos |
| Previdência privada existente | Não | PGBL/VGBL em vigor, taxa de administração atual |
| Percentual para Reino | Não | 10% já definido no /pessoal-investimento-reino |

---

## ENGINE DE DECISÃO — Perfil de Risco por Objetivo

### Teste de Ancoragem Comportamental (obrigatório — aplicar ANTES de classificar)

Perfil autodeclarado ("sou moderado") é irrelevante. O perfil real aparece na queda, não na alta. Aplicar este teste antes de qualquer alocação:

```
PERGUNTA 1 — Cenário de queda real:
  "Se R$ [valor investido] virar R$ [valor × 70%] em 6 meses
   e só recuperar em 2 anos — o que você faria?"
  A) Manteria sem olhar o extrato — aproveitaria para aportar mais
  B) Ficaria ansioso mas manteria a estratégia
  C) Reduziria a exposição para dormir melhor
  D) Resgataria tudo imediatamente

PERGUNTA 2 — Tolerância a período negativo:
  "Por quanto tempo você consegue ver seu patrimônio abaixo do que
   você investiu sem tomar uma decisão impulsiva?"
  A) Mais de 3 anos — entendo que é longo prazo
  B) 1 a 3 anos
  C) 6 a 12 meses
  D) Menos de 6 meses

ENGINE DE CLASSIFICAÇÃO COMPORTAMENTAL:
  Maioria A → ARROJADO confirmado
  Maioria B → MODERADO confirmado
  Maioria C → CONSERVADOR real (mesmo que tenha se declarado moderado)
  Maioria D → CONSERVADOR obrigatório — renda fixa de alta liquidez

REGRA INVIOLÁVEL: Se perfil autodeclarado ≠ perfil comportamental,
  usar sempre o MAIS CONSERVADOR dos dois.
  "O perfil que você acha que tem não importa. O que importa é o que
   você faz quando perde R$ 30.000 em um mês."
```

### Alocação por Perfil e Horizonte

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

## ENGINE DE DECISÃO — PGBL e VGBL (Previdência Privada)

Avaliar obrigatoriamente quando objetivo inclui aposentadoria OU horizonte > 10 anos. PGBL/VGBL são os principais instrumentos de planejamento tributário para aposentadoria no Brasil e devem ser considerados **antes** da alocação em outros produtos de longo prazo.

### Quando usar PGBL

```
SE usuário declara IR pelo modelo COMPLETO (não simplificado):
  E tem renda tributável (salário, pró-labore, aluguel):
  → PGBL É O PRIMEIRO INSTRUMENTO de aposentadoria a estruturar

BENEFÍCIO FISCAL — calcular para o usuário:
  Limite de dedução anual = renda bruta tributável × 12%
  Economia no IR = Limite × alíquota marginal do usuário

EXEMPLO (renda R$ 8.000/mês bruto, alíquota marginal 27,5%):
  Limite mensal   = R$ 8.000 × 12% = R$ 960/mês
  Limite anual    = R$ 11.520/ano
  Economia no IR  = R$ 11.520 × 27,5% = R$ 3.168/ano (restituição extra)
  → R$ 3.168 de retorno garantido antes de qualquer rendimento do fundo
  → Equivale a 27,5% de retorno imediato sobre o valor aportado

ATENÇÃO — PGBL é tributado integralmente no resgate (principal + rendimento):
  Por isso: usar SOMENTE com tabela regressiva de IR
  E SOMENTE para valores mantidos > 10 anos (IR cai para 10%)
  Nunca usar PGBL para objetivos de curto ou médio prazo
```

### Quando usar VGBL

```
SE usuário declara IR pelo modelo SIMPLIFICADO:
  Ou já atingiu o limite de 12% de dedução com PGBL:
  → VGBL é o instrumento adequado para o excedente

VGBL: tributado apenas sobre os rendimentos no resgate (não sobre o total)
  Sem benefício fiscal na entrada
  Melhor estrutura de saída para quem não tem dedução no IR
```

### Quando NÃO usar previdência privada

```
SE taxa de carregamento > 0%: NÃO contratar — negociar ou trocar de plano
SE taxa de administração > 1,0% a.a. (renda fixa): NÃO contratar
SE taxa de administração > 1,5% a.a. (renda variável): NÃO contratar
SE prazo de investimento < 5 anos: NÃO usar (IR na tabela progressiva — pode chegar a 27,5%)
SE fundo de ações disponível diretamente com custo < 0,5% a.a.: AVALIAR custo-benefício

REGRA: Um PGBL com taxa de administração de 2% a.a. pode consumir todo o
  benefício fiscal da dedução. Calcular sempre o custo total antes de recomendar.
```

### Portabilidade de Previdência Existente

```
SE usuário já tem PGBL/VGBL com taxa de carregamento ou administração alta:
  → Portabilidade para plano mais barato é gratuita e sem IR
  → Verificar: banco de origem geralmente tem planos mais caros
  → Corretoras oferecem planos com taxa de administração < 0,5% a.a.
  → Portabilidade pode gerar economia de R$ 1.000–3.000/ano em taxas
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
- **Produtos:** ETFs de índice (BOVA11, IVVB11), FIIs diversificados, BDRs
- **Rentabilidade alvo:** CDI + 4-8% a.a. (histórico de mercado, sem garantia)

**Alertas obrigatórios antes de recomendar renda variável:**
- **ETFs** são preferíveis a ações individuais para iniciantes — diversificação automática, custo < 0,5% a.a., sem risco de seleção ruim de empresa
- **FIIs:** escolher fundos com > 50 ativos no portfólio e volume diário > R$ 1M. FII concentrado em 1–2 imóveis pode ter vacância que zera dividendos por meses
- **BDRs:** carregam risco cambial explícito — se o real se valorizar 20%, o retorno cai proporcionalmente. Comunicar isso ao usuário antes de recomendar
- **Concentração:** nunca alocar > 50% da renda variável em FIIs de um único segmento (ex: todos lajes corporativas)
- **Fundos multimercado:** verificar taxa de administração + performance. Fundos com taxa total > 2% a.a. raramente justificam o custo

---

## SCRIPTS DE SIMULAÇÃO

### Simulação de Crescimento Patrimonial — com IR e Taxas (Retorno Líquido Real)

> **Regra inviolável:** Sempre simular com retorno LÍQUIDO (após IR e taxas de administração). Mostrar o bruto sem o líquido cria expectativa falsa e mina a confiança quando o extrato não bate com a projeção.

**Taxas reais líquidas de referência por perfil (horizonte > 10 anos):**

| Perfil | Taxa bruta estimada | IR + taxas | Taxa líquida real |
|--------|--------------------|-----------|--------------------|
| Conservador | 6,5–7,0% a.a. real | ~1,2% a.a. | **5,0–5,5% a.a. real** |
| Moderado | 7,0–8,0% a.a. real | ~1,3% a.a. | **5,5–6,5% a.a. real** |
| Arrojado | 8,0–10,0% a.a. real | ~1,5% a.a. | **6,0–7,5% a.a. real** |

*(Base: Selic/IPCA correntes via BCB API, IR regressivo 15% após 720 dias, taxa B3 0,2% a.a., sem taxa de administração de fundo)*

```
FÓRMULA (valores em termos reais — poder de compra constante):
  VP × (1+r)^n + PMT × [(1+r)^n − 1] / r
  onde r = taxa real líquida mensal = (1 + taxa_anual_liquida)^(1/12) − 1

ENTRADA:
  Patrimônio inicial: R$ [VP]
  Aporte mensal: R$ [PMT]
  Taxa real líquida anual: [r_liq]% (conforme tabela acima)
  Horizonte: [n] meses

SAÍDA OBRIGATÓRIA — mostrar SEMPRE as duas colunas:

  | Período | Bruto (sem IR/taxas) | Líquido real | Custo IR+taxas |
  |---------|----------------------|--------------|----------------|
  | Ano 5   | R$ [X]               | R$ [Y]       | R$ [X−Y]       |
  | Ano 10  | R$ [X]               | R$ [Y]       | R$ [X−Y]       |
  | Ano 20  | R$ [X]               | R$ [Y]       | R$ [X−Y]       |

  Total aportado:        R$ [X]
  Rendimento líquido:    R$ [Y]
  Custo total IR+taxas:  R$ [Z] — apresentar este número com clareza
```

**Exemplo corrigido — R$ 1.500/mês por 20 anos, perfil moderado (6,0% a.a. real líquido):**
```
  | Período | Bruto (8% a.a.) | Líquido (6% a.a.) | Custo IR+taxas |
  |---------|-----------------|-------------------|----------------|
  | Ano 5   | R$ 110.000      | R$ 101.000        | R$ 9.000       |
  | Ano 10  | R$ 275.000      | R$ 245.000        | R$ 30.000      |
  | Ano 20  | R$ 890.000      | R$ 685.000        | R$ 205.000     |

Total aportado:        R$ 360.000
Rendimento líquido:    R$ 325.000
Custo total IR+taxas:  R$ 205.000 ao longo de 20 anos

⚠️ A diferença de R$ 205.000 é real — é o custo de IR e taxas que não aparece
   no número bruto. Apresentar isso ao usuário com transparência gera confiança.
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
2. **Resultado do Teste Comportamental** — perfil real (não autodeclarado)
3. **Análise PGBL/VGBL** — elegibilidade, benefício fiscal calculado em R$, portabilidade se aplicável
4. **Alocação por Bloco** — percentuais justificados pelo perfil comportamental e horizonte
5. **Simulação de Crescimento Patrimonial** — projeção bruta E líquida (após IR e taxas)
6. **Stress Test de Carteira** — cenários de queda e ação recomendada
7. **Produtos por Bloco** — sugestões concretas com alertas de FII/BDR quando aplicável
8. **Regra de Aporte** — valor fixo, distribuição, automação
9. **Regra de Rebalanceamento** — frequência, gatilho, método
10. **Integração com Reino** — como a mordomia molda a estratégia
11. **Próximos Passos Reais** — corretora recomendada + especialista se necessário

### Próximos Passos Reais (entrega obrigatória ao final)

Toda consultoria termina com passos concretos e executáveis — não com "pense nisso":

```
PASSO 1 — Abrir conta em corretora (se não tiver):
  Recomendar corretora adequada ao perfil (ver seção PLATAFORMAS)
  Prazo: esta semana. Abertura de conta é 100% digital, leva 10 minutos.

PASSO 2 — Configurar aporte automático:
  Programar transferência do salário → corretora no mesmo dia do recebimento
  "Invista antes de gastar — não com o que sobrar"

PASSO 3 — Primeiro investimento:
  Começar pelo Bloco 1 (Tesouro Selic ou CDB liquidez diária)
  Meta: reserva de emergência completa antes de qualquer outro bloco

PASSO 4 — PGBL (se elegível):
  Solicitar proposta de plano com taxa de administração < 0,5% a.a.
  Prazo: antes do fechamento do ano fiscal para deduzir no IR

PASSO 5 — Buscar assessor de investimentos (se patrimônio > R$ 50k):
  Contato via corretora escolhida — gratuito
  Levar esta estratégia como ponto de partida para a conversa
```

### Próxima Skill

```
Para manter disciplina de execução → /pessoal-rotina-financeira-mensal
Para estruturar contribuições → /pessoal-investimento-reino
Para visão integrada → /gestor-financeiro
```

---

## PLATAFORMAS E ESPECIALISTAS — Onde Executar a Estratégia

> Esta seção é parte obrigatória da entrega. Toda consultoria de investimentos termina com orientação de onde e com quem executar — não apenas com a estratégia.

### Corretoras Reguladas (CVM + ANBIMA)

| Corretora | Destaque | Site |
|-----------|----------|------|
| **XP Investimentos** | Maior plataforma, ampla grade de produtos | xpi.com.br |
| **Rico** | Interface simples, boa para iniciantes | rico.com.vc |
| **NuInvest (Nubank)** | Integrada ao Nubank, taxa zero em muitos produtos | nuinvest.com.br |
| **BTG Digital** | Perfil mais sofisticado, renda fixa premium | btgpactualdigital.com |
| **Warren** | Carteiras automatizadas, UX cuidada | warren.com.br |
| **Inter Invest** | Integrado ao Banco Inter, taxa zero | bancointer.com.br |
| **EQI Investimentos** | Assessoria especializada, forte em renda fixa | eqi.com.br |

**Verificar se a corretora é regulada:** investidor.gov.br (cadastro CVM)

### Quando Recomendar Especialista (gatilhos obrigatórios)

```
SE patrimônio investido > R$ 100.000:
  → Recomendar assessor de investimentos (gratuito, vinculado à corretora)
  → Um erro de alocação nesse patamar custa mais do que o serviço

SE objetivo inclui aposentadoria + PGBL + IR complexo:
  → Recomendar CFP (Certified Financial Planner)
  → Especialmente crítico para autônomos e PJ sem INSS

SE renda mensal > R$ 10.000 com IR na alíquota máxima (27,5%):
  → Recomendar CFP + contador
  → Interação entre PGBL, IR e estratégia patrimonial é complexa
  → Erro aqui custa R$ 3.000–8.000/ano em imposto pago a mais

SE empresa familiar, herança ou planejamento sucessório:
  → Recomendar advogado especialista em sucessão + CFP
  → Estrutura de holding familiar pode ser mais eficiente tributariamente
```

### Como Encontrar um Especialista Certificado

| Tipo | Certificação | Onde encontrar | Custo |
|------|-------------|----------------|-------|
| **Planejador Financeiro CFP** | CFP® (PLANEJAR) | planejar.org.br/encontre-um-planejador | Fee ou % patrimônio |
| **Assessor de Investimentos** | AAI (ANCORD) | Via corretoras acima | **Gratuito** |
| **Analista de Investimentos** | CNPI (APIMEC) | Casas de análise (Empiricus, Suno, Ticker) | Assinatura mensal |
| **Profissional ANBIMA** | CPA-20, CEA | anbima.com.br/certificacoes | Via instituição |

**Diferença prática:**
- **CFP:** faz plano financeiro integrado (IR + aposentadoria + investimentos + proteção). Cobra fee fixo ou % do patrimônio. Ideal para situações complexas
- **Assessor (AAI):** remunerado pela corretora — gratuito para o cliente. Faz alocação e acompanha carteira. Ideal para maioria dos casos
- **CNPI:** analisa ativos específicos. Útil para quem quer investir em ações individuais com suporte

---

## Alertas e Disclaimers

> **⚠️ LEIA ANTES DE ENTREGAR QUALQUER ORIENTAÇÃO DE INVESTIMENTO**

- Esta skill é **educacional** — orienta estratégia e educa sobre produtos. **Não substitui** recomendação de investimento regulada (CFP, assessor AAI, CNPI)
- **Sempre recomendar** que o usuário valide a estratégia com um assessor certificado antes de executar, especialmente para valores > R$ 50.000
- Rentabilidade passada não garante resultados futuros — apresentar projeções como estimativas, não promessas
- Renda variável **pode cair 30–50% e demorar anos para recuperar** — verificar ancoragem comportamental antes de recomendar
- Evite produtos complexos (COE, derivativos, estruturados alavancados) — o risco raramente é proporcional ao retorno para pessoa física
- Simular sempre com retorno **líquido de IR e taxas** — nunca apresentar só o bruto
- Revisar estratégia anualmente ou quando houver: mudança de renda, casamento/divórcio, filhos, herança, mudança de emprego

## Princípios Orientadores

**Simplicidade:** Três blocos funcionais, poucos produtos, fácil de acompanhar.

**Disciplina:** Aportes regulares e rebalanceamento planejado superam tentativas de timing de mercado.

**Alinhamento:** Perfil de risco e horizonte determinam alocação — não modismos ou notícias do dia.

**Integração:** Crescimento patrimonial e generosidade crescente refletem mordomia fiel e intencional.

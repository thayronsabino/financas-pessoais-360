---
name: pessoal-estrategia-investimentos
description: >
  Define estratégia de investimentos pessoais por objetivo, prazo e perfil de risco, com carteira simples e disciplina de aportes. Use quando o usuário quer investir com método, já tem sobra mensal para aportes, tem dúvida entre segurança-liquidez-rentabilidade, menciona investimentos, carteira, alocação, perfil de risco (conservador, moderado, arrojado), objetivos financeiros, aposentadoria, reserva de emergência, renda fixa, renda variável, ações, fundos, rebalanceamento, ou quer organizar investimentos pessoais. Integra com princípios de mordomia e contribuições do reino.
owner: financeiro-pessoal
version: 1.0.0
last_updated: 2026-03-27
---

# Pessoal - Estratégia de Investimentos

## Visão Geral

Esta skill constrói uma estratégia de investimentos pessoais coerente com perfil de risco, objetivos financeiros e horizonte de tempo. Prioriza simplicidade, disciplina de aportes e integração com princípios de mordomia e contribuições do reino.

## Entradas Esperadas

- **Objetivos financeiros** (obrigatório): reserva de emergência, casa própria, aposentadoria, educação dos filhos, etc.
- **Horizonte de tempo** (obrigatório): curto prazo (<3 anos), médio prazo (3-10 anos), longo prazo (>10 anos)
- **Perfil de risco** (obrigatório): conservador, moderado ou arrojado
- **Valor de aporte mensal** (obrigatório): quanto consegue investir regularmente
- **Patrimônio atual** (opcional): investimentos já existentes
- **Percentual para contribuições do reino** (opcional): já definido em `/pessoal-investimento-reino`

## Fluxo de Execução

### 1. Mapeamento de Objetivos

Organize objetivos por prazo e importância:

**Curto prazo (até 3 anos)**
- Reserva de emergência (6-12 meses de despesas)
- Objetivos urgentes (casamento, viagem, reforma)

**Médio prazo (3-10 anos)**
- Entrada de imóvel
- Carro
- Educação dos filhos

**Longo prazo (>10 anos)**
- Aposentadoria
- Independência financeira
- Legado

### 2. Definição de Perfil de Risco

O perfil determina a tolerância a oscilações e orienta a alocação:

**Conservador**
- Baixa tolerância a perdas temporárias
- Prioriza segurança e previsibilidade
- Aceita rentabilidade menor em troca de estabilidade

**Moderado**
- Aceita alguma volatilidade para buscar retornos superiores
- Equilibra segurança com crescimento
- Tolera oscilações de curto prazo com foco no médio/longo prazo

**Arrojado**
- Alta tolerância a volatilidade
- Prioriza crescimento patrimonial de longo prazo
- Mantém disciplina em quedas temporárias

**Importante:** Perfil de risco pode variar por objetivo. Reserva de emergência é sempre conservadora; aposentadoria de longo prazo permite maior risco.

### 3. Alocação por Blocos

Organize a carteira em três blocos funcionais:

**Bloco 1: Liquidez e Segurança** (curto prazo)
- Reserva de emergência: 100% renda fixa líquida (Tesouro Selic, CDB com liquidez diária)
- Objetivos <3 anos: Renda fixa (CDB, LCI/LCA, Tesouro prefixado ou IPCA+)
- Percentual típico: 20-40% da carteira total (conservador: 40-70%)

**Bloco 2: Renda Fixa Estruturada** (médio prazo)
- Objetivos 3-10 anos: Tesouro IPCA+, CDBs de bancos médios, debêntures incentivadas, CRIs/CRAs
- Protege contra inflação e oferece previsibilidade
- Percentual típico: 30-50% (moderado: 40-60%; conservador: 30-60%)

**Bloco 3: Renda Variável e Crescimento** (longo prazo)
- Ações, fundos imobiliários (FIIs), fundos multimercados, ETFs
- Para objetivos >10 anos e patrimônio que suporta volatilidade
- Percentual típico: arrojado 40-60%; moderado 20-40%; conservador 0-20%

**Exemplo de alocação moderada para aposentadoria (horizonte 20 anos):**
- Liquidez: 20% (Tesouro Selic, CDB líquido)
- Renda Fixa: 40% (Tesouro IPCA+, CDBs, debêntures)
- Renda Variável: 40% (ações, FIIs, fundos)

### 4. Regras de Aporte e Rebalanceamento

**Disciplina de aportes:**
- Defina valor fixo mensal e trate como despesa obrigatória
- Automatize transferências no início do mês
- Distribua aportes conforme alocação-alvo ou reforce blocos abaixo do peso

**Rebalanceamento:**
- **Frequência:** Semestral ou anual (evita custos excessivos e IR)
- **Gatilho:** Quando um bloco desviar >10% do peso-alvo (ex: alvo 40%, atual 50%)
- **Método preferencial:** Use novos aportes para reequilibrar antes de vender ativos
- **Em crises:** Rebalancear disciplinadamente força "comprar na baixa" e "vender na alta"

**Exemplo:**
Carteira-alvo: 30% liquidez, 40% renda fixa, 30% renda variável  
Atual: 25% liquidez, 35% renda fixa, 40% renda variável (ações subiram)

Ação: Próximos aportes vão 100% para liquidez e renda fixa até reequilibrar. Se desvio for grande, considere vender parte das ações.

### 5. Integração com Contribuições do Reino

Se o usuário já definiu percentual para contribuições em `/pessoal-investimento-reino`, integre:

- Aportes mensais = Renda disponível - Contribuições do reino
- Contribuições têm prioridade e são separadas antes da alocação
- Estratégia de investimentos pessoais trabalha com o restante
- Ambos refletem mordomia: contribuir com propósito e investir com sabedoria

**Exemplo:**
Renda mensal disponível: R$ 2.000  
Contribuições do reino (10%): R$ 200  
Aportes para investimentos pessoais: R$ 1.800

## Saída Estruturada

Forneça ao usuário:

1. **Mapa de objetivos e prazos**  
   Tabela com objetivo, prazo, valor estimado necessário

2. **Alocação sugerida por bloco**  
   Percentuais para Liquidez, Renda Fixa e Renda Variável, com justificativa pelo perfil e horizonte

3. **Exemplos de ativos por bloco**  
   Sugestões concretas (Tesouro Selic, CDB, Tesouro IPCA+, ações, FIIs) sem recomendação específica de produtos

4. **Regra de aporte mensal**  
   Valor fixo, distribuição inicial entre blocos, automação

5. **Regra de rebalanceamento**  
   Frequência (semestral/anual), gatilho de desvio (>10%), método (aportes primeiro, vendas se necessário)

6. **Integração com contribuições do reino**  
   Como a estratégia respeita prioridades de mordomia

7. **Próximos passos**  
   Sugestão de skills relacionadas: `/pessoal-plano-dividas-reserva`, `/pessoal-rotina-financeira-mensal`, `/gestor-financeiro`

## Alertas e Disclaimers

- Esta skill é **educacional** e não substitui recomendação de investimento regulada (análise CNPI, agente autônomo, planejador CFP)
- Rentabilidade passada não garante resultados futuros
- Evite produtos complexos (COE, estruturados, derivativos) sem entender completamente risco, custo e liquidez
- Renda variável pode ter perdas temporárias; só invista valores que não precisará no curto prazo
- Considere impostos (IR sobre renda fixa e ganho de capital) e taxas (custódia, administração de fundos)
- Revise a estratégia anualmente ou quando houver mudanças significativas de vida (casamento, filhos, mudança de emprego)

## Princípios Orientadores

**Simplicidade:** Três blocos funcionais, poucos produtos, fácil de acompanhar.

**Diversificação:** Não concentrar em um único ativo ou prazo.

**Disciplina:** Aportes regulares e rebalanceamento planejado superam tentativas de "timing" de mercado.

**Alinhamento:** Perfil de risco e horizonte determinam alocação, não modismos ou notícias do dia.

**Integração:** Investimentos pessoais e contribuições do reino refletem mordomia fiel e intencional.

## Exemplo de Aplicação

**Entrada:**
- Objetivos: Reserva (R$ 30k), aposentadoria (20 anos)
- Perfil: Moderado
- Aporte mensal: R$ 1.500
- Contribuições do reino: R$ 300/mês já separados

**Saída:**
1. Mapa: Reserva (curto), aposentadoria (longo)
2. Alocação: 30% liquidez, 40% renda fixa, 30% renda variável
3. Ativos: Tesouro Selic (liquidez), Tesouro IPCA+ 2045 (renda fixa), ETF BOVA11 + FIIs (renda variável)
4. Aporte: R$ 1.500/mês → R$ 450 liquidez, R$ 600 renda fixa, R$ 450 renda variável (até completar reserva, depois ajustar)
5. Rebalanceamento: Revisar a cada 6 meses, ajustar se desvio >10%
6. Integração: R$ 300/mês já vão para contribuições; estratégia de investimentos usa os R$ 1.500 restantes
7. Próxima skill: `/pessoal-rotina-financeira-mensal` para acompanhamento
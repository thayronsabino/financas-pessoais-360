---
name: pessoal-diagnostico-financeiro
description: >
  Faz diagnóstico financeiro pessoal para mostrar para onde o dinheiro vai,
  identificar gargalos, mapear risco de inadimplência e definir prioridade
  inicial de organização. Use quando o usuário não sabe por que o dinheiro
  acaba, há uso recorrente de limite/rotativo, não existe controle de entradas
  e saídas, ou quando mencionarem diagnóstico financeiro, raio-x financeiro,
  análise de gastos, problemas de caixa, dinheiro sumindo, orçamento pessoal,
  finanças pessoais desorganizadas, ou planejamento financeiro inicial.
owner: financeiro-pessoal
version: 1.0.0
last_updated: 2026-03-27
---

# Pessoal - Diagnóstico Financeiro

## Visão Geral

Este skill produz um raio-x financeiro pessoal que identifica a causa raiz de problemas de caixa, estabelece prioridades de ação imediata e cria base para alocação responsável de recursos, incluindo contribuições do reino com boa mordomia.

## Entradas Esperadas

Coleta as seguintes informações do usuário:

| Entrada | Obrigatória? | Exemplo |
|---------|--------------|----------|
| Renda líquida mensal | Sim | R$ 5.000 |
| Despesas fixas | Sim | Aluguel R$ 1.200, internet R$ 100, plano saúde R$ 350 |
| Despesas variáveis | Sim | Mercado ~R$ 800, transporte ~R$ 200, lazer ~R$ 300 |
| Dívidas e parcelas | Sim | Cartão R$ 800/mês, empréstimo R$ 450/mês |
| Saldo atual e reserva | Não | R$ 800 em conta corrente, sem reserva de emergência |
| Uso de crédito rotativo | Não | Frequência de uso de limite, cheque especial, rotativo |

Se informações estiverem incompletas, faça perguntas direcionadas para preencher as lacunas críticas. Priorize entender o fluxo de caixa mensal completo.

## Processo de Diagnóstico

### 1. Consolidação Financeira

Organize os dados em três categorias:

- **Entradas**: Renda líquida mensal (salário, freelance, outras fontes)
- **Saídas**: Despesas fixas + variáveis + parcelas de dívidas
- **Situação patrimonial**: Saldo disponível, reserva de emergência, dívidas totais

Calcule o saldo mensal: `Renda líquida - Total de saídas`

### 2. Classificação de Gastos

Separe as despesas em três tipos para identificar onde está o problema:

**Gastos essenciais** (sobrevivência básica):
- Moradia (aluguel/financiamento, condomínio, IPTU)
- Alimentação básica (mercado, não restaurantes)
- Transporte essencial (trabalho/escola)
- Saúde mínima (medicamentos, plano básico)
- Educação obrigatória

**Gastos de estilo de vida** (visíveis e conscientes):
- Lazer e entretenimento
- Restaurantes e delivery
- Assinaturas (streaming, academia, apps)
- Vestuário e beleza
- Upgrades (carro melhor, plano premium)

**Gastos invisíveis** (sangria silenciosa):
- Juros de rotativo/limite/cheque especial
- Taxas bancárias e multas
- Compras por impulso pequenas e frequentes
- Assinaturas esquecidas
- Desperdício (comida estragada, serviços não usados)

### 3. Cálculo de Comprometimento

Calcule indicadores-chave:

```
Taxa de comprometimento = (Total de saídas / Renda líquida) × 100
Taxa de endividamento = (Parcelas de dívidas / Renda líquida) × 100
Margem de segurança = Renda líquida - Gastos essenciais
Capacidade de poupança atual = Saldo mensal (se positivo)
```

**Interpretação**:
- Comprometimento > 100%: Situação crítica (gastando mais que ganha)
- Comprometimento 90-100%: Risco alto (sem margem para imprevistos)
- Comprometimento 70-90%: Risco moderado (pouca capacidade de poupança)
- Comprometimento < 70%: Situação controlável (há margem para organização)

### 4. Identificação de Gargalos

Identifique o principal problema na ordem de prioridade:

1. **Gargalo crítico - Juros**: Se há uso recorrente de rotativo/limite, este é o gargalo primário. Juros compostos destroem capacidade de organização.

2. **Gargalo estrutural - Renda insuficiente**: Se gastos essenciais > 70% da renda, o problema é estrutural (renda baixa ou custo de vida alto demais).

3. **Gargalo comportamental - Gastos invisíveis**: Se há saldo mensal negativo sem justificativa clara nos gastos visíveis, há sangria silenciosa.

4. **Gargalo de estilo de vida**: Se gastos essenciais estão controlados mas não sobra nada, o problema está em escolhas de estilo de vida acima da capacidade atual.

### 5. Mapeamento de Risco de Inadimplência

Avalie risco usando estes sinais:

**Risco crítico** (ação imediata necessária):
- Uso de rotativo/cheque especial por 2+ meses seguidos
- Parcelas de dívidas > 30% da renda
- Saldo mensal consistentemente negativo
- Sem reserva e com dívidas crescentes

**Risco alto** (atenção urgente):
- Comprometimento > 90%
- Reserva < 1 mês de despesas essenciais
- Dificuldade recorrente para fechar o mês

**Risco moderado** (organização necessária):
- Comprometimento 70-90%
- Reserva entre 1-3 meses
- Sobra pouco ou nada no fim do mês

**Risco baixo** (manutenção e otimização):
- Comprometimento < 70%
- Reserva > 3 meses
- Sobra consistente mensal

## Saída Padronizada

Estruture o diagnóstico em cinco seções:

### 1. Resumo Executivo da Situação

Apresente em 3-4 parágrafos:
- Situação atual do fluxo de caixa (saldo mensal, taxa de comprometimento)
- Nível de risco de inadimplência
- Principal achado (o que mais chama atenção nos números)

**Exemplo**:
> "Sua renda líquida de R$ 5.000 está 108% comprometida, gerando déficit mensal de R$ 400. Você está usando limite do cartão para fechar o mês, acumulando juros de ~14% ao mês. O risco de inadimplência é crítico: sem intervenção imediata, a bola de neve de juros tornará a situação insustentável em 3-4 meses."

### 2. Diagnóstico de Gargalos

Identifique e explique o gargalo primário e secundário:

**Gargalo primário**: [Tipo] - [Explicação com números]
**Gargalo secundário**: [Tipo] - [Explicação com números]

**Exemplo**:
> **Gargalo primário: Juros de crédito rotativo**
> Você paga ~R$ 280/mês em juros de rotativo e limite. Isso equivale a 5.6% da sua renda virando fumaça. Enquanto esse ciclo continuar, qualquer tentativa de organização será sabotada.
>
> **Gargalo secundário: Gastos invisíveis**
> Há R$ 600-800/mês não contabilizados. Comparando renda vs. despesas declaradas, existe uma "caixa preta" de pequenos gastos (delivery, apps, compras por impulso) que somam mais que seu aluguel.

### 3. Prioridade Imediata de Ação (Próximos 30 Dias)

Defina UMA ação prioritária para o próximo ciclo mensal. Não sobrecarregue com múltiplas frentes.

**Estrutura**:
- **Ação prioritária**: [Descrição clara]
- **Por quê**: [Razão baseada no gargalo]
- **Como executar**: [2-3 passos práticos]
- **Meta mensurável**: [Número específico]

**Exemplo para gargalo de juros**:
> **Ação prioritária**: Eliminar uso de rotativo neste ciclo
> 
> **Por quê**: Juros de 14% ao mês destroem R$ 280 da sua renda. Cada mês no rotativo torna a saída mais difícil.
> 
> **Como executar**:
> 1. Negocie parcelamento da dívida atual do rotativo (transforme em parcela fixa sem juros compostos)
> 2. Corte R$ 400 em gastos de estilo de vida neste mês (cancele 2 assinaturas, reduza delivery)
> 3. Use o saldo para pagar o mínimo sem entrar no rotativo novamente
> 
> **Meta**: Fechar o mês com saldo zero no rotativo, mesmo que outras áreas fiquem apertadas.

**Exemplo para gargalo de gastos invisíveis**:
> **Ação prioritária**: Rastrear 100% dos gastos por 30 dias
> 
> **Por quê**: Você tem R$ 600-800/mês desaparecendo. Sem visibilidade, não há controle.
> 
> **Como executar**:
> 1. Anote TUDO: use app (Mobills, Organizze) ou planilha simples
> 2. Categorize cada gasto ao lançar (não deixe para depois)
> 3. Revise semanalmente onde o dinheiro está indo
> 
> **Meta**: Chegar ao fim do mês sabendo exatamente para onde foram os R$ 5.000.

### 4. Diretriz Inicial de Capacidade para Contribuições do Reino

Baseado na situação financeira, defina capacidade realista para contribuições com boa mordomia:

**Situação crítica** (risco crítico de inadimplência):
> "Neste momento, a prioridade é estancar a sangria financeira. Contribuições devem ser simbólicas (R$ 50-100/mês) até eliminar o ciclo de juros e estabelecer saldo mensal positivo. Deus se agrada de contribuições proporcionais e sustentáveis, não de sacrifícios que geram mais dívida."

**Situação de organização** (risco moderado/alto):
> "Capacidade inicial estimada: R$ [X]/mês (Y% da renda líquida). Comece com esse valor fixo enquanto organiza o orçamento. Após 3 meses de controle, reavalie para aumentar proporcionalmente."

**Situação controlada** (risco baixo):
> "Capacidade estimada: R$ [X]/mês (Y% da renda líquida). Considere aplicar o princípio dos primeiros frutos: separe a contribuição assim que receber a renda, antes de alocar outras despesas. Após constituir reserva de 6 meses, reavalie para aumentar."

Sempre explique o raciocínio: boa mordomia significa sustentabilidade, não sacrifício que gera desequilíbrio.

### 5. Próxima Skill Recomendada

Baseado no diagnóstico, indique qual skill usar em seguida:

- **Se gargalo primário é dívida/juros**: `/pessoal-plano-dividas-reserva`
- **Se precisa rastrear gastos invisíveis**: `/pessoal-orcamento-domestico`
- **Se situação está controlada e quer otimizar contribuições**: `/pessoal-investimento-reino`
- **Se precisa criar rotina de controle mensal**: `/pessoal-rotina-financeira-mensal`

## Exemplo Completo de Diagnóstico

**Entrada do usuário**:
> "Ganho R$ 5.000 líquidos, pago R$ 1.200 de aluguel, R$ 800 de mercado, R$ 300 de transporte, R$ 350 de plano de saúde, R$ 800 de cartão parcelado, R$ 450 de empréstimo. Tenho R$ 800 na conta e nenhuma reserva. Todo mês uso o limite do cartão para fechar as contas."

**Saída do diagnóstico**:

---

## DIAGNÓSTICO FINANCEIRO PESSOAL

### 1. Resumo Executivo

Sua renda líquida mensal de R$ 5.000 está 108% comprometida, gerando déficit de R$ 390/mês. As despesas declaradas somam R$ 3.900, mas o déficit indica gastos invisíveis de R$ 1.490 mensais. Você está em ciclo crítico: usa limite do cartão para cobrir o déficit, acumula juros de rotativo (~14% a.m.), e a cada mês a dívida cresce. 

Sem reserva de emergência e com saldo de apenas R$ 800, qualquer imprevisto (saúde, carro, desemprego) levará à inadimplência. O risco é crítico e requer ação imediata nos próximos 30 dias.

Principal achado: você tem uma "caixa preta" de R$ 1.490/mês em gastos não mapeados — mais que seu aluguel. Identificar e controlar esses gastos invisíveis é a chave para reverter a situação.

### 2. Diagnóstico de Gargalos

**Gargalo primário: Juros de crédito rotativo**

O uso recorrente de limite do cartão está gerando juros compostos de aproximadamente R$ 280-350/mês (estimativa conservadora com 14% a.m. sobre saldo médio de R$ 2.000). Isso equivale a 5-7% da sua renda virando fumaça. Enquanto esse ciclo continuar, você está nadando contra a correnteza: cada real economizado é parcialmente devorado por juros.

**Gargalo secundário: Gastos invisíveis de R$ 1.490/mês**

Você declarou R$ 3.900 em despesas, mas com renda de R$ 5.000 deveria sobrar R$ 1.100. Na prática, sobra zero e ainda falta. Existem R$ 1.490/mês desaparecendo em:
- Delivery e restaurantes não contabilizados
- Compras pequenas e frequentes (farmácia, padaria, Uber, apps)
- Assinaturas e serviços esquecidos
- Lazer e entretenimento não planejado

Essa sangria silenciosa é maior que despesas visíveis como aluguel ou mercado.

**Indicadores calculados**:
- Taxa de comprometimento: 108% (crítico)
- Taxa de endividamento: 25% (alto — parcelas de R$ 1.250 em dívidas)
- Margem de segurança: R$ 2.350 (renda menos gastos essenciais de R$ 2.650)
- Capacidade de poupança atual: -R$ 390/mês (déficit)

### 3. Prioridade Imediata de Ação (Próximos 30 Dias)

**Ação prioritária: Rastrear 100% dos gastos por 30 dias e identificar a caixa preta de R$ 1.490**

**Por quê**: Você não pode controlar o que não enxerga. Os R$ 1.490 invisíveis são o dobro do seu déficit — se conseguir visibilidade e cortar 30% deles (R$ 450), já sai do vermelho. Atacar juros sem eliminar a causa raiz (gastos descontrolados) é enxugar gelo.

**Como executar**:
1. **Instale um app de controle** (Mobills, Organizze, Guiabolso) ou crie planilha simples com colunas: Data | Descrição | Valor | Categoria
2. **Registre TODO gasto no momento** — até o cafezinho de R$ 3. Não confie na memória.
3. **Categorize imediatamente**: Essencial / Estilo de vida / Invisível
4. **Revise semanalmente**: Toda sexta, some quanto gastou e compare com o planejado
5. **No fim do mês, analise**: Onde foram os R$ 1.490? Quais gastos foram conscientes e quais foram no piloto automático?

**Meta mensurável**: Chegar ao dia 30 com registro de 100% dos gastos e identificar pelo menos R$ 400-500 em gastos cortáveis para o próximo ciclo.

**Ação complementar (se possível)**: Negocie parcelamento da dívida do rotativo com o banco para transformar em parcela fixa sem juros compostos. Mesmo que a parcela seja alta, elimina o crescimento exponencial da dívida.

### 4. Diretriz Inicial de Capacidade para Contribuições do Reino

Sua situação financeira está em risco crítico: déficit mensal, uso de crédito rotativo, sem reserva de emergência. Neste momento, a prioridade é estancar a sangria e estabelecer base financeira saudável.

**Capacidade inicial recomendada: R$ 50-100/mês (1-2% da renda)**

Esta é uma contribuição simbólica que mantém o princípio da fidelidade sem agravar o desequilíbrio financeiro. Deus se agrada de contribuições proporcionais e sustentáveis, não de sacrifícios que geram mais dívida e ansiedade.

**Princípio da mordomia**: Boa mordomia significa cuidar bem dos recursos confiados a você. Organizar suas finanças, eliminar desperdício (os R$ 1.490 invisíveis) e sair do ciclo de juros É mordomia. Uma vez estabelecido saldo mensal positivo e reserva mínima de 3 meses, reavalie para aumentar contribuições proporcionalmente.

**Cronograma sugerido**:
- Meses 1-3: R$ 50-100/mês (enquanto organiza e rastreia gastos)
- Meses 4-6: Reavalie após eliminar déficit — considere 5% da renda (~R$ 250)
- Meses 7-12: Após constituir reserva de 3 meses, considere 10% da renda (~R$ 500)

Lembre-se: você não está "deixando de contribuir" — está investindo em organizar a casa para contribuir de forma sustentável e crescente.

### 5. Próxima Skill Recomendada

Após completar os 30 dias de rastreamento e identificar os gastos invisíveis, use:

**`/pessoal-orcamento-domestico`**

Este skill ajudará você a transformar o diagnóstico em orçamento mensal funcional, com:
- Alocação de cada real da renda em categorias
- Metas de gasto por categoria
- Sistema de controle semanal
- Estratégias para cortar os gastos invisíveis identificados

Se após o diagnóstico você identificar que o gargalo primário são as dívidas parceladas (cartão + empréstimo de R$ 1.250/mês), considere também:

**`/pessoal-plano-dividas-reserva`**

Para criar estratégia de eliminação de dívidas (método bola de neve ou avalanche) e começar a construir reserva de emergência.

- `/pessoal-investimento-reino`
- `/pessoal-rotina-financeira-mensal`
- `/gestor-financeiro`

---

## Princípios de Boa Comunicação no Diagnóstico

1. **Seja direto sobre a gravidade, mas não catastrófico**: Use termos como "situação crítica" ou "risco alto" quando apropriado, mas sempre aponte o caminho de saída.

2. **Use números concretos, não percentuais abstratos**: "R$ 280/mês em juros" impacta mais que "taxa de 14% a.m."

3. **Traduza números em contexto real**: "Seus gastos invisíveis (R$ 1.490) são maiores que seu aluguel (R$ 1.200)" cria clareza imediata.

4. **Uma prioridade por vez**: Não sobrecarregue com 5 ações simultâneas. Identifique a alavanca de maior impacto para os próximos 30 dias.

5. **Explique o raciocínio**: Não apenas diga "faça X", explique por que X é mais importante que Y ou Z neste momento.

6. **Conecte finanças e fé com equilíbrio**: Ao abordar contribuições do reino, integre princípios de mordomia sem culpa ou pressão. Organização financeira É mordomia.

## Observações Finais

- Este skill é o ponto de entrada do sistema de finanças pessoais. Ele não resolve problemas — ele cria clareza sobre qual problema atacar primeiro.
- A qualidade do diagnóstico depende da qualidade das informações coletadas. Se o usuário não souber valores exatos, ajude a estimar baseado em extratos bancários e faturas.
- O diagnóstico deve ser revisitado a cada 3-6 meses, pois gargalos mudam conforme a situação evolui.
- Se o usuário mencionar contexto de família (cônjuge, filhos), ajuste a análise para considerar renda familiar total e despesas compartilhadas.
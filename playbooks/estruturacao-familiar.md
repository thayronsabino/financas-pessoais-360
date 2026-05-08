# Playbook: Estruturação Financeira Familiar

> **Tipo:** Playbook Operacional Premium  
> **Versão:** 1.0.0  
> **Estado-alvo:** Família sem orçamento → Família com Sistema de Orçamento Doméstico operacional  
> **Duração:** 3–6 meses  
> **Última atualização:** 2026-05-07

Este playbook estrutura financeiramente uma família que opera "no automático" — onde cada membro toma decisões isoladas, gastos vivem em pessoas diferentes (cartão dele, débito dela, compras da casa em 3 lugares) e ninguém tem visão do todo.

---

## 1. Quando Ativar

```
SE ALGUM destes for verdadeiro:
  - Família funciona com 2+ contas/cartões sem visão consolidada
  - Cônjuges não conhecem renda completa um do outro
  - Filhos crescendo sem participação financeira
  - "Some dinheiro" no fim do mês sem causa identificada
  - Conflitos sobre gastos sem dados objetivos
  - Decisões grandes (carro, viagem, escola) sem estrutura
ENTÃO: ATIVAR Estruturação Financeira Familiar
```

---

## 2. Estado-alvo de Saída

```
✅ Renda familiar consolidada e visível para todos os adultos
✅ Sistema de Orçamento Doméstico familiar operacional
✅ Reunião Financeira Familiar mensal estabelecida (ritual)
✅ Filhos com participação adequada por idade
✅ Camada de Proteção Financeira familiar definida e em construção
✅ Decisões grandes seguindo Framework de Priorização Financeira
✅ Dízimo familiar estruturado e automatizado
```

---

## 3. Estrutura do Playbook (5 Etapas)

### ETAPA 1 — Diagnóstico Familiar Conjunto (Semanas 1–2)

**Objetivo:** Visibilidade total da situação familiar.

#### Reunião Financeira #1 — Abertura Honesta

**Duração:** 90 minutos. **Participantes:** Cônjuges (filhos podem participar conforme idade — ver Etapa 4).

**Pauta estruturada:**

1. **Pacto inicial (10 min):** Combinar que durante este processo *não há culpados* — só dados. O objetivo é construir sistema, não apurar erros passados.
2. **Mapeamento de fontes de renda (15 min):**
   - Salários, freelas, aluguéis, dividendos, pensões
   - Renda variável: comissões, 13°, bônus, restituição IR
3. **Mapeamento de despesas por "ponto de saída" (45 min):**
   - Conta corrente A (cônjuge 1)
   - Conta corrente B (cônjuge 2)
   - Conta conjunta (se houver)
   - Cartões de crédito (cada um)
   - Dinheiro físico
4. **Listar todas as dívidas (15 min):** Saldo, taxa, parcela, em nome de quem
5. **Definir quem documenta (5 min):** Um dos cônjuges fica responsável pela planilha mestra

**Output:** Snapshot Financeiro familiar consolidado (usar `/pessoal-diagnostico-financeiro`).

#### Decisão de Modelo de Gestão (Reunião #2)

**Duração:** 60 minutos. **Quando:** 7 dias após a Reunião #1.

**3 modelos a escolher:**

| Modelo | Como funciona | Indicado para |
|--------|--------------|---------------|
| **100% Conjunto** | Toda renda → conta familiar única; cada um tem mesada pessoal | Casais com objetivos muito alinhados |
| **Misto Proporcional** | Cada um contribui % proporcional à renda para conta familiar; mantém conta individual | Casais com rendas diferentes ou autonomia importante |
| **Separado com Acordos** | Cada um cuida de despesas específicas (ele paga moradia, ela paga educação); revisão mensal | Casais que preferem mais autonomia |

**Decisão registrada:** Documentar o modelo escolhido. Pode ser revisado em 6 meses se não funcionar.

---

### ETAPA 2 — Sistema de Orçamento Doméstico Familiar (Semanas 3–6)

**Objetivo:** Implantar o Sistema de Orçamento Doméstico para a família.

#### Particularidades Familiares

**Categorias adicionais comuns em famílias:**
- Educação dos filhos (escola, material, atividades extracurriculares)
- Plano de saúde família
- Despesas com pets
- Mensagens (presentes para pais, sobrinhos)
- Reserva específica para férias familiares
- Reserva para troca de eletrodomésticos / manutenção

**Tetos compartilhados vs. individuais:**
- Compartilhados: moradia, alimentação básica, transporte, saúde, educação
- Individuais: cuidados pessoais, lazer próprio, vestuário, hobbies

#### Implantação

**Semana 3:** Executar `/pessoal-orcamento-domestico` adaptado para família. Distribuir os 4 blocos:

```
BLOCO REINO (10%+)
  Dízimo familiar consolidado (10% renda total)
  Ofertas (acordadas em conjunto)

BLOCO ESSENCIAL (45-55%)
  Moradia, contas, alimentação, transporte, saúde, educação dos filhos

BLOCO ESTILO DE VIDA (20-25%)
  Lazer familiar
  "Mesada" individual de cada cônjuge (autonomia)
  Restaurantes, viagens curtas

BLOCO FUTURO (15-25%)
  Camada de Proteção Financeira familiar (6 meses)
  Reserva para objetivos (escola dos filhos, casa, viagem)
  Investimentos longo prazo
```

**Semana 4–5:** Configurar tracking. Apps com modo família funcionam bem (Mobills Família, Organizze).

**Semana 6:** Primeiro Ciclo de Recalibração Financeira semanal em conjunto (toda sexta, 30 min).

---

### ETAPA 3 — Reunião Financeira Familiar Mensal (Ritual)

**A partir do mês 2, esta é a peça central do sistema.**

#### Estrutura Padrão (90 minutos)

**Primeira sexta de cada mês, ou primeiro sábado pela manhã.**

```
1. ABERTURA (10 min)
   - Oração ou momento de gratidão
   - Revisão dos compromissos do mês anterior

2. FECHAMENTO DO MÊS (30 min)
   - Comparativo planejado vs. realizado por categoria
   - Diagnóstico de desvios > 15%
   - Identificação de causas raiz

3. RECALIBRAÇÃO (20 min)
   - Ajustes de tetos
   - Decisões sobre eventos do próximo mês
   - Confirmação de aporte na Camada de Proteção Financeira

4. CONTRIBUIÇÕES DO REINO (10 min)
   - Validar dízimo
   - Avaliar ofertas regulares
   - Discutir projetos especiais

5. OBJETIVOS DE MÉDIO PRAZO (15 min)
   - Status dos objetivos (escola dos filhos, casa, troca de carro)
   - Ajustes necessários

6. ENCERRAMENTO (5 min)
   - 1 micro-hábito familiar para o próximo mês
   - Próxima reunião agendada
```

**Regras de ouro da reunião:**
- Sem celular
- Sem televisão
- Sem julgamento
- Decisões registradas

---

### ETAPA 4 — Participação dos Filhos por Idade

A educação financeira dos filhos é parte da estruturação. **Adapte a participação:**

#### 0–5 anos
- Os pais decidem; criança ainda não participa
- Foco: pais resolverem seus próprios padrões antes de transmitir

#### 6–10 anos
- Mesada simbólica (R$ 10–30/semana ou mensal)
- Cofrinho com 3 divisões: GASTAR / POUPAR / DAR (Reino)
- Conversa simples sobre dízimo: 10% para Deus
- Permitir erros pequenos (gastar tudo no doce e ficar sem)

#### 11–14 anos
- Mesada maior, com responsabilidades específicas (lanche da escola, material extra)
- Conta poupança em nome dos pais com extrato compartilhado
- Participação parcial em decisões: "vamos viajar para A ou B?"
- Educação sobre cartão e juros

#### 15–18 anos
- Considerar conta universitária jovem (Nubank, Inter, C6 — disponíveis para menores)
- Participar de parte da Reunião Financeira Familiar (a parte de objetivos)
- Trabalho/estágio: começar a contribuir simbolicamente para a casa
- Educação sobre Camada de Proteção Financeira própria

#### 19+ anos (morando em casa)
- Contribuição financeira proporcional para custos da casa (mesmo que pequena)
- Reunião financeira individual com os pais para coaching
- Início do próprio Sistema de Orçamento Doméstico

---

### ETAPA 5 — Construção da Camada de Proteção Financeira Familiar

**Características específicas para família:**

#### Cálculo da Meta

```
Camada de Proteção Familiar = 6-9 meses × Gastos Essenciais Familiares

Onde Gastos Essenciais Familiares incluem:
  + Moradia (aluguel/financiamento + condomínio + IPTU)
  + Contas básicas (água, luz, gás, internet, telefones)
  + Alimentação (mercado + feira)
  + Transporte essencial (combustível + transporte público + manutenção)
  + Saúde (plano + medicamentos recorrentes)
  + Educação dos filhos (escola + material)
  + Seguros essenciais (vida, residencial)
```

**Exemplo:** Família com gastos essenciais de R$ 5.500/mês → Camada de Proteção de R$ 33.000–49.500.

#### Ritmo de Construção

```
SE estado familiar = ORGANIZAÇÃO:
  Aporte mensal: 10-15% da renda líquida
  Prioridade: 70% para Camada / 30% para outros objetivos

SE estado familiar = ESTABILIZAÇÃO (pré-completar):
  Aporte mensal: 15-20% da renda líquida
  Prioridade: 50% Camada / 50% objetivos
```

---

## 4. Painel de Acompanhamento Familiar

```
╔══════════════════════════════════════════════════╗
║   ESTRUTURAÇÃO FINANCEIRA FAMILIAR — MÊS [N]/6  ║
╠══════════════════════════════════════════════════╣
║  ESTADO FAMILIAR:    [ESTADO]                    ║
║  MODELO DE GESTÃO:   [CONJUNTO/MISTO/SEPARADO]   ║
║  REUNIÃO MENSAL:     [ATIVA / PENDENTE]          ║
╠══════════════════════════════════════════════════╣
║  RENDA FAMILIAR:     R$ [X]                      ║
║  DÍZIMO FAMILIAR:    R$ [X] (10%)                ║
║  CAMADA PROTEÇÃO:    R$ [X] / R$ [META] = [X]%  ║
╠══════════════════════════════════════════════════╣
║  FILHOS PARTICIPANDO: [SIM/NÃO/PARCIAL]          ║
║  PRÓXIMA REUNIÃO:    [DATA]                      ║
╚══════════════════════════════════════════════════╝

PROGRESSO DA ESTRUTURAÇÃO
Diagnóstico Conjunto:    [██████████] 100% ✅
Modelo de Gestão:        [██████████] 100% ✅
Sistema de Orçamento:    [████████░░] 80%
Reunião Mensal:          [██████░░░░] 60%
Participação Filhos:     [███░░░░░░░] 30%
Camada de Proteção:      [████░░░░░░] 40%
```

---

## 5. Sinais de Alerta

```
SE em qualquer mês ocorrer:
  - Cancelamento da Reunião Financeira Familiar 2 meses seguidos
  - Conflito recorrente sobre gastos não resolvido por dados
  - Um cônjuge "esconde" gastos do outro
  - Decisões grandes sendo tomadas unilateralmente
  - Filhos sendo expostos a discussões financeiras tensas
ENTÃO:
  → PAUSAR cronograma
  → Considerar ativação do Playbook "Casal e Finanças" para resolução de dinâmica
```

---

## 6. Adaptações por Configuração Familiar

### Família Monoparental
- Reunião Financeira é individual (com Deus, com diário, com mentor)
- Filhos com 11+ anos participam mais cedo
- Camada de Proteção 9–12 meses (não há "renda secundária" para emergências)

### Família com Pais Idosos Dependentes
- Adicionar bloco específico: "Cuidado com pais"
- Considerar custos de saúde, cuidador, eventual moradia
- Planejamento de longo prazo

### Família com Renda Muito Alta
- Risco oposto: "som dinheiro" mesmo com sobra grande
- Foco em estilo de vida proporcional, não inflado
- Bloco Reino crescente (Método Wesleyano)

### Família com Renda Apertada
- Manter dízimo 10% inviolável
- Camada de Proteção em construção lenta (R$ 50/mês se necessário)
- Foco em educação financeira dos filhos para quebrar ciclo

---

## 7. Skills do Pacote Usadas

| Etapa | Skill Principal |
|-------|----------------|
| 1 | `/pessoal-diagnostico-financeiro` (familiar) |
| 2 | `/pessoal-orcamento-domestico` (familiar) |
| 3 | `/pessoal-rotina-financeira-mensal` (Reunião Familiar) |
| 5 | `/pessoal-plano-dividas-reserva` (Camada Familiar) |
| Contínuo | `/pessoal-investimento-reino` (Bloco Reino familiar) |

---

## 8. Princípios Operacionais

**Família com sistema é família tranquila.** A maioria dos conflitos financeiros não é por falta de dinheiro — é por falta de dados e estrutura.

**Reunião Financeira é não-negociável.** Mensal, no calendário, com pauta. Pular reunião é pular o sistema.

**Filhos aprendem por exposição estruturada.** Não é "agora você é adulto, vire-se" aos 18. É construção gradual desde os 6.

**Sem culpados, com dados.** Quem gastou mais não é "o errado". O orçamento que não comportou aquele gasto é que precisa de ajuste — ou aquele gasto que precisa de redução. Distinção crítica.

**Dízimo familiar é decisão familiar.** 10% sobre renda total da família, sai antes de qualquer outra categoria.

**Mordomia inclui criar herdeiros fiéis.** Provérbios 22:6 — instrua o menino no caminho em que deve andar.

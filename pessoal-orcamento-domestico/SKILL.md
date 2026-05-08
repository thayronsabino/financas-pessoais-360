---
name: pessoal-orcamento-domestico
description: >
  Implanta o Sistema de Orçamento Doméstico — estrutura de controle de fluxo financeiro com categorias, tetos por bloco, Ciclo de Recalibração Financeira semanal e integração de contribuições do Reino como primeira prioridade. Use quando o usuário mencionar orçamento familiar, planejamento financeiro pessoal, controle de gastos, organizar finanças da casa, definir teto de gastos, planejar economia mensal, criar orçamento pessoal, controlar despesas mensais, estabelecer meta de poupança, dividir salário em categorias, quando gastos variam sem controle, ou falta dinheiro antes do fim do mês.
owner: financeiro-pessoal
version: 2.0.0
last_updated: 2026-05-07
---

# Sistema de Orçamento Doméstico

## Postura do Sistema

Este skill não explica o que é um orçamento. Ele implanta um Sistema de Orçamento Doméstico funcional, com tetos por bloco, motor de decisão para estouros e Ciclo de Recalibração Financeira semanal. O usuário sai com um sistema operacional, não com um documento.

> "Um orçamento que não é revisado toda semana é um documento morto. O Sistema de Orçamento Doméstico é uma rotina viva."

## Arquivos Consultados pelo Sistema

| Arquivo | Quando consultar |
|---------|------------------|
| `../REFERENCIAS-BRASIL-2026.md` | Para faixas de IR/INSS (cálculo do líquido) e referências de comprometimento saudável |
| `../GLOSSARIO.md` | Para terminologia padronizada (Bloco Reino, Bloco Essencial, Camada de Proteção Financeira, etc.) |
| `../EDUCACAO-FINANCEIRA-BASICA.md` | Para usuário iniciante que precisa entender conceitos básicos primeiro |
| `../PRINCIPIOS-BIBLICOS-EXPANDIDOS.md` | Para temas como contentamento, idolatria do consumo, hospitalidade |
| `../playbooks/estruturacao-familiar.md` | Quando o usuário é família sem orçamento estruturado |
| `../playbooks/casal-e-financas.md` | Quando há conflito ou desalinhamento entre cônjuges |
| `../playbooks/idoso-aposentadoria-insuficiente.md` | Para 60+ com aperto financeiro |
| `../playbooks/informal-sem-cnpj.md` | Para trabalhador informal com renda variável |
| `../frameworks/priorizacao-financeira.md` | Para validar a alocação dos blocos por estado financeiro |

## Regra de Linguagem

```
PROTOCOLO:
- Primeira menção: termo proprietário + tradução entre parênteses
  Ex: "Bloco Reino (categoria de dízimo e ofertas)"
  Ex: "Ciclo de Recalibração Financeira (revisão semanal)"
- Menções subsequentes: termo proprietário direto
- Estado SOBREVIVÊNCIA ou iniciante: priorizar linguagem simples
- Estado ESTABILIZAÇÃO+: termos proprietários consolidados

A linguagem serve ao usuário, não o contrário.
```

---

## FINANCIAL STATE ENGINE

O Sistema de Orçamento Doméstico opera diferente por estado financeiro:

| Estado | Abordagem do Orçamento | Protocolo Ativo |
|--------|----------------------|-----------------|
| **SOBREVIVÊNCIA** | Orçamento de crise: cortes agressivos, foco em essenciais | Estancar Sangria |
| **ORGANIZAÇÃO** | Orçamento de base: categorias definidas, tetos realistas | Construção de Base |
| **ESTABILIZAÇÃO** | Orçamento de crescimento: sobra direcionada para reserva | Proteção Ativa |
| **EXPANSÃO** | Orçamento de multiplicação: excedente para investimentos | Multiplicação Responsável |

**Regra:** Antes de definir tetos, classificar o estado financeiro. Um usuário em SOBREVIVÊNCIA não recebe estrutura de EXPANSÃO.

---

## CAMADAS COGNITIVAS

| Camada | O Sistema Faz |
|--------|---------------|
| **DIAGNÓSTICO** | Mapeia gastos reais dos últimos 3 meses |
| **INTERPRETAÇÃO** | Identifica padrão de consumo e categorias problemáticas |
| **ESTRATÉGIA** | Define blocos, tetos e regras de ajuste |
| **EXECUÇÃO** | Entrega Sistema de Orçamento Doméstico operacional |
| **SUSTENTAÇÃO** | Implanta Ciclo de Recalibração Financeira semanal |

---

## Entradas Necessárias

| Entrada | Obrigatória? | Exemplo |
|---------|--------------|---------|
| Renda líquida mensal | Sim | R$ 6.500 |
| Custos fixos | Sim | Moradia, contas, escola, seguros |
| Custos variáveis estimados | Sim | Mercado, transporte, lazer |
| Meta de poupança | Não | 15% da renda |
| Contribuições do reino | Não | Dízimo 10%, ofertas |

---

## ENGINE DE DECISÃO — Estrutura de Blocos

### Blocos do Sistema de Orçamento Doméstico

O sistema organiza o orçamento em 4 blocos funcionais:

```
SE estado = SOBREVIVÊNCIA:
  BLOCO ESSENCIAL: 65-70% (moradia, alimentação, transporte, saúde)
  BLOCO ESTILO DE VIDA: 10-15% (cortes agressivos)
  BLOCO DÍVIDAS: máximo disponível
  BLOCO REINO: dízimo 10% inviolável + ofertas pausadas
  BLOCO FUTURO: residual (mínimo R$ 50/mês de colchão)

SE estado = ORGANIZAÇÃO:
  BLOCO ESSENCIAL: 50-55% (necessidades básicas)
  BLOCO ESTILO DE VIDA: 20-25%
  BLOCO REINO: 10-13% (dízimo + ofertas proporcionais)
  BLOCO FUTURO: 15-20% (reserva + quitação de dívidas)

SE estado = ESTABILIZAÇÃO ou acima:
  BLOCO ESSENCIAL: 45-50%
  BLOCO ESTILO DE VIDA: 25-30%
  BLOCO REINO: 10-15% (dízimo + ofertas crescentes)
  BLOCO FUTURO: 20-25% (reserva + investimentos)
```

### Regra das Primícias (Contribuições do Reino)

**Abordagem Primícias (recomendada):**
- Dízimo (10%) sai PRIMEIRO, antes de qualquer categoria
- Orçamento é construído sobre a renda pós-dízimo
- Ofertas saem do Bloco Estilo de Vida conforme capacidade

**Abordagem Categoria Fixa:**
- Dízimo entra no Bloco Essencial
- Demais blocos ajustados para comportar

---

## Estrutura das Categorias

### Bloco Essencial (Sobrevivência básica)
- Moradia (aluguel/financiamento, condomínio, IPTU)
- Serviços (água, luz, gás, internet, telefone)
- Alimentação (mercado, feira)
- Transporte (combustível, transporte público, prestação veículo)
- Saúde (plano, medicamentos recorrentes)
- Educação (escola, cursos obrigatórios)

### Bloco Estilo de Vida (Escolhas conscientes)
- Lazer e entretenimento
- Restaurantes e delivery
- Assinaturas (streaming, academia, apps)
- Vestuário e cuidados pessoais
- Presentes e imprevistos
- Ofertas voluntárias especiais

### Bloco Reino (Investimento de fé)
- Dízimo (10% mínimo inviolável — primeira linha do orçamento)
- Ofertas regulares
- Projetos ministeriais e missões

### Bloco Futuro (Não tocar)
- Camada de Proteção Financeira (reserva de emergência)
- Poupança para objetivos
- Investimentos de longo prazo
- Pagamento acelerado de dívidas

---

## Processo de Implantação

### Fase 1 — Diagnóstico Real (não o ideal)

Antes de criar o orçamento:
- Liste todos os gastos dos últimos 3 meses (extratos bancários, cartões)
- Calcule a média mensal por categoria
- Compare com a renda líquida: sobra ou falta?

> O orçamento parte do que é real — não do que o usuário gostaria de gastar.

### Fase 2 — Definição de Tetos por Bloco

Para cada categoria:
- Use a média histórica como base
- Aplique cortes realistas onde houver excesso (5–10% por vez, nunca 50%)
- Marque categorias inflexíveis vs. flexíveis

**Exemplo para renda de R$ 6.500:**

```
BLOCO REINO — R$ 650 (10%) [PRIMÍCIA — sai primeiro]
────────────────────────────────────────────
BLOCO ESSENCIAL — R$ 3.250 (50%)
  Moradia:       R$ 1.400
  Serviços:      R$ 450
  Alimentação:   R$ 800
  Transporte:    R$ 400
  Saúde:         R$ 200

BLOCO ESTILO DE VIDA — R$ 1.625 (25%)
  Lazer:         R$ 500
  Restaurantes:  R$ 400
  Assinaturas:   R$ 150
  Vestuário:     R$ 300
  Imprevistos:   R$ 275

BLOCO FUTURO — R$ 975 (15%)
  Reserva:       R$ 700
  Objetivos:     R$ 275
────────────────────────────────────────────
TOTAL:           R$ 6.500 (100%)
```

### Fase 3 — ENGINE DE DECISÃO para Estouros

```
SE categoria estourou:

  AÇÃO 1 (prioridade): Compensar na mesma semana
    → Estouro em Lazer? Reduza Restaurantes ou Vestuário no mesmo mês
    → Nunca compense tirando do Bloco Futuro ou do Bloco Reino

  AÇÃO 2: Revisar o teto
    → Se estoura 3 meses seguidos, o teto está irrealista
    → Aumente essa categoria e reduza outra permanentemente
    → Documente o ajuste no Ciclo de Recalibração Financeira

  AÇÃO 3 (emergências reais):
    → Use a Camada de Proteção Financeira (reserva)
    → Reponha nos próximos 2 meses
    → "Promoção imperdível" NÃO é emergência
```

### Fase 4 — Ciclo de Recalibração Financeira Semanal (15 minutos)

Toda sexta ou domingo — sem exceção:

1. **Consolidar** — gastos da semana (extratos + notas)
2. **Atualizar** — saldo restante por categoria (quanto resta do teto?)
3. **Identificar** — estouros e aplicar Engine de Decisão
4. **Planejar** — semana seguinte (compras grandes, eventos)
5. **Registrar** — aprendizados (o que funcionou, o que não funcionou)

**Ferramenta:** Planilha simples ou app (Mobills, Organizze, Guiabolso)

### Fase 5 — Ciclo de Recalibração Financeira Mensal (30 minutos)

No último dia do mês:

1. **Balanço geral** — sobrou ou faltou?
2. **Categorias problemáticas** — quais estouraram?
3. **Ajuste de tetos** — realocar percentuais se necessário
4. **Confirmar contribuições do Reino** — dízimo calculado, ofertas realizadas
5. **Definir foco do próximo mês** — onde economizar mais?

---

## Adaptações por Situação

### Renda Variável (autônomos, comissionados)

```
SE renda variável:
  Base de cálculo = menor renda dos últimos 6 meses
  Meses acima da base → excedente 100% para Camada de Proteção Financeira
  Meta de reserva = 6 meses (não 3)
```

### Renda Muito Apertada (próximo ao salário mínimo)

```
SE comprometimento essencial > 70%:
  Ajuste temporário: 60% essencial / 20% estilo de vida / 10% futuro
  MANTER dízimo 10% — ofertas voluntárias podem ser pausadas
  Foco: reduzir custos fixos (moradia menor, transporte mais barato)
```

### Casal com Orçamento Conjunto

```
SE casal:
  Contribuição de cada um = proporcional à renda
  Categorias individuais (cuidados pessoais) ficam separadas
  Ciclo de Recalibração Financeira semanal = em conjunto
  Dízimo = sobre renda familiar total
```

### Com Dívidas Altas

```
SE dívidas > 20% da renda:
  Inverta temporariamente:
  50% essenciais / 20% estilo de vida / 30% quitação
  Retorne ao padrão após quitar dívidas caras
  Use /pessoal-plano-dividas-reserva para estratégia completa
```

---

## Saída Esperada

### PAINEL DO SISTEMA DE ORÇAMENTO DOMÉSTICO

```
╔══════════════════════════════════════════════╗
║     SISTEMA DE ORÇAMENTO DOMÉSTICO           ║
╠══════════════════════════════════════════════╣
║  ESTADO FINANCEIRO:  [ESTADO]                ║
║  PROTOCOLO ATIVO:    [PROTOCOLO]             ║
╠══════════════════════════════════════════════╣
║  RENDA LÍQUIDA:  R$ [X]                      ║
║  DÍZIMO (1°):    R$ [X] — [X%]               ║
║  ESSENCIAL:      R$ [X] — [X%]               ║
║  ESTILO VIDA:    R$ [X] — [X%]               ║
║  FUTURO:         R$ [X] — [X%]               ║
╠══════════════════════════════════════════════╣
║  META SOBRA:     R$ [X]/mês                  ║
╚══════════════════════════════════════════════╝

PROGRESSO DA ESTABILIZAÇÃO
Reserva:   [████░░░░░░] X%
Dívidas:   [███████░░░] X%
Controle:  [████░░░░░░] X%

MAPA OPERACIONAL
[✔] Sistema de Orçamento implantado
[ ] Ciclo de Recalibração semanal ativo
[ ] Dívidas caras eliminadas
[ ] Camada de Proteção Financeira (3 meses)
[ ] Estratégia patrimonial ativa
```

### Tabela de Orçamento Mensal

```
| Bloco           | Categoria    | Teto  | Gasto | Saldo | Status |
|-----------------|--------------|-------|-------|-------|--------|
| REINO           | Dízimo       | X.XXX | X.XXX | X     | ✅ 1°  |
| ESSENCIAL       | Moradia      | X.XXX | X.XXX | X     | ✅     |
| ESSENCIAL       | Alimentação  | X.XXX | X.XXX | X     | ✅     |
| ESTILO DE VIDA  | Lazer        | X.XXX | X.XXX | X     | ⚠️     |
| FUTURO          | Reserva      | X.XXX | X.XXX | X     | ✅     |
| **TOTAL**       |              | X.XXX | X.XXX | X     |        |
```

### Regras de Ajuste Personalizadas

Definir 3 regras específicas para a situação do usuário:
- "Se estouro Lazer, compenso em Restaurantes na mesma semana"
- "Camada de Proteção Financeira só para: desemprego, saúde, manutenção urgente"
- "Revisar tetos a cada 3 meses ou quando houver mudança de renda"

### Bloco de Contribuições do Reino

```
Dízimo:  R$ [X] ([X]% da renda) — Primeira linha, sai antes de tudo
Ofertas: R$ [X]/mês — acumulados para campanhas trimestrais
```

### Próxima Skill

```
SE há dívidas ativas → /pessoal-plano-dividas-reserva
SE não há dívidas E quer criar hábitos → /pessoal-rotina-financeira-mensal
SE não há dívidas E quer estruturar contribuições → /pessoal-investimento-reino
```

---

## Princípios de Sustentabilidade

**Realismo antes de idealismo:** Cortes de 50% em lazer não se sustentam. Reduza 10% por mês.

**Automatize o futuro:** Transfira o Bloco Futuro no dia do salário, antes de gastar.

**Permita flexibilidade:** Um mês que estoura por motivo válido tem compensação no próximo — não abandono.

**Revise, não abandone:** Se não funcionar, ajuste. O Sistema de Orçamento Doméstico é ferramenta viva.

**Envolva a família:** Orçamento individual funciona. Familiar exige alinhamento de todos.

## Armadilhas Comuns

- **Subestimar variáveis:** Mercado, transporte e lazer custam sempre mais que o estimado. Use média real
- **Esquecer despesas anuais:** IPTU, seguro, matrícula. Divida por 12 e reserve mensalmente
- **Ignorar pequenos gastos:** Cafezinho, app, Uber. Somados consomem 10–15% da renda
- **Compra por emoção:** Regra das 24 horas — se couber no orçamento amanhã, compre
- **Desistir no primeiro estouro:** Ninguém acerta no primeiro mês. Ajuste e siga

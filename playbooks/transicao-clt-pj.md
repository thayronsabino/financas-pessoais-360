# Playbook: Transição CLT → PJ

> **Tipo:** Playbook Operacional Premium  
> **Versão:** 1.0.0  
> **Estado-alvo:** Trabalhador CLT → Profissional PJ estruturado  
> **Duração:** 1–3 meses (preparação) + 6 meses (estabilização)  
> **Última atualização:** 2026-05-07

A transição de CLT para PJ é um movimento financeiro de alto risco e alto retorno. Este playbook estrutura a mudança evitando os 7 erros comuns: (1) subestimar carga tributária, (2) não constituir reserva específica, (3) ignorar previdência, (4) misturar pessoa física e jurídica, (5) confundir faturamento com renda, (6) não calcular benefícios CLT perdidos, (7) não planejar transição emocional.

---

## 1. Quando Ativar

```
SE o usuário menciona:
  - "Estou pensando em virar PJ"
  - "Recebi proposta de PJ que paga R$ X"
  - "Já sou PJ mas estou desorganizado"
  - "Quero abrir empresa para prestar serviço"
ENTÃO: ATIVAR Transição CLT → PJ

PRÉ-REQUISITO CRÍTICO:
  Estado financeiro = ESTABILIZAÇÃO ou superior
  → Camada de Proteção Financeira de pelo menos 3 meses ANTES da transição
  → Sem dívidas com taxa > Selic
  
SE não estiver em ESTABILIZAÇÃO:
  → Concluir Estado anterior antes de transicionar
  → Transição em SOBREVIVÊNCIA = risco extremo
```

---

## 2. Estado-alvo de Saída

```
✅ Decisão consciente CLT vs. PJ baseada em comparativo real (não em "valor bruto")
✅ Camada de Proteção Financeira específica para PJ constituída (12 meses)
✅ Empresa aberta com regime tributário ótimo (Simples vs. Lucro Presumido)
✅ Pessoa física e jurídica completamente separadas (contas, cartões, despesas)
✅ Pró-labore e distribuição de lucros estruturados
✅ Previdência privada complementar ativa (ou estratégia equivalente)
✅ Plano de saúde particular contratado
✅ Reserva trabalhista (substituto FGTS + 13° + férias)
✅ Contador contratado e processos de fim de mês estabelecidos
```

---

## 3. Análise CLT vs. PJ (Fase Decisória)

### 3.1 Comparativo Real de Renda Líquida

**CLT — Salário R$ 10.000 (exemplo):**

```
Salário bruto:                    R$ 10.000,00
(-) INSS (14% até teto)            R$ -951,63
(-) IR (27,5% - dedução)           R$ -1.146,52
                                   ─────────────
SALÁRIO LÍQUIDO:                   R$ 7.901,85

BENEFÍCIOS NÃO TRIBUTÁVEIS:
  + Vale refeição (~R$ 600)
  + Vale transporte (~R$ 200)
  + Plano de saúde (~R$ 800 valor equivalente)
  + Plano odonto (~R$ 80)
  + Seguro de vida em grupo (~R$ 50)
  + FGTS (8% acumulado): R$ 800/mês
  + 13° salário: ~R$ 833/mês equivalente
  + Férias + 1/3: ~R$ 1.111/mês equivalente
                                   ─────────────
VALOR TOTAL DO PACOTE CLT:        ~R$ 12.376/mês
```

**PJ — Faturamento R$ 14.000 (proposta equivalente comum):**

```
Faturamento bruto:                R$ 14.000,00

(-) Simples Nacional (Anexo III, fator R ≥ 28%):
    Alíquota inicial 6% (até R$ 180k anual)
    Alíquota 11,2% (R$ 180k–360k anual)
    Estimativa média: 8-12%        R$ -1.400,00

(-) Pró-labore (mín. R$ 1.518 + INSS 11%):
    Pró-labore: R$ 1.518
    INSS sobre pró-labore (11%):    R$ -167,00
    IR sobre pró-labore: ISENTO

(-) Plano de saúde particular:     R$ -800,00
(-) Plano odonto:                  R$ -80,00
(-) Contador (~R$ 200-400/mês):    R$ -300,00
(-) Previdência privada:           R$ -700,00 (10% para suprir falta de FGTS+13°+férias)
                                   ─────────────
RENDA LÍQUIDA EFETIVA:             ~R$ 10.553,00

DIFERENÇA EM RELAÇÃO AO PACOTE CLT: + R$ -1.823 → 
TRANSIÇÃO COM ESSA PROPOSTA = PERDA
```

### 3.2 Regra de Equivalência

**Regra heurística:** Para que PJ compense, o faturamento precisa ser **40–60% maior** que o salário CLT equivalente.

```
SE proposta_pj < salario_clt × 1.40:
  TRANSIÇÃO_NÃO_COMPENSA → recusar ou negociar mais

SE proposta_pj entre salario_clt × 1.40 e × 1.60:
  TRANSIÇÃO_NEUTRA → analisar caso a caso

SE proposta_pj > salario_clt × 1.60:
  TRANSIÇÃO_VANTAJOSA → seguir adiante
```

### 3.3 Variáveis Não-Financeiras a Considerar

- **Estabilidade:** CLT tem demissão com aviso prévio + multa; PJ pode ser cortado em 30 dias
- **Aposentadoria:** CLT recolhe automaticamente; PJ exige disciplina (pró-labore + previdência)
- **Crédito:** Bancos olham CLT como mais "seguro" para empréstimos
- **Tempo:** PJ exige tempo administrativo (fiscal, contador, emissão de NF)
- **Futuro profissional:** PJ permite múltiplos clientes; CLT é exclusividade típica

---

## 4. Cronograma de Transição

### MÊS -2 (Preparação Profunda)

#### Semana 1 — Decisão Estruturada

- [ ] Calcular comparativo real CLT vs. PJ (seção 3 acima)
- [ ] Aplicar regra de equivalência
- [ ] Decidir: aceitar / negociar / recusar
- [ ] Se aceitar, negociar período de aviso prévio adequado

#### Semana 2 — Fortalecimento da Camada de Proteção

- [ ] Verificar estado da Camada de Proteção Financeira
- [ ] Se < 6 meses: postergar transição até completar
- [ ] Se ≥ 6 meses: planejar elevar para 12 meses antes do fim do CLT

#### Semana 3 — Pesquisa Tributária e Empresarial

- [ ] Decidir tipo de empresa: ME, EPP, EIRELI (extinta) → preferir Sociedade Limitada Unipessoal (SLU)
- [ ] Decidir regime: Simples Nacional × Lucro Presumido
- [ ] Pesquisar contadores: fixed fee mensal vs. % do faturamento
- [ ] Endereço da empresa: residencial × coworking × CNPJ virtual

#### Semana 4 — Contratação e Documentação

- [ ] Contratar contador
- [ ] Iniciar abertura da empresa (CNPJ)
- [ ] Abrir conta bancária PJ (Inter, Cora, BTG, Bradesco, etc.)
- [ ] Solicitar certificado digital (e-CNPJ)

---

### MÊS -1 (Pré-Operacional)

#### Semana 5–6 — Estrutura Operacional

- [ ] CNPJ ativo e regular
- [ ] Conta bancária PJ funcional
- [ ] Cartão de crédito PJ (separação total da PF)
- [ ] Contrato de prestação de serviços com cliente revisado por advogado
- [ ] Sistema de emissão de notas fiscais (NFE.io, eNotas, sistema da prefeitura)

#### Semana 7 — Configuração Financeira

- [ ] Calcular pró-labore (mínimo legal: 1 salário mínimo)
- [ ] Configurar transferência automática de pró-labore (PJ → PF)
- [ ] Definir reserva específica para tributos (parcela mensal)
- [ ] Definir reserva trabalhista (substitui FGTS+13°+férias)

#### Semana 8 — Encerramento CLT

- [ ] Pedido de demissão formal
- [ ] Cálculo de verbas rescisórias: saldo salário, FGTS, 13° proporcional, férias
- [ ] **Não solicitar saque do FGTS** se houver opção de saque-aniversário (manter FGTS como reserva extra)
- [ ] Migração do plano de saúde (CLT pode manter por até 24 meses pagando — Lei 9656/98)

---

### MÊS 1–6 (Estabilização PJ)

#### Mês 1 — Primeiros Passos

**Estrutura financeira mensal recém-iniciada:**

```
FATURAMENTO RECEBIDO NA PJ
  ↓
Reserva tributária (separar 8-12% imediatamente)
  ↓
Pró-labore (mensal, regular, com INSS)
  ↓
Pagamento de despesas operacionais (contador, ferramentas)
  ↓
Distribuição de lucros (após apuração contábil)
  ↓
PESSOA FÍSICA → Sistema de Orçamento Doméstico
```

**Tarefas:**
- [ ] Primeira nota fiscal emitida
- [ ] Primeira apuração de impostos com contador
- [ ] Primeiro pró-labore transferido
- [ ] Configuração de reserva tributária separada

#### Mês 2–3 — Consolidação de Ritmo

- [ ] Revisão das margens com contador
- [ ] Validação de fator R (se Simples Anexo III)
- [ ] Ajuste de pró-labore se necessário
- [ ] Início da previdência privada (PGBL para deduzir IR ou VGBL)

#### Mês 4–6 — Otimização

- [ ] Avaliação do regime tributário (Simples vs. Lucro Presumido — se faturamento alto)
- [ ] Estruturação de múltiplos clientes (se possível, para reduzir risco)
- [ ] Constituição da Camada de Proteção Financeira PJ (12 meses)

---

## 5. Estrutura Financeira PJ Padrão

### 5.1 Separação Total PF × PJ

```
PESSOA JURÍDICA (CNPJ)
├── Conta corrente PJ
├── Cartão crédito PJ
├── Despesas: contador, ferramentas, escritório
└── Recebimentos: clientes via NF

       ↓ (PRÓ-LABORE + DISTRIBUIÇÃO)

PESSOA FÍSICA (CPF)
├── Conta corrente PF
├── Cartão crédito PF
├── Despesas: vida pessoal, família
└── Sistema de Orçamento Doméstico
```

**Regra inviolável:** **Nunca** misturar gastos PF na conta PJ. Almoço pessoal = conta PF. Notebook de trabalho = conta PJ. Plano de saúde familiar = depende (pode ser benefício PJ se justificável).

### 5.2 Estrutura Mensal Sugerida

```
FATURAMENTO PJ: R$ 14.000

PJ:
  Reserva tributária (10%):            R$ 1.400 (separa em conta dedicada)
  Despesas operacionais:               R$ 800 (contador, ferramentas)
  Reserva trabalhista (10%):           R$ 1.400 (substitui FGTS+13°+férias)
  Pró-labore + Distribuição:           R$ 10.400 (transfere para PF)

PF:
  Recebido: R$ 10.400
  Bloco Reino (10%):                   R$ 1.040
  Bloco Essencial (45%):               R$ 4.680
  Bloco Estilo de Vida (20%):          R$ 2.080
  Bloco Futuro (15%):                  R$ 1.560
  Previdência privada (10%):           R$ 1.040
```

### 5.3 Reservas Específicas PJ

| Reserva | Finalidade | Valor Sugerido |
|---------|-----------|----------------|
| **Tributária** | Pagar impostos sem aperto | 10–12% do faturamento mensal |
| **Trabalhista** | Substituir FGTS + 13° + férias | 10% do faturamento mensal |
| **Operacional** | Contador, ferramentas, eventuais | 5% do faturamento mensal |
| **Camada de Proteção PJ** | Período sem cliente | 12 meses de despesas pessoais |

---

## 6. Painel de Acompanhamento

```
╔══════════════════════════════════════════════════╗
║   TRANSIÇÃO CLT → PJ — MÊS [N]                  ║
╠══════════════════════════════════════════════════╣
║  FASE:               [PRÉ / OPERACIONAL / EST]  ║
║  REGIME TRIBUTÁRIO:  [SIMPLES / LUCRO PRES]      ║
║  REGIME ANEXO:       [III / V] (Fator R: [X]%)  ║
╠══════════════════════════════════════════════════╣
║  FATURAMENTO MÊS:    R$ [X]                      ║
║  PRÓ-LABORE:         R$ [X]                      ║
║  TRIBUTOS PAGOS:     R$ [X] ([X]% do fat.)       ║
║  RENDA LÍQUIDA PF:   R$ [X]                      ║
╠══════════════════════════════════════════════════╣
║  RESERVA TRIBUTÁRIA:    R$ [X] / [META]          ║
║  RESERVA TRABALHISTA:   R$ [X] / [META]          ║
║  CAMADA PROTEÇÃO PJ:    R$ [X] / [META 12m]      ║
║  PREVIDÊNCIA:           R$ [X] acumulado         ║
╚══════════════════════════════════════════════════╝

PROGRESSO DA TRANSIÇÃO
Decisão Estruturada:    [██████████] 100% ✅
Empresa Aberta:         [██████████] 100% ✅
Sep. PF/PJ:             [██████████] 100% ✅
Camada Proteção PJ:     [████░░░░░░] 40%
Previdência Ativa:      [████████░░] 80%
```

---

## 7. Erros Comuns a Evitar

```
ERRO 1 — Comemorar o "salário bruto" PJ
  Realidade: o líquido após tributos+previdência+saúde+contador é o que conta

ERRO 2 — Não constituir reserva tributária
  Resultado: ao apurar impostos, falta dinheiro → atraso → multa

ERRO 3 — Misturar conta PF e PJ
  Resultado: contabilidade caótica, multa do Fisco, descontrole

ERRO 4 — Esquecer da previdência
  Resultado: ao envelhecer, sem aposentadoria construída

ERRO 5 — Pró-labore zero ou simbólico
  Resultado: zero contribuição INSS = futuro sem cobertura previdenciária

ERRO 6 — Cliente único
  Resultado: PJ vira CLT disfarçado; perda do cliente = renda zero

ERRO 7 — Achar que distribuição de lucros é "salário"
  Resultado: descontrole entre o que pode/deve ser sacado
```

---

## 8. Sinais de Alerta (Reavaliar Transição)

```
SE em qualquer momento ocorrer:
  - Faturamento mensal cai > 30% em 2 meses seguidos
  - Cliente único exige exclusividade (pode caracterizar vínculo CLT)
  - Camada de Proteção PJ consumida sem reposição
  - Atraso recorrente nos tributos
  - Mistura de contas PF/PJ
ENTÃO:
  → Voltar para o /gestor-financeiro
  → Considerar reverter para CLT se possível
  → Buscar contador para reorganização tributária
```

---

## 9. Skills do Pacote Usadas

| Fase | Skill Principal |
|------|----------------|
| Pré (decisão) | `/gestor-financeiro` (avaliação de prontidão) |
| Pré (reserva) | `/pessoal-plano-dividas-reserva` (Camada Proteção 12m) |
| Operacional | `/pessoal-orcamento-domestico` (PF do PJ) |
| Estabilização | `/pessoal-rotina-financeira-mensal` (mensal) |
| Estabilização | `/pessoal-estrategia-investimentos` (previdência) |
| Contínuo | `/pessoal-investimento-reino` (dízimo sobre pró-labore + distribuição) |

---

## 10. Princípios Operacionais

**Faturamento NÃO é salário.** A primeira armadilha mental do PJ é tratar o dinheiro que entra como se fosse renda imediatamente disponível.

**O Fisco vai cobrar — esteja pronto.** Reserva tributária separada é não-negociável.

**Aposentadoria é sua responsabilidade agora.** Sem FGTS automático, sem INSS automático, sem chefe te enquadrando — você se enquadra.

**Cliente único é vínculo CLT mascarado.** Diversifique sempre que possível. Cliente único = "pessoalidade + subordinação + onerosidade + não eventualidade" → Receita Federal pode reclassificar.

**Contador não é luxo, é infraestrutura.** PJ sem contador é PF acumulando complicações.

**Dízimo sobre faturamento líquido.** Após tributos da PJ, o dízimo (10%) incide sobre o que efetivamente fica com você (pró-labore + distribuição).

**A liberdade do PJ tem preço operacional.** Você ganha autonomia, mas paga em tempo administrativo. Aceite ou contrate alguém.

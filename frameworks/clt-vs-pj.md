# Framework: CLT vs. PJ

> **Tipo:** Framework de Decisão Financeira  
> **Versão:** 1.0.0  
> **Aplicação:** Avaliação comparativa entre regime CLT e PJ para decidir transição ou aceitar proposta  
> **Última atualização:** 2026-05-07

Este framework calcula a **renda líquida real** em cada regime, considerando tributos, benefícios e custos, para responder uma pergunta concreta: *"Esta proposta de PJ vale mais que meu CLT atual?"*. A decisão não é "quanto vou ganhar bruto", é **quanto fica no fim**.

---

## 1. A Armadilha do Bruto

A primeira proposta tipicamente vem como: *"Você ganha R$ 8.000 CLT — vamos te oferecer R$ 11.000 PJ."*

**Sem análise, parece um aumento de 37,5%.**

Com análise, descobre-se que o ganho líquido pode ser **negativo**. A diferença está em tributos, benefícios CLT perdidos e custos PJ ignorados.

---

## 2. Engine de Cálculo Comparativo

### 2.1 Calcular Pacote Total CLT

```
PACOTE TOTAL CLT = SALÁRIO LÍQUIDO + BENEFÍCIOS

SALÁRIO LÍQUIDO = bruto − INSS − IR

  INSS (até teto R$ 8.157,41 em 2026):
    Faixa 1: até 1.518   → 7,5%
    Faixa 2: até 2.793   → 9%
    Faixa 3: até 4.190   → 12%
    Faixa 4: até teto    → 14%

  IR (mensal, tabela progressiva 2026):
    Até 2.428,80         → isento
    Até 2.826,65         → 7,5% − R$ 182,16
    Até 3.751,05         → 15% − R$ 394,16
    Até 4.664,68         → 22,5% − R$ 675,49
    Acima                → 27,5% − R$ 908,73

BENEFÍCIOS (somar valor mensal equivalente):
  + Vale refeição/alimentação
  + Vale transporte
  + Plano de saúde (valor de mercado)
  + Plano odonto
  + Seguro de vida em grupo
  + FGTS (8% do bruto = futuro)
  + 13º salário (1/12 do anual = bruto/12)
  + Férias + 1/3 (1/12 do anual ≈ bruto × 1,33 / 12)
  + Estabilidade (não monetizável, mas relevante)
```

### 2.2 Calcular Renda Líquida PJ

```
RENDA LÍQUIDA PJ = FATURAMENTO − TRIBUTOS − CUSTOS − RESERVAS

TRIBUTOS DA PJ (Simples Nacional Anexo III, fator R ≥ 28%):
  Até R$ 180k anual    → 6%
  Até R$ 360k anual    → 11,2%
  Até R$ 720k anual    → 13,5%
  Até R$ 1,8M anual    → 16%

  Para faturamento mensal de R$ X:
  Calcular faixa anual proporcional (X × 12)
  Aplicar alíquota correspondente

INSS sobre pró-labore (mínimo legal: 1 SM = R$ 1.518):
  Pró-labore × 11% (até teto)

IR sobre pró-labore: ISENTO até 2.428,80
                     Acima disso, tabela progressiva normal

CUSTOS OPERACIONAIS:
  + Plano de saúde particular (~R$ 600-1.500 dependendo cobertura)
  + Plano odonto (~R$ 50-100)
  + Contador (~R$ 250-450/mês para PJ simples)
  + Ferramentas/softwares profissionais
  + Eventual aluguel de coworking
  + Certificado digital (~R$ 200/ano)

RESERVAS (separar do fluxo, mas técnicamente é "renda" sua):
  + Reserva trabalhista (10% para substituir 13º+férias+FGTS)
  + Previdência privada (mínimo 10% para suprir aposentadoria)
```

---

## 3. Exemplo Concreto Detalhado

### Cenário: CLT R$ 8.000 vs. Proposta PJ R$ 11.000

#### Cálculo CLT R$ 8.000:

```
SALÁRIO LÍQUIDO:
  Bruto:                R$ 8.000,00
  INSS (14% sobre teto, contribuição máxima):
    Cálculo escalonado: ~R$ 951,63
  IR (27,5% − R$ 908,73):
    Base: 8.000 − 951,63 = 7.048,37
    IR: 7.048,37 × 27,5% − 908,73 = 1.029,57
  
  LÍQUIDO:              R$ 6.018,80

BENEFÍCIOS (valores típicos):
  VR/VA:                R$ 800
  VT:                   R$ 200
  Plano de saúde:       R$ 1.000 (valor de mercado individual)
  Plano odonto:         R$ 80
  Seguro vida grupo:    R$ 50
  FGTS (8%):            R$ 640/mês acumulado
  13º (1/12):           R$ 666,67/mês equivalente
  Férias + 1/3 (1/12):  R$ 888,89/mês equivalente
  
  Total benefícios:     R$ 4.325,56

VALOR TOTAL CLT:       R$ 10.344,36/mês equivalente
```

#### Cálculo PJ R$ 11.000:

```
FATURAMENTO BRUTO:     R$ 11.000,00

TRIBUTOS:
  Faturamento anual:   R$ 132.000 (na faixa 6% Anexo III)
  Simples Nacional:    R$ 660 (6% × 11.000)
  
  Pró-labore mínimo:   R$ 1.518
  INSS (11% s/ pró-labore): R$ 167
  IR sobre pró-labore: ISENTO (abaixo de 2.428,80)
  
  Total tributos:      R$ 827

CUSTOS OPERACIONAIS:
  Plano saúde particular: R$ 800 (cobertura equivalente)
  Plano odonto:        R$ 80
  Contador:            R$ 350
  Ferramentas:         R$ 100
  Certificado digital: R$ 17/mês
  
  Total custos:        R$ 1.347

RESERVAS (próprias da PJ):
  Reserva trabalhista (10%):  R$ 1.100
  Previdência privada (10%):  R$ 1.100
  
  Total reservas:      R$ 2.200

RENDA LÍQUIDA EFETIVA: 
  11.000 − 827 − 1.347 − 2.200 = R$ 6.626

BENEFÍCIOS PJ: R$ 0 (sem 13º, férias, FGTS automático)

VALOR TOTAL PJ:        R$ 6.626/mês
```

#### Comparativo:

```
CLT R$ 8.000:    R$ 10.344 valor total
PJ  R$ 11.000:   R$ 6.626 valor total

DIFERENÇA: PJ perde R$ 3.718/mês
  → Para EQUIVALÊNCIA, o PJ precisaria pagar ~R$ 14.000 de faturamento
  → Para VANTAGEM real (sair do trabalho com algo a mais), R$ 16.000+
```

---

## 4. Regra de Equivalência Simplificada

```
PJ_EQUIVALENTE_AO_CLT ≈ CLT × 1,40 a 1,60

  Multiplicador 1,40: cobre tributos PJ + custos básicos
  Multiplicador 1,50: cobre tudo acima + benefícios CLT (saúde, etc.)
  Multiplicador 1,60: vale a pena sair (ganho real)

DECISÃO:
  proposta_pj < clt × 1,40   → 🔴 RECUSAR ou negociar
  proposta_pj entre 1,40 e 1,60 → 🟡 NEUTRO (avaliar fatores não-financeiros)
  proposta_pj > clt × 1,60   → 🟢 VANTAJOSO (transição compensa financeiramente)
```

---

## 5. Fatores Não-Financeiros

### A favor de PJ
```
+ Múltiplos clientes possíveis (diversificação de renda)
+ Flexibilidade de horário e local
+ Possibilidade de crescimento sem teto
+ Otimização tributária (legal)
+ Construção de reputação como marca
+ Decisão sobre projetos a aceitar
```

### A favor de CLT
```
+ Estabilidade (FGTS, aviso prévio, multa rescisória)
+ Recolhimento previdenciário automático
+ Benefícios sem trabalho administrativo
+ Crédito mais acessível (bancos preferem CLT)
+ Menos preocupação fiscal
+ Plano de saúde e odonto como "padrão"
+ Direito a férias remuneradas
```

### Pesos por perfil

| Perfil | Recomendação |
|--------|--------------|
| Família com filhos pequenos + único provedor | Preferir CLT (estabilidade) |
| Profissional sênior com rede de contatos | PJ pode ser vantajoso |
| Início de carreira sem reserva | Preferir CLT até constituir reserva |
| Especialista em alta demanda | PJ frequentemente vantajoso |
| Próximo da aposentadoria | Preferir CLT (continuidade INSS) |

---

## 6. Painel de Decisão

```
╔══════════════════════════════════════════════════╗
║   FRAMEWORK: CLT vs. PJ                          ║
╠══════════════════════════════════════════════════╣
║  CLT atual:                                      ║
║    Salário bruto:     R$ [X]                     ║
║    Salário líquido:   R$ [X]                     ║
║    Benefícios:        R$ [X]                     ║
║    PACOTE TOTAL:      R$ [X]                     ║
╠══════════════════════════════════════════════════╣
║  PROPOSTA PJ:                                    ║
║    Faturamento:       R$ [X]                     ║
║    Tributos:          R$ [X] ([X]%)              ║
║    Custos:            R$ [X]                     ║
║    Reservas:          R$ [X]                     ║
║    LÍQUIDO REAL:      R$ [X]                     ║
╠══════════════════════════════════════════════════╣
║  DIFERENCIAL:         [+/-R$ X] / mês            ║
║  MULTIPLICADOR PJ:    [X.XX]x                    ║
║  DECISÃO:             [RECUSAR/NEUTRO/ACEITAR]   ║
╚══════════════════════════════════════════════════╝
```

---

## 7. Decisão Estruturada

```
PASSO 1 — Calcular PACOTE TOTAL CLT (líquido + benefícios)
PASSO 2 — Calcular LÍQUIDO REAL PJ (após tributos, custos, reservas)
PASSO 3 — Aplicar regra de equivalência (CLT × 1,40 a 1,60)
PASSO 4 — Considerar fatores não-financeiros (perfil, fase de vida)
PASSO 5 — Validar pré-requisitos:
  ✓ Camada de Proteção Financeira ≥ 6 meses (idealmente 12)
  ✓ Sem dívidas com taxa > Selic
  ✓ Disposição para gestão administrativa
PASSO 6 — Decisão consciente
```

---

## 8. Caso Especial — "Pejotização" Forçada

Quando a empresa **exige** a transição (não oferece opção):

```
SE empresa exige transição CLT → PJ sem aumento real:
  → Pode caracterizar relação trabalhista disfarçada (Súmula 444 do TST)
  → Justiça do Trabalho frequentemente reverte
  → Procurar advogado trabalhista para análise

SINAIS DE PEJOTIZAÇÃO IRREGULAR:
  - Cliente único
  - Subordinação (comparece em horário fixo)
  - Pessoalidade (não pode mandar substituto)
  - Onerosidade (recebe sempre, sem dependência de entrega)
  - Não-eventualidade (relação contínua)

→ Quando 4+ desses elementos coexistem: vínculo CLT disfarçado
```

---

## 9. Princípios Operacionais

**Renda líquida real é o que importa.** Faturamento bruto é vaidade.

**Benefícios CLT têm valor monetário.** Plano de saúde, FGTS, 13°, férias somam ~30-40% do bruto. Ignorá-los é erro grave.

**PJ exige autodisciplina financeira.** Sem chefe descontando INSS, sem RH organizando férias — você é o RH e o financeiro de si mesmo.

**Camada de Proteção Financeira é pré-requisito.** Transitar para PJ sem reserva de 6+ meses = risco extremo.

**Multiplicador 1,40 é piso de "não perder".** Para "ganhar de fato", buscar 1,50–1,60+.

**Mordomia inclui prudência (Lc 14:28).** Calcular custos antes de transicionar honra Aquele que confiou recursos a você.

**Decisão tem impacto na família.** Cônjuge e filhos vivem a estabilidade ou instabilidade — envolvê-los na decisão é mordomia familiar.

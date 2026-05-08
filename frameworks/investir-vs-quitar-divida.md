# Framework: Investir vs. Quitar Dívida

> **Tipo:** Framework de Decisão Financeira  
> **Versão:** 1.0.0  
> **Aplicação:** Decisão entre direcionar recurso livre para investimento ou quitação de dívida  
> **Última atualização:** 2026-05-07

Este framework resolve a dúvida mais comum em finanças pessoais: *"Tenho R$ X sobrando — invisto ou quito a dívida?"*. A resposta não é opinião — é matemática + contexto + mordomia.

---

## 1. A Regra Matemática Fundamental

```
SE taxa_da_dívida (líquida de IR) > rentabilidade_do_investimento (líquida de IR):
  AÇÃO = QUITAR DÍVIDA
SENÃO:
  AÇÃO = INVESTIR
```

**Em palavras:** Toda vez que sua dívida custa mais do que seu investimento rende, **quitar é matematicamente superior**. Não há "mas" — é aritmética.

---

## 2. Aplicação Prática com Dados Brasil 2026

**Selic atual (referência):** 14,75% a.a.  
**Selic líquida** após IR de 15% (após 720 dias): **~12,5% a.a.**  
*Para detalhes atualizados, consultar `../docs/REFERENCIAS-BRASIL-2026.md`*

### Tabela de Decisão Instantânea

| Tipo de Dívida | Taxa Anual | Decisão |
|---------------|------------|---------|
| Rotativo do cartão | ~438% | 🔴 **QUITAR JÁ** — antes de qualquer outra coisa |
| Cartão parcelado | ~189% | 🔴 **QUITAR** |
| Cheque especial | ~136% | 🔴 **QUITAR** |
| Crédito pessoal | ~117% | 🔴 **QUITAR** |
| CDC (financiamento) | ~46% | 🔴 **QUITAR** |
| Crédito consignado privado | ~52% | 🔴 **QUITAR** |
| Financiamento veículo | ~36% | 🔴 **QUITAR** |
| Crédito consignado público | ~26% | 🔴 **QUITAR** (taxa > Selic líquida) |
| Financiamento imobiliário | ~11% | 🟡 **DEPENDE** (geralmente investir é melhor) |
| Crédito rural | ~8,5% | 🟡 **DEPENDE** |

**Regra heurística simples 2026:**
> *"Qualquer dívida com taxa > 12% a.a. deve ser quitada antes de investir."*

---

## 3. Engine de Decisão Completo

```
ENTRADAS:
  - taxa_anual_divida (%)
  - prazo_aplicacao_potencial (dias)
  - selic_atual (%) [consultar ../docs/REFERENCIAS-BRASIL-2026.md]
  - tem_camada_protecao_completa? (sim/não)

PASSO 1 — Calcular IR de Investimento por prazo:
  SE prazo ≤ 180 dias:    IR = 22,5%
  SE 181-360 dias:        IR = 20%
  SE 361-720 dias:        IR = 17,5%
  SE > 720 dias:          IR = 15%

PASSO 2 — Calcular Selic líquida:
  selic_liquida = selic_atual × (1 - IR)
  Ex: 14,75% × (1 - 0,15) = 12,54%

PASSO 3 — Comparar:
  SE taxa_anual_divida > selic_liquida:
    → QUITAR DÍVIDA
  SENÃO:
    → INVESTIR

PASSO 4 — Validação de Pré-requisitos:
  SE NÃO tem_camada_protecao_completa:
    SE taxa_divida < selic + 5pp:
      → MIX: 50% Camada de Proteção / 50% dívida
  SE há rotativo ativo:
    → SEMPRE QUITAR primeiro (não há discussão)
```

---

## 4. Casos Práticos

### Caso 1 — Empréstimo pessoal de R$ 10.000 a 9% a.m. (~117% a.a.)

```
Taxa da dívida: 117% a.a.
Selic líquida: 12,5% a.a.
Diferencial: 117% − 12,5% = 104,5pp

DECISÃO: QUITAR (com folga matemática gigante)

Cada R$ 1.000 quitado economiza ~R$ 1.170/ano.
Cada R$ 1.000 investido rende apenas ~R$ 125/ano líquido.
Diferença: R$ 1.045/ano por cada R$ 1.000.
```

### Caso 2 — Financiamento imobiliário a 11% a.a.

```
Taxa da dívida: 11% a.a.
Selic líquida: 12,5% a.a.
Diferencial: 11% − 12,5% = -1,5pp (investimento ligeiramente melhor)

DECISÃO COMPLEXA:
  → Matematicamente, investir é marginalmente melhor
  → Considerar fatores não-financeiros:
     • Liberdade psicológica de quitar (alta para muitos)
     • Possibilidade de Tesouro IPCA+ render acima da inflação
     • Risco de mercado em renda variável
  → Recomendação prática: DIVERSIFICAR
     50% para amortização do imóvel (segurança + liberdade)
     50% para Tesouro IPCA+ longo prazo (potencial de retorno superior)
```

### Caso 3 — Consignado público a 26% a.a.

```
Taxa da dívida: 26% a.a.
Selic líquida: 12,5% a.a.
Diferencial: 26% − 12,5% = 13,5pp

DECISÃO: QUITAR (matematicamente claro)

Mesmo que pareça "barato" socialmente, 26% > Selic líquida significa:
  Cada R$ 1.000 quitado: economia de R$ 260/ano
  Cada R$ 1.000 investido: ~R$ 125/ano líquido
```

### Caso 4 — Rotativo do cartão R$ 2.000 a 36,5% a.m. (~438% a.a.)

```
DECISÃO: QUITAR IMEDIATAMENTE — sem qualquer discussão

Não importa qual investimento — não existe nenhum produto legal e seguro 
que renda 438% a.a. Continuar no rotativo equivale a perder dinheiro 
todo dia.

Inclusive: este é o ÚNICO caso onde você deve interromper aportes 
para Camada de Proteção Financeira para concentrar tudo na quitação.
```

---

## 5. Exceções e Nuances

### Exceção 1 — Sem Camada de Proteção Mínima

```
SE não tem nenhuma reserva (R$ 0 ou < R$ 1.000):
  Mesmo com dívida cara, separar R$ 100-200/mês para Colchão Mínimo
  
RAZÃO:
  Sem reserva, qualquer imprevisto força novo endividamento
  Pequena reserva paralela é "isolamento" do ciclo de dívida
  
DIVISÃO PRÁTICA:
  80% recurso livre → quitação da dívida
  20% recurso livre → Camada 1 até atingir R$ 1.500
```

### Exceção 2 — Dívida Boa que Gera Renda

```
EXEMPLO: Empréstimo para investir em equipamento profissional 
         que aumenta renda em valor superior à parcela.

SE retorno_da_atividade > custo_da_divida:
  Pode-se manter a dívida e investir em paralelo
  Mas: validar que o retorno é REAL, não projeção otimista

EXEMPLOS NÃO QUALIFICAM:
  - "Vou investir e o rendimento paga a dívida" — fantasia
  - "Tenho garantia de 2% a.m." — golpe quase certo
```

### Exceção 3 — Dívida em Renegociação Vantajosa

```
SE banco oferece desconto significativo (>40%) para quitação à vista:
  Pode valer a pena usar parte da Camada de Proteção
  PARA quitar com desconto, depois recompor a Camada
  
CÁLCULO:
  desconto_oferecido > selic × prazo_de_recompor_camada?
  Se sim, vale.
```

### Exceção 4 — Aproximação da Aposentadoria

```
SE faltam < 5 anos para aposentadoria E há financiamento imobiliário:
  Quitar pode trazer "paz mental" mais valiosa que ganho marginal
  Considerar quitação mesmo se matemática for marginal
  
IMPACTO DE LONGO PRAZO < IMPACTO PSICOLÓGICO de entrar na aposentadoria
sem dívidas
```

---

## 6. Painel de Decisão

```
╔══════════════════════════════════════════════════╗
║   FRAMEWORK: INVESTIR vs. QUITAR DÍVIDA          ║
╠══════════════════════════════════════════════════╣
║  TAXA DA DÍVIDA:     [X]% a.a.                   ║
║  SELIC LÍQUIDA:      [X]% a.a.                   ║
║  DIFERENCIAL:        [+/-X]pp                    ║
╠══════════════════════════════════════════════════╣
║  CAMADA PROTEÇÃO:    [COMPLETA / EM CONST.]      ║
║  ROTATIVO ATIVO:     [SIM / NÃO]                 ║
╠══════════════════════════════════════════════════╣
║  DECISÃO:            [QUITAR / INVESTIR / MIX]   ║
║  ALOCAÇÃO:           [%] dívida / [%] investir   ║
╚══════════════════════════════════════════════════╝
```

---

## 7. Princípios Operacionais

**Matemática primeiro, emoção depois.** A decisão começa com a regra: taxa da dívida vs. Selic líquida.

**Rotativo do cartão NÃO é decisão.** É emergência. Quitar imediatamente, sempre.

**Camada de Proteção Mínima vale mais que aritmética perfeita.** Sem reserva, qualquer crise reinicia o ciclo de endividamento.

**Mordomia inclui liberdade.** Provérbios 22:7: *"O rico domina sobre os pobres, e o que toma emprestado é servo do que empresta."* — eliminar dívidas libera capacidade de servir.

**Crédito acessível ≠ crédito barato.** Consignado público a 26% a.a. soa bom socialmente, mas é caro mais que a Selic. A taxa é o que importa.

**O melhor investimento de hoje é a quitação de uma dívida cara.** Garantia, sem IR, sem volatilidade, sem risco — apenas economia direta.

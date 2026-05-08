# Playbook: Recuperação Financeira em 90 Dias

> **Tipo:** Playbook Operacional Premium  
> **Versão:** 1.0.0  
> **Estado-alvo:** SOBREVIVÊNCIA → ORGANIZAÇÃO  
> **Protocolo associado:** Estancar Sangria → Construção de Base  
> **Última atualização:** 2026-05-07

Este playbook é o caminho cirúrgico de saída do Estado SOBREVIVÊNCIA. Não é orientação genérica — é um cronograma semana a semana com marcos verificáveis, com o objetivo de estancar a sangria de juros e estabelecer base mínima de estabilidade em 90 dias.

---

## 1. Quando Ativar

```
SE pelo menos UM destes for verdadeiro:
  - Comprometimento > 100% (déficit mensal)
  - Rotativo do cartão ativo por 2+ meses
  - Cheque especial em uso recorrente
  - Inadimplência com nome no SPC/Serasa
  - Parcelas de dívida > 40% da renda
ENTÃO: ATIVAR Recuperação Financeira em 90 Dias
```

**Pré-requisitos do usuário:**
- Disposição para cortes agressivos (mínimo 20% do estilo de vida) por 90 dias
- Acesso a extratos bancários e faturas dos últimos 3 meses
- Compromisso com Ciclo de Recalibração Financeira semanal

---

## 2. Estado-alvo de Saída (Dia 90)

```
✅ Rotativo zerado
✅ Cheque especial não utilizado por 30 dias
✅ Saldo mensal positivo (mínimo R$ 100/mês)
✅ Colchão Mínimo (R$ 1.000–1.500) constituído
✅ Sistema de Orçamento Doméstico operacional
✅ Ciclo de Recalibração Financeira semanal estabelecido
✅ Plano de quitação para dívidas restantes definido
✅ Dízimo (10%) mantido durante todo o período
```

---

## 3. Cronograma de 13 Semanas

### FASE 1 — Estancar Sangria (Semanas 1–4)

#### Semana 1 — Diagnóstico Cirúrgico

**Objetivo:** Visibilidade total da situação.

| Dia | Ação | Skill |
|-----|------|-------|
| 1 | Diagnóstico financeiro completo | `/pessoal-diagnostico-financeiro` |
| 2 | Listar TODAS as dívidas: saldo, taxa, parcela, data de vencimento | — |
| 3 | Cancelar/bloquear cartões problemáticos (manter 1 só para emergência) | — |
| 4 | Identificar a "caixa preta" — gastos invisíveis dos últimos 60 dias | — |
| 5–7 | Iniciar registro de 100% dos gastos (app: Mobills/Organizze) | — |

**Marco semana 1:** Lista completa de dívidas + diagnóstico de gargalo + app de tracking ativo.

#### Semana 2 — Cortes Imediatos

**Objetivo:** Liberar caixa para atacar a dívida mais cara.

**Cortes obrigatórios (executar em 24–48h):**
- [ ] Cancelar 50% das assinaturas (manter apenas as essenciais)
- [ ] Eliminar delivery por 30 dias (preparar marmitas)
- [ ] Cortar lazer pago (substituir por opções gratuitas)
- [ ] Renegociar plano de telefone/internet (downgrade ou portabilidade)
- [ ] Suspender academia se não usar 3x/semana
- [ ] Suspender oferta voluntária temporariamente (DÍZIMO MANTIDO em 10%)

**Meta de corte:** Liberar mínimo 20% do Bloco Estilo de Vida = caixa para atacar dívida.

**Marco semana 2:** Mínimo R$ 300 de caixa adicional liberado.

#### Semana 3 — Negociação e Renegociação

**Objetivo:** Reduzir o custo das dívidas existentes.

**Ordem de ação:**
1. **Renegociar rotativo:** Procurar o banco e parcelar em parcelas fixas SEM juros compostos
2. **Verificar Lei 14.690/2023:** Se rotativo > 2x valor original, contestar
3. **Acessar Desenrola Brasil 2.0** (desenrola.gov.br) — descontos de até 90% para inadimplentes
4. **Acessar Serasa Limpa Nome** (serasa.com.br/limpa-nome) — descontos médios 50–80%
5. **Avaliar portabilidade:** Trocar dívida cara (rotativo 438% a.a.) por crédito pessoal (117% a.a.) ou consignado (26% a.a.) se elegível

**Marco semana 3:** Pelo menos UMA dívida renegociada com redução de pelo menos 30% do custo total.

#### Semana 4 — Implantação do Bloco Reino e Início do Plano

**Objetivo:** Estabelecer dízimo na primeira linha + iniciar quitação.

| Dia | Ação |
|-----|------|
| 22 | Configurar transferência automática de dízimo (10%) para o dia do salário |
| 23–25 | Concentrar 100% do recurso livre na dívida mais cara (Avalanche) |
| 26 | Iniciar Sistema de Orçamento Doméstico simplificado (4 blocos) |
| 27–28 | Primeiro Ciclo de Recalibração Semanal (15 min) |

**Marco Fase 1 (Dia 30):** 
- Sangria estancada (parou de aumentar a dívida)
- Dízimo automatizado
- Primeiro ataque à dívida cara concluído

---

### FASE 2 — Construção de Base (Semanas 5–8)

#### Semana 5–6 — Sistema de Orçamento Doméstico Completo

**Objetivo:** Implantar o sistema operacional de controle.

**Tarefas:**
- [ ] Implantar Sistema de Orçamento Doméstico completo via `/pessoal-orcamento-domestico`
- [ ] Definir tetos por categoria com base em dados reais (mês 1 de tracking)
- [ ] Configurar regras de Engine de Decisão para estouros
- [ ] Estabelecer Ciclo de Recalibração Financeira semanal (toda sexta, 15 min)

**Marco semana 6:** Orçamento operacional com tetos definidos + 1 mês de tracking real.

#### Semana 7 — Plano Estruturado de Quitação

**Objetivo:** Cronograma claro de saída das dívidas.

**Tarefas:**
- [ ] Executar `/pessoal-plano-dividas-reserva` com dados consolidados
- [ ] Aplicar Engine de Decisão Avalanche vs. Bola de Neve
- [ ] Gerar simulação de quitação (prazo + economia)
- [ ] Definir aporte mensal fixo no Bloco Futuro

**Marco semana 7:** Cronograma de quitação com data estimada de fim por dívida.

#### Semana 8 — Início do Colchão Mínimo

**Objetivo:** Começar a construir Camada de Proteção Financeira.

**Tarefas:**
- [ ] Abrir conta em Tesouro Selic ou CDB com liquidez diária
- [ ] Transferir R$ 100/semana para Camada 1 (Colchão Mínimo)
- [ ] Configurar transferência automática

**Marco Fase 2 (Dia 60):**
- Sistema de Orçamento Doméstico em pleno funcionamento
- Plano de quitação ativo
- Camada de Proteção Financeira iniciada (~R$ 400)
- 30 dias seguidos sem usar rotativo

---

### FASE 3 — Estabilização (Semanas 9–13)

#### Semana 9–10 — Consolidação dos Hábitos

**Objetivo:** Tornar o sistema sustentável.

**Tarefas:**
- [ ] Análise dos primeiros 60 dias no Ciclo de Recalibração
- [ ] Ajuste de tetos de categorias com base em dados reais
- [ ] Identificar 1–3 micro-hábitos para os próximos 30 dias
- [ ] Avaliar retomada de ofertas voluntárias mínimas (R$ 50/mês)

**Marco semana 10:** 60 dias de tracking + ajustes finos do orçamento.

#### Semana 11–12 — Aceleração da Quitação

**Objetivo:** Verificar progresso e acelerar onde possível.

**Tarefas:**
- [ ] Verificar se há renda extra possível (freelance pontual, venda de itens não usados)
- [ ] Direcionar 100% de renda extra para a dívida mais cara
- [ ] Re-simular quitação com possível aceleração

**Marco semana 12:** Aceleração de pelo menos 1 mês no cronograma original (se possível).

#### Semana 13 — Avaliação Final e Próximo Ciclo

**Objetivo:** Consolidar conquista e definir próximo capítulo.

**Tarefas:**
- [ ] Fazer Ciclo de Recalibração Mensal completo via `/pessoal-rotina-financeira-mensal`
- [ ] Comparar Snapshot inicial vs. Snapshot atual
- [ ] Atualizar Mecanismo de Memória Financeira
- [ ] Decidir próximo passo: continuar quitando dívidas ou avançar para Estado ESTABILIZAÇÃO

**Marco final (Dia 90):**
- Estado financeiro: SOBREVIVÊNCIA → ORGANIZAÇÃO ✅
- Risco: CRÍTICO → MODERADO ✅
- Camada de Proteção Financeira: Colchão Mínimo completo ✅
- Sistema operacional consolidado ✅

---

## 4. Painel de Acompanhamento Semanal

```
╔══════════════════════════════════════════════════╗
║   RECUPERAÇÃO 90 DIAS — SEMANA [N] de 13         ║
╠══════════════════════════════════════════════════╣
║  FASE:        [ESTANCAR / BASE / ESTABILIZAÇÃO]  ║
║  SEMANA:      [N]                                ║
║  PROTOCOLO:   [ATIVO]                            ║
║  TRAJETÓRIA:  [POSITIVA ↑ / ESTÁVEL → / RISCO ↓] ║
╠══════════════════════════════════════════════════╣
║  DÍVIDA INICIAL:  R$ [X]                         ║
║  DÍVIDA ATUAL:    R$ [Y]   (-Z% reduzida)        ║
║  RESERVA:         R$ [W]   (+W acumulado)        ║
║  ÚLTIMO ROTATIVO: [N] dias atrás                 ║
╠══════════════════════════════════════════════════╣
║  PRÓXIMO MARCO:   [DESCRIÇÃO]                    ║
╚══════════════════════════════════════════════════╝

PROGRESSO DAS FASES
Fase 1 (Estancar):     [██████████] 100% ✅
Fase 2 (Base):         [██████░░░░] 60%
Fase 3 (Estabilização): [░░░░░░░░░░] 0%

CHECKLIST DA SEMANA
[✔] Ciclo de Recalibração Semanal feito
[✔] Tracking de gastos completo
[ ] Aporte na dívida prioritária
[ ] Aporte na Camada de Proteção Financeira
```

---

## 5. Sinais de Alerta (Disparam Reavaliação)

```
SE em qualquer semana ocorrer:
  - Uso do rotativo após semana 4
  - Saldo mensal voltou a ser negativo
  - Estouro recorrente em 3+ categorias
  - Abandono do tracking por 7+ dias
  - Tentação de pegar novo empréstimo
ENTÃO:
  → PAUSAR cronograma
  → Voltar ao /gestor-financeiro para reavaliação
  → Identificar causa raiz da regressão
  → Possível ajuste de prazo (de 90 para 120–150 dias)
```

---

## 6. Adaptações por Perfil

### Perfil A — Renda CLT estável + dívida concentrada
- Cronograma padrão de 90 dias é factível
- Negociação com banco geralmente bem-sucedida
- Foco: cortes + Avalanche

### Perfil B — Renda variável (autônomo, comissionado)
- Estender para 120 dias
- Reservar 10% adicional para meses de baixa
- Construir Colchão Mínimo MAIOR (R$ 2.500–3.000)

### Perfil C — Múltiplas dívidas pequenas
- Aplicar Bola de Neve nas 4 primeiras semanas (vitórias rápidas para motivação)
- Migrar para Avalanche nas semanas 5–13

### Perfil D — Inadimplente com nome sujo
- Semana 3 é crítica: priorizar Desenrola Brasil 2.0 e Serasa Limpa Nome
- Negociar acordos com desconto significativo
- Foco em remover nome do SPC/Serasa antes de quitar 100%

---

## 7. Princípios Operacionais

**Crise não negocia conforto.** Os primeiros 30 dias exigem cortes que parecem agressivos. Eles não são — são proporcionais à urgência.

**O dízimo é piso, não negociação.** 10% mantido em qualquer situação. Ofertas voluntárias acima de 10% podem ser pausadas — nunca o dízimo.

**Velocidade > perfeição no início.** Semana 1: comece a registrar gastos mesmo que imperfeito. Semana 2: comece a cortar mesmo que doa. Refinamentos vêm depois.

**Marco semanal é não-negociável.** Se a semana terminou sem o marco, a próxima começa com diagnóstico do que travou.

**Recuperação não é privação eterna.** É um capítulo de 90 dias. Após o Dia 90, estilo de vida volta (com tetos sãos) — mas a base está construída.

---

## 8. Skills do Pacote Usadas

| Semana | Skill Principal |
|--------|----------------|
| 1 | `/pessoal-diagnostico-financeiro` |
| 5–6 | `/pessoal-orcamento-domestico` |
| 7 | `/pessoal-plano-dividas-reserva` |
| 8 | `/pessoal-investimento-reino` (calibrar capacidade) |
| 9–13 | `/pessoal-rotina-financeira-mensal` (semanal e mensal) |
| Final | `/gestor-financeiro` (avaliação de saída) |

---

## 9. Próximo Capítulo (Pós Dia 90)

Após concluir este playbook, o usuário deve:

1. Migrar para **Estado ORGANIZAÇÃO** consolidado
2. Continuar quitação das dívidas restantes (sem pressa de 90 dias)
3. Crescer a Camada de Proteção Financeira até 3 meses de essenciais (Camada 2)
4. Retomar ofertas voluntárias gradualmente
5. Em 6–12 meses adicionais: avançar para **Estado ESTABILIZAÇÃO**

**Skill de transição:** `/pessoal-rotina-financeira-mensal` torna-se a skill central no longo prazo.

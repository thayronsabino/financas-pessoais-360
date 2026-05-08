# Glossário Proprietário — Finanças Pessoais 360

> **Versão:** 1.0.0  
> **Última atualização:** 2026-05-07

Este arquivo consolida toda a terminologia proprietária do pacote **Finanças Pessoais 360**. Toda skill que use um termo proprietário deve referenciar a definição padrão aqui.

---

## A — Como Usar Este Glossário

- **Skills devem usar a terminologia padrão** — não criar variações dos termos
- **Ao apresentar um termo pela primeira vez na sessão**, expandi-lo: *"Camada de Proteção Financeira (reserva de emergência)"*
- **Em sessões subsequentes**, usar o termo proprietário diretamente — isso constrói a "cara de sistema proprietário"

---

## B — Termos Proprietários (Ordem Alfabética)

### Bloco Essencial
**Tipo:** Categoria do Sistema de Orçamento Doméstico  
**Definição:** Conjunto de despesas necessárias para a sobrevivência básica do usuário e da família — moradia, alimentação básica, transporte essencial, saúde mínima, educação obrigatória.  
**Range típico:** 45–60% da renda líquida (varia por estado financeiro).  
**Skill principal:** `pessoal-orcamento-domestico`

### Bloco Estilo de Vida
**Tipo:** Categoria do Sistema de Orçamento Doméstico  
**Definição:** Despesas conscientes e flexíveis que refletem escolhas de qualidade de vida — lazer, restaurantes, assinaturas, vestuário, cuidados pessoais, presentes.  
**Range típico:** 15–30% da renda líquida.  
**Skill principal:** `pessoal-orcamento-domestico`

### Bloco Futuro
**Tipo:** Categoria do Sistema de Orçamento Doméstico  
**Definição:** Recursos destinados a Camada de Proteção Financeira, poupança para objetivos, investimentos de longo prazo e quitação acelerada de dívidas. **Inviolável** salvo emergências reais.  
**Range típico:** 15–25% da renda líquida.  
**Skill principal:** `pessoal-orcamento-domestico`

### Bloco Reino
**Tipo:** Categoria do Sistema de Orçamento Doméstico  
**Definição:** Contribuições dedicadas ao Reino — dízimo (10% inviolável), ofertas regulares, projetos ministeriais. **Sai antes de qualquer outra categoria** (princípio das primícias).  
**Range típico:** 10–15% (ou mais conforme nível Stewardship).  
**Skill principal:** `pessoal-investimento-reino`

### Camada de Proteção Financeira
**Tipo:** Conceito proprietário (substitui "reserva de emergência")  
**Definição:** Recurso líquido reservado para absorver choques financeiros sem comprometer o orçamento corrente. Constituída em três camadas progressivas:
- **Camada 1 — Colchão Mínimo:** R$ 1.000–1.500 (1 mês de essenciais)
- **Camada 2 — Proteção Básica:** 3 meses de gastos essenciais
- **Camada 3 — Proteção Completa:** 6–12 meses conforme perfil profissional

**Onde guardar:** Tesouro Selic, CDB liquidez diária > 100% CDI, LCI/LCA pós-carência.  
**Skills relacionadas:** `pessoal-plano-dividas-reserva`, `pessoal-orcamento-domestico`

### Camadas Cognitivas
**Tipo:** Framework de raciocínio do sistema  
**Definição:** As 5 camadas de pensamento que toda skill executa em sequência antes de gerar output:
1. **Diagnóstico** — "O que está acontecendo?"
2. **Interpretação** — "Por que isso está acontecendo?"
3. **Estratégia** — "O que precisa mudar?"
4. **Execução** — "Qual é o próximo passo?"
5. **Sustentação** — "Como manter isso vivo?"

**Aplicação:** Toda skill deve declarar e seguir as 5 camadas. Saltar camadas (especialmente da 1 para a 4) é o que cria respostas superficiais.

### Ciclo de Recalibração Financeira
**Tipo:** Conceito proprietário (substitui "revisão mensal")  
**Definição:** Rotina mensal estruturada em 5 fases: Fechamento → Análise Comparativa → Diagnóstico de Desvios → Recalibração de Metas → Planejamento do Próximo Ciclo.  
**Frequência:** Mensal obrigatória + revisão semanal de 15 minutos.  
**Skill principal:** `pessoal-rotina-financeira-mensal`

### Dízimo (Princípio Inviolável)
**Tipo:** Princípio absoluto do sistema  
**Definição:** 10% da renda destinados ao Reino. **Não negociável** em nenhuma situação financeira — seja crise, dívida ou inadimplência.  
**Regra absoluta:** Em aperto, ajustam-se as **ofertas voluntárias acima de 10%** — nunca o dízimo.  
**Base bíblica:** Malaquias 3:10  
**Skills:** Aplica-se a todas, especialmente `pessoal-investimento-reino`

### Estados Financeiros (5 Estados)
**Tipo:** Engine central de classificação do usuário  
**Definição:** Classificação operacional do estado financeiro real do usuário, que determina o protocolo ativo:

1. **SOBREVIVÊNCIA** — Déficit mensal, rotativo ativo, inadimplência → Protocolo Estancar Sangria
2. **ORGANIZAÇÃO** — Orçamento funcional, dívidas reduzindo, sem reserva → Protocolo Construção de Base
3. **ESTABILIZAÇÃO** — Reserva ativa (3+ meses), consistência mensal, dívidas controladas → Proteção Ativa
4. **EXPANSÃO** — Investimentos ativos, patrimônio crescendo, generosidade aumentando → Protocolo Multiplicação Responsável
5. **LEGADO** — Patrimônio sustentável, planejamento sucessório, impacto real → Legado Vivo

**Regra de ouro:** Um usuário em SOBREVIVÊNCIA não recebe orientação de EXPANSÃO. O sistema respeita o estado real.

### Financial State Engine
**Tipo:** Engine de classificação do sistema  
**Definição:** Motor que classifica automaticamente o usuário em um dos 5 Estados Financeiros com base nos indicadores fornecidos. Determina o protocolo ativo e o modo de operação.  
**Onde está:** Implementado em todas as skills (consultivo) e centralizado em `gestor-financeiro`.

### Gargalo Primário
**Tipo:** Conceito de diagnóstico  
**Definição:** Tipo de problema financeiro principal identificado pelo Sistema de Mapeamento de Fluxo Financeiro:
- **Juros** — uso recorrente de rotativo/cheque especial
- **Estrutural** — gastos essenciais > 70% da renda
- **Invisível** — saldo negativo sem justificativa nos gastos visíveis
- **Estilo de vida** — essenciais controlados mas não sobra nada

**Skill principal:** `pessoal-diagnostico-financeiro`

### Mecanismo de Memória Financeira
**Tipo:** Sistema de persistência entre sessões  
**Definição:** Estrutura padronizada (Snapshot) que registra estado financeiro, indicadores, desvios e ações ao final de cada sessão, permitindo continuidade real entre interações.  
**Especificação técnica:** Ver `MEMORY-SYSTEM.md`  
**Skills que escrevem:** `pessoal-diagnostico-financeiro`, `pessoal-rotina-financeira-mensal`

### Método Wesleyano
**Tipo:** Princípio de mordomia aplicada  
**Definição:** Princípio de John Wesley: *"Ganhe tudo o que puder, economize tudo o que puder, dê tudo o que puder."* Renda crescente deve gerar **generosidade crescente** — não apenas estilo de vida crescente.  
**Aplicação prática:** A cada aumento de renda ou estado financeiro mais avançado, aumentar proporcionalmente as contribuições ao Reino.  
**Skill principal:** `pessoal-investimento-reino`

### Painel Financeiro Operacional
**Tipo:** Formato de output proprietário  
**Definição:** Dashboard ASCII estruturado entregue ao final de toda análise consultiva, contendo: Estado Financeiro, Risco, Protocolo Ativo, Trajetória, Prioridade, Próximo Marco e Mapa Operacional com progress bars.  
**Obrigatório em:** Todas as skills.

### Plano de Generosidade Sustentável
**Tipo:** Conceito proprietário  
**Definição:** Estrutura completa de contribuições do Reino — dízimo, ofertas regulares, projetos especiais — calibrada por estado financeiro através do Stewardship Engine.  
**Skill principal:** `pessoal-investimento-reino`

### Primícias (Princípio das)
**Tipo:** Princípio bíblico aplicado  
**Definição:** O dízimo (10%) sai PRIMEIRO da renda, antes de qualquer outra categoria. A pergunta orientadora é "**o que sobra depois do dízimo?**" — nunca "sobrou para o dízimo?"  
**Base bíblica:** Provérbios 3:9–10

### Protocolo Construção de Base
**Tipo:** Protocolo Operacional  
**Ativação:** Sangria estancada OU Estado ORGANIZAÇÃO  
**Objetivo:** Criar estabilidade, colchão e previsibilidade sustentável  
**Duração:** 3–12 meses  
**Critério de saída:** Reserva básica de 3 meses + dívidas caras eliminadas

### Protocolo Estancar Sangria Financeira
**Tipo:** Protocolo Operacional  
**Ativação:** Rotativo ativo OU déficit > 10% OU cheque especial em uso  
**Objetivo:** Interromper crescimento exponencial de juros  
**Duração:** 30–90 dias  
**Critério de saída:** Rotativo zerado + saldo mensal positivo por 60 dias consecutivos

### Protocolo Generosidade Sustentável
**Tipo:** Protocolo Operacional  
**Ativação:** Estado ESTABILIZAÇÃO ou superior + saldo positivo consistente  
**Objetivo:** Crescer contribuições de forma planejada (Método Wesleyano)  
**Regra:** +0,5% de ofertas a cada mês com saldo positivo, até meta de longo prazo (15–20% da renda).  
**Skill principal:** `pessoal-investimento-reino`

### Protocolo Multiplicação Responsável
**Tipo:** Protocolo Operacional  
**Ativação:** Reserva completa + orçamento consistente + dívidas controladas  
**Objetivo:** Expansão patrimonial alinhada ao Reino e à família  
**Duração:** Indefinida — estado de maturidade financeira

### Risk Engine
**Tipo:** Engine de avaliação  
**Definição:** Motor que classifica o risco financeiro do usuário em CRÍTICO, ALTO, MODERADO ou BAIXO com base em comprometimento, reserva, parcelas e padrões de consumo.  
**Skill central:** `gestor-financeiro` (replicado nas demais).

### Sistema de Mapeamento de Fluxo Financeiro
**Tipo:** Conceito proprietário (substitui "diagnóstico financeiro")  
**Definição:** Processo estruturado de mapeamento de entradas, saídas, classificação de gastos (essenciais, estilo de vida, invisíveis) e cálculo de indicadores-chave para identificar o Gargalo Primário.  
**Skill principal:** `pessoal-diagnostico-financeiro`

### Sistema de Orçamento Doméstico
**Tipo:** Conceito proprietário  
**Definição:** Estrutura operacional de controle de fluxo financeiro com 4 blocos (Reino, Essencial, Estilo de Vida, Futuro), tetos por categoria e Ciclo de Recalibração Financeira semanal.  
**Skill principal:** `pessoal-orcamento-domestico`

### Snapshot Financeiro
**Tipo:** Registro do Mecanismo de Memória  
**Definição:** Registro estruturado em formato JSON ou tabela contendo todos os indicadores relevantes do usuário em um momento específico. Permite comparação histórica.  
**Especificação:** Ver `MEMORY-SYSTEM.md`

### Stewardship Engine
**Tipo:** Engine de capacidade de mordomia  
**Definição:** Motor que determina o nível sustentável de contribuições por estado financeiro:
- **MÍNIMO** (Sobrevivência): dízimo 10% inviolável, ofertas pausadas
- **BASE** (Organização): dízimo + 2–5% ofertas
- **CRESCIMENTO** (Estabilização): dízimo + 3–7% ofertas crescentes
- **MULTIPLICAÇÃO** (Expansão): dízimo + 5–10%+ ofertas planejadas
- **IMPACTO** (Legado): contribuições estruturais + planejamento sucessório

**Skill principal:** `pessoal-investimento-reino`

---

## C — Termos Comuns (Não Proprietários, mas Padronizados)

### Comprometimento (taxa de)
Total de saídas mensais ÷ renda líquida × 100. Acima de 100% = déficit ativo.

### Endividamento (taxa de)
Parcelas de dívidas ÷ renda líquida × 100. Acima de 30% = risco alto.

### Margem de Segurança
Renda líquida − Gastos essenciais. Indica o "espaço" para Bloco Estilo de Vida e Bloco Futuro.

### Capacidade de Poupança
Saldo mensal positivo que pode ser direcionado para a Camada de Proteção Financeira ou investimentos.

---

## D — Princípios Inegociáveis

Estes são os "axiomas" do sistema. Skills NUNCA podem violá-los:

1. **Dízimo é piso (10%) — nunca alvo.** Não é progressivo. Não tem exceção.
2. **Camada de Proteção Financeira antes de investimentos de longo prazo** — exceto se já existir.
3. **Quitar dívida com taxa > Selic líquida antes de investir.**
4. **O sistema decide; não lista opções.** Apresentar o caminho correto com autoridade consultiva.
5. **Estado real, não estado desejado.** Não dar orientação de Expansão para usuário em Sobrevivência.
6. **Mordomia inclui cuidar da casa (1 Tm 5:8)** — contribuir sem sustentabilidade não é generosidade fiel.

---

## E — Manutenção do Glossário

**Quando atualizar este arquivo:**
- Ao introduzir novo termo proprietário em qualquer skill
- Ao alterar a definição de um termo existente
- Ao mudar parâmetros de Engines (Risk, Stewardship, etc.)

**Como atualizar:**
1. Editar a entrada relevante (ou adicionar nova em ordem alfabética)
2. Atualizar a "Última atualização" no topo
3. Atualizar referências cruzadas nas skills se a mudança for material

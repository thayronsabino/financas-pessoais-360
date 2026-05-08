# Playbook: Idoso com Aposentadoria Insuficiente

> **Tipo:** Playbook Operacional Premium  
> **Versão:** 1.0.0  
> **Estado-alvo:** Idoso vivendo com aperto → Idoso com dignidade financeira  
> **Duração:** 3-6 meses para estabilização inicial  
> **Última atualização:** 2026-05-08

Mais de **70% dos aposentados brasileiros recebem até 1 salário mínimo**. Para muitos, a aposentadoria não cobre nem necessidades básicas. Este playbook estrutura o cuidado de quem chegou à terceira idade sem reserva suficiente, frequentemente sustentando filhos/netos, com endividamento por consignado e crescente vulnerabilidade.

> **Princípio orientador:** Dignidade na velhice é mordomia coletiva. Cuidar dos idosos é dever bíblico explícito (Êxodo 20:12, 1 Timóteo 5:8) e responsabilidade da família e da igreja antes de ser do Estado.

---

## 1. Quando Ativar

```
SE perfil do usuário corresponde a:
  - 60+ anos
  - Aposentadoria como principal/única fonte de renda
  - Renda mensal insuficiente para gastos essenciais OU
  - Endividamento por consignado já comprometendo aposentadoria OU
  - Sustentando filhos/netos com a aposentadoria OU
  - Sem reserva acumulada e sem patrimônio
ENTÃO: ATIVAR Idoso com Aposentadoria Insuficiente
```

**Esse playbook também serve para a FAMÍLIA do idoso** — frequentemente é o filho/neto que busca ajuda.

---

## 2. Estado-alvo de Saída

```
✅ Custo de vida do idoso reduzido ao mínimo digno
✅ Crédito consignado sob controle (renegociado se necessário)
✅ Apoio público/familiar mapeado e ativado
✅ Camada de Proteção Mínima possível (R$ 500-1.000) constituída
✅ Filhos/netos não dependentes da aposentadoria (se houver dependência)
✅ Plano de sucessão / cuidados futuros conversado em família
✅ Dignidade preservada — sem vergonha de buscar apoio que tem direito
```

---

## 3. Diagnóstico Específico do Idoso

### Perguntas de abertura (com cuidado pastoral)

```
"Antes de olharmos números, quero te perguntar: como você está se sentindo? 
A vida ficou mais difícil financeiramente? Você tem com quem conversar 
sobre isso na família?"

"Há quanto tempo a aposentadoria começou a não dar?"

"Você ajuda alguém com a sua aposentadoria? Filho, neto, neta?"

"Você está usando o cartão consignado ou empréstimo no INSS?"
```

### Mapa da renda real

```
ENTRADAS:
  + Aposentadoria (INSS) — R$ ?
  + Pensão por morte (se houver) — R$ ?
  + BPC/LOAS (se ainda não recebe e tem direito) — R$ ?
  + Renda extra (aluguel, trabalho complementar, ajuda família) — R$ ?

SAÍDAS:
  - Moradia (aluguel, condomínio, IPTU)
  - Alimentação
  - Saúde (medicamentos, plano, exames)
  - Transporte
  - Contas básicas (luz, água, gás, internet)
  - Parcelas de consignado / cartão
  - Sustento de filhos/netos
  - Lazer / hobbies (sim, mesmo idoso precisa)
```

### Risco específico — Crédito Consignado

O consignado parece "barato" mas é armadilha clássica para idosos:
```
ARMADILHAS COMUNS:
  - Margem consignável até 35% + 5% cartão consignado
  - Bancos oferecem refinanciamento sucessivo (rolagem)
  - Aposentadoria líquida cai 40% — vida fica impossível
  - Idosos vulneráveis a venda casada e abusos
  
LEGISLAÇÃO PROTETIVA (consultar):
  - Lei 14.181/2021 — Proteção do superendividamento
  - Limite legal de 35% da aposentadoria + 5% cartão
  - Direito a renegociação humanizada
```

---

## 4. Cronograma de Estabilização

### MÊS 1 — Diagnóstico e Apoio Imediato

#### Semana 1 — Mapeamento Completo

- [ ] Listar TODAS as fontes de renda
- [ ] Listar TODAS as despesas mensais
- [ ] Listar TODAS as dívidas (consignado, cartão, fiado em mercado)
- [ ] Identificar quem mais depende dessa aposentadoria

#### Semana 2 — Verificar Direitos Não Acessados

```
BENEFÍCIOS QUE MUITOS IDOSOS NÃO SABEM QUE TÊM DIREITO:

📋 BPC/LOAS (Benefício de Prestação Continuada):
  - Para 65+ anos com renda familiar per capita < 1/4 do salário mínimo
  - Não exige contribuição prévia ao INSS
  - Não acumula com aposentadoria, mas pode ser opção para quem nunca contribuiu
  - Como solicitar: Meu INSS (app/site) ou agência

🚌 GRATUIDADES E DESCONTOS:
  - Transporte público gratuito (60+ na maioria das cidades)
  - Carteira do Idoso (CRAS) — viagens interestaduais gratuitas/desconto
  - Meia-entrada em cinema, teatro, eventos (Lei do Idoso)
  - 50% de desconto em remédios (Farmácia Popular)
  - IPTU com desconto ou isenção (varia por município — verificar)
  - Isenção IR para portadores de doenças graves (cardiopatia, câncer, etc.)

🏥 SAÚDE:
  - SUS atendimento prioritário 60+
  - Medicamentos do programa Farmácia Popular (gratuitos ou descontos)
  - Atenção: doenças graves dão isenção de IR e PIX-saúde

🏠 PROGRAMAS HABITACIONAIS:
  - Verificar Minha Casa Minha Vida para idoso
  - Programas estaduais (Casa Paulista, etc.)
  - Aluguel social (em alguns municípios)
```

#### Semana 3 — Atacar o Consignado

```
SE há consignado consumindo > 30% da aposentadoria:

PASSO 1 — Reunir todos os contratos
  Solicitar histórico no Meu INSS

PASSO 2 — Verificar legalidade
  Margem total não pode passar de 35% + 5% cartão = 40%
  Se passou: ILEGAL, contestar com banco e/ou Procon

PASSO 3 — Procurar renegociação humanizada
  - Banco diretamente
  - Procon
  - Defensoria Pública (gratuito, ideal)
  - Ministério Público (em casos de abuso)

PASSO 4 — Avaliar portabilidade
  Trocar consignado caro por consignado mais barato em outro banco
  (a margem permanece, mas a parcela diminui)

NUNCA aceitar:
  ❌ Refinanciamento com prazo maior só para reduzir parcela
  ❌ Novo empréstimo para "pagar dívida atual"
  ❌ Cartão consignado oferecido como solução
```

#### Semana 4 — Conversa Familiar

Frequentemente, parte da solução está em **conversar com a família**:

```
TEMAS A CONVERSAR (preparar conversa estruturada):

1. SE FILHO/NETO MORA E DEPENDE FINANCEIRAMENTE:
   Pode contribuir com algo — mesmo simbólico?
   Mesa familiar dividida (Bloco Essencial proporcional)?
   Mudança no padrão da casa?

2. SE IDOSO MORA SOZINHO E TEM CASA:
   Faria sentido alugar quarto / morar com filho?
   Vender casa atual e comprar menor (gerando capital)?
   Reverse mortgage (raro no Brasil, mas existe)?

3. SE FILHOS PODEM CONTRIBUIR:
   Mesada simbólica para os pais (R$ 100-300/mês cada um)
   Substituir presentes esporádicos por contribuição regular
   Cobrir uma despesa específica (plano de saúde, remédios)

4. SE HÁ NETO COM RENDA:
   Mesma lógica — pais que ajudaram criar agora precisam ser ajudados

PRINCÍPIO BÍBLICO (1 Timóteo 5:4-8):
  "Mas, se alguma viúva tiver filhos ou netos, aprendam estes 
   primeiro a exercer piedade para com a sua própria família, e 
   a recompensar seus pais; porque isto é bom e agradável diante 
   de Deus."
```

---

### MÊS 2-3 — Construção de Base Possível

#### Reorganização de Custos Essenciais

```
MORADIA:
  - Avaliar mudança para imóvel menor / mais barato
  - Considerar mudar para cidade do interior (custo menor)
  - Morar com filho (aceito como mordomia, não como derrota)

ALIMENTAÇÃO:
  - Programas locais: SESC Mesa Brasil, bancos de alimentos
  - Igreja local frequentemente tem programa de assistência
  - Compras coletivas (família junta)

SAÚDE:
  - Migrar para SUS para tudo possível
  - Plano de saúde só se cobre algo específico que SUS demora
  - Farmácia Popular para remédios crônicos
  - Programa do governo para doenças específicas

TRANSPORTE:
  - Cartão idoso para transporte público (gratuito)
  - Vender carro se não é essencial (libera capital + reduz custo)

LAZER:
  - Atividades gratuitas: parques, igreja, grupos de terceira idade
  - SESC tem mensalidade reduzida e oferece muito
  - Bibliotecas, centros culturais
```

#### Camada de Proteção Mínima (Adaptada para Idoso)

```
PARA IDOSOS, A LÓGICA MUDA:
  - Reserva tradicional (6 meses) é frequentemente impossível
  - Foco em "Reserva de Emergência Imediata": R$ 500 - R$ 1.500
  - Para emergências de curto prazo (medicamentos, conserto, etc.)

ONDE GUARDAR:
  - Conta poupança (sim, neste caso a poupança serve — pequeno valor)
  - Tesouro Selic se há valor maior (>R$ 1.000)
  - NÃO usar consignado como "reserva"

COMO CONSTRUIR:
  - R$ 50/mês durante 1 ano = R$ 600
  - Migrar de Bloco Estilo de Vida (mesmo pequeno)
  - Ofertas/presentes recebidos da família ➝ direto para reserva
```

---

### MÊS 4-6 — Consolidação e Sucessão

#### Conversa de Sucessão

Tema delicado mas necessário:

```
PERGUNTAS FAMILIARES (idoso + filhos):

1. CUIDADOS FUTUROS:
   - Quem cuida quando precisar?
   - Casa de repouso (custo médio: R$ 4.000-12.000/mês)
   - Cuidador em casa
   - Morar com filho (qual?)

2. PATRIMÔNIO:
   - O que existe? (casa, conta, FGTS sacável, INSS)
   - Documentação organizada?
   - Há testamento? Faz sentido fazer?

3. DOCUMENTOS LEGAIS:
   - Procuração para emergências
   - Diretrizes antecipadas de vontade (saúde)
   - Inventário/herança facilitada

4. ASPECTOS ESPIRITUAIS:
   - Funeral (já planejado? coberto?)
   - Memorial / despedida
   - Mensagens / cartas para netos
```

#### Apoio Espiritual e Comunitário

```
IGREJA LOCAL:
  - Pastor saber da situação (não para "vergonha", mas para apoio)
  - Frequentemente igrejas têm:
    * Diaconia (apoio material em emergências)
    * Visitação a idosos
    * Grupos de oração específicos
    * Programa de cestas básicas

GRUPOS DE TERCEIRA IDADE:
  - SESC, Centros de Convivência
  - Combatem isolamento (que afeta saúde mental e física)
  - Atividades gratuitas

DIGNIDADE NÃO É ORGULHO:
  Buscar apoio quando se precisa é sabedoria, não fraqueza.
  Aceitar ajuda da família é honra para quem dá e quem recebe.
  Atos 6 — a igreja primitiva organizou apoio sistemático às viúvas.
```

---

## 5. Painel do Idoso

```
╔══════════════════════════════════════════════════╗
║   PLANO DE DIGNIDADE NA APOSENTADORIA            ║
╠══════════════════════════════════════════════════╣
║  RENDA MENSAL:     R$ [X]                        ║
║  GASTOS ESSENCIAIS: R$ [X]                       ║
║  COMPROMETIMENTO:  [X]%                          ║
║  CONSIGNADO ATIVO:  R$ [X]/mês                  ║
╠══════════════════════════════════════════════════╣
║  BENEFÍCIOS NÃO ACESSADOS:                       ║
║  [✔] Carteira do Idoso                           ║
║  [✔] Farmácia Popular                            ║
║  [ ] BPC/LOAS (verificar elegibilidade)          ║
║  [ ] Isenção IPTU                                ║
║  [ ] Isenção IR (se aplicável)                   ║
╠══════════════════════════════════════════════════╣
║  APOIO FAMILIAR:    [ATIVADO / EM CONVERSA]      ║
║  APOIO IGREJA:      [ATIVADO / NÃO]              ║
║  RESERVA MÍNIMA:    R$ [X] / R$ 1.000            ║
╠══════════════════════════════════════════════════╣
║  PRÓXIMO PASSO: [AÇÃO ESPECÍFICA]                ║
╚══════════════════════════════════════════════════╝
```

---

## 6. Princípios Específicos para Idosos

**Dignidade > orgulho.** Buscar apoio público que se tem direito, aceitar ajuda da família, frequentar igreja com pedido oração — não é "dar trabalho", é mordomia da própria vida.

**Cuidar dos pais é mandamento, não favor.** Êxodo 20:12 — "Honra teu pai e tua mãe". 1 Timóteo 5:8 vai mais longe: quem não cuida dos seus negou a fé. Filhos que se omitem precisam ser confrontados (com amor).

**Velhice não é fim — é estação.** Idosos têm muito a oferecer: sabedoria, oração, presença com netos, mentoria, hospitalidade. Renda menor não significa contribuição menor à família/comunidade.

**Consignado é veneno disfarçado de remédio.** Para idoso, principalmente. Margem alta + rolagem sucessiva + parcelas longas = morrer devendo.

**Saúde mental do idoso importa.** Solidão, depressão e ansiedade são comuns. Convivência social é parte do plano financeiro (afeta saúde, evita gastos médicos).

**Patrimônio é instrumento, não meta.** Casa pode ser vendida. Carro pode ser trocado. Recursos servem ao idoso — não o contrário.

---

## 7. Quando Encaminhar

```
SE detectar:
  - Sinais de abuso financeiro contra o idoso (família ou bancos)
    → Disque 100 (Direitos Humanos) ou Delegacia do Idoso
  
  - Depressão ou ansiedade aguda
    → CAPS, psicólogo, ou ../docs/PROTOCOLO-CRISE-ESPIRITUAL.md
  
  - Negligência por parte de filhos
    → Conversa pastoral com família
    → Em casos extremos: Ministério Público (Estatuto do Idoso)
  
  - Doença grave sem cobertura
    → Defensoria Pública pode garantir tratamento via SUS
    → Algumas doenças dão direito a saque do FGTS, PIS, isenção IR
```

---

## 8. Skills do Pacote Usadas

| Etapa | Skill |
|-------|-------|
| Diagnóstico | `/pessoal-diagnostico-financeiro` (adaptado) |
| Reorganização | `/pessoal-orcamento-domestico` (versão simplificada) |
| Renegociação | `/pessoal-plano-dividas-reserva` (foco em consignado) |
| Acompanhamento | `/pessoal-rotina-financeira-mensal` (adaptado para baixa frequência) |
| Apoio espiritual | Consultar `../docs/PRINCIPIOS-BIBLICOS-EXPANDIDOS.md` |

---

## 9. Mensagem ao Idoso

```
"A vida ficou mais difícil do que você esperava ter aos [idade] anos. 
Isso não é culpa sua — é resultado de muitas coisas (sistema 
previdenciário, custo de vida, decisões de quem governou).

Sua aposentadoria é um direito que você construiu trabalhando. 
Buscar tudo o que tem direito não é 'esmolar' — é receber o que 
foi pago durante décadas.

Aceitar ajuda da família e da igreja não é fraqueza. É comunidade 
funcionando como Deus desenhou. Você cuidou dos seus quando podia. 
Agora é tempo de ser cuidado também.

Os anos da velhice podem ser anos de paz, oração, presença com 
quem amamos, sabedoria compartilhada. Vamos cuidar da parte 
financeira para que você tenha mente livre para esses dons."
```

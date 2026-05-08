# Mecanismo de Memória Financeira — Especificação Técnica

> **Versão:** 1.0.0  
> **Última atualização:** 2026-05-07  
> **Compatibilidade:** Todas as skills do pacote Finanças Pessoais 360

Este arquivo define a **persistência de estado financeiro entre sessões**. Sem ele, o Mecanismo de Memória Financeira é apenas um modelo conceitual — com ele, vira um sistema vivo capaz de referenciar histórico real do usuário.

---

## 1. Localização Padrão

```
~/.financas-360/
├── memory/
│   ├── usuario-default.json      # Snapshots cronológicos do usuário
│   └── usuario-{id}.json         # Suporte futuro a múltiplos usuários
├── trajetoria/
│   └── usuario-default.md        # Resumo legível da evolução
└── referencias/
    └── brasil-2026-cache.json    # Cache local com TTL de 30 dias
```

**Convenção:** Em ambientes onde `~/.financas-360/` não puder ser criado (ex: Claude.ai sem filesystem), o sistema usa **memória da sessão** seguindo o mesmo schema.

---

## 2. Schema do Snapshot Financeiro

Toda skill que escreve memória deve gerar um snapshot conforme este schema:

```json
{
  "schema_version": "1.0.0",
  "snapshot_id": "snap-2026-05-07-001",
  "data": "2026-05-07",
  "skill_origem": "pessoal-diagnostico-financeiro",
  "usuario_ref": "default",

  "estado_financeiro": "ORGANIZACAO",
  "risco": "MODERADO",
  "protocolo_ativo": "CONSTRUCAO_DE_BASE",
  "trajetoria": "POSITIVA",

  "indicadores": {
    "renda_liquida": 6500.00,
    "saldo_mensal": 850.00,
    "comprometimento_pct": 87,
    "endividamento_pct": 18,
    "margem_seguranca": 2400.00,
    "taxa_poupanca_pct": 13,
    "reserva_atual": 4500.00,
    "reserva_meta": 19500.00,
    "reserva_progresso_pct": 23,
    "divida_total": 8000.00,
    "divida_caras_total": 0
  },

  "blocos_orcamento": {
    "reino": { "valor": 650, "pct": 10, "status": "ok" },
    "essencial": { "valor": 3200, "pct": 49, "status": "ok" },
    "estilo_vida": { "valor": 1300, "pct": 20, "status": "ok" },
    "futuro": { "valor": 1100, "pct": 17, "status": "ok" },
    "flexivel": { "valor": 250, "pct": 4, "status": "ok" }
  },

  "gargalo_primario": null,
  "gargalo_secundario": null,

  "contribuicoes_reino": {
    "dizimo_valor": 650,
    "dizimo_pct": 10,
    "ofertas_valor": 0,
    "ofertas_pct": 0,
    "nivel_stewardship": "BASE"
  },

  "desvios_destacados": [
    {
      "categoria": "alimentacao",
      "desvio_pct": 15,
      "padrao": "recorrente_3_meses",
      "causa_raiz": "delivery_excessivo",
      "acao_corretiva": "limite_1x_semana"
    }
  ],

  "acao_prioritaria": {
    "descricao": "Atingir 3 meses de Camada de Proteção Financeira",
    "meta": "R$ 9.750",
    "prazo_meses": 6
  },

  "skill_recomendada_proxima": "pessoal-rotina-financeira-mensal",

  "marcos_alcancados": [
    "Rotativo zerado em 2026-02",
    "Colchão Mínimo (R$ 1.500) em 2026-03"
  ],

  "marcos_pendentes": [
    "Reserva de 3 meses",
    "Quitação do empréstimo pessoal"
  ],

  "metadata": {
    "session_id": "session-uuid-aqui",
    "duracao_sessao_min": 25,
    "modo": "CONSULTORIA"
  }
}
```

---

## 3. Schema do Arquivo de Trajetória

`trajetoria/usuario-default.md` — formato legível humano:

```markdown
# Trajetória Financeira — Usuário Default

## Estado Atual
- **Estado:** ORGANIZAÇÃO (desde 2026-03)
- **Risco:** MODERADO
- **Protocolo:** Construção de Base
- **Trajetória:** Positiva ↑

## Linha do Tempo

### 2026-05-07 — Diagnóstico de Maio
- Reserva: R$ 4.500 (23% da meta)
- Dívida: R$ 8.000
- Foco: Camada de Proteção Financeira

### 2026-04-03 — Ciclo de Recalibração
- Alimentação estourou 22% (corrigida no plano)
- Dívida do cartão caiu R$ 450
- Reserva cresceu R$ 800

### 2026-03-15 — Colchão Mínimo Atingido
- Marco: R$ 1.500 acumulados ✅

### 2026-02-08 — Rotativo Zerado
- Marco: Saída do Estado SOBREVIVÊNCIA ✅

### 2026-01-12 — Diagnóstico Inicial
- Estado: SOBREVIVÊNCIA
- Risco: CRÍTICO
- Protocolo: Estancar Sangria
```

---

## 4. Contratos de Operação

### 4.1 LEITURA (todas as skills)

Ao iniciar uma sessão, a skill DEVE:

```
1. Tentar ler ~/.financas-360/memory/usuario-default.json
2. Se existir, carregar o último snapshot
3. Extrair: estado_financeiro, risco, protocolo_ativo, indicadores
4. Comparar com dados atuais da sessão (se já coletados)
5. Apresentar referência ao usuário:
   "Na última sessão (2026-04-03), você estava em ORGANIZAÇÃO com
    reserva de R$ 4.500. Hoje vamos atualizar esse panorama."
```

**Se o arquivo não existir** (primeira sessão ou ambiente sem filesystem):
- Operar normalmente sem referência histórica
- Ao final da sessão, criar o primeiro snapshot

### 4.2 ESCRITA (skills que executam diagnóstico ou ciclo)

Skills que DEVEM escrever snapshots:
- `pessoal-diagnostico-financeiro` — sempre que executar diagnóstico completo
- `pessoal-rotina-financeira-mensal` — a cada Ciclo de Recalibração
- `pessoal-orcamento-domestico` — ao concluir implantação ou revisão

Skills que NÃO escrevem (são consumidoras de memória):
- `gestor-financeiro` (lê para tomar decisões de roteamento)
- `pessoal-plano-dividas-reserva` (lê para calibrar plano)
- `pessoal-estrategia-investimentos` (lê para validar pré-requisitos)
- `pessoal-investimento-reino` (lê para calibrar Stewardship Engine)

### 4.3 APPEND (regra de ouro)

**Snapshots são imutáveis.** Toda nova execução cria novo snapshot — nunca sobrescreve o anterior.

O arquivo `usuario-default.json` deve ser estruturado como **array de snapshots em ordem cronológica**:

```json
{
  "schema_version": "1.0.0",
  "usuario_ref": "default",
  "criado_em": "2026-01-12",
  "ultimo_snapshot": "2026-05-07",
  "snapshots": [
    { /* snapshot 1 */ },
    { /* snapshot 2 */ },
    { /* snapshot 3 */ }
  ]
}
```

### 4.4 LIMITE DE TAMANHO

Para evitar crescimento infinito:
- Manter os **últimos 24 snapshots** (cerca de 2 anos de revisões mensais)
- Snapshots mais antigos são consolidados no arquivo de trajetória (`.md`)
- Política: ao chegar em 25 snapshots, gerar resumo do mais antigo no `.md` e removê-lo do JSON

---

## 5. Casos de Uso

### Caso 1 — Continuidade entre sessões

**Sessão 1 (Janeiro):**
```
Skill: /pessoal-diagnostico-financeiro
Ação: Diagnóstico completo
Output: snapshot-2026-01-12.json salvo
       Estado: SOBREVIVÊNCIA, Risco: CRÍTICO
```

**Sessão 2 (Abril):**
```
Skill: /pessoal-rotina-financeira-mensal
Leitura: snapshot-2026-01-12.json
Apresentação ao usuário:
  "Comparando com janeiro:
   - Estado: SOBREVIVÊNCIA → ORGANIZAÇÃO ✅
   - Reserva: R$ 0 → R$ 4.500
   - Dívida cara: R$ 2.500 → R$ 0 ✅
   Você saiu da SOBREVIVÊNCIA. Vamos consolidar a Construção de Base."
```

### Caso 2 — Detecção de regressão

```
Snapshot anterior: estado = ESTABILIZAÇÃO, reserva = R$ 18.000
Snapshot atual:    estado = ORGANIZAÇÃO,  reserva = R$ 12.000

DETECÇÃO AUTOMÁTICA:
  Trajetória = REGRESSIVA
  Alerta: "Houve consumo da Camada de Proteção Financeira de R$ 6.000.
          Vamos analisar o que aconteceu antes de seguir."
```

### Caso 3 — Continuidade entre skills

```
Sessão atual:
1. /gestor-financeiro lê memória → identifica estado ORGANIZAÇÃO
2. Roteia para /pessoal-orcamento-domestico
3. Skill de orçamento já parte sabendo:
   - Renda atual: R$ 6.500
   - Gastos historicamente problemáticos: alimentação, lazer
   - Camada de Proteção em construção (23% da meta)
4. Não precisa coletar dados redundantemente
```

---

## 6. Engine de Detecção de Trajetória

Comparar o snapshot atual com o anterior:

```
SE estado_atual.indice_estado > snapshot_anterior.indice_estado:
  trajetoria = "PROGRESSIVA ↑"

SE estado_atual.indice_estado < snapshot_anterior.indice_estado:
  trajetoria = "REGRESSIVA ↓"
  → Disparar análise de causa raiz

SE estado_atual.indice_estado == snapshot_anterior.indice_estado:
  SE indicadores_progredindo:
    trajetoria = "ESTÁVEL POSITIVO →"
  SE indicadores_estagnados:
    trajetoria = "ESTÁVEL NEUTRO →"
  SE indicadores_regredindo:
    trajetoria = "ESTÁVEL NEGATIVO →"
    → Alertar: estagnação prolongada pode anteceder regressão
```

**Índice numérico dos estados (para comparação):**
```
SOBREVIVENCIA  = 1
ORGANIZACAO    = 2
ESTABILIZACAO  = 3
EXPANSAO       = 4
LEGADO         = 5
```

---

## 7. Privacidade e Segurança

**Dados pessoais sensíveis** registrados nos snapshots:
- Renda líquida
- Dívidas
- Saldos de reserva
- Contribuições do Reino

**Diretrizes:**

1. **Localização:** Apenas em diretório do usuário (`~/.financas-360/`) — nunca em local público
2. **Permissões de arquivo:** 600 (apenas o dono lê e escreve) em ambientes Unix-like
3. **Nunca enviar snapshots para serviços externos sem consentimento explícito**
4. **Anonimização:** Para fins de análise agregada futura, snapshots devem poder ser anonimizados removendo `usuario_ref` e valores absolutos (manter apenas percentuais e ratios)

---

## 8. Implementação em Ambientes Diferentes

### 8.1 Claude Code (CLI com filesystem)
- Persistência completa em `~/.financas-360/`
- Skills usam `Write`/`Read` tools para JSON
- Atualização automática a cada sessão

### 8.2 Claude.ai (sem filesystem permanente)
- Memória da sessão apenas
- Usuário pode "salvar manualmente" copiando o snapshot ASCII
- No início de nova conversa, usuário cola o snapshot anterior — sistema parseia
- Schema permanece o mesmo

### 8.3 Codex / Cursor / outros agentes
- Seguem o mesmo modelo do Claude Code
- Skills detectam ambiente e adaptam

### 8.4 Sem suporte a filesystem
- Snapshot apresentado ao usuário ao final da sessão como **bloco de código JSON**
- Usuário copia e cola na sessão seguinte
- Skill instrui: *"Cole o snapshot anterior se você o salvou para continuarmos a partir dali."*

---

## 9. Roadmap de Evolução

| Versão | Funcionalidade | Status |
|--------|---------------|--------|
| 1.0.0 | Schema básico, snapshots cronológicos, trajetória | ✅ Atual |
| 1.1.0 | Cache de referências (REFERENCIAS-BRASIL-2026) com TTL | Planejado |
| 1.2.0 | Multi-usuário (família) com agregação | Planejado |
| 2.0.0 | Sincronização opcional via API/webhook | Futuro |
| 2.1.0 | Análise estatística agregada anonimizada | Futuro |

---

## 10. Validação do Schema

Toda skill que escreve snapshot DEVE validar:

**Campos obrigatórios:**
- `schema_version`, `snapshot_id`, `data`, `skill_origem`, `usuario_ref`
- `estado_financeiro` (∈ enum dos 5 estados)
- `risco` (∈ {CRITICO, ALTO, MODERADO, BAIXO})
- `indicadores.renda_liquida`, `indicadores.saldo_mensal`

**Campos opcionais mas recomendados:**
- `gargalo_primario`, `gargalo_secundario`
- `desvios_destacados`
- `marcos_alcancados`, `marcos_pendentes`

**Validações cruzadas:**
- `comprometimento_pct + taxa_poupanca_pct ≤ 100`
- `reserva_atual ≤ reserva_meta`
- Se `estado_financeiro = SOBREVIVENCIA`, então `risco ∈ {CRITICO, ALTO}`
- Se `estado_financeiro ≥ EXPANSAO`, então `risco = BAIXO` e `reserva_progresso_pct = 100`

---

## 11. Mensagem ao Usuário (Primeira Sessão)

Ao detectar que não há memória prévia, a skill apresenta:

```
Esta é nossa primeira sessão registrada. Ao final, vou gerar um Snapshot 
Financeiro — um registro estruturado da sua situação atual.

Em sessões futuras, esse snapshot permite:
✓ Comparar evolução mês a mês
✓ Detectar regressões automaticamente  
✓ Eliminar coleta redundante de dados
✓ Acompanhar marcos alcançados

[Em ambientes sem filesystem persistente:]
Você receberá o snapshot em formato JSON — guarde-o e cole no início 
da próxima sessão para continuarmos a partir do ponto atual.
```

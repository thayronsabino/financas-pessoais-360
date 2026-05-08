# Changelog — MordomIA

> Todas as mudanças relevantes do projeto. Segue [Keep a Changelog](https://keepachangelog.com/pt-BR/) e [Semantic Versioning](https://semver.org/lang/pt-BR/).

---

## [2.1.0] — 2026-05-08

### 🌟 Adicionado — Alma Pastoral e Expansão de Cobertura

**Arquivos centrais (3 novos):**
- `PRINCIPIOS-BIBLICOS-EXPANDIDOS.md` — fundamentação teológica profunda com 8 princípios:
  - Idolatria do dinheiro
  - Ansiedade financeira
  - Contentamento
  - Generosidade radical
  - Riqueza como teste, não como meta
  - Honestidade nos negócios
  - Confiança em Deus na escassez
  - Hospitalidade como mordomia de recursos
- `PROTOCOLO-CRISE-ESPIRITUAL.md` — documento crítico para situações que transcendem finanças:
  - 5 níveis de severidade
  - Rede de apoio (CVV 188, CAPS, AA/NA/JA, Disque 180, Lei Maria da Penha)
  - Mensagens prontas para cuidador
- `EDUCACAO-FINANCEIRA-BASICA.md` — acessibilidade para iniciantes absolutos:
  - Glossário de termos básicos
  - 5 erros comuns
  - Sistema "caderno e caneta" para começar sem app

**Playbooks (3 novos):**
- `playbooks/idoso-aposentadoria-insuficiente.md` — 60+ com aperto financeiro
- `playbooks/informal-sem-cnpj.md` — trabalhador informal sem proteção
- `playbooks/endividamento-por-saude.md` — família em crise por doença grave

**Documentos de projeto:**
- `ROADMAP.md` — visão de longo prazo (v2.2 → v5.0)
- `CHANGELOG.md` — este arquivo

### 🔧 Modificado

- `gestor-financeiro/SKILL.md`:
  - Adicionada **Postura Pastoral Obrigatória** (5 regras inegociáveis)
  - Adicionada **Regra de Linguagem Proprietária** (quando expandir vs. usar termo direto)
  - Tabela de Playbooks atualizada (8 entradas)
  - Tabela de Arquivos Centrais expandida (6 entradas)
  - Notas Finais ampliadas

- Todas as 6 skills `pessoal-*`:
  - Adicionada seção "Arquivos Consultados pelo Sistema" com novos arquivos centrais
  - Adicionada **Regra de Linguagem** específica para a skill

- `README.md`: rebranding completo para MordomIA, atualização de GitHub
- `PACOTE.md`: 8 playbooks + 6 arquivos centrais + 10 princípios inegociáveis
- `INSTALAR.md`: novos métodos detalhados, troubleshooting, política de versões
- `install.py`: instalação completa (skills + playbooks + frameworks + centrais + docs)

### 🌐 Atualizado

- Repositório oficial: `github.com/thayronsabino/mordomia`
- Comandos npx skills: `npx skills add thayronsabino/mordomia`
- Landing page (`landing-page/index.html`): GitHub atualizado, og:url corrigido
- Landing page (`landing-page/SISTEMA.md`): instruções de instalação atualizadas

### 📊 Métricas

| Métrica | v2.0 | v2.1 |
|---------|------|------|
| Skills | 7 | 7 |
| Playbooks | 5 | **8** |
| Frameworks | 5 | 5 |
| Arquivos centrais | 3 | **6** |
| Total de arquivos `.md` | ~22 | **35+** |

### 🎯 Princípios Inegociáveis (atualizados de 6 → 10)

1. Acolhimento antes de números (NOVO)
2. Dízimo é piso (10%) — nunca alvo
3. Camada de Proteção Financeira antes de investimentos
4. Quitar dívida com taxa > Selic líquida antes de investir
5. O sistema decide; não lista opções
6. Estado real, não estado desejado
7. Mordomia inclui cuidar da própria casa (1 Tm 5:8)
8. Sistema reconhece limites — encaminha quando transcende finanças (NOVO)
9. Mordomia operacional + mordomia espiritual juntas (NOVO)
10. Linguagem serve ao usuário (NOVO)

---

## [2.0.0] — 2026-05-07

### 🚀 Adicionado — Capacidade Operacional

**Engines de Decisão:**
- Financial State Engine (5 estados: Sobrevivência → Legado)
- Risk Engine (4 níveis: Crítico → Baixo)
- Stewardship Engine (5 níveis: Mínimo → Impacto)

**Camadas Cognitivas (5):**
- Diagnóstico → Interpretação → Estratégia → Execução → Sustentação

**Protocolos Operacionais (3):**
- Protocolo Estancar Sangria Financeira
- Protocolo Construção de Base
- Protocolo Multiplicação Responsável

**Playbooks Premium (5):**
- `playbooks/recuperacao-90-dias.md`
- `playbooks/estruturacao-familiar.md`
- `playbooks/casal-e-financas.md`
- `playbooks/transicao-clt-pj.md`
- `playbooks/generosidade-sustentavel.md`

**Frameworks de Decisão (5):**
- `frameworks/investir-vs-quitar-divida.md`
- `frameworks/clt-vs-pj.md`
- `frameworks/casa-vs-aluguel.md`
- `frameworks/priorizacao-financeira.md`
- `frameworks/comprar-a-vista-vs-parcelado.md`

**Arquivos Centrais (3):**
- `REFERENCIAS-BRASIL-2026.md` — dados macroeconômicos, tributários, legislativos
- `GLOSSARIO.md` — terminologia proprietária
- `MEMORY-SYSTEM.md` — especificação do Mecanismo de Memória Financeira

**Funcionalidades adicionais:**
- Painéis Operacionais ASCII (dashboards) em todas as skills
- Engine de Detecção de Demandas Específicas (gatilhos para playbooks/frameworks)
- Linguagem proprietária consolidada:
  - Sistema de Mapeamento de Fluxo Financeiro
  - Sistema de Orçamento Doméstico
  - Camada de Proteção Financeira
  - Ciclo de Recalibração Financeira
  - Plano de Generosidade Sustentável
- Mecanismo de Memória Financeira (snapshots cronológicos, schema JSON)
- Cross-references explícitos entre todos os componentes

### 🔧 Modificado

- 7 skills core completamente reescritas com novos engines, camadas cognitivas, painéis operacionais
- Tom geral: de tutorial para consultor decisivo
- Outputs: de markdown para dashboards operacionais
- Versão das skills: 1.0.0 → 2.0.0 (3.0.0 para gestor-financeiro)

### 📊 Métricas

| Métrica | v1.0 | v2.0 |
|---------|------|------|
| Skills | 7 | 7 |
| Playbooks | 0 | **5** |
| Frameworks | 0 | **5** |
| Arquivos centrais | 0 | **3** |
| Total de arquivos `.md` | ~10 | **~22** |

---

## [1.0.0] — 2026-03-27

### 🌱 Lançamento Inicial — Foundation

**7 Skills Core:**
- `gestor-financeiro` — orquestrador
- `pessoal-diagnostico-financeiro` — raio-X financeiro
- `pessoal-orcamento-domestico` — orçamento com 4 blocos
- `pessoal-plano-dividas-reserva` — quitação + reserva
- `pessoal-estrategia-investimentos` — estratégia patrimonial
- `pessoal-rotina-financeira-mensal` — revisão mensal
- `pessoal-investimento-reino` — dízimo, ofertas, projetos ministeriais

**Características:**
- Filosofia de mordomia cristã embutida
- Dízimo 10% como princípio inviolável
- `pessoal-investimento-reino` obrigatório em consultoria
- Fluxos visuais (Mermaid, tabelas) em devolutivas
- Compatibilidade com Claude, Codex e 55+ agentes

**Princípios estabelecidos (6):**
1. Dízimo é piso (10%) — nunca alvo
2. Camada de Proteção antes de investimentos
3. Quitar dívida cara antes de investir
4. O sistema decide; não lista opções
5. Estado real, não estado desejado
6. Mordomia inclui cuidar da própria casa (1 Tm 5:8)

---

## Convenções deste Changelog

```
🌟 Adicionado    Para novos recursos
🔧 Modificado    Para mudanças em recursos existentes
🐛 Corrigido     Para correções de bugs
🗑️ Removido      Para recursos removidos
🔒 Segurança     Para correções de segurança
⚠️ Depreciado    Para recursos que serão removidos
🌐 Atualizado    Para atualizações de dados (taxas, regulamentação)
📊 Métricas      Para indicadores quantitativos da versão
```

---

## Próximas Versões

Ver `ROADMAP.md` para detalhes completos das versões futuras (v2.2 → v5.0).

| Versão | Data planejada | Foco |
|--------|---------------|------|
| 2.2.0 | Junho/2026 | Ajustes incrementais |
| 3.0.0 | Setembro/2026 | Simulation Layer (scripts executáveis) |
| 3.5.0 | Dezembro/2026 | Web Integration (taxas em tempo real) |
| 4.0.0 | Março/2027 | Operational Layer (CLI, dashboard) |
| 4.5.0 | Junho/2027 | Multi-Idioma (en, es) |
| 5.0.0 | 2028+ | Platform (SaaS opcional) |

---

**Repositório:** https://github.com/thayronsabino/mordomia  
**Releases:** https://github.com/thayronsabino/mordomia/releases

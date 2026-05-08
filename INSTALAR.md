# Instalação — MordomIA

> **Repositório oficial:** https://github.com/thayronsabino/mordomia  
> **Versão atual:** 2.1.0  
> **Última atualização:** 2026-05-08

Escolha o método de instalação conforme seu ambiente.

---

## 🌐 Antes de Começar

### Pré-requisitos

| Método | Requisitos |
|--------|-----------|
| A — npx skills | Node.js 16+, internet, agente compatível (Claude Code, Codex, Cursor) |
| B — Upload Claude.ai | Conta Claude.ai com acesso a Habilidades |
| C — Clone Git | Git instalado, sistema de skills compatível |
| D — Script Python | Python 3.6+, internet |

### Agentes compatíveis

✅ **Funciona em:**
- Claude Code (CLI)
- Claude Desktop (Mac/Windows)
- Claude.ai (web)
- Codex CLI
- Cursor
- Continue.dev
- Aider
- Mais 50+ agentes que suportam o padrão `SKILL.md`

⚠️ **Compatibilidade limitada:**
- ChatGPT (sem suporte nativo, mas pode ler arquivos manualmente)
- Gemini CLI (suporte parcial)

---

## Método A — npx skills (recomendado)

**Para Claude Code, Codex, Cursor e 55+ agentes que suportam `npx skills`.**

### Instalação completa

```bash
npx skills add thayronsabino/mordomia
```

Esse comando instala automaticamente:
- 7 skills core
- 8 playbooks premium
- 5 frameworks de decisão
- 6 arquivos centrais (referências, glossário, memory system, princípios bíblicos, protocolo de crise, educação básica)

### Instalação de skill específica

```bash
# Apenas o orquestrador (você precisará dos outros depois)
npx skills add thayronsabino/mordomia --skill gestor-financeiro

# Múltiplas skills
npx skills add thayronsabino/mordomia --skill gestor-financeiro
npx skills add thayronsabino/mordomia --skill pessoal-orcamento-domestico
```

### Instalação explícita de tudo

```bash
npx skills add thayronsabino/mordomia --skill '*'
```

### Atualização

```bash
npx skills update thayronsabino/mordomia
```

### Desinstalação

```bash
npx skills remove thayronsabino/mordomia
```

---

## Método B — Upload via Habilidades (Claude.ai)

**Para usuários do Claude.ai sem terminal.**

### Passo a passo

1. **Baixe o pacote:**
   - Acesse: https://github.com/thayronsabino/mordomia
   - Clique em **Code → Download ZIP**
   - Descompacte em uma pasta local

2. **Acesse Habilidades no Claude.ai:**
   - Abra: https://claude.ai
   - Clique no avatar (canto superior direito)
   - **Configurações → Habilidades**

3. **Faça upload das 7 skills (uma por vez):**

| Ordem | Arquivo | Função |
|-------|---------|--------|
| 1 | `gestor-financeiro/SKILL.md` | **Orquestrador — instale primeiro** |
| 2 | `pessoal-diagnostico-financeiro/SKILL.md` | Sistema de Mapeamento de Fluxo Financeiro |
| 3 | `pessoal-orcamento-domestico/SKILL.md` | Sistema de Orçamento Doméstico |
| 4 | `pessoal-plano-dividas-reserva/SKILL.md` | Quitação + Camada de Proteção |
| 5 | `pessoal-estrategia-investimentos/SKILL.md` | Crescimento Patrimonial |
| 6 | `pessoal-rotina-financeira-mensal/SKILL.md` | Ciclo de Recalibração Financeira |
| 7 | `pessoal-investimento-reino/SKILL.md` | Plano de Generosidade Sustentável |

4. **Após o upload de todas, invoque o orquestrador:**

```
/gestor-financeiro
```

### Limitações do Método B

```
⚠️ No Claude.ai, as skills funcionam, MAS:

- Os arquivos centrais (REFERENCIAS-BRASIL-2026.md, PRINCIPIOS-BIBLICOS-EXPANDIDOS.md, 
  PROTOCOLO-CRISE-ESPIRITUAL.md, EDUCACAO-FINANCEIRA-BASICA.md, GLOSSARIO.md, 
  MEMORY-SYSTEM.md) NÃO são automaticamente acessíveis.

- Os playbooks e frameworks NÃO são automaticamente acessíveis.

- O Claude conseguirá orientar usando o conhecimento das skills, mas perde 
  parte da profundidade que vem dos arquivos centrais.

SOLUÇÃO RECOMENDADA: 
  Subir também os arquivos centrais e playbooks como anexos no início da 
  conversa, ou usar Método A (npx skills) para experiência completa.
```

---

## Método C — Clone do Repositório

**Para desenvolvedores ou quem quer customizar.**

```bash
git clone https://github.com/thayronsabino/mordomia.git
cd mordomia
```

Estrutura completa:

```
mordomia/
├── README.md
├── PACOTE.md
├── INSTALAR.md  ← (este arquivo)
├── ROADMAP.md
├── DESIGN.md
├── LICENSE
├── install.py
│
├── REFERENCIAS-BRASIL-2026.md
├── GLOSSARIO.md
├── MEMORY-SYSTEM.md
├── PRINCIPIOS-BIBLICOS-EXPANDIDOS.md
├── PROTOCOLO-CRISE-ESPIRITUAL.md
├── EDUCACAO-FINANCEIRA-BASICA.md
│
├── gestor-financeiro/SKILL.md
├── pessoal-diagnostico-financeiro/SKILL.md
├── pessoal-orcamento-domestico/SKILL.md
├── pessoal-plano-dividas-reserva/SKILL.md
├── pessoal-estrategia-investimentos/SKILL.md
├── pessoal-rotina-financeira-mensal/SKILL.md
├── pessoal-investimento-reino/SKILL.md
│
├── playbooks/
│   ├── recuperacao-90-dias.md
│   ├── estruturacao-familiar.md
│   ├── casal-e-financas.md
│   ├── transicao-clt-pj.md
│   ├── generosidade-sustentavel.md
│   ├── idoso-aposentadoria-insuficiente.md
│   ├── informal-sem-cnpj.md
│   └── endividamento-por-saude.md
│
├── frameworks/
│   ├── investir-vs-quitar-divida.md
│   ├── clt-vs-pj.md
│   ├── casa-vs-aluguel.md
│   ├── priorizacao-financeira.md
│   └── comprar-a-vista-vs-parcelado.md
│
└── landing-page/
    ├── index.html
    ├── style.css
    ├── main.js
    ├── Manifesto — MordomIA.md
    ├── SISTEMA.md
    └── Landing Page da MordomIA Fin.md
```

### Apontar agente para a pasta clonada

**Claude Code:**

```bash
# Editar ~/.claude/skills/ para apontar para a pasta clonada
# OU configurar no settings.json o caminho completo
```

**Cursor:**

```bash
# Configurações → Skills → Add Local Path
# Apontar para a pasta mordomia/
```

---

## Método D — Script Python (fallback)

**Para ambientes sem Node.js. Funciona em Windows, Mac e Linux.**

### Requisitos

- Python 3.6 ou superior
- Conexão com internet
- 50 MB de espaço em disco

### Instalação

```bash
# Baixar o script
curl -O https://raw.githubusercontent.com/thayronsabino/mordomia/main/install.py

# Executar
python install.py
```

### Opções

```bash
# Instalar em pasta específica
python install.py --destino /caminho/desejado

# Instalar apenas as skills (sem playbooks/frameworks)
python install.py --skills-only

# Instalar versão específica
python install.py --versao 2.1.0

# Modo silencioso (sem prompts)
python install.py --quiet
```

### O que o script faz

```
1. Verifica Python e internet
2. Baixa o pacote do GitHub (release oficial)
3. Descompacta na pasta destino
4. Verifica integridade dos arquivos
5. Cria estrutura de diretórios correta
6. Não cria atalhos nem instala globalmente — apenas baixa os arquivos
```

---

## Estrutura Pós-Instalação

Após qualquer método de instalação, você terá:

```
[pasta-de-instalação]/
├── 6 arquivos centrais (.md)
├── 7 pastas de skills (cada uma com SKILL.md)
├── playbooks/ (8 arquivos)
├── frameworks/ (5 arquivos)
├── landing-page/ (4 arquivos)
└── arquivos de documentação (README, PACOTE, INSTALAR, ROADMAP, etc.)
```

**Total:** 35+ arquivos `.md` + scripts auxiliares

---

## Dependências Entre Skills

Como as skills se relacionam internamente:

```
gestor-financeiro (entrada — orquestrador)
│
├── pessoal-diagnostico-financeiro
│   └─→ aponta para: orcamento, plano-dividas, ou rotina
│
├── pessoal-orcamento-domestico
│   └─→ aponta para: plano-dividas, investimento-reino, ou rotina
│
├── pessoal-plano-dividas-reserva
│   └─→ aponta para: rotina, ou estrategia-investimentos (após reserva)
│
├── pessoal-estrategia-investimentos
│   └─→ aponta para: rotina-mensal, investimento-reino
│
├── pessoal-investimento-reino
│   └─→ obrigatório em qualquer cadeia consultiva
│
└── pessoal-rotina-financeira-mensal
    └─→ hub de manutenção mensal de longo prazo
```

**O que o gestor-financeiro também aciona:**

```
gestor-financeiro
├── Lê arquivos centrais (REFERENCIAS, GLOSSARIO, PRINCIPIOS, etc.)
├── Detecta gatilhos e ativa frameworks (5 disponíveis)
├── Detecta situações e ativa playbooks (8 disponíveis)
└── Aciona PROTOCOLO-CRISE-ESPIRITUAL.md quando necessário
```

---

## Verificação da Instalação

Após instalar, valide com:

### 1. Verificação de arquivos

```bash
# Linux/Mac
ls -la mordomia/
ls -la mordomia/playbooks/
ls -la mordomia/frameworks/

# Windows (PowerShell)
Get-ChildItem mordomia/
Get-ChildItem mordomia/playbooks/
Get-ChildItem mordomia/frameworks/
```

Você deve ver pelo menos:
- 6 arquivos `.md` na raiz (REFERENCIAS, GLOSSARIO, MEMORY-SYSTEM, PRINCIPIOS-BIBLICOS-EXPANDIDOS, PROTOCOLO-CRISE-ESPIRITUAL, EDUCACAO-FINANCEIRA-BASICA)
- 7 pastas de skill com `SKILL.md` em cada
- 8 arquivos em `playbooks/`
- 5 arquivos em `frameworks/`

### 2. Teste funcional

No seu agente:

```
/gestor-financeiro
```

Você deve receber resposta de boas-vindas explicando o sistema, perguntando como você se sente em relação à sua situação financeira (acolhimento pastoral) e indicando que vai conduzir a triagem.

### 3. Verificar referências cruzadas

Pergunte ao agente:

```
"Liste todos os playbooks disponíveis no MordomIA."
```

A resposta deve listar 8 playbooks (não 5 — versões antigas listavam apenas 5).

```
"Quais arquivos centrais existem no pacote?"
```

A resposta deve mencionar 6 arquivos centrais (versões antigas tinham apenas 3).

---

## Solução de Problemas

### "npx skills add não é reconhecido"

```bash
# Verificar Node.js
node --version

# Se Node não estiver instalado:
# Mac: brew install node
# Ubuntu: sudo apt install nodejs
# Windows: baixar de nodejs.org
```

### "Skill não aparece após upload no Claude.ai"

```
1. Atualizar a página (F5)
2. Verificar que o frontmatter (---name: ...---) está intacto no SKILL.md
3. Tentar fazer upload novamente
4. Reportar bug em github.com/thayronsabino/mordomia/issues
```

### "Agente não está reconhecendo termos proprietários"

```
Causa: provavelmente apenas as skills foram instaladas, sem os arquivos centrais.

Solução: 
- Se Método A: Reinstalar com --skill '*'
- Se Método B: Subir arquivos centrais como anexo
- Se Método C: Garantir que clone foi completo
```

### "Quero instalar apenas para usar offline"

```
Use Método C (clone) ou Método D (Python script).
Após instalar, os arquivos ficam locais — não há dependência de internet 
para uso. Apenas o REFERENCIAS-BRASIL-2026.md pode ficar desatualizado 
(precisa atualização trimestral manual ou via futura integração web).
```

---

## Atualizações

### Como saber se há nova versão

```bash
# Via npx
npx skills info thayronsabino/mordomia

# Via GitHub
git -C mordomia/ fetch && git -C mordomia/ status
```

Verifique também:
- https://github.com/thayronsabino/mordomia/releases

### Política de versões

| Tipo | Frequência | Conteúdo |
|------|-----------|----------|
| Patch (2.1.x) | Mensal | Correções, atualização de taxas |
| Minor (2.x.0) | Trimestral | Novos playbooks, frameworks |
| Major (x.0.0) | Anual | Mudanças estruturais (ver `ROADMAP.md`) |

---

## Desinstalação

### Método A (npx skills)

```bash
npx skills remove thayronsabino/mordomia
```

### Método B (Claude.ai)

Remover cada skill via **Configurações → Habilidades → Remover**.

### Método C/D (clone ou Python)

```bash
# Linux/Mac
rm -rf mordomia/

# Windows
Remove-Item -Recurse -Force mordomia/
```

---

## Próximos Passos

Após instalar:

1. ✅ **Leia o `README.md`** para visão geral
2. ✅ **Leia o `PACOTE.md`** para entender a ordem das skills
3. ✅ **Invoque `/gestor-financeiro`** e comece sua jornada
4. ✅ **Para iniciantes:** consulte `EDUCACAO-FINANCEIRA-BASICA.md`
5. ✅ **Para entender filosofia:** leia `landing-page/Manifesto — MordomIA.md`

---

## Suporte

- 🐛 **Bugs e dúvidas:** https://github.com/thayronsabino/mordomia/issues
- 💬 **Discussões:** https://github.com/thayronsabino/mordomia/discussions
- 📖 **Documentação completa:** [`README.md`](README.md), [`PACOTE.md`](PACOTE.md), [`ROADMAP.md`](ROADMAP.md)

---

**MordomIA v2.1.0** | Apache License 2.0 | https://github.com/thayronsabino/mordomia

# Contribuindo com o MordomIA

Obrigado por considerar contribuir! O MordomIA é um projeto **open source** sob Apache License 2.0, e contribuições alinhadas com seus princípios são muito bem-vindas.

---

## 🎯 Tipos de Contribuição Aceitas

### ✅ Contribuições bem-vindas

```
1. ATUALIZAÇÃO DE DADOS
   Pull Request atualizando REFERENCIAS-BRASIL-2026.md
   Sempre citando fonte oficial (BCB, Receita Federal, IBGE, etc.)

2. NOVO PLAYBOOK
   Caso brasileiro/internacional não coberto
   Estrutura aderente aos playbooks existentes
   Validado por pelo menos 1 conselheiro pastoral + 1 financeiro

3. NOVO FRAMEWORK
   Decisão financeira específica e frequente
   Engine de decisão claro (lógica IF/THEN)
   Aplicação prática com casos de uso

4. SCRIPTS DE SIMULAÇÃO (Python/JS)
   Com testes (cobertura ≥ 80%)
   Documentação clara de inputs/outputs
   Aderência ao REFERENCIAS-BRASIL-2026.md

5. TRADUÇÕES
   Skills, playbooks ou frameworks em outros idiomas
   Adaptação cultural respeitando princípios bíblicos universais

6. CASOS DE USO REAIS (anonimizados)
   Transcrições de jornadas reais com permissão explícita
   Mostram o pacote em ação

7. CORREÇÃO DE BUGS / TYPOS
   Sempre bem-vindos

8. DOCUMENTAÇÃO
   Melhorias, exemplos adicionais, clarificações
```

### ❌ Contribuições que NÃO aceitamos

```
✗ Conteúdo que sugere dízimo abaixo de 10%
✗ Endividamento como solução para qualquer problema
✗ Esquemas de "ficar rico rápido" ou similares
✗ Pirâmides financeiras / esquemas Ponzi
✗ Recomendação de investimentos em criptomoedas voláteis 
  sem ressalvas explícitas
✗ Conteúdo que pula acolhimento e vai direto para técnica
✗ Linguagem moralista ou de julgamento
✗ Substitutos para terapia, advocacia, medicina ou aconselhamento pastoral
✗ Conteúdo politicamente partidário
✗ Conteúdo sectário (denominacional excludente)
```

---

## 🛡️ Princípios Inegociáveis

Toda contribuição precisa respeitar:

```
1. DÍZIMO 10% É PISO ABSOLUTO
   Não há versão futura onde dízimo < 10% será sugerido.

2. ACOLHIMENTO ANTES DE NÚMEROS
   Toda primeira interação começa com escuta empática.

3. ESTADO REAL, NÃO ESTADO DESEJADO
   Não dar orientação de Expansão para usuário em Sobrevivência.

4. SISTEMA RECONHECE LIMITES
   Quando o problema transcende finanças, encaminhar para apoio profissional.

5. MORDOMIA OPERACIONAL + ESPIRITUAL
   As duas dimensões juntas, sempre.

6. GRATUITO PARA USO LOCAL
   O pacote em arquivos locais será sempre gratuito.

7. CÓDIGO ABERTO (Apache 2.0)
   Versões futuras mantêm licença permissiva.

8. PRINCÍPIOS BÍBLICOS COMO NÚCLEO
   Mesmo internacionalização não dilui o núcleo cristão.
```

---

## 🔄 Processo de Contribuição

### Passo a passo

```
1. FORK DO REPOSITÓRIO
   github.com/thayronsabino/mordomia → seu fork

2. CRIAR BRANCH
   feature/[descricao] ou fix/[descricao]
   Exemplos:
     feature/playbook-imigrante-recem-chegado
     fix/typo-em-glossario
     update/referencias-junho-2026

3. FAZER MUDANÇAS
   Seguir padrões do projeto (próxima seção)
   Manter o estilo de markdown e estrutura

4. COMMIT
   Mensagens claras (português ou inglês)
   Convenção: tipo: descrição
   Exemplos:
     feat: adiciona playbook para imigrantes
     fix: corrige link quebrado em README.md
     docs: atualiza CHANGELOG para v2.2
     update: taxas Selic junho/2026

5. PULL REQUEST
   Título: descrição clara do que muda
   Descrição:
     - Problema que resolve
     - Solução proposta
     - Como testou (se aplicável)
     - Checklist de princípios respeitados

6. REVIEW
   Mantenedores avaliam alinhamento com princípios
   Pode haver pedidos de ajuste — normal

7. MERGE
   Após aprovação técnica + pastoral
```

---

## 📐 Padrões do Projeto

### Estrutura de Skill (`SKILL.md`)

```markdown
---
name: nome-da-skill
description: >
  Descrição clara em 2-3 frases que explica quando usar a skill.
  Inclui palavras-chave que o gestor-financeiro pode detectar.
owner: financeiro-pessoal
version: 1.0.0
last_updated: AAAA-MM-DD
---

# Nome Proprietário da Skill

## Postura do Sistema
[Tom decisivo, autoridade consultiva]

## Arquivos Consultados pelo Sistema
[Tabela com arquivos centrais e quando consultar]

## Regra de Linguagem
[Quando expandir termos proprietários]

## CAMADAS COGNITIVAS
[5 camadas: Diagnóstico → Sustentação]

## Entradas Necessárias
[Tabela de inputs]

## ENGINE DE DECISÃO — [Tema]
[Matrizes IF/THEN]

## Processo / Estrutura
[Detalhamento operacional]

## Output Estruturado
[Painel Operacional ASCII]

## Próxima Skill
[Roteamento]
```

### Estrutura de Playbook

```markdown
# Playbook: [Nome]

> **Tipo:** Playbook Operacional Premium
> **Versão:** 1.0.0
> **Estado-alvo:** [origem] → [destino]
> **Duração:** [tempo]
> **Última atualização:** AAAA-MM-DD

[Texto introdutório com princípio orientador]

## 1. Quando Ativar
[Critérios objetivos com lógica IF/THEN]

## 2. Estado-alvo de Saída
[Checklist de critérios de saída]

## 3. [Diagnóstico Específico ou Estrutura]

## 4. Cronograma Detalhado
[Semanas/meses com marcos]

## 5. Painel de Acompanhamento
[Dashboard ASCII]

## 6. Sinais de Alerta

## 7. Adaptações por Perfil

## 8. Skills do Pacote Usadas

## 9. Princípios Operacionais

## 10. Mensagem ao Usuário
```

### Estrutura de Framework

```markdown
# Framework: [Decisão]

> **Tipo:** Framework de Decisão Financeira
> **Versão:** 1.0.0
> **Aplicação:** [contexto]
> **Última atualização:** AAAA-MM-DD

## 1. Regra Fundamental
[Equação ou princípio matemático]

## 2. Aplicação Prática
[Tabelas com casos comuns]

## 3. Engine de Decisão
[IF/THEN detalhado]

## 4. Casos Práticos
[3-5 exemplos com cálculos]

## 5. Exceções e Nuances

## 6. Painel de Decisão
[Dashboard ASCII]

## 7. Princípios Operacionais
```

### Convenções de markdown

```markdown
- Cabeçalhos h1 (#) apenas para o título do documento
- Cabeçalhos h2 (##) para seções principais
- Cabeçalhos h3 (###) para subseções
- Tabelas com headers explícitos
- Blocos de código com linguagem especificada (```python, ```bash, ```txt)
- Citações bíblicas em > blockquote, com referência no final
- Emojis usados com parcimônia, principalmente em listas de status (✅ ❌ ⚠️)
- Painéis ASCII centralizados, com largura ~50 caracteres
```

### Convenções de linguagem

```
- PORTUGUÊS BRASILEIRO como idioma padrão
- Acentuação completa (não escrever "nao" em vez de "não")
- Termos técnicos financeiros podem permanecer em inglês quando padrão
  (ex: "rotativo" do cartão, "consignado", "pré-fixado")
- Termos proprietários do MordomIA escritos com Iniciais Maiúsculas
  (ex: "Camada de Proteção Financeira", "Sistema de Orçamento Doméstico")
- Versículos bíblicos: usar Almeida Revista e Atualizada (ARA) preferencialmente
```

---

## 🧪 Testes e Validação

### Para skills, playbooks e frameworks

```
ANTES DE ABRIR PR, VERIFICAR:

[ ] Frontmatter completo e válido (name, description, owner, version, last_updated)
[ ] Seção de "Arquivos Consultados pelo Sistema" presente
[ ] Pelo menos 1 caso de uso completo descrito
[ ] Painel Operacional ASCII (se aplicável)
[ ] Linguagem aderente ao tom do projeto (decisivo + pastoral)
[ ] Todos os links internos funcionam
[ ] Termos proprietários consistentes com GLOSSARIO.md
[ ] Princípios bíblicos integrados naturalmente (não como decoração)
[ ] Cobertura de casos de borda
```

### Para atualizações de REFERENCIAS-BRASIL-2026.md

```
[ ] Todos os valores citam fonte oficial
[ ] Data de "Última atualização" atualizada
[ ] Próxima revisão obrigatória recalculada
[ ] Sem mudanças não validadas (toda mudança tem fonte verificável)
```

### Para scripts (Python/JS, futuramente)

```
[ ] Testes unitários (pytest, jest)
[ ] Cobertura ≥ 80%
[ ] Documentação de função (docstrings)
[ ] Validação de inputs
[ ] Tratamento de edge cases
[ ] README específico do script
```

---

## 🌍 Tradução

Ao traduzir conteúdo:

```
1. PRESERVAR PRINCÍPIOS UNIVERSAIS
   - Versículos bíblicos: usar tradução padrão do idioma alvo
   - Princípios cristãos não-localizáveis (são os mesmos em qualquer idioma)

2. ADAPTAR REFERÊNCIAS LOCAIS
   - Substituir REFERENCIAS-BRASIL-2026.md por REFERENCIAS-[PAIS]-[ANO].md
   - Adaptar legislação (FGTS → equivalente local)
   - Adaptar moedas (R$ → USD/EUR/MXN)
   - Adaptar instituições (BCB → Fed/BCE/Banxico)

3. PRESERVAR LINGUAGEM PROPRIETÁRIA
   - "Camada de Proteção Financeira" → "Financial Protection Layer" (não "Emergency Fund")
   - "Sistema de Mapeamento de Fluxo Financeiro" → "Financial Flow Mapping System"
   - Manter identidade do MordomIA mesmo em outros idiomas

4. RESPEITAR CONTEXTO CULTURAL
   - Casos brasileiros (rotativo do cartão, consignado, etc.) podem virar opcionais
   - Adicionar casos típicos do país alvo
   - Verificar se a sensibilidade pastoral é apropriada à cultura
```

---

## 💬 Comunicação

### Abrir uma issue

```
Use o GitHub Issues para:
- Reportar bug
- Sugerir melhoria
- Propor novo recurso
- Pedir clarificação
- Compartilhar caso de uso

URL: https://github.com/thayronsabino/mordomia/issues
```

### Discussões

```
Use Discussions para:
- Conversas mais amplas sobre direção do projeto
- Pedir feedback sobre ideias antes de implementar
- Compartilhar histórias de uso
- Network com outros contribuidores

URL: https://github.com/thayronsabino/mordomia/discussions
```

### Contato direto

Para casos sensíveis (dados pessoais, conflitos, denúncias):
- Email: [a definir]
- Sigilo respeitado

---

## 🤝 Código de Conduta

```
SEMPRE:
✅ Ser respeitoso com outros contribuidores
✅ Aceitar feedback construtivo
✅ Lembrar que mantenedores são voluntários
✅ Honrar diversidade (não excluir por idade, raça, gênero, denominação)
✅ Manter foco no propósito do projeto

NUNCA:
❌ Usar linguagem ofensiva, discriminatória ou desrespeitosa
❌ Atacar pessoas por suas crenças ou falta delas
❌ Spamar ou usar o projeto para promover negócios não relacionados
❌ Plagiar conteúdo de terceiros sem atribuição
❌ Sectarismo denominacional excludente
```

**Violações** podem resultar em remoção de contribuições e, em casos graves, banimento do projeto.

---

## 🎓 Reconhecimento

Contribuidores aprovados terão:
- Nome no `CONTRIBUTORS.md` (a ser criado)
- Reconhecimento na release notes da versão
- Crédito em casos de uso reais (com permissão)

---

## ❓ Dúvidas Frequentes

### Posso usar o MordomIA em meu negócio (consultoria, igreja)?

Sim. Apache License 2.0 permite uso comercial. Apenas é obrigatório referenciar a fonte original: `github.com/thayronsabino/mordomia`.

### Posso adaptar o MordomIA para minha denominação?

Sim, em fork próprio. Mas:
- Mantenha princípios bíblicos universais
- Não tente fazer o repositório oficial virar denominacional
- Diferenças teológicas secundárias são respeitadas em forks

### Posso traduzir o MordomIA?

Absolutamente sim — é um dos roadmaps prioritários (v4.5). Veja seção "Tradução" acima.

### Posso vender produtos baseados no MordomIA?

Sim. Cursos, livros, consultorias baseados nos princípios do MordomIA podem ser comerciais. Apenas:
- Referencie a fonte
- Não restrinja redistribuição do código original
- Não diga que é "MordomIA Oficial" se não for autorizado

### Como saber se minha contribuição vai ser aceita?

Antes de investir tempo grande:
1. Abra uma **issue** descrevendo a ideia
2. Aguarde feedback dos mantenedores
3. Receba "go-ahead" antes de codificar

Para correções pequenas (typos, links quebrados), pode ir direto para PR.

---

## 🙏 Por Que Contribuir

```
Sua contribuição pode:

▸ Ajudar uma família a sair de SOBREVIVÊNCIA
▸ Levar dignidade financeira a um idoso
▸ Apoiar uma família em crise por doença
▸ Salvar um casamento da pressão financeira
▸ Educar uma pessoa que nunca teve acesso a finanças
▸ Multiplicar a generosidade em comunidades cristãs
▸ Mostrar que tecnologia + fé + cuidado humano juntos transformam vidas

Cada contribuição honesta é mordomia ativa.
"O que vocês receberam de graça, deem também de graça." — Mateus 10:8
```

---

**MordomIA** | Apache License 2.0 | https://github.com/thayronsabino/mordomia

> Última atualização: 2026-05-08

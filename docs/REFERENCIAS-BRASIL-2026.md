# Referências Brasil 2026 — Dados Dinâmicos

> **Validade:** Maio/2026 a Dezembro/2026  
> **Última atualização:** 2026-05-07  
> **Próxima revisão obrigatória:** 2026-06-21 (45 dias — ciclo Copom)  
> **Como atualizar:** Executar `python update-referencias.py` ou ver seção "Fontes Oficiais e Atualização" ao final.

Este arquivo centraliza todos os dados macroeconômicos, regulatórios e tributários usados pelas skills do pacote **MordomIA**. Todas as skills devem referenciar este arquivo em vez de manter taxas hardcoded.

---

## 0. PROTOCOLO DE DADOS AO VIVO — PARA O AGENTE

> **Leia isto antes de usar qualquer taxa abaixo.**

O Banco Central do Brasil disponibiliza uma API pública, gratuita e sem autenticação que retorna JSON com os valores mais recentes. **Sempre que houver ferramenta de busca web disponível (WebSearch, Firecrawl, fetch), busque os dados ao vivo antes de usar o cache abaixo.**

### APIs BCB — Indicadores de Política Monetária

| Indicador | Série SGS | URL da API |
|-----------|-----------|------------|
| **Selic Meta** (% a.a.) | 432 | `https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/1?formato=json` |
| **IPCA** (% a.m.) | 433 | `https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados/ultimos/1?formato=json` |
| **CDI** (% a.a.) | 12 | `https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados/ultimos/1?formato=json` |
| **TR** (% a.m.) | 226 | `https://api.bcb.gov.br/dados/serie/bcdata.sgs.226/dados/ultimos/1?formato=json` |
| **IGP-M** (% a.m.) | 189 | `https://api.bcb.gov.br/dados/serie/bcdata.sgs.189/dados/ultimos/1?formato=json` |

**Formato da resposta:** `[{"data": "DD/MM/YYYY", "valor": "X.XX"}]`

### API BCB — Taxas de Crédito por Modalidade

```
https://olinda.bcb.gov.br/olinda/servico/taxaJuros/versao/v2/odata/TaxasJuros
  ?$top=300&$format=json&$orderby=DataEmissao%20desc
  &$select=Modalidade,TaxaJurosMes,TaxaJurosAno,DataEmissao
```

### Protocolo de uso pelo agente

```
PASSO 1 — Tentar busca ao vivo:
  Buscar Selic (série 432) e IPCA (série 433) via WebSearch/Firecrawl/fetch
  Se obtiver valor → usar o valor ao vivo, informar a data da série

PASSO 2 — Se a busca falhar:
  Usar os valores em cache das seções abaixo
  Exibir aviso: "⚠️ Usando taxa em cache de [data da última atualização].
  Verifique em bcb.gov.br para o valor atual."

PASSO 3 — Se cache > 45 dias:
  Exibir aviso reforçado: "⚠️ Taxas podem estar desatualizadas (Copom pode
  ter alterado a Selic). Execute update-referencias.py ou consulte bcb.gov.br."
```

### Automação (atualização automática do cache)

Execute localmente para atualizar este arquivo com dados ao vivo:

```bash
pip install requests
python update-referencias.py
```

Para automação recorrente (recomendado a cada 45 dias):
- **GitHub Actions:** criar workflow `.github/workflows/update-referencias.yml`
- **Windows:** `schtasks /create /sc weekly /tn "MordomIA BCB" /tr "python update-referencias.py"`
- **Linux/Mac:** `crontab -e` → `0 8 1,15 * * python /caminho/update-referencias.py`

⚠️ **AVISO DE DERIVA:** Se a data atual for posterior a **45 dias** da "última atualização", os dados podem estar defasados (o Copom se reúne a cada 45 dias). As skills devem alertar o usuário e sugerir consulta às fontes oficiais.

---

## 1. POLÍTICA MONETÁRIA

| Indicador | Valor | Acumulado 12m | Tendência |
|-----------|-------|---------------|-----------|
| **Selic Meta** | 14,75% a.a. | — | → Estável |
| **CDI** | ~14,65% a.a. | ~14,40% | → Estável |
| **IPCA (oficial)** | 0,38% a.m. | 4,82% | ↓ Cedendo |
| **IGP-M** | 0,12% a.m. | 6,15% | ↓ Cedendo |
| **TR (Taxa Referencial)** | ~0,15% a.m. | 1,88% | → Estável |
| **Poupança** | 0,5% a.m. + TR | ~7,9% | (rendimento abaixo da inflação real) |

**Juros real (Selic − IPCA 12m):** ~9,5% a.a. (alto historicamente)

> 📡 *Valores acima são cache. Para dados ao vivo, ver seção 0 — Protocolo de Dados ao Vivo.*

---

## 2. TAXAS DE JUROS MÉDIAS POR MODALIDADE (BCB)

| Modalidade | Taxa Mensal | Taxa Anual | Classificação |
|-----------|-------------|------------|---------------|
| **Rotativo do cartão de crédito** | ~36,5% | ~438% | 🔴 CRÍTICA — quitar imediatamente |
| **Cartão parcelado** | ~15,8% | ~189% | 🔴 ALTA |
| **Cheque especial** | ~10,8% | ~136% | 🔴 ALTA |
| **Crédito pessoal não consignado** | ~9,7% | ~117% | 🟡 MÉDIA |
| **CDC (financiamento bens)** | ~3,2% | ~46% | 🟡 MÉDIA |
| **Financiamento de veículos** | ~2,6% | ~36% | 🟡 BAIXA-MÉDIA |
| **Crédito consignado privado** | ~3,6% | ~52% | 🟡 MÉDIA |
| **Crédito consignado público** | ~2,2% | ~26% | 🟢 BAIXA |
| **Financiamento imobiliário (SBPE)** | ~0,9% | ~11% | 🟢 BAIXA |
| **Crédito rural** | ~0,7% | ~8,5% | 🟢 BAIXA |

**Regra de ouro:** Qualquer dívida com taxa **> Selic** está destruindo patrimônio. Priorizar quitação dessas dívidas antes de qualquer investimento.

---

## 3. TRIBUTAÇÃO PESSOA FÍSICA

### 3.1 IR sobre Renda do Trabalho (vigente em 2026)

| Faixa Mensal | Alíquota | Parcela a Deduzir |
|--------------|----------|-------------------|
| Até R$ 2.428,80 | Isento | — |
| De R$ 2.428,81 a R$ 2.826,65 | 7,5% | R$ 182,16 |
| De R$ 2.826,66 a R$ 3.751,05 | 15% | R$ 394,16 |
| De R$ 3.751,06 a R$ 4.664,68 | 22,5% | R$ 675,49 |
| Acima de R$ 4.664,68 | 27,5% | R$ 908,73 |

**Desconto simplificado:** R$ 564,80/mês (substitui deduções).
**Faixa de isenção 2026:** R$ 2.428,80 (proposta de R$ 5.000 ainda em tramitação).

### 3.2 IR sobre Investimentos — Tabela Regressiva

**Renda Fixa, Fundos, Tesouro Direto:**

| Prazo da Aplicação | Alíquota IR |
|--------------------|-------------|
| Até 180 dias | 22,5% |
| De 181 a 360 dias | 20% |
| De 361 a 720 dias | 17,5% |
| Acima de 720 dias | 15% |

**Renda Variável (ações):**
- 15% sobre ganho de capital em operações comuns
- 20% em day-trade
- **Isenção:** vendas de ações até R$ 20.000/mês

**Fundos Imobiliários (FII):**
- 20% sobre ganho de capital
- **Isenção sobre dividendos** (rendimentos mensais)

**Isentos:**
- Caderneta de poupança
- LCI / LCA (Letras de Crédito Imobiliário/Agronegócio)
- CRI / CRA
- Debêntures incentivadas
- Dividendos de ações (até reforma)

### 3.3 IOF (Imposto sobre Operações Financeiras)

- **Câmbio (compra de moeda):** 1,1% (até 2027 conforme cronograma)
- **Empréstimos PF:** 0,38% + 0,0082% ao dia (limite 365 dias)
- **Resgate de fundos antes de 30 dias:** alíquota regressiva (96% → 0%)

---

## 4. PREVIDÊNCIA — INSS

### 4.1 Faixas de Contribuição Empregado/CLT (2026)

| Salário de Contribuição | Alíquota Efetiva |
|-------------------------|-----------------|
| Até R$ 1.518,00 | 7,5% |
| De R$ 1.518,01 a R$ 2.793,88 | 9% |
| De R$ 2.793,89 a R$ 4.190,83 | 12% |
| De R$ 4.190,84 a R$ 8.157,41 | 14% |

**Teto INSS 2026:** R$ 8.157,41 (contribuição máxima ~R$ 951,63/mês)

### 4.2 Contribuição Autônomo / MEI / PJ

- **MEI:** R$ 75,90/mês (5% salário mínimo) + ICMS (R$ 1) ou ISS (R$ 5)
- **Plano Simplificado (autônomo):** 11% sobre 1 salário mínimo = R$ 167,00/mês
- **Plano Normal:** 20% sobre o valor declarado (entre 1 SM e teto)
- **Pró-labore (sócio):** 11% sobre o valor (com teto)

---

## 5. GARANTIAS DO SISTEMA FINANCEIRO (FGC)

| Cobertura | Limite |
|-----------|--------|
| **Por CPF, por instituição** | R$ 250.000 |
| **Limite global por CPF (4 anos)** | R$ 1.000.000 |
| **Produtos cobertos** | Poupança, CDB, RDB, LCI, LCA, LH, LC, conta corrente |
| **Produtos NÃO cobertos** | Tesouro Direto (garantido pelo Tesouro Nacional), fundos, ações, debêntures, FII |

**Estratégia:** Para valores > R$ 250 mil, distribuir entre instituições diferentes.

---

## 6. TESOURO DIRETO — Títulos Disponíveis

| Título | Indexador | Liquidez | Indicado para |
|--------|-----------|----------|---------------|
| **Tesouro Selic** | 100% Selic | Diária | Reserva de emergência, curto prazo |
| **Tesouro Prefixado** | Taxa fixa | No vencimento (ou marcação a mercado) | Aposta em queda de juros |
| **Tesouro IPCA+** | IPCA + taxa | No vencimento | Médio/longo prazo, proteção inflação |
| **Tesouro RendA+** | IPCA + taxa | Conversão em 240 parcelas | Aposentadoria |
| **Tesouro Educa+** | IPCA + taxa | Conversão em 60 parcelas | Educação dos filhos |

**Custos:** 
- Taxa B3: 0,2% a.a. (sobre valor) — ZERADA para Tesouro Selic até R$ 10.000
- Taxa de custódia da corretora: depende (muitas zeram)
- IR regressivo conforme tabela acima

---

## 7. LEGISLAÇÃO E PROGRAMAS RELEVANTES

### 7.1 Lei 14.690/2023 — Limite de Rotativo
**Em vigor desde:** Janeiro/2024  
**Resumo:** Dívida de cartão de crédito rotativo NÃO pode ultrapassar **2x o valor original**.  
**Aplicação prática:** Se o usuário tem dívida que ultrapassou esse limite, deve contestar com o banco — o excedente é ilegal.

### 7.2 Desenrola Brasil 2.0
**Status 2026:** Programa permanente para renegociação de dívidas com descontos significativos (até 90% em alguns casos).  
**Acesso:** desenrola.gov.br ou Caixa Econômica Federal.  
**Aplicação:** Indicar para usuários com dívidas em atraso ou negativados.

### 7.3 Serasa Limpa Nome
**Status:** Programa privado contínuo do Serasa.  
**Acesso:** serasa.com.br/limpa-nome  
**Aplicação:** Negociação direta com credores via plataforma, descontos médios de 50–80%.

### 7.4 Cadastro Positivo
**Status:** Inclusão automática desde 2019.  
**Implicação:** Pagamentos em dia melhoram score; histórico positivo facilita crédito futuro.

### 7.5 PIX — Limites e Custos
- **Pessoa Física:** Sem custos para envio/recebimento.
- **Limites:** Definidos pela instituição. Padrão noturno (20h–6h): R$ 1.000.
- **Pix Saque/Troco:** Disponível em estabelecimentos credenciados.

---

## 8. SIMPLES NACIONAL (PJ — relevante para skill `transicao-clt-pj`)

### Anexos e Faixas (vigente 2026)

**Anexo III — Serviços (mais comum para PJ pessoa física):**

| Faixa Faturamento Anual | Alíquota Inicial |
|------------------------|------------------|
| Até R$ 180.000 | 6% |
| De R$ 180.000,01 a R$ 360.000 | 11,2% |
| De R$ 360.000,01 a R$ 720.000 | 13,5% |
| De R$ 720.000,01 a R$ 1.800.000 | 16% |
| De R$ 1.800.000,01 a R$ 3.600.000 | 21% |
| De R$ 3.600.000,01 a R$ 4.800.000 | 33% |

**Anexo V — Serviços com fator R baixo:** Alíquota inicial 15,5% (sobe para 30,5%).

**Fator R:** Folha de pagamento ÷ Receita bruta últimos 12 meses
- Se Fator R **≥ 28%** → tributação Anexo III (mais barato)
- Se Fator R **< 28%** → tributação Anexo V (mais caro)

---

## 9. INDICADORES PARA DECISÕES

### 9.1 Taxa de Equilíbrio "Investir vs. Quitar Dívida"
```
SE taxa_da_dívida (líquida de IR) > Selic_líquida_de_IR:
  AÇÃO = QUITAR DÍVIDA
SENÃO:
  AÇÃO = INVESTIR
```

**Selic líquida 2026:** ~12,5% (após IR 15%) — qualquer dívida com taxa nominal > 12,5% deve ser quitada antes de investir.

### 9.2 Reserva de Emergência — Multiplicador por Perfil

| Perfil Profissional | Meses de Gastos Essenciais |
|--------------------|----------------------------|
| Servidor público estável | 3 meses |
| CLT estável (1+ ano) | 6 meses |
| CLT com instabilidade | 6–9 meses |
| Autônomo / freelancer | 9–12 meses |
| PJ / empreendedor | 12 meses |
| Renda variável (comissão) | 12 meses |

### 9.3 Comprometimento Máximo Saudável

- **Despesas essenciais:** ≤ 50% da renda
- **Parcelas de dívida:** ≤ 30% da renda (limite legal de margem consignável: 35% + 5% cartão)
- **Gastos totais:** ≤ 80% da renda (mínimo 20% para Bloco Futuro)

---

## 10. CONTEXTO ECONÔMICO RELEVANTE (Maio 2026)

- Selic em ciclo de manutenção após picos de 2025
- Inflação cedendo gradualmente, dentro da banda superior da meta
- Mercado de crédito: spreads ainda elevados (custo de capital alto para PF)
- Tesouro IPCA+ longo (2045+) com taxas reais entre 6,5% e 7,5% — historicamente atrativo
- Reforma Tributária do Consumo em implementação progressiva (2026–2033)

---

## 11. FONTES OFICIAIS E ATUALIZAÇÃO

### Fontes a consultar para atualização

| Dado | Fonte Oficial |
|------|---------------|
| Selic, Meta de Inflação | bcb.gov.br |
| Taxas médias por modalidade | bcb.gov.br/estatisticas/historicotaxasjuros |
| IPCA, IGP-M | ibge.gov.br / fgv.br |
| Tabela IR, IOF | gov.br/receitafederal |
| INSS — faixas | gov.br/inss |
| FGC — limites | fgc.org.br |
| Tesouro Direto | tesourodireto.com.br |
| Simples Nacional | gov.br/receitafederal/simples-nacional |
| Desenrola Brasil | desenrola.gov.br |

### Procedimento de atualização (a cada 45 dias — ciclo Copom)

**Automático (recomendado):**
```bash
pip install requests
python update-referencias.py
```
O script atualiza Selic, CDI, IPCA, TR, IGP-M e taxas de crédito direto da API do BCB.

**Manual (para dados não cobertos pelo script):**
1. Tabela IR (seção 3.1): atualizar anualmente — fonte: gov.br/receitafederal
2. Faixas INSS (seção 4.1): atualizar anualmente — fonte: gov.br/inss
3. Simples Nacional (seção 8): atualizar anualmente — fonte: gov.br/receitafederal
4. Contexto econômico (seção 10): atualizar a cada trimestre
5. Atualizar a "Última atualização" e "Próxima revisão" no cabeçalho
6. Se houver mudança regulatória relevante, criar entrada na seção 7

---

## 12. AVISO LEGAL

Este arquivo é **referência educacional** atualizada periodicamente. Não constitui:
- Recomendação fiscal (consultar contador)
- Recomendação de investimento (consultar CFP/CNPI)
- Aconselhamento jurídico (consultar advogado)

Para decisões com impacto financeiro material, sempre validar com fontes oficiais e profissionais habilitados.

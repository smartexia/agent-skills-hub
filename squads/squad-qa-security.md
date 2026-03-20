# 🛡️ Squad QA & Security

> **Missão**: Garantir qualidade, confiabilidade e segurança em todos os sistemas — desde testes automatizados até auditorias de segurança e compliance. Este squad opera como o guardião da qualidade do produto.

---

## 👥 Composição do Time

### QA & Testes

| Papel | Agente | Arquivo |
|-------|--------|---------|
| 📸 **Evidence Collector** | Evidence Collector | [testing-evidence-collector.md](../testing/testing-evidence-collector.md) |
| 🔍 **Reality Checker** | Reality Checker | [testing-reality-checker.md](../testing/testing-reality-checker.md) |
| 📊 **Test Results Analyzer** | Test Results Analyzer | [testing-test-results-analyzer.md](../testing/testing-test-results-analyzer.md) |
| ⚡ **Performance Benchmarker** | Performance Benchmarker | [testing-performance-benchmarker.md](../testing/testing-performance-benchmarker.md) |
| 🔌 **API Tester** | API Tester | [testing-api-tester.md](../testing/testing-api-tester.md) |
| ♿ **Accessibility Auditor** | Accessibility Auditor | [testing-accessibility-auditor.md](../testing/testing-accessibility-auditor.md) |
| 🔧 **Workflow Optimizer** | Workflow Optimizer | [testing-workflow-optimizer.md](../testing/testing-workflow-optimizer.md) |
| 🧰 **Tool Evaluator** | Tool Evaluator | [testing-tool-evaluator.md](../testing/testing-tool-evaluator.md) |

### Segurança

| Papel | Agente | Arquivo |
|-------|--------|---------|
| 🔒 **Security Engineer** | Security Engineer | [engineering-security-engineer.md](../engineering/engineering-security-engineer.md) |
| 🚨 **Threat Detection** | Threat Detection Engineer | [engineering-threat-detection.md](../engineering/engineering-threat-detection.md) |
| 📋 **Compliance Auditor** | Compliance Auditor | [compliance-auditor.md](../specialized/compliance-auditor.md) |
| ⛓️ **Blockchain Security** | Blockchain Security Auditor | [blockchain-security-auditor.md](../specialized/blockchain-security-auditor.md) |

---

## 🔄 Workflow do Squad

```
┌──────────────────────────────────────────────────────────────────┐
│                  SQUAD QA & SECURITY - WORKFLOW                   │
│                                                                   │
│  FASE 1: PLANEJAMENTO DE QUALIDADE                               │
│  ├── Workflow Optimizer → Estratégia de testes + test plan       │
│  ├── Tool Evaluator → Seleção de ferramentas e frameworks        │
│  ├── Security Engineer → Threat modeling + security requirements │
│  └── Compliance Auditor → Requisitos de compliance (GDPR, SOC2)  │
│                                                                   │
│  FASE 2: TESTES FUNCIONAIS & DE INTEGRAÇÃO                       │
│  ├── Evidence Collector → Execução de testes + evidências        │
│  ├── API Tester → Testes de endpoints (contrato + carga)         │
│  ├── Reality Checker → Validação de comportamento real           │
│  └── Accessibility Auditor → Auditoria WCAG                      │
│                                                                   │
│  FASE 3: TESTES NÃO-FUNCIONAIS & SEGURANÇA                       │
│  ├── Performance Benchmarker → Load tests + profiling            │
│  ├── Security Engineer → SAST, DAST e pen testing                │
│  ├── Threat Detection → Análise de vulnerabilidades              │
│  └── Blockchain Security → Auditoria de contratos inteligentes   │
│                                                                   │
│  FASE 4: ANÁLISE & GATE DE QUALIDADE                             │
│  ├── Test Results Analyzer → Análise de resultados + cobertura   │
│  ├── Reality Checker → Gate de aprovação (go/no-go)              │
│  ├── Compliance Auditor → Certificação de conformidade           │
│  └── Workflow Optimizer → Retrospectiva + melhorias no processo  │
│                                                                   │
│  ◆ Bug Loop: Encontrar → Reportar → Corrigir → Validar          │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Skills Recomendadas

### Segurança
- `security-audit` — Auditoria de segurança
- `security-auditor` — Auditor de segurança
- `pentest-checklist` — Checklist de pentest
- `burp-suite-testing` — Burp Suite
- `web-security-testing` — Testes de segurança web
- `api-security-testing` — Segurança de APIs
- `sast-configuration` — SAST
- `vulnerability-scanner` — Scanner de vulnerabilidades

### Testes & QA
- `e2e-testing` — Testes end-to-end
- `playwright-skill` — Playwright
- `testing-qa` — QA geral
- `testing-patterns` — Padrões de teste
- `tdd-workflow` — TDD
- `code-review-checklist` — Checklist de code review
- `code-review-excellence` — Excelência em code review

---

## 💡 Exemplo de Ativação

```
Ative o Squad de QA & Security. Preciso fazer uma auditoria completa
de qualidade e segurança antes do lançamento de um sistema de
pagamentos.

Comece pela Fase 1: o Security Engineer deve fazer o threat modeling
do sistema, o Workflow Optimizer deve criar o plano de testes e o
Compliance Auditor deve mapear os requisitos de PCI-DSS e LGPD que
precisamos atender.
```

---

## 📊 Métricas de Sucesso

| Métrica | Target |
|---------|--------|
| Test coverage | > 80% |
| Critical bugs escapados para prod | 0 |
| Vulnerabilidades críticas | 0 ao lançar |
| API response time (P95) | < 200ms |
| WCAG compliance | Nível AA |
| Pen test findings resolvidos | 100% dos críticos/altos |

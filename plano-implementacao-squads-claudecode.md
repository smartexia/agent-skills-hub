# 🏢 Sistema de Squads — Plano de Implementação

Organizar os agentes e skills existentes do projeto em **Squads** prontos para uso — times completos com papéis definidos que podem ser ativados para resolver missões específicas.

## Contexto do Projeto

O projeto possui:
- **10+ divisões de agentes**: Engineering, Design, Marketing, Product, Project Management, Testing, Support, Sales, Specialized, Spatial Computing, Game Dev, Academic
- **1254+ skills** na pasta `skills/`
- **NEXUS Strategy** (orquestração multi-agente por fases)
- Nenhum sistema de Squads existe atualmente

## Proposed Changes

### Squads Directory

#### [NEW] [squads/](file:///d:/Github-Bernardo-Projetos/agency-agents-main/squads/)
Nova pasta raiz para todos os squads.

#### [NEW] [README.md](file:///d:/Github-Bernardo-Projetos/agency-agents-main/squads/README.md)
Índice principal dos Squads com visão geral, navegação e instrução de uso.

---

### Os 8 Squads

#### [NEW] [squad-tech-development.md](file:///d:/Github-Bernardo-Projetos/agency-agents-main/squads/squad-tech-development.md)
**🖥️ Squad Tecnologia & Desenvolvimento de Software**
Time completo para construir um sistema do zero.

| Papel | Agente | Divisão |
|-------|--------|---------|
| Product Owner | Product Manager | Product |
| Scrum Master / PM | Senior Project Manager | Project Management |
| Analista de Requisitos / Technical Writer | Technical Writer | Engineering |
| Arquiteto de Software | Software Architect + Backend Architect | Engineering |
| Desenvolvedor Frontend | Frontend Developer | Engineering |
| Desenvolvedor Backend | Backend Architect + Senior Developer | Engineering |
| Desenvolvedor Mobile | Mobile App Builder | Engineering |
| UI/UX Designer | UI Designer + UX Architect | Design |
| QA / Tester | Evidence Collector + Reality Checker + API Tester | Testing |
| DevOps | DevOps Automator | Engineering |
| Security | Security Engineer | Engineering |
| DBA | Database Optimizer | Engineering |

**Skills recomendadas**: `architecture`, `react-best-practices`, `nextjs-best-practices`, `fastapi-pro`, `docker-expert`, `postgresql`, `testing-patterns`, `code-review-excellence`, `git-advanced-workflows`, `deployment-procedures`, `clean-code`, `tdd-workflow`, `api-design-principles`, `database-design`, `typescript-pro`, `python-pro`

---

#### [NEW] [squad-marketing-growth.md](file:///d:/Github-Bernardo-Projetos/agency-agents-main/squads/squad-marketing-growth.md)
**📢 Squad Marketing & Growth**
Time completo para campanhas multi-canal e crescimento.

| Papel | Agente | Divisão |
|-------|--------|---------|
| Estrategista de Growth | Growth Hacker | Marketing |
| Content Creator | Content Creator | Marketing |
| SEO Specialist | SEO Specialist | Marketing |
| Social Media Manager | Social Media Strategist | Marketing |
| Twitter/X Specialist | Twitter Engager | Marketing |
| Instagram Specialist | Instagram Curator | Marketing |
| TikTok Specialist | TikTok Strategist | Marketing |
| LinkedIn Specialist | LinkedIn Content Creator | Marketing |
| Community Builder | Reddit Community Builder | Marketing |
| Analytics | Analytics Reporter | Support |
| Copywriter | Book Co-Author | Marketing |
| Brand Guardian | Brand Guardian | Design |

**Skills recomendadas**: `seo-fundamentals`, `seo-content-writer`, `seo-keyword-strategist`, `content-creator`, `copywriting`, `social-content`, `instagram`, `growth-engine`, `analytics-tracking`, `brand-guidelines`, `marketing-ideas`, `marketing-psychology`, `competitive-landscape`, `programmatic-seo`

---

#### [NEW] [squad-design-ux.md](file:///d:/Github-Bernardo-Projetos/agency-agents-main/squads/squad-design-ux.md)
**🎨 Squad Design & UX**
Time completo para design de produto, pesquisa e identidade visual.

| Papel | Agente | Divisão |
|-------|--------|---------|
| UI Designer Lead | UI Designer | Design |
| UX Researcher | UX Researcher | Design |
| UX Architect | UX Architect | Design |
| Brand Guardian | Brand Guardian | Design |
| Visual Storyteller | Visual Storyteller | Design |
| Whimsy/Delight | Whimsy Injector | Design |
| Image/AI Art | Image Prompt Engineer | Design |
| Inclusive Design | Inclusive Visuals Specialist | Design |
| Frontend (Prototipação) | Frontend Developer | Engineering |
| Product Manager | Product Manager | Product |

**Skills recomendadas**: `ui-ux-pro-max`, `product-design`, `frontend-design`, `mobile-design`, `design-spells`, `canvas-design`, `tailwind-design-system`, `shadcn`, `radix-ui-design-system`, `baseline-ui`, `web-design-guidelines`, `accessibility-compliance-accessibility-audit`

---

#### [NEW] [squad-sales.md](file:///d:/Github-Bernardo-Projetos/agency-agents-main/squads/squad-sales.md)
**💼 Squad Vendas (Sales)**
Time completo para pipeline de vendas B2B/B2C.

| Papel | Agente | Divisão |
|-------|--------|---------|
| Outbound Strategist | Outbound Strategist | Sales |
| Discovery Coach | Discovery Coach | Sales |
| Deal Strategist | Deal Strategist | Sales |
| Sales Engineer | Sales Engineer | Sales |
| Proposal Strategist | Proposal Strategist | Sales |
| Pipeline Analyst | Pipeline Analyst | Sales |
| Account Strategist | Account Strategist | Sales |
| Sales Coach | Sales Coach | Sales |
| CRM/Data Support | Sales Data Extraction Agent | Specialized |
| Analytics | Analytics Reporter | Support |

**Skills recomendadas**: `sales-automator`, `hubspot-integration`, `salesforce-development`, `pipedrive-automation`, `email-sequence`, `competitor-alternatives`, `pricing-strategy`, `business-analyst`

---

#### [NEW] [squad-management-ops.md](file:///d:/Github-Bernardo-Projetos/agency-agents-main/squads/squad-management-ops.md)
**📋 Squad Gestão & Operações**
Time completo para gestão, compliance e operações.

| Papel | Agente | Divisão |
|-------|--------|---------|
| Studio Producer | Studio Producer | Project Management |
| Project Shepherd | Project Shepherd | Project Management |
| Senior Project Manager | Senior Project Manager | Project Management |
| Studio Operations | Studio Operations | Project Management |
| Experiment Tracker | Experiment Tracker | Project Management |
| Finance Tracker | Finance Tracker | Support |
| Legal Compliance | Legal Compliance Checker | Support |
| Executive Summary | Executive Summary Generator | Support |
| Support Responder | Support Responder | Support |
| Infrastructure | Infrastructure Maintainer | Support |
| Workflow Architect | Workflow Architect | Specialized |

**Skills recomendadas**: `project-development`, `product-manager-toolkit`, `workflow-automation`, `workflow-patterns`, `jira-automation`, `asana-automation`, `notion-automation`, `linear`, `trello-automation`, `documentation`, `kpi-dashboard-design`

---

#### [NEW] [squad-qa-security.md](file:///d:/Github-Bernardo-Projetos/agency-agents-main/squads/squad-qa-security.md)
**🛡️ Squad QA & Security**
Time completo para qualidade, testes e segurança.

| Papel | Agente | Divisão |
|-------|--------|---------|
| Evidence Collector | Evidence Collector | Testing |
| Reality Checker | Reality Checker | Testing |
| Test Results Analyzer | Test Results Analyzer | Testing |
| Performance Benchmarker | Performance Benchmarker | Testing |
| API Tester | API Tester | Testing |
| Accessibility Auditor | Accessibility Auditor | Testing |
| Workflow Optimizer | Workflow Optimizer | Testing |
| Tool Evaluator | Tool Evaluator | Testing |
| Security Engineer | Security Engineer | Engineering |
| Threat Detection | Threat Detection Engineer | Engineering |
| Compliance Auditor | Compliance Auditor | Specialized |
| Blockchain Security | Blockchain Security Auditor | Specialized |

**Skills recomendadas**: `security-audit`, `security-auditor`, `pentest-checklist`, `burp-suite-testing`, `web-security-testing`, `api-security-testing`, `e2e-testing`, `playwright-skill`, `testing-qa`, `code-review-checklist`, `sast-configuration`, `vulnerability-scanner`

---

#### [NEW] [squad-data-ai.md](file:///d:/Github-Bernardo-Projetos/agency-agents-main/squads/squad-data-ai.md)
**🤖 Squad Data & AI**
Time completo para dados, ML e inteligência artificial.

| Papel | Agente | Divisão |
|-------|--------|---------|
| AI Engineer | AI Engineer | Engineering |
| Data Engineer | Data Engineer | Engineering |
| Data Remediation | AI Data Remediation Engineer | Engineering |
| ML Model QA | Model QA Specialist | Specialized |
| Analytics Reporter | Analytics Reporter | Support |
| Data Consolidation | Data Consolidation Agent | Specialized |
| Trend Researcher | Trend Researcher | Product |
| Backend Architect | Backend Architect | Engineering |
| DevOps | DevOps Automator | Engineering |

**Skills recomendadas**: `ai-ml`, `ai-engineer`, `data-engineer`, `data-scientist`, `ml-engineer`, `rag-implementation`, `rag-engineer`, `embedding-strategies`, `llm-ops`, `llm-evaluation`, `vector-database-engineer`, `data-quality-frameworks`, `spark-optimization`, `polars`, `scikit-learn`

---

#### [NEW] [squad-game-dev.md](file:///d:/Github-Bernardo-Projetos/agency-agents-main/squads/squad-game-dev.md)
**🎮 Squad Game Development**
Time completo para desenvolvimento de jogos.

| Papel | Agente | Divisão |
|-------|--------|---------|
| Game Designer | Game Designer | Game Dev |
| Level Designer | Level Designer | Game Dev |
| Technical Artist | Technical Artist | Game Dev |
| Audio Engineer | Game Audio Engineer | Game Dev |
| Narrative Designer | Narrative Designer | Game Dev |
| Unity/Unreal/Godot Engineers | (Engine-specific agents) | Game Dev |
| 3D/Blender | Blender Addon Engineer | Game Dev |
| UI Designer | UI Designer | Design |
| QA | Evidence Collector | Testing |
| DevOps | DevOps Automator | Engineering |

**Skills recomendadas**: `game-development`, `unity-developer`, `unity-ecs-patterns`, `unreal-engine-cpp-pro`, `godot-gdscript-patterns`, `threejs-fundamentals`, `shader-programming-glsl`, `algorithmic-art`

---

### README do Projeto

#### [MODIFY] [README.md](file:///d:/Github-Bernardo-Projetos/agency-agents-main/README.md)
Adicionar seção sobre Squads no README principal do projeto, depois da seção "Real-World Use Cases".

## Verification Plan

### Manual Verification
- Verificar que cada agente referenciado nos squads existe no arquivo correto do projeto
- Verificar que cada skill recomendada existe como pasta em `skills/`
- Abrir os arquivos criados e ler para confirmar formatação e conteúdo

> [!NOTE]
> Este projeto é uma coleção de arquivos Markdown, não há código executável ou testes automatizados para rodar. A verificação é feita por revisão manual dos arquivos criados.

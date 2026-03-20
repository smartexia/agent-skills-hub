# 🏢 Squads — Times Prontos para Missão

> **Squads** são composições pré-definidas de agentes e skills organizados como times completos. Cada squad é otimizado para um tipo de missão — basta ativar o squad certo e começar a trabalhar.

---

## Como Usar

### Com Claude Code CLI

```bash
# Ative um squad inteiro no início da sessão
cat squads/squad-tech-development.md | claude --print

# Ou referencie durante a conversa
"Ative o Squad de Tecnologia e me ajude a criar um sistema de e-commerce do zero"
```

### Com Antigravity / Gemini

```
Leia o arquivo squads/squad-tech-development.md e assuma os papéis descritos para me ajudar a desenvolver um sistema.
```

### Princípio: Composição > Divisão

- **Divisões** (pastas `engineering/`, `marketing/`, etc.) = agentes individuais por área
- **Squads** = times completos com agentes de múltiplas divisões trabalhando juntos
- **NEXUS** (`strategy/nexus-strategy.md`) = orquestração completa do pipeline multi-agente

---

## 📋 Squads Disponíveis

| Squad | Missão | Arquivo |
|-------|--------|---------|
| 🖥️ [Tech & Development](squad-tech-development.md) | Construir sistemas de software do zero | `squad-tech-development.md` |
| 📢 [Marketing & Growth](squad-marketing-growth.md) | Campanhas multi-canal e crescimento | `squad-marketing-growth.md` |
| 🎨 [Design & UX](squad-design-ux.md) | Design de produto e identidade visual | `squad-design-ux.md` |
| 💼 [Sales](squad-sales.md) | Pipeline de vendas B2B/B2C | `squad-sales.md` |
| 📋 [Gestão & Operações](squad-management-ops.md) | Gestão de projetos e operações | `squad-management-ops.md` |
| 🛡️ [QA & Security](squad-qa-security.md) | Qualidade, testes e segurança | `squad-qa-security.md` |
| 🤖 [Data & AI](squad-data-ai.md) | Dados, ML e inteligência artificial | `squad-data-ai.md` |
| 🎮 [Game Development](squad-game-dev.md) | Desenvolvimento de jogos | `squad-game-dev.md` |

---

## 🔗 Relacionamento com NEXUS

Os Squads são **subconjuntos táticos** do sistema NEXUS. Enquanto NEXUS orquestra o ciclo completo (Discovery → Strategy → Scaffold → Build → Harden → Launch → Operate), cada Squad foca numa missão específica com autonomia.

Use NEXUS quando precisar do pipeline completo. Use Squads quando precisar de um time focado.

---

## 🆕 Criando Novos Squads

Para criar um novo squad, siga o template:

1. Crie um arquivo `squad-[nome].md` nesta pasta
2. Defina a missão, composição do time (agentes + divisões), workflow e skills recomendadas
3. Use agentes das divisões existentes e skills da pasta `skills/`
4. Adicione à tabela acima

# 🎮 Squad Game Development

> **Missão**: Desenvolver jogos completos — desde o concept e game design até o build final e lançamento. Este squad opera como um estúdio de jogos independente com todas as disciplinas necessárias.

---

## 👥 Composição do Time

### Design & Criação

| Papel | Agente | Arquivo |
|-------|--------|---------|
| 🎮 **Game Designer** | Game Designer | [game-designer.md](../game-development/game-designer.md) |
| 🗺️ **Level Designer** | Level Designer | [level-designer.md](../game-development/level-designer.md) |
| 📖 **Narrative Designer** | Narrative Designer | [narrative-designer.md](../game-development/narrative-designer.md) |
| 🎨 **Technical Artist** | Technical Artist | [technical-artist.md](../game-development/technical-artist.md) |
| 🔊 **Audio Engineer** | Game Audio Engineer | [game-audio-engineer.md](../game-development/game-audio-engineer.md) |

### Engenharia & Desenvolvimento

| Papel | Agente | Arquivo |
|-------|--------|---------|
| 🟦 **Unity Engineer** | (Unity agents) | [unity/](../game-development/unity/) |
| 🔵 **Unreal Engineer** | (Unreal agents) | [unreal-engine/](../game-development/unreal-engine/) |
| 🟩 **Godot Engineer** | (Godot agents) | [godot/](../game-development/godot/) |
| 🎲 **Roblox Engineer** | (Roblox agents) | [roblox-studio/](../game-development/roblox-studio/) |
| 🧊 **3D / Blender** | Blender Addon Engineer | [blender/](../game-development/blender/) |

### Suporte & Qualidade

| Papel | Agente | Arquivo |
|-------|--------|---------|
| 🎯 **UI Designer** | UI Designer | [design-ui-designer.md](../design/design-ui-designer.md) |
| 📸 **QA Lead** | Evidence Collector | [testing-evidence-collector.md](../testing/testing-evidence-collector.md) |
| ⚡ **Performance** | Performance Benchmarker | [testing-performance-benchmarker.md](../testing/testing-performance-benchmarker.md) |
| 🚀 **DevOps / Build** | DevOps Automator | [engineering-devops-automator.md](../engineering/engineering-devops-automator.md) |

---

## 🔄 Workflow do Squad

```
┌──────────────────────────────────────────────────────────────────┐
│                SQUAD GAME DEVELOPMENT - WORKFLOW                  │
│                                                                   │
│  FASE 1: PRÉ-PRODUÇÃO (Concept & Design)                         │
│  ├── Game Designer → GDD (Game Design Document) completo         │
│  ├── Narrative Designer → Roteiro, lore e diálogos               │
│  ├── Level Designer → Mapa de fases e progression curve          │
│  ├── Technical Artist → Arte concept + style guide               │
│  └── Audio Engineer → Sound design direction                      │
│                                                                   │
│  FASE 2: PROTOTIPAÇÃO                                            │
│  ├── Game Designer → Core loop prototype (grey-box)              │
│  ├── Engine Engineer → Sistemas básicos (physics, input, camera) │
│  ├── Level Designer → Primeiro nível playable                    │
│  └── Evidence Collector → Playtest sessions + feedback            │
│                                                                   │
│  FASE 3: PRODUÇÃO                                                │
│  ├── Engine Engineers → Implementação dos sistemas               │
│  ├── Technical Artist → Assets 3D/2D + shaders + VFX            │
│  ├── Audio Engineer → Trilha + SFX + implementação               │
│  ├── UI Designer → HUD + menus + UX do jogo                      │
│  ├── Narrative Designer → Cutscenes + voice direction             │
│  └── Level Designer → Construção de todas as fases               │
│                                                                   │
│  FASE 4: POLISH & LANÇAMENTO                                     │
│  ├── Evidence Collector → QA sistemático por plataforma          │
│  ├── Performance Benchmarker → Profiling + otimização            │
│  ├── DevOps Automator → Build pipeline + platform submission     │
│  └── Game Designer → Balance tuning final                        │
│                                                                   │
│  ◆ Ciclo iterativo: Prototype → Playtest → Refine               │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Skills Recomendadas

### Engines & Desenvolvimento
- `game-development` — Desenvolvimento de jogos geral
- `unity-developer` — Unity
- `unity-ecs-patterns` — Unity ECS
- `unreal-engine-cpp-pro` — Unreal Engine + C++
- `godot-gdscript-patterns` — Godot + GDScript

### Gráficos & Renderização
- `shader-programming-glsl` — Shaders GLSL
- `threejs-fundamentals` — Three.js (web games)
- `algorithmic-art` — Arte procedural/algorítmica
- `3d-modeling` — Modelagem 3D

### Web & Distribuição
- `typescript-pro` — TypeScript (web games)
- `docker-expert` — Docker (servidores de jogo)
- `deployment-procedures` — Deploy

---

## 💡 Exemplo de Ativação

```
Ative o Squad de Game Development. Quero criar um jogo de plataforma
2D indie em Godot com temática de pixel art.

Comece pela Fase 1: o Game Designer deve criar o GDD com o core loop,
mecânicas principais e progression system. O Narrative Designer deve
esboçar a história e mundo. O Level Designer deve criar o mapa das
fases e a difficulty curve.
```

---

## 📊 Métricas de Sucesso

| Métrica | Target |
|---------|--------|
| Frame rate (PC) | 60 FPS estável |
| Frame rate (Mobile) | 30-60 FPS estável |
| Crash rate | < 0.1% das sessões |
| Session length (target) | Definido por design |
| Day-1 retention | > 40% |
| Store rating | > 4.0 estrelas |

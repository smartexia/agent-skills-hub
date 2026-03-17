#!/usr/bin/env python3
"""
Gera o index.html da biblioteca de agentes e skills.
Executa: python build_page.py
"""
import os, re, json, base64

AGENTS_BASE  = os.path.dirname(os.path.abspath(__file__))
SKILLS_BASE  = os.path.join(AGENTS_BASE, 'skills')

PROJECT_NAME = "Agent Skills Hub"
PROJECT_LOGO = "⚡"
PROJECT_BADGE = "Open Source · Ready for Coolify"
PROJECT_HERO_TAG = "Deploy-ready · Open Source"

# ── Categorias de Agentes ───────────────────────────────────────────────────
AGENT_CATS = [
    {"id":"academic",           "label":"Academic",           "icon":"🎓"},
    {"id":"design",             "label":"Design",             "icon":"🎨"},
    {"id":"engineering",        "label":"Engineering",        "icon":"⚙️"},
    {"id":"game-development",   "label":"Game Dev",           "icon":"🎮"},
    {"id":"marketing",          "label":"Marketing",          "icon":"📣"},
    {"id":"paid-media",         "label":"Paid Media",         "icon":"💰"},
    {"id":"product",            "label":"Product",            "icon":"🧭"},
    {"id":"project-management", "label":"Project Mgmt",       "icon":"📋"},
    {"id":"sales",              "label":"Sales",              "icon":"🤝"},
    {"id":"spatial-computing",  "label":"Spatial Computing",  "icon":"🥽"},
    {"id":"specialized",        "label":"Specialized",        "icon":"⭐"},
    {"id":"support",            "label":"Support",            "icon":"🛟"},
    {"id":"testing",            "label":"Testing",            "icon":"🧪"},
]

# ── Auto-categorização de Skills por keywords no nome/id ───────────────────
SKILL_CAT_RULES = [
    ("🤖 AI & Agents",       ["agent","ai-","llm","rag","embedding","langchain","crewai","autogen","openai","anthropic","gemini","ollama","hugging","vector","mcp-"]),
    ("⚙️ Engineering",       ["backend","api-","architecture","microservice","database","sql","postgres","mongo","redis","kafka","graphql","grpc","rest","websocket","docker","kubernetes","devops","ci-cd","pipeline","terraform","aws","gcp","azure","cloud","serverless","supabase"]),
    ("🖥️ Frontend",          ["react","vue","angular","svelte","nextjs","nuxt","typescript","javascript","css","tailwind","ui-","ux-","frontend","web-","html","component","animation","three.js","webgl"]),
    ("📱 Mobile",            ["android","ios","flutter","react-native","swift","kotlin","mobile"]),
    ("🔒 Security",          ["security","pentest","exploit","vulnerability","ctf","malware","reverse","forensic","crypto","auth","oauth","jwt","firewall","injection","xss","sqli","threat","incident","siem","soc","red-team","blue-team","attack","defense","owasp"]),
    ("🎮 Game Dev",          ["game","unity","unreal","godot","level-design","narrative","shader","vfx","audio-engine","blender"]),
    ("📊 Data & Analytics",  ["data-","analytics","dashboard","bi-","tableau","powerbi","snowflake","dbt","spark","airflow","etl","ml-","machine-learning","model","dataset","pandas","numpy","jupyter","visualization"]),
    ("📣 Marketing & SEO",   ["seo","marketing","content-","social","tiktok","instagram","linkedin","twitter","email","copywriting","brand","growth","conversion","funnel","ads","campaign","influencer"]),
    ("🧪 Testing & QA",      ["test","qa-","quality","e2e","playwright","cypress","jest","pytest","selenium","accessibility","a11y","performance-test","load-test","benchmark"]),
    ("🛠️ DevTools",          ["git","github","gitlab","ci","cd","lint","prettier","eslint","webpack","vite","build","deploy","monitoring","logging","tracing","observability","debugg","profil"]),
    ("📝 Docs & Writing",    ["documentation","docs","readme","api-doc","technical-writ","markdown","openapi","swagger","changelog","spec"]),
    ("🔧 Automation",        ["automation","workflow","n8n","zapier","make","airtable","notion","slack","webhook","cron","scheduler","rpa","script"]),
    ("🏗️ Architecture",      ["architect","design-pattern","ddd","clean-arch","solid","pattern","refactor","review","code-quality"]),
    ("💼 Business & Sales",  ["sales","crm","hubspot","salesforce","proposal","deal","prospect","outbound","lead","revenue","finance","accounting","legal","compliance","hr","recruit"]),
    ("🌐 Web & APIs",        ["scraping","crawler","browser","puppeteer","playwright","fetch","http","webhook","integration","parser"]),
]

def auto_cat_skill(skill_id, skill_desc=''):
    text = (skill_id + ' ' + skill_desc).lower()
    for cat_label, keywords in SKILL_CAT_RULES:
        if any(k in text for k in keywords):
            return cat_label
    return "📦 Other"

def humanize_slug(value):
    cleaned = value.replace('_', ' ').replace('-', ' ').strip()
    return re.sub(r'\s+', ' ', cleaned).title()

def strip_frontmatter(content):
    content = content.strip()
    if content.startswith('---'):
        end = content.find('\n---', 3)
        if end != -1:
            return content[end+4:].strip()
    return content

def parse_frontmatter(content):
    meta = {}
    content = content.strip()
    if not content.startswith('---'):
        return meta
    end = content.find('\n---', 3)
    if end == -1:
        return meta
    fm = content[3:end]
    for line in fm.split('\n'):
        line = line.strip()
        if ':' in line:
            key, _, val = line.partition(':')
            meta[key.strip()] = val.strip().strip('"\'')
    return meta

# ── Carrega Agentes ─────────────────────────────────────────────────────────
def load_agents():
    agents = []
    for cat in AGENT_CATS:
        cat_dir = os.path.join(AGENTS_BASE, cat["id"])
        if not os.path.isdir(cat_dir):
            continue
        for fname in sorted(f for f in os.listdir(cat_dir) if f.endswith('.md')):
            fpath = os.path.join(cat_dir, fname)
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            meta   = parse_frontmatter(content)
            prompt = strip_frontmatter(content)
            agents.append({
                "type":   "agent",
                "cat":    cat["id"],
                "file":   f"{cat['id']}/{fname}",
                "name":   meta.get("name", fname.replace('.md','')),
                "emoji":  meta.get("emoji", "🤖"),
                "vibe":   meta.get("vibe", ""),
                "desc":   meta.get("description", ""),
                "prompt": prompt,
            })
    return agents

# ── Carrega Skills ──────────────────────────────────────────────────────────
def load_skills():
    if not os.path.isdir(SKILLS_BASE):
        print(f"[WARN] Pasta de skills nao encontrada em {SKILLS_BASE}")
        return []

    skills = []
    for entry in sorted(os.scandir(SKILLS_BASE), key=lambda e: e.name.lower()):
        if not entry.is_dir():
            continue

        skill_path = os.path.join(entry.path, 'SKILL.md')
        if not os.path.exists(skill_path):
            continue

        with open(skill_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()

        meta = parse_frontmatter(content)
        prompt = strip_frontmatter(content)
        if not prompt.strip():
            continue

        desc = str(meta.get('description', '')).replace('\\n', ' ').strip()
        if not desc or len(desc) < 5:
            for line in prompt.split('\\n'):
                line = line.strip().lstrip('#').strip()
                if len(line) > 20:
                    desc = line[:120]
                    break

        skill_id = entry.name
        cat = auto_cat_skill(skill_id, desc)
        display_name = str(meta.get('name', skill_id))

        skills.append({
            "type":   "skill",
            "id":     skill_id,
            "cat":    cat,
            "file":   f"skills/{entry.name}/SKILL.md",
            "name":   humanize_slug(display_name),
            "raw_id": skill_id,
            "source": str(meta.get('source', 'community')),
            "risk":   str(meta.get('risk', 'unknown')),
            "desc":   desc[:200],
            "prompt": prompt,
        })
    return skills

# ── Gera HTML ────────────────────────────────────────────────────────────────
def build_html(agents, skills):
    agent_cats_with_count = []
    for c in AGENT_CATS:
        cnt = sum(1 for a in agents if a['cat'] == c['id'])
        if cnt:
            agent_cats_with_count.append({**c, "count": cnt})

    skill_cats = {}
    for s in skills:
        skill_cats.setdefault(s['cat'], 0)
        skill_cats[s['cat']] += 1
    skill_cats_list = sorted(skill_cats.items(), key=lambda x: -x[1])

    total_agents = len(agents)
    total_skills  = len(skills)

    def to_b64(obj):
        """Serializa para JSON e codifica em base64 — 100% seguro em <script>."""
        raw = json.dumps(obj, ensure_ascii=False)
        return base64.b64encode(raw.encode('utf-8')).decode('ascii')

    agents_b64    = to_b64(agents)
    skills_b64    = to_b64(skills)
    agent_cats_b64 = to_b64(agent_cats_with_count)
    skill_cats_b64 = to_b64([{"id":k,"label":k,"count":v} for k,v in skill_cats_list if isinstance(k, str)])

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>{PROJECT_NAME} - {total_agents} Agentes | {total_skills} Skills</title>
<style>
:root{{
  --bg:#070c18;--sidebar:#0a1020;--surface:#0e1628;--surface2:#111c33;
  --border:#182540;--border2:#1e3055;
  --blue:#3b82f6;--blue-dim:#1d4ed8;--blue-glow:rgba(59,130,246,.18);
  --orange:#f97316;--orange-glow:rgba(249,115,22,.15);
  --purple:#8b5cf6;--purple-glow:rgba(139,92,246,.15);
  --green:#22c55e;
  --text:#e2e8f0;--muted:#4a6080;--subtext:#7a9ab8;
  --r:10px;--nav-h:56px;--sb-w:252px;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden}}

/* ── TOPBAR ── */
.topbar{{
  position:fixed;top:0;left:0;right:0;z-index:200;height:var(--nav-h);
  background:rgba(7,12,24,.93);backdrop-filter:blur(14px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;gap:10px;padding:0 14px;
}}
.sb-toggle{{width:32px;height:32px;border-radius:7px;background:var(--surface2);border:1px solid var(--border2);color:var(--subtext);cursor:pointer;font-size:.95rem;display:flex;align-items:center;justify-content:center;transition:all .14s;flex-shrink:0}}
.sb-toggle:hover{{color:var(--text);border-color:var(--blue)}}
.logo{{font-size:1.05rem;font-weight:900;white-space:nowrap;background:linear-gradient(90deg,var(--blue),var(--orange));-webkit-background-clip:text;-webkit-text-fill-color:transparent}}

/* TAB SWITCHER */
.tab-switcher{{display:flex;gap:4px;padding:5px;background:var(--surface2);border:1px solid var(--border2);border-radius:10px;flex-shrink:0}}
.tab-btn{{
  padding:5px 16px;border-radius:7px;border:none;cursor:pointer;
  font-size:.8rem;font-weight:700;transition:all .16s;
  background:none;color:var(--muted);display:flex;align-items:center;gap:6px;
}}
.tab-btn.active{{color:#fff}}
.tab-btn.agents.active{{background:var(--blue);box-shadow:0 2px 12px rgba(59,130,246,.4)}}
.tab-btn.skills.active{{background:var(--purple);box-shadow:0 2px 12px rgba(139,92,246,.4)}}
.tab-btn:not(.active):hover{{background:rgba(255,255,255,.05);color:var(--subtext)}}
.tab-pill{{font-size:.65rem;padding:1px 6px;border-radius:8px;font-weight:800}}
.tab-btn.agents .tab-pill{{background:rgba(59,130,246,.2);color:var(--blue)}}
.tab-btn.agents.active .tab-pill{{background:rgba(255,255,255,.2);color:#fff}}
.tab-btn.skills .tab-pill{{background:rgba(139,92,246,.2);color:var(--purple)}}
.tab-btn.skills.active .tab-pill{{background:rgba(255,255,255,.2);color:#fff}}

.search-wrap{{flex:1;max-width:380px;margin:0 auto;position:relative}}
.search-wrap input{{width:100%;background:var(--surface2);border:1px solid var(--border2);border-radius:8px;color:var(--text);font-size:.85rem;padding:7px 36px 7px 32px;outline:none;transition:border-color .15s}}
.search-wrap input:focus{{border-color:var(--blue)}}
.search-wrap input::placeholder{{color:var(--muted)}}
.s-icon{{position:absolute;left:10px;top:50%;transform:translateY(-50%);color:var(--muted);font-size:.82rem;pointer-events:none}}
.s-kbd{{position:absolute;right:8px;top:50%;transform:translateY(-50%);background:var(--surface);border:1px solid var(--border2);border-radius:4px;padding:1px 5px;font-size:.62rem;color:var(--muted);pointer-events:none}}
.badge{{background:var(--orange-glow);border:1px solid rgba(249,115,22,.3);color:var(--orange);font-size:.72rem;font-weight:700;padding:3px 10px;border-radius:20px;white-space:nowrap;margin-left:auto}}

/* ── LAYOUT ── */
.layout{{display:flex;padding-top:var(--nav-h);min-height:100vh}}

/* ── SIDEBAR ── */
.sidebar{{
  position:fixed;top:var(--nav-h);left:0;bottom:0;width:var(--sb-w);
  background:var(--sidebar);border-right:1px solid var(--border);
  overflow-y:auto;overflow-x:hidden;
  transition:transform .25s cubic-bezier(.4,0,.2,1);z-index:100;
  display:flex;flex-direction:column;
}}
.sidebar.collapsed{{transform:translateX(calc(-1 * var(--sb-w)))}}
.sb-search{{padding:10px 10px 6px}}
.sb-search input{{width:100%;background:var(--surface2);border:1px solid var(--border2);border-radius:7px;color:var(--text);font-size:.78rem;padding:5px 10px;outline:none;transition:border-color .14s}}
.sb-search input:focus{{border-color:var(--blue)}}
.sb-search input::placeholder{{color:var(--muted)}}
.sb-all{{
  margin:0 10px 4px;display:flex;align-items:center;gap:7px;
  padding:7px 10px;border-radius:7px;cursor:pointer;
  background:none;border:none;color:var(--subtext);
  font-size:.8rem;font-weight:600;width:calc(100% - 20px);text-align:left;transition:all .14s;
}}
.sb-all:hover,.sb-all.active{{background:var(--blue-glow);color:var(--blue)}}
.sb-all-c{{margin-left:auto;font-size:.68rem;font-weight:700;background:rgba(59,130,246,.12);color:var(--blue);padding:1px 6px;border-radius:9px}}
.sb-div{{height:1px;background:var(--border);margin:3px 10px 6px}}
.sb-lbl{{font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);padding:0 12px 5px}}
.sb-cat-btn{{
  display:flex;align-items:center;gap:7px;padding:5px 10px;
  cursor:pointer;background:none;border:none;
  color:var(--subtext);font-size:.78rem;font-weight:700;
  width:100%;text-align:left;transition:all .13s;
}}
.sb-cat-btn:hover{{color:var(--text);background:rgba(255,255,255,.025)}}
.sb-cat-btn.active-cat{{color:var(--orange)}}
.sb-cat-icon{{font-size:.9rem;flex-shrink:0}}
.sb-cat-name{{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.sb-cat-cnt{{font-size:.65rem;font-weight:700;flex-shrink:0;background:var(--surface2);color:var(--muted);padding:1px 6px;border-radius:9px;transition:all .13s}}
.sb-cat-btn.active-cat .sb-cat-cnt{{background:var(--orange-glow);color:var(--orange)}}
.sb-caret{{font-size:.58rem;flex-shrink:0;transition:transform .18s}}
.sb-cat-btn.open .sb-caret{{transform:rotate(90deg)}}
.sb-items{{overflow:hidden;max-height:0;transition:max-height .28s cubic-bezier(.4,0,.2,1)}}
.sb-items.open{{max-height:4000px}}
.sb-item{{
  display:flex;align-items:center;gap:6px;padding:4px 10px 4px 26px;
  cursor:pointer;font-size:.74rem;color:var(--subtext);
  transition:all .11s;border-left:2px solid transparent;
  white-space:nowrap;overflow:hidden;
}}
.sb-item:hover{{color:var(--text);background:rgba(255,255,255,.025)}}
.sb-item.sel{{color:var(--blue);border-left-color:var(--blue);background:var(--blue-glow)}}
.sb-item-em{{font-size:.82rem;flex-shrink:0}}
.sb-item-name{{overflow:hidden;text-overflow:ellipsis}}
/* skill badge */
.risk-badge{{font-size:.6rem;padding:1px 5px;border-radius:4px;flex-shrink:0;font-weight:700}}
.risk-safe{{background:rgba(34,197,94,.1);color:#22c55e;border:1px solid rgba(34,197,94,.2)}}
.risk-unknown{{background:rgba(249,115,22,.08);color:var(--orange);border:1px solid rgba(249,115,22,.18)}}
.risk-caution{{background:rgba(239,68,68,.1);color:#ef4444;border:1px solid rgba(239,68,68,.2)}}
.sb-footer{{margin-top:auto;padding:10px;border-top:1px solid var(--border);font-size:.7rem;color:var(--muted);text-align:center;line-height:1.6}}
.sb-footer strong{{color:var(--orange)}}
.sidebar::-webkit-scrollbar{{width:3px}}
.sidebar::-webkit-scrollbar-thumb{{background:var(--border2);border-radius:2px}}

/* ── MAIN ── */
.main{{flex:1;margin-left:var(--sb-w);transition:margin-left .25s cubic-bezier(.4,0,.2,1);min-width:0}}
.main.expanded{{margin-left:0}}

/* ── HERO ── */
.hero{{padding:40px 32px 32px;position:relative;overflow:hidden}}
.hero::before{{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 70% 80% at 60% -10%,rgba(59,130,246,.1) 0%,transparent 65%),radial-gradient(ellipse 40% 50% at 90% 50%,rgba(249,115,22,.07) 0%,transparent 60%);pointer-events:none}}
.hero-inner{{max-width:680px;position:relative}}
.hero-tag{{display:inline-flex;align-items:center;gap:6px;background:var(--orange-glow);border:1px solid rgba(249,115,22,.3);color:var(--orange);font-size:.7rem;font-weight:700;padding:4px 12px;border-radius:20px;margin-bottom:12px;text-transform:uppercase;letter-spacing:.06em}}
.hero h1{{font-size:clamp(1.5rem,3vw,2.5rem);font-weight:900;line-height:1.15;margin-bottom:10px}}
.hero h1 em{{font-style:normal;color:var(--orange)}}
.hero p{{color:var(--subtext);font-size:.9rem;line-height:1.75;max-width:540px;margin-bottom:20px}}
.hero-stats{{display:flex;gap:8px;flex-wrap:wrap}}
.stat{{background:var(--surface2);border:1px solid var(--border2);border-radius:8px;padding:7px 14px;display:flex;align-items:center;gap:7px}}
.stat strong{{font-size:1.15rem;color:var(--blue);font-weight:800}}
.stat.s-purple strong{{color:var(--purple)}}
.stat span{{font-size:.78rem;color:var(--subtext)}}

/* ── WHERE TO USE PANEL ── */
.use-panel{{margin:0 32px 28px;background:var(--surface2);border:1px solid var(--border2);border-radius:var(--r);overflow:hidden}}
.use-toggle{{display:flex;align-items:center;gap:8px;padding:12px 18px;cursor:pointer;background:none;border:none;width:100%;text-align:left;color:var(--text);font-size:.88rem;font-weight:700;border-bottom:1px solid transparent;transition:all .14s}}
.use-toggle:hover{{background:rgba(255,255,255,.02)}}
.use-toggle.open{{border-bottom-color:var(--border)}}
.use-lbl{{background:var(--blue-glow);border:1px solid rgba(59,130,246,.3);color:var(--blue);font-size:.65rem;font-weight:700;padding:2px 8px;border-radius:9px;text-transform:uppercase;letter-spacing:.05em}}
.use-arrow{{margin-left:auto;color:var(--muted);font-size:.72rem;transition:transform .2s}}
.use-toggle.open .use-arrow{{transform:rotate(180deg)}}
.use-body{{display:none;padding:18px}}
.use-body.open{{display:block}}

/* 2-column: agents vs skills */
.use-cols{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px}}
@media(max-width:620px){{.use-cols{{grid-template-columns:1fr}}}}
.use-col{{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:16px}}
.use-col-head{{display:flex;align-items:center;gap:8px;margin-bottom:12px;font-size:.85rem;font-weight:800}}
.use-col-head .chip{{padding:3px 10px;border-radius:6px;font-size:.7rem;font-weight:700}}
.chip-blue{{background:var(--blue-glow);border:1px solid rgba(59,130,246,.3);color:var(--blue)}}
.chip-purple{{background:var(--purple-glow);border:1px solid rgba(139,92,246,.3);color:var(--purple)}}
.use-list{{list-style:none;display:flex;flex-direction:column;gap:8px}}
.use-list li{{display:flex;flex-direction:column;gap:3px}}
.use-list li .dest{{font-size:.78rem;font-weight:700;color:var(--text)}}
.use-list li .how{{font-size:.74rem;color:var(--subtext);line-height:1.5}}
.use-list li .code{{font-family:monospace;font-size:.72rem;background:rgba(0,0,0,.3);border:1px solid var(--border);border-radius:4px;padding:3px 7px;color:#7dd3fc;display:inline-block;margin-top:2px}}
.use-diff{{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:14px}}
.use-diff h4{{font-size:.8rem;font-weight:700;color:var(--orange);margin-bottom:10px}}
.diff-row{{display:flex;gap:10px;align-items:flex-start;margin-bottom:8px;font-size:.8rem}}
.diff-row:last-child{{margin-bottom:0}}
.diff-tag{{flex-shrink:0;padding:2px 8px;border-radius:5px;font-size:.68rem;font-weight:800}}
.d-agent{{background:var(--blue-glow);border:1px solid rgba(59,130,246,.3);color:var(--blue)}}
.d-skill{{background:var(--purple-glow);border:1px solid rgba(139,92,246,.3);color:var(--purple)}}
.diff-row p{{color:var(--subtext);line-height:1.55}}
.diff-row strong{{color:var(--text)}}

/* ── SECTION BAR ── */
.section-bar{{display:flex;align-items:center;gap:10px;padding:0 32px 16px}}
.section-bar h2{{font-size:.95rem;font-weight:800;color:var(--subtext)}}
.s-line{{flex:1;height:1px;background:linear-gradient(to right,var(--border2),transparent)}}
.view-toggle{{display:flex;gap:3px}}
.view-btn{{width:28px;height:28px;border-radius:6px;background:var(--surface2);border:1px solid var(--border);color:var(--muted);cursor:pointer;font-size:.8rem;display:flex;align-items:center;justify-content:center;transition:all .13s}}
.view-btn.active,.view-btn:hover{{background:var(--blue-glow);border-color:var(--blue);color:var(--blue)}}

/* ── CONTENT ── */
.content{{padding:0 24px 60px}}
.cat-block{{margin-bottom:40px}}
.cat-block-hdr{{display:flex;align-items:center;gap:9px;margin-bottom:12px;padding-bottom:10px;border-bottom:1px solid var(--border)}}
.cat-block-icon{{width:32px;height:32px;border-radius:8px;background:var(--surface2);border:1px solid var(--border2);display:flex;align-items:center;justify-content:center;font-size:.9rem}}
.cat-block-name{{font-size:.98rem;font-weight:800}}
.cat-block-desc{{font-size:.74rem;color:var(--muted);flex:1}}
.cat-block-cnt{{background:var(--blue-glow);border:1px solid rgba(59,130,246,.2);color:var(--blue);font-size:.7rem;font-weight:700;padding:2px 9px;border-radius:18px}}

/* ── GRID ── */
.grid-v{{display:grid;grid-template-columns:repeat(auto-fill,minmax(265px,1fr));gap:11px}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:16px;cursor:pointer;transition:all .17s;position:relative;overflow:hidden;display:flex;flex-direction:column;gap:9px}}
.card::after{{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--blue),var(--orange));opacity:0;transition:opacity .17s}}
.card:hover{{border-color:var(--border2);transform:translateY(-2px);box-shadow:0 6px 24px rgba(0,0,0,.3)}}
.card:hover::after{{opacity:1}}
.skill-card::after{{background:linear-gradient(90deg,var(--purple),var(--blue))}}
.card-hd{{display:flex;align-items:flex-start;gap:9px}}
.card-em{{font-size:1.4rem;line-height:1;flex-shrink:0;margin-top:1px}}
.card-mt{{flex:1;min-width:0}}
.card-name{{font-size:.88rem;font-weight:700;line-height:1.3;margin-bottom:2px}}
.card-path{{font-size:.64rem;color:var(--muted);font-family:monospace;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.card-desc{{font-size:.76rem;color:var(--subtext);line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}}
.card-vibe{{background:var(--orange-glow);border:1px solid rgba(249,115,22,.18);border-radius:6px;padding:5px 9px;font-size:.71rem;color:var(--orange);font-style:italic;line-height:1.5}}
.card-meta-row{{display:flex;align-items:center;gap:6px}}
.card-source{{font-size:.65rem;color:var(--muted);flex:1}}
.card-actions{{display:flex;gap:5px;margin-top:1px}}
.btn-xs{{flex:1;padding:6px 7px;border-radius:6px;font-size:.71rem;font-weight:700;cursor:pointer;border:none;transition:all .13s;text-align:center}}
.btn-blue{{background:rgba(59,130,246,.12);color:var(--blue);border:1px solid rgba(59,130,246,.25)}}
.btn-blue:hover{{background:rgba(59,130,246,.22)}}
.btn-org{{background:var(--orange-glow);color:var(--orange);border:1px solid rgba(249,115,22,.25)}}
.btn-org:hover{{background:rgba(249,115,22,.25)}}
.btn-pur{{background:var(--purple-glow);color:var(--purple);border:1px solid rgba(139,92,246,.25)}}
.btn-pur:hover{{background:rgba(139,92,246,.3)}}
.btn-ok{{background:rgba(34,197,94,.1);color:#22c55e;border:1px solid rgba(34,197,94,.25)}}

/* ── LIST VIEW ── */
.list-v{{display:flex;flex-direction:column;gap:4px}}
.row{{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:9px 14px;cursor:pointer;transition:all .13s;display:flex;align-items:center;gap:10px}}
.row:hover{{border-color:var(--border2);background:var(--surface2)}}
.row-em{{font-size:1.1rem;flex-shrink:0;width:24px;text-align:center}}
.row-name{{font-size:.83rem;font-weight:700;min-width:170px;flex-shrink:0}}
.row-desc{{font-size:.76rem;color:var(--subtext);flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.row-acts{{display:flex;gap:5px;flex-shrink:0}}

/* ── EMPTY ── */
.empty{{text-align:center;padding:70px 24px;color:var(--muted)}}
.empty .ei{{font-size:3rem;margin-bottom:14px}}

/* ── MODAL ── */
.overlay{{position:fixed;inset:0;background:rgba(0,0,0,.75);backdrop-filter:blur(8px);z-index:300;display:flex;align-items:center;justify-content:center;padding:18px;opacity:0;pointer-events:none;transition:opacity .2s}}
.overlay.open{{opacity:1;pointer-events:all}}
.modal{{background:var(--surface);border:1px solid var(--border2);border-radius:14px;width:100%;max-width:680px;max-height:90vh;overflow-y:auto;transform:scale(.96) translateY(12px);transition:transform .2s;display:flex;flex-direction:column}}
.overlay.open .modal{{transform:scale(1) translateY(0)}}
.modal-hd{{display:flex;align-items:flex-start;gap:12px;padding:20px 22px 14px;border-bottom:1px solid var(--border);position:sticky;top:0;background:var(--surface);z-index:1;border-radius:14px 14px 0 0;flex-shrink:0}}
.modal-em{{font-size:1.9rem;line-height:1;flex-shrink:0}}
.modal-info{{flex:1}}
.modal-name{{font-size:1.2rem;font-weight:800;margin-bottom:3px}}
.modal-cat{{font-size:.76rem;font-weight:600;color:var(--blue)}}
.modal-x{{width:28px;height:28px;border-radius:7px;background:var(--surface2);border:1px solid var(--border);color:var(--subtext);cursor:pointer;font-size:.9rem;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:all .12s}}
.modal-x:hover{{color:var(--text);border-color:var(--muted)}}
.modal-bd{{padding:18px 22px 22px;display:flex;flex-direction:column;gap:14px}}
.modal-vibe{{background:var(--orange-glow);border:1px solid rgba(249,115,22,.2);border-radius:7px;padding:9px 13px;color:var(--orange);font-style:italic;font-size:.86rem;line-height:1.6}}
.modal-desc{{color:var(--subtext);font-size:.88rem;line-height:1.75}}
/* BIG COPY BUTTON */
.copy-main-btn{{
  display:flex;align-items:center;justify-content:center;gap:10px;
  width:100%;padding:13px;border-radius:10px;
  font-size:.92rem;font-weight:800;cursor:pointer;border:none;
  transition:all .17s;letter-spacing:.01em;
}}
.copy-main-btn.agent-btn{{background:linear-gradient(135deg,var(--blue-dim),var(--blue));color:#fff;box-shadow:0 4px 18px rgba(59,130,246,.3)}}
.copy-main-btn.agent-btn:hover{{transform:translateY(-2px);box-shadow:0 6px 26px rgba(59,130,246,.4)}}
.copy-main-btn.skill-btn{{background:linear-gradient(135deg,#6d28d9,var(--purple));color:#fff;box-shadow:0 4px 18px rgba(139,92,246,.3)}}
.copy-main-btn.skill-btn:hover{{transform:translateY(-2px);box-shadow:0 6px 26px rgba(139,92,246,.4)}}
.copy-main-btn.copied{{background:linear-gradient(135deg,#15803d,var(--green));box-shadow:0 4px 18px rgba(34,197,94,.3)}}
.btn-chars{{font-size:.73rem;font-weight:400;opacity:.8}}
/* where to paste info */
.paste-guide{{background:var(--surface2);border:1px solid var(--border2);border-radius:8px;padding:12px 14px}}
.paste-guide h5{{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin-bottom:10px}}
.paste-grid{{display:grid;grid-template-columns:1fr 1fr;gap:8px}}
.paste-item{{background:var(--surface);border:1px solid var(--border);border-radius:7px;padding:9px 11px}}
.paste-item .dest{{font-size:.75rem;font-weight:700;color:var(--text);margin-bottom:3px}}
.paste-item .path{{font-family:monospace;font-size:.7rem;color:#7dd3fc;background:rgba(0,0,0,.3);border:1px solid var(--border);border-radius:4px;padding:2px 6px;display:inline-block}}
/* preview */
.preview-box{{background:rgba(0,0,0,.4);border:1px solid var(--border);border-radius:8px;max-height:260px;overflow-y:auto;position:relative}}
.preview-box pre{{font-family:monospace;font-size:.72rem;color:#a5f3fc;line-height:1.75;padding:12px;white-space:pre-wrap;word-break:break-word}}
.fade-bot{{position:absolute;bottom:0;left:0;right:0;height:36px;background:linear-gradient(to top,rgba(0,0,0,.4),transparent);pointer-events:none;border-radius:0 0 8px 8px}}
.preview-box::-webkit-scrollbar{{width:4px}}
.preview-box::-webkit-scrollbar-thumb{{background:var(--border2)}}
.preview-lbl{{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--muted);margin-bottom:7px;display:flex;justify-content:space-between}}
.file-row{{background:rgba(0,0,0,.3);border:1px solid var(--border);border-radius:7px;padding:9px 12px;display:flex;gap:9px;align-items:center}}
.file-path{{font-family:monospace;font-size:.79rem;color:#67e8f9;flex:1;word-break:break-all}}
.copy-path-btn{{flex-shrink:0;background:var(--blue-glow);border:1px solid rgba(59,130,246,.3);color:var(--blue);padding:4px 11px;border-radius:6px;cursor:pointer;font-size:.72rem;font-weight:700;transition:all .13s}}
.copy-path-btn:hover{{background:rgba(59,130,246,.3)}}
.modal-close-btn{{width:100%;padding:9px;border-radius:8px;font-size:.83rem;font-weight:700;cursor:pointer;border:1px solid var(--border2);background:none;color:var(--subtext);transition:all .14s}}
.modal-close-btn:hover{{background:var(--surface2);color:var(--text)}}
.sec-lbl{{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--muted)}}

/* ── TOAST ── */
.toast{{position:fixed;bottom:26px;right:26px;z-index:400;background:var(--surface2);border:1px solid var(--green);color:var(--green);padding:9px 16px;border-radius:9px;font-size:.83rem;font-weight:600;transform:translateY(14px);opacity:0;transition:all .2s;pointer-events:none}}
.toast.show{{transform:translateY(0);opacity:1}}

/* ── SCROLLBARS ── */
::-webkit-scrollbar{{width:5px;height:5px}}
::-webkit-scrollbar-track{{background:transparent}}
::-webkit-scrollbar-thumb{{background:var(--border2);border-radius:3px}}

@media(max-width:720px){{
  .sidebar{{transform:translateX(calc(-1 * var(--sb-w)))}}
  .sidebar.mobile-open{{transform:translateX(0)}}
  .main{{margin-left:0!important}}
  .hero,.content{{padding-left:16px;padding-right:16px}}
  .use-panel,.section-bar{{margin-left:16px;margin-right:16px}}
  .row-desc{{display:none}}
  .paste-grid{{grid-template-columns:1fr}}
}}
</style>
</head>
<body>

<header class="topbar">
  <button class="sb-toggle" onclick="toggleSidebar()" title="B">☰</button>
  <div class="logo">{PROJECT_LOGO} {PROJECT_NAME}</div>

  <div class="tab-switcher">
    <button class="tab-btn agents active" id="tabAgents" onclick="switchTab('agents')">
      🤖 Agentes <span class="tab-pill">{total_agents}</span>
    </button>
    <button class="tab-btn skills" id="tabSkills" onclick="switchTab('skills')">
      ⚡ Skills <span class="tab-pill">{total_skills}</span>
    </button>
  </div>

  <div class="search-wrap">
    <span class="s-icon">🔍</span>
    <input id="searchMain" type="text" placeholder="Buscar... (Ctrl+K)" oninput="onSearch(this.value)"/>
    <span class="s-kbd">⌘K</span>
  </div>
  <span class="badge" id="mainCount">{total_agents} itens</span>
</header>

<div class="layout">
  <aside class="sidebar" id="sidebar">
    <div class="sb-search">
      <input id="sbSearch" type="text" placeholder="Filtrar..." oninput="onSbSearch(this.value)"/>
    </div>
    <button class="sb-all" id="btnAll" onclick="selectCat('all')">
      <span id="allIcon">🏠</span><span>Todos</span>
      <span class="sb-all-c" id="allCount">{total_agents}</span>
    </button>
    <div class="sb-div"></div>
    <div class="sb-lbl" id="sbLbl">Categorias</div>
    <div id="sbCats"></div>
    <div class="sb-footer"><strong id="sbFooter">{total_agents} agentes</strong><br>{PROJECT_BADGE}</div>
  </aside>

  <main class="main" id="main">
    <section class="hero">
      <div class="hero-inner">
        <div class="hero-tag">{PROJECT_HERO_TAG}</div>
        <h1 id="heroTitle">{total_agents} Agentes de IA<br>prontos para <em>copiar e usar</em></h1>
        <p id="heroDesc">Clique em qualquer agente, copie o prompt completo e cole direto no Claude, ChatGPT, Gemini ou qualquer sistema — sem abrir arquivo nenhum.</p>
        <div class="hero-stats">
          <div class="stat"><strong>{total_agents}</strong><span>Agentes</span></div>
          <div class="stat s-purple"><strong>{total_skills}</strong><span>Skills</span></div>
          <div class="stat"><strong>100%</strong><span>Prompts completos</span></div>
        </div>
      </div>
    </section>

    <!-- WHERE TO USE -->
    <div class="use-panel">
      <button class="use-toggle" id="useToggle" onclick="toggleUse()">
        <span>📍</span>
        <span>Onde colar o prompt — Agentes vs Skills</span>
        <span class="use-lbl">Tutorial</span>
        <span class="use-arrow">▼</span>
      </button>
      <div class="use-body" id="useBody">
        <div class="use-diff" style="margin-bottom:14px">
          <h4>🤔 Qual a diferença?</h4>
          <div class="diff-row"><span class="diff-tag d-agent">Agente</span><p><strong>É uma persona completa.</strong> Tem identidade, missão, regras e estilo de comunicação. Use como System Prompt pra fazer o AI "ser" aquele especialista durante toda a conversa.</p></div>
          <div class="diff-row"><span class="diff-tag d-skill">Skill</span><p><strong>É uma habilidade específica.</strong> Define como executar uma tarefa concreta (ex: "como revisar código", "como escrever SEO"). Injeta conhecimento pontual no AI.</p></div>
        </div>
        <div class="use-cols">
          <div class="use-col">
            <div class="use-col-head"><span>🤖</span> <span>Agentes</span> <span class="chip chip-blue">onde colar</span></div>
            <ul class="use-list">
              <li>
                <div class="dest">☁️ Claude.ai (web)</div>
                <div class="how">Crie um Project → Settings → System Prompt → cole o prompt</div>
              </li>
              <li>
                <div class="dest">🤖 ChatGPT</div>
                <div class="how">Settings → Personalize → Custom Instructions → cole no campo inferior</div>
              </li>
              <li>
                <div class="dest">💎 Gemini</div>
                <div class="how">Gems → Create Gem → Instructions → cole o prompt</div>
              </li>
              <li>
                <div class="dest">⚡ Claude Code (CLI)</div>
                <div class="how">Coloque o arquivo .md na pasta:</div>
                <code class="code">.claude/agents/nome-do-agente.md</code>
              </li>
              <li>
                <div class="dest">💬 Qualquer chat</div>
                <div class="how">Cole como <strong>primeira mensagem</strong> da conversa — funciona em tudo</div>
              </li>
            </ul>
          </div>
          <div class="use-col">
            <div class="use-col-head"><span>⚡</span> <span>Skills</span> <span class="chip chip-purple">onde colar</span></div>
            <ul class="use-list">
              <li>
                <div class="dest">⚡ Claude Code (CLI)</div>
                <div class="how">Coloque o SKILL.md na pasta:</div>
                <code class="code">.claude/skills/nome-da-skill/SKILL.md</code>
              </li>
              <li>
                <div class="dest">☁️ Claude.ai / ChatGPT / Gemini</div>
                <div class="how">Cole como System Prompt ou adicione junto ao contexto da conversa</div>
              </li>
              <li>
                <div class="dest">🔧 CLAUDE.md do projeto</div>
                <div class="how">Cole o conteúdo relevante diretamente no <code class="code">CLAUDE.md</code> do seu projeto</div>
              </li>
              <li>
                <div class="dest">💬 Qualquer chat</div>
                <div class="how">Cole no início da conversa como instrução de contexto</div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <div class="section-bar">
      <h2 id="sectionTitle">Todos os Agentes</h2>
      <div class="s-line"></div>
      <div class="view-toggle">
        <button class="view-btn active" id="btnGrid" onclick="setView('grid')" title="Grade">⊞</button>
        <button class="view-btn" id="btnList" onclick="setView('list')" title="Lista">☰</button>
      </div>
    </div>

    <div class="content" id="content"></div>
  </main>
</div>

<!-- MODAL -->
<div class="overlay" id="overlay" onclick="closeMBg(event)">
  <div class="modal">
    <div class="modal-hd">
      <div class="modal-em" id="mEm"></div>
      <div class="modal-info">
        <div class="modal-name" id="mName"></div>
        <div class="modal-cat" id="mCat"></div>
      </div>
      <button class="modal-x" onclick="closeM()">✕</button>
    </div>
    <div class="modal-bd">
      <div id="mVibe" class="modal-vibe" style="display:none"></div>
      <div class="modal-desc" id="mDesc"></div>

      <button class="copy-main-btn" id="copyMainBtn" onclick="copyFull()">
        <span id="copyMainTxt">📋 Copiar Prompt Completo</span>
        <span class="btn-chars" id="copyChars"></span>
      </button>

      <div class="paste-guide" id="pasteGuide"></div>

      <div>
        <div class="preview-lbl">
          <span class="sec-lbl">📄 Preview do prompt</span>
          <span id="previewMeta" style="font-size:.7rem;color:var(--muted)"></span>
        </div>
        <div class="preview-box">
          <pre id="mPreview"></pre>
          <div class="fade-bot"></div>
        </div>
      </div>

      <div>
        <div class="sec-lbl" style="margin-bottom:7px">📁 Arquivo original</div>
        <div class="file-row">
          <span class="file-path" id="mFile"></span>
          <button class="copy-path-btn" onclick="copyFilePath()">Copiar caminho</button>
        </div>
      </div>

      <button class="modal-close-btn" onclick="closeM()">Fechar</button>
    </div>
  </div>
</div>
<div class="toast" id="toast"></div>

<script>
function _d(b){{try{{return JSON.parse(decodeURIComponent(escape(atob(b))))}}catch(e){{return JSON.parse(atob(b))}}}}
const AGENTS=_d("{agents_b64}");
const SKILLS=_d("{skills_b64}");
const AGENT_CATS=_d("{agent_cats_b64}");
const SKILL_CATS=_d("{skill_cats_b64}");

const PASTE_AGENT=`<h5>📍 Onde colar este agente</h5><div class="paste-grid">
<div class="paste-item"><div class="dest">☁️ Claude.ai</div><div>Project → Settings → System Prompt</div></div>
<div class="paste-item"><div class="dest">🤖 ChatGPT</div><div>Settings → Custom Instructions</div></div>
<div class="paste-item"><div class="dest">⚡ Claude Code</div><div class="path">.claude/agents/nome.md</div></div>
<div class="paste-item"><div class="dest">💬 Qualquer chat</div><div>1ª mensagem da conversa</div></div>
</div>`;

const PASTE_SKILL=`<h5>📍 Onde colar esta skill</h5><div class="paste-grid">
<div class="paste-item"><div class="dest">⚡ Claude Code</div><div class="path">.claude/skills/nome/SKILL.md</div></div>
<div class="paste-item"><div class="dest">📄 CLAUDE.md</div><div>Cole no arquivo CLAUDE.md do projeto</div></div>
<div class="paste-item"><div class="dest">☁️ Claude.ai / ChatGPT</div><div>System Prompt ou contexto</div></div>
<div class="paste-item"><div class="dest">💬 Qualquer chat</div><div>1ª mensagem da conversa</div></div>
</div>`;

let tab='agents', cat='all', search='', view='grid';
let selAgent=null, sbFilter='', sbOpen=new Set();
let sidebarOpen=true;

function toggleSidebar(){{
  sidebarOpen=!sidebarOpen;
  const sb=document.getElementById('sidebar'),main=document.getElementById('main');
  if(window.innerWidth<=720)sb.classList.toggle('mobile-open',sidebarOpen);
  else{{sb.classList.toggle('collapsed',!sidebarOpen);main.classList.toggle('expanded',!sidebarOpen)}}
}}

function switchTab(t){{
  tab=t;cat='all';search='';selAgent=null;
  document.getElementById('searchMain').value='';
  document.getElementById('tabAgents').classList.toggle('active',t==='agents');
  document.getElementById('tabSkills').classList.toggle('active',t==='skills');
  const isA=t==='agents';
  document.getElementById('heroTitle').innerHTML=isA
    ?'{total_agents} Agentes de IA<br>prontos para <em>copiar e usar</em>'
    :'{total_skills} Skills especializadas<br>prontas para <em>copiar e usar</em>';
  document.getElementById('heroDesc').textContent=isA
    ?"Clique em qualquer agente, copie o prompt completo e cole no Claude, ChatGPT, Gemini — sem abrir arquivo nenhum."
    :"Habilidades específicas para injetar em qualquer IA. Copie e cole como instrução de contexto ou no CLAUDE.md do projeto.";
  document.getElementById('allIcon').textContent=isA?'🏠':'🏠';
  buildSidebar();renderContent();window.scrollTo({{top:0,behavior:'smooth'}});
}}

function getItems(){{return tab==='agents'?AGENTS:SKILLS}}
function getCats(){{return tab==='agents'?AGENT_CATS:SKILL_CATS}}

function buildSidebar(){{
  const items=getItems(), cats=getCats();
  const q=sbFilter.toLowerCase();
  const filtCats=cats.filter(c=>!q||c.label.toLowerCase().includes(q)||c.id.toLowerCase().includes(q));
  const container=document.getElementById('sbCats');
  const isA=tab==='agents';

  container.innerHTML=filtCats.map(c=>{{
    const cItems=items.filter(a=>(isA?a.cat:a.cat)===c.id);
    const isOpen=sbOpen.has(c.id), isActive=cat===c.id;
    const icon=c.icon||(isA?'📁':'⚡');
    return `<div class="sb-cat">
      <button class="sb-cat-btn ${{isActive?'active-cat':''}} ${{isOpen?'open':''}}" onclick="toggleCat('${{c.id}}')">
        <span class="sb-cat-icon">${{icon}}</span>
        <span class="sb-cat-name">${{c.label}}</span>
        <span class="sb-cat-cnt">${{cItems.length}}</span>
        <span class="sb-caret">▶</span>
      </button>
      <div class="sb-items ${{isOpen?'open':''}}">
        <div style="padding:3px 0 3px 26px">
          <button style="background:none;border:none;color:var(--blue);font-size:.73rem;font-weight:700;cursor:pointer;padding:2px 0" onclick="selectCat('${{c.id}}')">Ver todos (${{cItems.length}}) →</button>
        </div>
        ${{cItems.slice(0,40).map(a=>{{
          const idx=items.indexOf(a);
          const em=isA?a.emoji:'⚡';
          return `<div class="sb-item ${{selAgent===a?'sel':''}}" onclick="openModal(${{idx}})">
            <span class="sb-item-em">${{em}}</span>
            <span class="sb-item-name">${{isA?a.name:a.name}}</span>
          </div>`;
        }}).join('')}}
        ${{cItems.length>40?`<div style="font-size:.7rem;color:var(--muted);padding:3px 26px">+${{cItems.length-40}} mais → use busca</div>`:''}}
      </div>
    </div>`;
  }}).join('');

  const total=items.length;
  document.getElementById('btnAll').classList.toggle('active',cat==='all');
  document.getElementById('allCount').textContent=total;
  document.getElementById('sbLbl').textContent=tab==='agents'?'Categorias':'Categorias';
  document.getElementById('sbFooter').innerHTML=tab==='agents'
    ?`<strong>{total_agents} agentes</strong> · {total_skills} skills`
    :`{total_agents} agentes · <strong>{total_skills} skills</strong>`;
}}

function toggleCat(id){{
  if(sbOpen.has(id)){{sbOpen.delete(id)}}else{{sbOpen.add(id);selectCat(id)}}
  buildSidebar();
}}
function selectCat(id){{
  cat=id;selAgent=null;search='';
  document.getElementById('searchMain').value='';
  buildSidebar();renderContent();
  window.scrollTo({{top:0,behavior:'smooth'}});
}}
function onSbSearch(v){{sbFilter=v;buildSidebar()}}
function onSearch(v){{search=v;cat='all';selAgent=null;buildSidebar();renderContent()}}
function setView(v){{
  view=v;
  document.getElementById('btnGrid').classList.toggle('active',v==='grid');
  document.getElementById('btnList').classList.toggle('active',v==='list');
  renderContent();
}}

function getFiltered(){{
  const items=getItems(), isA=tab==='agents';
  return items.filter(a=>{{
    const mc=cat==='all'||a.cat===cat;
    const q=search.toLowerCase();
    const ms=!q||a.name.toLowerCase().includes(q)||a.desc.toLowerCase().includes(q)||(isA&&a.vibe.toLowerCase().includes(q))||a.cat.toLowerCase().includes(q);
    return mc&&ms;
  }});
}}

function renderContent(){{
  const filtered=getFiltered(), isA=tab==='agents';
  document.getElementById('mainCount').textContent=filtered.length+' itens';
  let title=isA?'Todos os Agentes':'Todas as Skills';
  if(search)title=`Busca: "${{search}}"`;
  else if(cat!=='all')title=cat;
  document.getElementById('sectionTitle').textContent=title;
  const container=document.getElementById('content');
  if(!filtered.length){{container.innerHTML=`<div class="empty"><div class="ei">🔍</div><p>Nenhum resultado para <strong>"${{search}}"</strong></p></div>`;return}}
  const groups={{}};
  filtered.forEach(a=>{{
    if(!groups[a.cat])groups[a.cat]={{label:a.cat,agents:[]}};
    groups[a.cat].agents.push(a);
  }});
  container.innerHTML=Object.entries(groups).map(([cid,g])=>{{
    const ci=getCats().find(c=>c.id===cid)||{{}};
    return `<div class="cat-block">
      <div class="cat-block-hdr">
        <div class="cat-block-icon">${{ci.icon||'📁'}}</div>
        <div class="cat-block-name">${{g.label}}</div>
        <div class="cat-block-cnt">${{g.agents.length}}</div>
      </div>
      <div class="${{view==='grid'?'grid-v':'list-v'}}">
        ${{g.agents.map(a=>view==='grid'?renderCard(a):renderRow(a)).join('')}}
      </div>
    </div>`;
  }}).join('');
}}

function renderCard(a){{
  const idx=getItems().indexOf(a);
  const isA=tab==='agents';
  const copyLabel=isA?'📋 Copiar Prompt':'📋 Copiar Skill';
  return `<div class="card ${{isA?'':'skill-card'}}" onclick="openModal(${{idx}})">
    <div class="card-hd">
      <div class="card-em">${{isA?a.emoji:'⚡'}}</div>
      <div class="card-mt">
        <div class="card-name">${{a.name}}</div>
        <div class="card-path">${{a.file}}</div>
      </div>
    </div>
    <div class="card-desc">${{a.desc||''}}</div>
    ${{isA&&a.vibe?`<div class="card-vibe">${{a.vibe}}</div>`:''}}
    ${{!isA?`<div class="card-meta-row"><span class="card-source">📦 ${{a.source||'community'}}</span><span class="risk-badge risk-${{a.risk||'unknown'}}">${{a.risk||'?'}}</span></div>`:''}}
    <div class="card-actions">
      <button class="btn-xs btn-blue" onclick="event.stopPropagation();openModal(${{idx}})">Ver</button>
      <button class="btn-xs ${{isA?'btn-org':'btn-pur'}}" id="qb${{idx}}" onclick="event.stopPropagation();quickCopy(${{idx}})">${{copyLabel}}</button>
    </div>
  </div>`;
}}
function renderRow(a){{
  const idx=getItems().indexOf(a);
  const isA=tab==='agents';
  return `<div class="row" onclick="openModal(${{idx}})">
    <div class="row-em">${{isA?a.emoji:'⚡'}}</div>
    <div class="row-name">${{a.name}}</div>
    <div class="row-desc">${{a.desc||''}}</div>
    <div class="row-acts">
      <button class="btn-xs btn-blue" onclick="event.stopPropagation();openModal(${{idx}})">Ver</button>
      <button class="btn-xs ${{isA?'btn-org':'btn-pur'}}" onclick="event.stopPropagation();quickCopy(${{idx}})">Copiar</button>
    </div>
  </div>`;
}}

function openModal(idx){{
  const a=getItems()[idx]; selAgent=a;
  const isA=a.type==='agent';
  const cat=isA?(AGENT_CATS.find(c=>c.id===a.cat)||{{}}):{{}};
  document.getElementById('mEm').textContent=isA?a.emoji:'⚡';
  document.getElementById('mName').textContent=a.name;
  document.getElementById('mCat').textContent=(isA?(cat.icon+' '+cat.label):('📦 '+a.cat));
  const vibeEl=document.getElementById('mVibe');
  if(isA&&a.vibe){{vibeEl.textContent='💬 "'+a.vibe+'"';vibeEl.style.display='block'}}
  else vibeEl.style.display='none';
  document.getElementById('mDesc').textContent=a.desc||'';
  document.getElementById('mFile').textContent=a.file;
  const chars=a.prompt.length, lines=a.prompt.split('\\n').length;
  document.getElementById('copyChars').textContent=chars.toLocaleString()+' chars';
  document.getElementById('previewMeta').textContent=lines+' linhas · '+chars.toLocaleString()+' chars';
  document.getElementById('mPreview').textContent=a.prompt;
  document.getElementById('pasteGuide').innerHTML=isA?PASTE_AGENT:PASTE_SKILL;
  const btn=document.getElementById('copyMainBtn');
  btn.className='copy-main-btn '+(isA?'agent-btn':'skill-btn');
  document.getElementById('copyMainTxt').textContent=isA?'📋 Copiar Prompt Completo':'📋 Copiar Skill Completa';
  document.getElementById('overlay').classList.add('open');
  document.body.style.overflow='hidden';
  buildSidebar();
}}
function closeMBg(e){{if(e.target===document.getElementById('overlay'))closeM()}}
function closeM(){{
  selAgent=null;
  document.getElementById('overlay').classList.remove('open');
  document.body.style.overflow='';
  buildSidebar();
}}
function copyFull(){{
  if(!selAgent)return;
  navigator.clipboard.writeText(selAgent.prompt).then(()=>{{
    const btn=document.getElementById('copyMainBtn');
    const txt=document.getElementById('copyMainTxt');
    btn.className='copy-main-btn copied';
    txt.textContent='✅ Copiado! Cole como System Prompt';
    setTimeout(()=>{{
      btn.className='copy-main-btn '+(selAgent?.type==='agent'?'agent-btn':'skill-btn');
      txt.textContent=selAgent?.type==='agent'?'📋 Copiar Prompt Completo':'📋 Copiar Skill Completa';
    }},3000);
    toast('✅ Copiado! Cole no Claude, ChatGPT ou qualquer AI.');
  }});
}}
function quickCopy(idx){{
  const a=getItems()[idx];
  navigator.clipboard.writeText(a.prompt).then(()=>{{
    const btn=document.getElementById('qb'+idx);
    if(btn){{const o=btn.textContent;btn.textContent='✅ Copiado!';btn.className='btn-xs btn-ok';setTimeout(()=>{{btn.textContent=o;btn.className='btn-xs '+(tab==='agents'?'btn-org':'btn-pur')}},1800)}}
    toast('✅ '+a.name+' copiado!');
  }});
}}
function copyFilePath(){{
  if(selAgent)navigator.clipboard.writeText(selAgent.file).then(()=>toast('📁 Caminho copiado!'));
}}
function toggleUse(){{
  document.getElementById('useToggle').classList.toggle('open');
  document.getElementById('useBody').classList.toggle('open');
}}
function toast(msg){{
  const t=document.getElementById('toast');t.textContent=msg;t.classList.add('show');
  clearTimeout(t._t);t._t=setTimeout(()=>t.classList.remove('show'),2500);
}}
document.addEventListener('keydown',e=>{{
  if(e.key==='Escape')closeM();
  if((e.metaKey||e.ctrlKey)&&e.key==='k'){{e.preventDefault();document.getElementById('searchMain').focus();document.getElementById('searchMain').select()}}
  if(e.key==='b'&&!e.metaKey&&!e.ctrlKey&&document.activeElement.tagName!=='INPUT')toggleSidebar();
}});
buildSidebar();renderContent();
</script>
</body>
</html>"""

if __name__ == '__main__':
    print("Carregando agentes...")
    agents = load_agents()
    print(f"  {len(agents)} agentes carregados")

    print("Carregando skills...")
    skills = load_skills()
    print(f"  {len(skills)} skills carregadas")

    print("Gerando HTML...")
    html = build_html(agents, skills)

    out = os.path.join(AGENTS_BASE, 'index.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)

    size_mb = os.path.getsize(out) / 1024 / 1024
    print(f"index.html gerado: {size_mb:.1f} MB")
    print(f"Arquivo: {out}")

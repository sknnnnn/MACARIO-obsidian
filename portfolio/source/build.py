#!/usr/bin/env python3
"""
Portfolio de Ignacio Sconza — generador editorial bilingüe.

Cada texto se escribe una sola vez como t("español", "english"), de modo que
ambas versiones comparten exactamente la misma estructura, jerarquía y
diagramación. Uso:

    python3 build.py            # genera portfolio_es.html y portfolio_en.html
    node render.js              # exporta los PDF con Chromium

Fuentes del contenido: vault MACARIO (Obsidian), repositorios
sknnnnn/GxK12-2 y sknnnnn/proyecto-raices, archivo Figma "PRANA STUDIOS"
(páginas "GXK12.2 — Etapa 1 — Diseños aprobados" y "Proyecto Raices") y
capturas del sitio público de Raíces aportadas por Ignacio. Ver
../RELEVAMIENTO.md.
"""
import pathlib

HERE = pathlib.Path(__file__).parent
LANG = "es"


def t(es, en):
    return es if LANG == "es" else en


EMAIL = "ignaciotsconza@gmail.com"
PHONE_DISPLAY = "+54 9 11 6521-1354"
PHONE_LINK = "tel:+5491165211354"
IG = "https://www.instagram.com/nachosconza"
IG_DISPLAY = "instagram.com/nachosconza"
RAICES_URL = "https://proyectoraices.com.ar"

# ---------------------------------------------------------------- iconos
ICONS = {
    # Desarrollo digital: corchetes + barra
    "dev": '<svg class="ico" viewBox="0 0 24 24"><path d="M8 6 3 12l5 6"/><path d="M16 6l5 6-5 6"/><path d="M13.5 4 10.5 20"/></svg>',
    # Diseño y experiencia: marco con nodo en esquina
    "ux": '<svg class="ico" viewBox="0 0 24 24"><rect x="3" y="5" width="15" height="14"/><path d="M3 9h15"/><circle class="f" cx="19.5" cy="4.5" r="2.3"/></svg>',
    # Branding: círculo con núcleo
    "brand": '<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><circle class="f" cx="12" cy="12" r="3"/></svg>',
    # Audiovisual: triángulo + línea de tiempo
    "av": '<svg class="ico" viewBox="0 0 24 24"><path d="M6 4v12l10-6z"/><path d="M3 20h18"/><path d="M9 18v4"/></svg>',
    # Tecnología e innovación: rombo con chispa
    "tech": '<svg class="ico" viewBox="0 0 24 24"><path d="M12 3l9 9-9 9-9-9z"/><path d="M12 8v8M8 12h8"/></svg>',
    # Gestión: barras escalonadas
    "pm": '<svg class="ico" viewBox="0 0 24 24"><path d="M3 6h10M3 12h15M3 18h8"/><circle class="f" cx="18" cy="6" r="1.8"/><circle class="f" cx="15" cy="18" r="1.8"/></svg>',
    # Análisis y sistemas: grafo
    "sys": '<svg class="ico" viewBox="0 0 24 24"><circle cx="5" cy="18" r="2.3"/><circle cx="12" cy="6" r="2.3"/><circle cx="19" cy="15" r="2.3"/><path d="M6.3 16 10.8 8M13.8 7.3l3.8 6M7.3 17.7l9.4-2.2"/></svg>',
}


def hdr(section, folio):
    return (f'<div class="hdr"><div>Ignacio Sconza — Portfolio 2026</div>'
            f'<div class="c">{section}</div><div class="r"><b>{folio:02d}</b> / {{TOTAL}}</div></div>')


def status(kind, label):
    return f'<span class="st {kind}">{label}</span>'


def fig(src, cap, h=None, pos="top center", extra=""):
    style = f'height:{h};' if h else ''
    return (f'<div class="fig" style="{style}{extra}"><div class="frame">'
            f'<img class="shot" src="{src}" style="object-position:{pos}" alt=""></div>'
            f'<div class="cap">{cap}</div></div>')


def nfig(src, cap, w=None, h=None):
    """Figura con proporción natural: se fija el ancho (w) o el alto (h)."""
    if h:
        img = f'<img class="shot byh" src="{src}" style="height:{h}" alt="">'
        fst = 'width:min-content'
    else:
        img = f'<img class="shot nat" src="{src}" style="width:100%" alt="">'
        fst = f'width:{w or "100%"}'
    return f'<figure class="nf" style="{fst}">{img}<figcaption class="cap">{cap}</figcaption></figure>'


# ---------------------------------------------------------------- páginas
PAGES = []


def page(fn):
    PAGES.append(fn)
    return fn


@page
def cover(n):
    return f'''
<section class="page wine">
  <div class="hdr"><div>Portfolio 2026</div><div class="c">{t("Diseño · Desarrollo · Creatividad", "Design · Development · Creativity")}</div><div class="r">{"Español" if LANG=="es" else "English"}</div></div>
  <svg class="abs" style="left:0;top:0;width:297mm;height:210mm" viewBox="0 0 297 210">
    <g stroke="rgba(255,231,206,.35)" stroke-width=".25" fill="none">
      <path d="M196 46 L262 92 L214 150 Z"/>
      <path d="M196 46 L150 0 M262 92 L297 84 M214 150 L232 210"/>
    </g>
    <g fill="#FED3A8"><circle cx="196" cy="46" r="2.2"/><circle cx="262" cy="92" r="2.2"/><circle cx="214" cy="150" r="2.2"/></g>
    <g fill="none" stroke="#FED3A8" stroke-width=".35"><circle cx="196" cy="46" r="6"/><circle cx="262" cy="92" r="6"/><circle cx="214" cy="150" r="6"/></g>
    <g font-family="JetBrains Mono" font-size="3.1" letter-spacing=".5" style="fill:#FFE7CE">
      <text x="204" y="44">01 — {t("DISEÑO", "DESIGN")}</text>
      <text x="238" y="104">02 — {t("DESARROLLO", "DEVELOPMENT")}</text>
      <text x="222" y="152">03 — {t("CREATIVIDAD", "CREATIVITY")}</text>
    </g>
    <g font-family="JetBrains Mono" font-size="2.3" letter-spacing=".4" style="fill:rgba(255,231,206,.62)">
      <text x="204" y="49.5">X 196 · Y 046</text><text x="238" y="108.5">X 262 · Y 092</text><text x="222" y="156.5">X 214 · Y 150</text>
    </g>
  </svg>
  <div class="abs" style="left:14mm;top:52mm;width:170mm">
    <div class="kicker" style="color:#FED3A8">{t("Portfolio profesional", "Professional portfolio")}</div>
    <h1 class="h-xxl mt2" style="font-size:96pt">Ignacio<br>Sconza</h1>
  </div>
  <div class="abs" style="left:14mm;bottom:14mm;width:150mm">
    <div class="lead-ser" style="font-size:21pt;color:#FFE7CE">{t("Diseño, desarrollo y creatividad aplicada a soluciones digitales.", "Design, development and creativity applied to digital solutions.")}</div>
    <div class="rule mt3 mb2"></div>
    <div class="row between small" style="color:rgba(255,231,206,.85)">
      <a href="mailto:{EMAIL}">{EMAIL}</a><a href="{PHONE_LINK}">{PHONE_DISPLAY}</a><a href="{IG}">{IG_DISPLAY}</a>
    </div>
  </div>
</section>'''


@page
def index(n):
    items = [
        ("01", t("Presentación", "Introduction"), t("Quién soy y cómo pienso", "Who I am and how I think"), 3),
        ("02", t("Capacidades", "Capabilities"), t("Un ecosistema de disciplinas", "An ecosystem of disciplines"), 4),
        ("03", t("Cómo trabajo", "How I work"), t("Cinco etapas que se repiten", "Five stages that loop"), 6),
        ("04", "GXK12:2", t("Caso · e-commerce y experiencia digital", "Case · e-commerce and digital experience"), 7),
        ("05", t("Proyecto Raíces", "Proyecto Raíces"), t("Caso · plataforma digital de turismo", "Case · digital travel platform"), 15),
        ("06", t("Laboratorio", "Lab"), t("Exploración, sistemas e IA", "Exploration, systems and AI"), 20),
        ("07", t("Formación y herramientas", "Education and tools"), t("Base y ecosistema de trabajo", "Foundation and toolkit"), 21),
        ("08", t("Contacto", "Contact"), t("Conversemos", "Let’s talk"), 23),
    ]
    rows = "".join(f'''
      <div class="row" style="align-items:baseline;border-top:1px solid var(--line);padding:2.6mm 0">
        <div class="mono wine-t" style="width:12mm;font-size:7pt">{a}</div>
        <div class="h-s" style="width:62mm;font-size:13pt">{b}</div>
        <div class="muted small flex1">{c}</div>
        <div class="mono small">{d:02d}</div>
      </div>''' for a, b, c, d in items)
    return f'''
<section class="page">
  {hdr(t("Índice", "Contents"), n)}
  <div class="body grid">
    <div style="grid-column:1/6" class="col between">
      <div>
        <div class="kicker">{t("Índice", "Contents")}</div>
        <h2 class="h-xl mt2">{t("Lo que <span class='ser'>vas a encontrar</span>", "What you’ll <span class='ser'>find here</span>")}</h2>
      </div>
      <p class="lead muted" style="max-width:95mm">{t("Este documento reúne cómo pienso, cómo trabajo y dos proyectos que muestran cómo conecto estrategia, diseño y tecnología de principio a fin.", "This document brings together how I think, how I work, and two projects that show how I connect strategy, design and technology from start to finish.")}</p>
    </div>
    <div style="grid-column:7/13" class="col end">
      {rows}
      <div style="border-top:1px solid var(--line)"></div>
    </div>
  </div>
</section>'''


@page
def intro(n):
    traits = [
        (t("Integrar", "Integrate"), t("Conecto disciplinas que suelen trabajar por separado: estrategia, diseño, desarrollo y contenido.", "I connect disciplines that usually work apart: strategy, design, development and content.")),
        (t("Comprender", "Understand"), t("Antes de diseñar, entiendo el problema, el contexto y las restricciones reales.", "Before designing, I understand the problem, the context and the real constraints.")),
        (t("Construir", "Build"), t("Llevo las ideas a productos concretos, documentados y verificables.", "I turn ideas into concrete products that are documented and verifiable.")),
        (t("Explorar", "Explore"), t("Pruebo herramientas, lenguajes visuales y formas nuevas de trabajar —incluida la IA— con criterio.", "I test tools, visual languages and new ways of working —AI included— with judgement.")),
    ]
    tr = "".join(f'''<div class="col gap1" style="border-top:1.5px solid var(--ink);padding-top:3mm">
        <div class="mono wine-t" style="font-size:6.6pt">0{i+1}</div><div class="h-s">{a}</div><div class="small muted">{b}</div></div>''' for i, (a, b) in enumerate(traits))
    return f'''
<section class="page">
  {hdr(t("01 · Presentación", "01 · Introduction"), n)}
  <div class="body grid">
    <div style="grid-column:1/8" class="col between">
      <div>
        <div class="kicker"><span class="n">01</span>{t("Presentación", "Introduction")}</div>
        <h2 class="h-l mt3" style="font-size:46pt">{t("Conecto diseño, tecnología y creatividad para transformar <span class='ser wine-t'>ideas</span> en proyectos <span class='ser wine-t'>concretos.</span>", "I connect design, technology and creativity to turn <span class='ser wine-t'>ideas</span> into <span class='ser wine-t'>real</span> projects.")}</h2>
      </div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:5mm">{tr}</div>
    </div>
    <div style="grid-column:9/13" class="col between">
      <div class="col gap2" style="padding-top:12mm">
        <p class="lead" style="font-size:11.5pt">{t("Soy un profesional multidisciplinario. Me interesa involucrarme en todas las etapas de un proyecto: desde la conceptualización y la planificación hasta el diseño, el desarrollo y la producción final.", "I’m a multidisciplinary professional. I like being involved in every stage of a project: from concept and planning to design, development and final production.")}</p>
        <p class="muted">{t("Mi perfil combina pensamiento creativo, sensibilidad visual y comprensión tecnológica. No se trata de hacer un poco de todo, sino de entender cómo se conectan las partes de un producto digital y participar en su construcción de principio a fin.", "My profile combines creative thinking, visual sensitivity and technical understanding. It isn’t about doing a little of everything; it’s about understanding how the parts of a digital product fit together and helping build it end to end.")}</p>
      </div>
      <div class="panel">
        <div class="kicker mb1">{t("Disponible para", "Open to")}</div>
        <div class="small">{t("Oportunidades laborales · Proyectos freelance · Colaboraciones creativas", "Full-time roles · Freelance projects · Creative collaborations")}</div>
      </div>
    </div>
  </div>
</section>'''


def AREAS_():
  return [
    ("dev", t("Desarrollo digital", "Digital development"), [
        t("Sitios web y plataformas", "Websites and platforms"),
        t("E-commerce y productos digitales", "E-commerce and digital products"),
        t("Arquitectura de productos digitales", "Digital product architecture"),
        t("Estructuras y funcionalidades", "Structures and features"),
        t("Procesos de construcción tecnológica", "Technology build processes")]),
    ("ux", t("Diseño y experiencia digital", "Design and digital experience"), [
        t("Diseño UI/UX y de interfaces", "UI/UX and interface design"),
        t("Experiencias digitales y productos interactivos", "Digital experiences and interactive products"),
        t("Diseño gráfico y comunicación visual", "Graphic design and visual communication"),
        t("Arquitectura de información", "Information architecture"),
        t("Flujos y experiencias", "Flows and journeys")]),
    ("brand", t("Branding y dirección creativa", "Branding and creative direction"), [
        t("Formación en branding e identidad visual", "Training in branding and visual identity"),
        t("Conceptos y lenguajes visuales", "Concepts and visual languages"),
        t("Exploración de sistemas gráficos", "Graphic system exploration"),
        t("Comunicación visual", "Visual communication")]),
    ("av", t("Producción audiovisual", "Audiovisual production"), [
        t("Edición de video", "Video editing"),
        t("Edición y tratamiento de imágenes", "Image editing and treatment"),
        t("Experimentación con contenido visual", "Visual content experimentation"),
        t("Producción y exploración audiovisual", "Audiovisual production and exploration")]),
    ("tech", t("Tecnología e innovación", "Technology and innovation"), [
        t("IA aplicada a procesos creativos", "AI applied to creative processes"),
        t("Automatización y herramientas digitales", "Automation and digital tools"),
        t("Experimentación tecnológica", "Technology experimentation"),
        t("Nuevas posibilidades de diseño y desarrollo", "New design and development possibilities")]),
    ("pm", t("Gestión y organización", "Management and organisation"), [
        t("Planificación de proyectos y tareas", "Project and task planning"),
        t("Coordinación de procesos de trabajo", "Workflow coordination"),
        t("Documentación y comunicación", "Documentation and communication"),
        t("Trabajo colaborativo", "Collaborative work")]),
    ("sys", t("Análisis y sistemas", "Analysis and systems"), [
        t("Análisis y visualización de datos", "Data analysis and visualisation"),
        t("Diseño y modelado de sistemas", "System design and modelling"),
        t("Estructuras, relaciones y comportamientos", "Structures, relationships and behaviours")]),
  ]


@page
def eco(n):
    import math
    cx, cy, R = 70, 72, 52
    nodes, labels, lines = "", "", ""
    for i, (k, name, _) in enumerate(AREAS_()):
        a = -math.pi / 2 + i * 2 * math.pi / 7
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        lines += f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}"/>'
        nxt = -math.pi / 2 + (i + 1) * 2 * math.pi / 7
        x2, y2 = cx + R * math.cos(nxt), cy + R * math.sin(nxt)
        lines += f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke-dasharray="1 1.5"/>'
        nodes += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="#9E1F32"/><circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="none" stroke="#9E1F32" stroke-width=".3"/>'
        anchor = "start" if math.cos(a) > 0.2 else ("end" if math.cos(a) < -0.2 else "middle")
        dx = 8 if anchor == "start" else (-8 if anchor == "end" else 0)
        dy = -8 if math.sin(a) < -0.9 else (9.5 if math.sin(a) > 0.9 else 1.2)
        labels += f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{anchor}"><tspan class="nn">0{i+1}</tspan> {name}</text>'
    svg = f'''<svg class="eco" viewBox="-44 0 232 140" style="width:100%;height:100%;overflow:visible">
      <style>.eco text{{font-family:'Familjen Grotesk';font-size:4.3px;font-weight:600;fill:#1B1517}} .eco .nn{{font-family:'JetBrains Mono';font-size:2.8px;fill:#9E1F32;font-weight:500}}</style>
      <g stroke="rgba(27,21,23,.35)" stroke-width=".3">{lines}</g>
      <circle cx="{cx}" cy="{cy}" r="17" fill="#1B5956"/>
      <text x="{cx}" y="{cy-1.5}" text-anchor="middle" style="fill:#FFE7CE;font-size:4.4px">{t("Producto", "Digital")}</text>
      <text x="{cx}" y="{cy+3.6}" text-anchor="middle" style="fill:#FFE7CE;font-size:4.4px">{t("digital", "product")}</text>
      {nodes}{labels}</svg>'''
    return f'''
<section class="page sand">
  {hdr(t("02 · Capacidades", "02 · Capabilities"), n)}
  <div class="body grid">
    <div style="grid-column:1/5" class="col between">
      <div>
        <div class="kicker"><span class="n">02</span>{t("Capacidades", "Capabilities")}</div>
        <h2 class="h-l mt3">{t("Un ecosistema, <span class='ser wine-t'>no una lista.</span>", "An ecosystem, <span class='ser wine-t'>not a list.</span>")}</h2>
      </div>
      <div class="col gap2">
        <p>{t("Cada disciplina aporta una mirada distinta sobre el mismo objetivo: construir un producto digital que funcione, comunique y pueda crecer.", "Each discipline brings a different lens to the same goal: building a digital product that works, communicates and can grow.")}</p>
        <p class="muted small">{t("El valor no está en cada área por separado, sino en las conexiones: una decisión de arquitectura cambia una interfaz; una decisión de marca cambia un flujo; una herramienta nueva cambia la forma de producir.", "The value isn’t in each area on its own but in the connections: an architecture decision changes an interface; a brand decision changes a flow; a new tool changes how things get made.")}</p>
      </div>
    </div>
    <div style="grid-column:5/13;position:relative;padding:2mm 0 0 0">{svg}</div>
  </div>
</section>'''


@page
def areas(n):
    cards = ""
    for i, (k, name, items) in enumerate(AREAS_()):
        lis = "".join(f"<li>{x}</li>" for x in items)
        cards += f'''<div class="col gap1" style="border-top:1.5px solid var(--ink);padding-top:3mm">
          <div class="row between" style="align-items:flex-start"><div class="mono wine-t" style="font-size:6.6pt">0{i+1}</div><div class="petrol-t">{ICONS[k]}</div></div>
          <div class="h-s" style="min-height:11mm;font-size:13pt">{name}</div>
          <ul class="l" style="font-size:9.2pt">{lis}</ul></div>'''
    return f'''
<section class="page">
  {hdr(t("02 · Capacidades", "02 · Capabilities"), n)}
  <div class="body col">
    <div class="row between" style="align-items:flex-end">
      <h2 class="h-m" style="max-width:150mm">{t("Siete áreas que se cruzan en cada proyecto", "Seven areas that intersect in every project")}</h2>
      <div class="cap" style="max-width:85mm;text-align:right">{t("Capacidades presentadas tal como las practico. No incluyen niveles ni certificaciones.", "Capabilities as I practise them. No levels or certifications are implied.")}</div>
    </div>
    <div class="flex1 mt3" style="display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:1fr 1fr;column-gap:6mm;row-gap:6mm">
      {cards}
      <div class="panel-pet col between" style="padding:4.5mm">
        <div class="kicker">{t("En los casos", "In the cases")}</div>
        <div class="lead-ser" style="font-size:15pt">{t("GXK12:2 y Proyecto Raíces muestran estas áreas trabajando juntas, de la estrategia al código.", "GXK12:2 and Proyecto Raíces show these areas working together, from strategy to code.")}</div>
      </div>
    </div>
  </div>
</section>'''


@page
def method(n):
    import math
    steps = [
        ("01", t("Explorar", "Explore"), t("Investigar, comprender el problema, descubrir oportunidades y conceptualizar.", "Research, understand the problem, uncover opportunities and shape a concept.")),
        ("02", t("Diseñar", "Design"), t("Definir experiencias, estructuras, sistemas e identidades visuales.", "Define experiences, structures, systems and visual identities.")),
        ("03", t("Construir", "Build"), t("Desarrollar soluciones y transformar ideas en productos concretos.", "Develop solutions and turn ideas into concrete products.")),
        ("04", t("Experimentar", "Experiment"), t("Probar tecnologías, herramientas, conceptos y posibilidades.", "Test technologies, tools, concepts and possibilities.")),
        ("05", t("Evolucionar", "Evolve"), t("Evaluar, aprender, iterar y mejorar.", "Evaluate, learn, iterate and improve.")),
    ]
    cx, cy, R = 60, 60, 44
    pts = []
    for i in range(5):
        a = -math.pi / 2 + i * 2 * math.pi / 5
        pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
    arcs = ""
    for i in range(5):
        a1 = -math.pi / 2 + i * 2 * math.pi / 5 + .2
        a2 = -math.pi / 2 + (i + 1) * 2 * math.pi / 5 - .2
        x1, y1 = cx + R * math.cos(a1), cy + R * math.sin(a1)
        x2, y2 = cx + R * math.cos(a2), cy + R * math.sin(a2)
        arcs += f'<path d="M{x1:.1f} {y1:.1f} A{R} {R} 0 0 1 {x2:.1f} {y2:.1f}" marker-end="url(#ar)"/>'
    nodes = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7.5" fill="#FED3A8"/><text x="{x:.1f}" y="{y+1.6:.1f}" text-anchor="middle">{s[0]}</text>' for (x, y), s in zip(pts, steps))
    # atajos internos: experimentar → diseñar, evolucionar → explorar
    chords = f'<path d="M{pts[3][0]:.1f} {pts[3][1]:.1f} Q{cx} {cy} {pts[1][0]:.1f} {pts[1][1]:.1f}" stroke-dasharray="1.2 1.6"/><path d="M{pts[4][0]:.1f} {pts[4][1]:.1f} Q{cx-6} {cy-4} {pts[0][0]:.1f} {pts[0][1]:.1f}" stroke-dasharray="1.2 1.6"/>'
    svg = f'''<svg viewBox="0 0 120 120" style="width:100%;height:100%">
      <defs><marker id="ar" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0L6 3L0 6z" fill="#FED3A8"/></marker></defs>
      <g fill="none" stroke="#FED3A8" stroke-width=".45">{arcs}</g>
      <g fill="none" stroke="rgba(255,231,206,.45)" stroke-width=".35">{chords}</g>
      <g font-family="JetBrains Mono" font-size="4.6" font-weight="700" fill="#1B5956">{nodes}</g>
      <text x="{cx}" y="{cy+1}" text-anchor="middle" font-family="Instrument Serif" font-style="italic" font-size="7" fill="#FFE7CE">{t("se repite", "it loops")}</text>
    </svg>'''
    lst = "".join(f'''<div class="col gap1" style="border-top:1px solid var(--line-inv);padding:3.2mm 0">
      <div class="row gap2" style="align-items:baseline"><div class="mono peach-t" style="width:7mm;font-size:7pt">{a}</div><div class="h-s" style="font-size:15pt">{b}</div></div>
      <div class="small muted" style="padding-left:11mm">{c}</div></div>''' for a, b, c in steps)
    return f'''
<section class="page petrol">
  {hdr(t("03 · Cómo trabajo", "03 · How I work"), n)}
  <div class="body grid">
    <div style="grid-column:1/5" class="col between">
      <div>
        <div class="kicker"><span class="n">03</span>{t("Cómo trabajo", "How I work")}</div>
        <h2 class="h-l mt3">{t("Cinco etapas que <span class='ser peach-t'>vuelven a empezar.</span>", "Five stages that <span class='ser peach-t'>start over.</span>")}</h2>
        <p class="muted mt2">{t("No es una línea recta. Experimentar puede devolver un proyecto al diseño; evolucionar abre una nueva exploración. Cada vuelta deja el producto más claro y más sólido.", "It isn’t a straight line. Experimenting can send a project back to design; evolving opens a new round of exploration. Each loop leaves the product clearer and sturdier.")}</p>
      </div>
      <div class="box">
        <div class="kicker mb1">{t("En la práctica", "In practice")}</div>
        <div class="small"><b>Raíces</b> — {t("tras cerrar la etapa funcional, el proyecto volvió a diseñar: un “System Reset” reorganizó la base en Foundation → Components → Patterns → Pages → Content sin rehacer lo que funcionaba.", "after the functional stage closed, the project went back to design: a “System Reset” reorganised the base into Foundation → Components → Patterns → Pages → Content without rebuilding what worked.")}</div>
        <div class="small mt1"><b>GXK12:2</b> — {t("la lógica de disponibilidad del carrito se diseñó, se implementó, se probó y volvió a Figma para alinear la interfaz con las decisiones tomadas.", "the cart’s availability logic was designed, implemented, tested and sent back to Figma to align the interface with the decisions made.")}</div>
      </div>
    </div>
    <div style="grid-column:5/9;display:flex;align-items:center;justify-content:center"><div style="width:100%;aspect-ratio:1">{svg}</div></div>
    <div style="grid-column:9/13" class="col" style="justify-content:center">
      <div class="col flex1" style="justify-content:center">{lst}<div style="border-top:1px solid var(--line-inv)"></div></div>
    </div>
  </div>
</section>'''


# ================================================================ GXK12:2
def meta_row(items, inv=False):
    return "".join(f'<div class="col gap1" style="border-top:1px solid {"var(--line-inv)" if inv else "var(--line)"};padding-top:2mm"><div class="kicker">{a}</div><div class="small">{b}</div></div>' for a, b in items)


@page
def gxk_open(n):
    meta = [
        (t("Tipo", "Type"), t("Ecosistema de e-commerce y experiencia digital", "E-commerce ecosystem and digital experience")),
        (t("Rol", "Role"), t("Integral: estrategia, UX/UI, identidad, desarrollo y documentación", "End-to-end: strategy, UX/UI, identity, development and documentation")),
        (t("Estado", "Status"), t("En desarrollo · 2026", "In development · 2026")),
        ("Stack", "Next.js · TypeScript · Supabase"),
    ]
    return f'''
<section class="page dark">
  {hdr(t("04 · Caso de estudio", "04 · Case study"), n)}
  <img src="img/gxk/gk-ilustracion.png" class="abs" style="right:18mm;top:30mm;height:128mm" alt="">
  <div class="abs cap" style="right:18mm;top:160mm;width:70mm;text-align:right">{t("G & K, personajes anfitriones de la marca. Asset utilizado en la Home implementada.", "G & K, the brand’s host characters. Asset used on the implemented Home page.")}</div>
  <div class="abs" style="left:14mm;top:30mm;width:160mm">
    <div class="kicker"><span class="n">04</span>{t("Caso 01", "Case 01")}</div>
    <h2 class="h-xxl mt3" style="font-size:108pt">GXK12:2</h2>
    <p class="lead mt3" style="max-width:130mm;color:#FFE7CE">{t("Cómo se construye un producto digital completo: de una marca con identidad fuerte a una tienda, un recorrido de compra y un panel de gestión, con cada disciplina conectada a la siguiente.", "How a complete digital product gets built: from a brand with a strong identity to a store, a purchase journey and a management panel, with each discipline feeding the next.")}</p>
  </div>
  <div class="abs" style="left:14mm;bottom:13mm;width:175mm;display:grid;grid-template-columns:repeat(4,1fr);gap:5mm">{meta_row(meta, True)}</div>
</section>'''


@page
def gxk_context(n):
    role = [t("Conceptualización", "Concept"), t("Estrategia y arquitectura del producto", "Product strategy and architecture"), t("Diseño de experiencia", "Experience design"), t("Diseño de interfaces", "Interface design"), t("Identidad y dirección visual", "Identity and visual direction"), t("Desarrollo tecnológico", "Technical development"), t("Organización y documentación", "Organisation and documentation"), t("Integración de herramientas y procesos", "Tool and process integration")]
    lis = "".join(f"<li>{r}</li>" for r in role)
    return f'''
<section class="page">
  {hdr("GXK12:2 · " + t("Contexto", "Context"), n)}
  <div class="body grid" style="grid-template-rows:auto minmax(0,1fr);row-gap:6mm">
    <div style="grid-column:1/5;grid-row:1/3" class="col gap3">
      <div>
        <div class="kicker mb1">01 — {t("Presentación y contexto", "Overview and context")}</div>
        <p class="lead" style="font-size:11.5pt">{t("GXK es una marca de indumentaria con un catálogo amplio, alta rotación y stock reducido: unas 2–3 unidades por variante. Hoy vende principalmente por Instagram.", "GXK is a clothing brand with a wide catalogue, high turnover and small stock: around 2–3 units per variant. Today it sells mainly through Instagram.")}</p>
        <p class="muted small">{t("Su esencia está escrita en una frase: “un espacio de exploración y transformación a través de la ropa”. Slogan: <b>NO TE CONFORMES. TRANSFORMATE.</b>", "Its essence fits in one line: “a space for exploration and transformation through clothing”. Slogan: <b>NO TE CONFORMES. TRANSFORMATE.</b> (“Don’t settle. Transform.”)")}</p>
      </div>
      <div>
        <div class="kicker mb1">02 — {t("Objetivo y oportunidad", "Goal and opportunity")}</div>
        <p>{t("Centralizar la operación en una tienda propia y darle al equipo un panel privado para gestionar catálogo, stock, fotos y pedidos sin conocimientos técnicos.", "Centralise operations in an owned store and give the team a private panel to manage catalogue, stock, photos and orders without technical knowledge.")}</p>
        <p class="muted small">{t("La oportunidad: que la tienda no parezca un e-commerce genérico, sino “la puerta de la casa GXK”.", "The opportunity: a store that doesn’t feel like generic e-commerce, but like “the door to the GXK house”.")}</p>
      </div>
      <div class="flex1"></div>
      <div class="cap">{t("Fuentes: Brand & E-commerce Bible, Requerimientos y Metodología (Obsidian); repositorio GxK12-2; archivo Figma.", "Sources: Brand & E-commerce Bible, Requirements and Methodology (Obsidian); GxK12-2 repository; Figma file.")}</div>
    </div>
    <div style="grid-column:6/9;grid-row:1" class="col gap2">
      <div class="kicker">03 — {t("Mi rol", "My role")}</div>
      <ul class="l tight small" style="columns:1">{lis}</ul>
    </div>
    <div style="grid-column:9/13;grid-row:1" class="panel-ink col gap2">
      <div class="kicker">{t("Cómo se construye", "How it’s built")}</div>
      <p class="small">{t("Defino producto, alcance, arquitectura y dirección visual, y apruebo cada diseño. La implementación se realiza con agentes de IA (Claude Code) sobre decisiones ya aprobadas, en ramas aisladas, con pruebas y revisión antes de integrar.", "I define product, scope, architecture and visual direction, and approve every design. Implementation is carried out with AI agents (Claude Code) on decisions that are already approved, in isolated branches, with tests and review before anything is merged.")}</p>
      <p class="small" style="color:var(--peach)">Figma → {t("aprobación", "approval")} → {t("implementación", "implementation")} → QA</p>
    </div>
    <div style="grid-column:6/13;grid-row:2;display:flex;align-items:flex-end">
      {nfig("img/gxk/fig-indice-etapa1.jpg", t("10 — Material visual · Índice de diseños aprobados en Figma: 14 áreas, de la tienda al Admin, con su fuente de verdad. La Home toma como fuente la implementación validada.", "10 — Visual material · Index of approved designs in Figma: 14 areas, from store to Admin, each with its source of truth. The Home uses the validated implementation as its source."))}
    </div>
  </div>
</section>'''


@page
def gxk_concept(n):
    pairs = [t("elegante + urbano", "elegant + urban"), t("minimalista + exagerado", "minimal + exaggerated"), t("serio + absurdo", "serious + absurd"), t("clásico + experimental", "classic + experimental"), t("premium + cercano", "premium + approachable")]
    cyc = [t("Estructura", "Structure"), t("Tensión", "Tension"), t("Ruptura", "Rupture"), t("Resolución", "Resolution")]
    cycle = "".join(f'<div class="col" style="flex:1;border-top:2px solid {"var(--wine)" if i==2 else "var(--ink)"};padding-top:2mm"><div class="mono" style="font-size:6.2pt">0{i+1}</div><div class="h-s" style="font-size:10.5pt">{c}</div></div>' for i, c in enumerate(cyc))
    return f'''
<section class="page">
  {hdr("GXK12:2 · " + t("Conceptualización", "Concept"), n)}
  <div class="body grid">
    <div style="grid-column:1/6" class="col between">
      <div>
        <div class="kicker mb1">04 — {t("Conceptualización", "Concept")}</div>
        <h2 class="h-m">{t("De una marca con personalidad a un <span class='ser wine-t'>sistema</span> que se pueda construir.", "From a brand with personality to a <span class='ser wine-t'>system</span> that can be built.")}</h2>
        <p class="mt2 small">{t("Primero se escribió la <b>Brand & E-commerce Bible</b>: esencia, voz, reglas de producto, stock, pagos, entregas y cambios. Después, la <b>Dirección Visual</b> tradujo esa identidad en reglas. La jerarquía es explícita: la Bible define qué es GXK; la dirección visual, cómo se ve.", "First came the <b>Brand & E-commerce Bible</b>: essence, voice, product rules, stock, payments, delivery and returns. Then the <b>Visual Direction</b> translated that identity into rules. The hierarchy is explicit: the Bible defines what GXK is; the visual direction defines how it looks.")}</p>
      </div>
      <div>
        <div class="kicker mb1">{t("Personalidad en tensión", "Personality in tension")}</div>
        <div class="small" style="columns:2;column-gap:5mm">{"<br>".join(pairs)}</div>
        <div class="small mt1"><span class="ser" style="font-size:12pt">{t("Rasgo común: curiosidad.", "Common trait: curiosity.")}</span></div>
      </div>
      <div class="panel">
        <div class="kicker mb1">{t("Regla maestra", "Master rule")}</div>
        <div class="lead-ser" style="font-size:16pt">{t("“GXK no rompe las reglas porque sí. Decide cuándo dejar de cumplirlas.”", "“GXK doesn’t break rules for the sake of it. It decides when to stop following them.”")}</div>
      </div>
    </div>
    <div style="grid-column:7/13" class="col gap3">
      <div>
        <div class="kicker mb1">05 — {t("Proceso de diseño", "Design process")}</div>
        <div class="row gap1">{cycle}</div>
        <div class="small muted mt1">{t("Ciclo compositivo de la V0.2. Jerarquía de decisión: <b>claridad → identidad → exploración → efecto visual</b>. Si un efecto perjudica la claridad, se elimina.", "Compositional cycle from V0.2. Decision hierarchy: <b>clarity → identity → exploration → visual effect</b>. If an effect hurts clarity, it goes.")}</div>
      </div>
      {nfig("img/gxk/fig-superficies.jpg", t("Sistema de superficies medido en Figma: valores exactos, textura de grano y contraste de texto (9,8:1 para el texto principal). Diseño aprobado.", "Surface system measured in Figma: exact values, grain texture and text contrast (9.8:1 for body text). Approved design."))}
      <div class="flex1"></div>
      <div>
        <div class="kicker mb2">{t("Reglas base del sistema", "System base rules")}</div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3mm">
          <div class="box"><div class="h-s">12 · 8 · 4</div><div class="small muted">{t("columnas desktop · tablet · mobile", "columns desktop · tablet · mobile")}</div></div>
          <div class="box"><div class="h-s">0 {t("radio", "radius")}</div><div class="small muted">{t("sin sombras, sin glass, sin blur", "no shadows, glass or blur")}</div></div>
          <div class="box"><div class="h-s" style="color:#C4430A">{t("Naranja = señal", "Orange = signal")}</div><div class="small muted">{t("nunca color estructural", "never a structural colour")}</div></div>
        </div>
      </div>
    </div>
  </div>
</section>'''


@page
def gxk_ux(n):
    d = [
        (t("Confirmación al agregar", "Add-to-cart confirmation"), t("Un panel (hoja inferior en mobile) reemplaza el “Agregado ✓”. No se cierra solo ni se apila; foco, Escape y anuncio accesible especificados.", "A panel (bottom sheet on mobile) replaces “Added ✓”. It doesn’t auto-close or stack; focus, Escape and screen-reader announcement are specified.")),
        (t("Disponibilidad honesta", "Honest availability"), t("Un error al consultar no equivale a “sin stock”. «Iniciar compra» queda bloqueado mientras se verifica y se ofrece «Reintentar».", "A failed check is not the same as “out of stock”. “Start checkout” stays locked while verifying, and “Retry” is offered.")),
        (t("Selectores, no chips", "Selectors, not chips"), t("En el carrito, talle y color se editan con desplegables; los chips se probaron y se descartaron.", "In the cart, size and colour are edited with dropdowns; chips were tested and dropped.")),
        (t("Regla comercial visible", "Visible business rule"), t("El carrito no reserva stock: gana el primer pago confirmado. La interfaz lo dice sin dramatismo.", "The cart doesn’t hold stock: the first confirmed payment wins. The interface says so, calmly.")),
    ]
    rows = "".join(f'<div style="border-top:1px solid var(--line);padding-top:2mm"><div class="h-s" style="font-size:10pt">{a}</div><div class="small muted">{b}</div></div>' for a, b in d)
    buy = t("encontrar → elegir → pagar → terminar", "find → choose → pay → done")
    exp = t("outfits → campañas → historias → G/K → aventuras → universo → familia → eventos", "outfits → campaigns → stories → G/K → adventures → universe → family → events")
    flow = [t("Tienda", "Store"), t("Ficha", "Product"), t("Confirmación", "Confirmation"), t("Carrito", "Cart"), t("Datos", "Details"), t("Entrega", "Delivery"), t("Pago", "Payment"), t("Estado del pedido", "Order status")]
    fl = "".join(f'<div class="col" style="flex:1"><div style="height:2.4mm;background:{"var(--wine)" if i in (2,3) else "var(--ink)"}"></div><div class="mono mt1" style="font-size:5.8pt">0{i+1}</div><div class="small" style="font-weight:600;font-size:7.6pt">{x}</div></div>' for i, x in enumerate(flow))
    return f'''
<section class="page">
  {hdr("GXK12:2 · UX", n)}
  <div class="body grid">
    <div style="grid-column:1/7" class="col gap3">
      <div>
        <div class="kicker mb1">06 — {t("Decisiones de UX/UI", "UX/UI decisions")}</div>
        <h2 class="h-m">{t("“Encontrá rápido lo que viniste a buscar para tener más tiempo de descubrir lo que todavía no sabías que querías.”", "“Find what you came for fast, so you have more time to discover what you didn’t know you wanted.”")}</h2>
      </div>
      <div class="row gap2">
        <div class="panel-ink flex1" style="padding:4mm"><div class="kicker">{t("Quiero comprar", "I want to buy")}</div><div class="small mt1">{buy}</div></div>
        <div class="panel flex1" style="padding:4mm"><div class="kicker">{t("Quiero explorar", "I want to explore")}</div><div class="small mt1">{exp}</div></div>
      </div>
      <div class="small muted">{t("Dos velocidades en un mismo producto: la compra no puede perder claridad por la exploración, y la exploración no puede sentirse como un catálogo.", "Two speeds in one product: buying can’t lose clarity because of exploration, and exploration can’t feel like a catalogue.")}</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:4mm 5mm">{rows}</div>
    </div>
    <div style="grid-column:8/13" class="col gap3">
      {nfig("img/gxk/fig-carrito-confirmacion.jpg", t("Confirmación al agregar · desktop. Diseño aprobado en Figma (Etapa 1). Imágenes de producto como marcadores.", "Add-to-cart confirmation · desktop. Approved design in Figma (Stage 1). Product images are placeholders."))}
      <div class="flex1"></div>
      <div>
        <div class="kicker mb2">{t("Recorrido de compra diseñado", "Designed purchase journey")}</div>
        <div class="row gap1">{fl}</div>
        <div class="small muted mt2">{t("Cada paso tiene sus estados: vacío, carga, error, sin stock y confirmación, en desktop y mobile.", "Each step has its states: empty, loading, error, out of stock and confirmation, on desktop and mobile.")}</div>
      </div>
    </div>
  </div>
</section>'''


@page
def gxk_ui1(n):
    return f'''
<section class="page sand">
  {hdr("GXK12:2 · " + t("Interfaces", "Interfaces"), n)}
  <div class="body col">
    <div class="grid" style="align-items:end">
      <div style="grid-column:1/6">
        <div class="kicker mb1">07 — {t("Diseño de interfaces", "Interface design")}</div>
        <h2 class="h-m" style="font-size:22pt">{t("Tienda y ficha: <span class='ser wine-t'>tipografía protagonista,</span> información sin ruido.", "Store and product page: <span class='ser wine-t'>type-led,</span> information without noise.")}</h2>
      </div>
      <div style="grid-column:7/10" class="small">{t("La ficha responde a la Bible: fotos grandes, nombre, tipo, precio, talle, color, guía de talles, composición, envíos, cambios y consulta por WhatsApp con el producto ya escrito.", "The product page follows the Bible: large photos, name, type, price, size, colour, size guide, composition, shipping, returns and a WhatsApp query with the product already filled in.")}</div>
      <div style="grid-column:10/13" class="small muted">{t("En mobile, la acción de compra queda fija abajo y dice qué falta elegir. Las fotos son marcadores: el sistema se valida antes que la producción fotográfica.", "On mobile, the buy action stays pinned and says what’s still missing. Photos are placeholders: the system is validated before the photo shoot.")}</div>
    </div>
    <div class="flex1"></div>
    <div class="row between" style="align-items:flex-start">
      {nfig("img/gxk/fig-tienda-desktop-crop.jpg", t("Tienda · desktop · filtros abiertos", "Store · desktop · filters open"), h="92mm")}
      {nfig("img/gxk/fig-pdp-desktop-crop.jpg", t("Ficha de producto · desktop", "Product page · desktop"), h="92mm")}
      {nfig("img/gxk/fig-pdp-mobile-crop.jpg", t("Ficha · mobile", "Product · mobile"), h="92mm")}
    </div>
    <div class="cap mt2">{t("Diseños aprobados de la Etapa 1 · Figma.", "Approved Stage 1 designs · Figma.")}</div>
  </div>
</section>'''


@page
def gxk_ui2(n):
    return f'''
<section class="page">
  {hdr("GXK12:2 · " + t("Interfaces", "Interfaces"), n)}
  <div class="body row gap3">
    <div class="row gap2" style="align-items:flex-start">
      {nfig("img/gxk/fig-checkout-pago.jpg", t("Checkout · paso 3, pago y revisión · desktop. Medios definidos por la Bible: Mercado Pago, reserva 50/50 y efectivo en la entrega.", "Checkout · step 3, payment and review · desktop. Methods set by the Bible: Mercado Pago, 50/50 deposit and cash on delivery."), h="96mm")}
      {nfig("img/gxk/fig-checkout-mobile.jpg", t("Checkout · mobile", "Checkout · mobile"), h="96mm")}
    </div>
    <div class="col gap3 flex1">
      {nfig("img/gxk/fig-admin-inicio.jpg", t("Admin · Inicio. Los números son <b>datos de ejemplo</b>, rotulados así en el propio diseño.", "Admin · Home. Figures are <b>sample data</b>, labelled as such in the design itself."))}
      <div class="flex1"></div>
      <div class="panel col gap1">
        <div class="kicker">{t("Panel de gestión", "Management panel")}</div>
        <div class="h-s">{t("“Lo que pide acción va primero.”", "“What needs action comes first.”")}</div>
        <div class="small muted">{t("Un único administrador inicial, sin conocimientos técnicos: pedidos por preparar, incidencias y stock bajo (≤ 3 unidades) arriba; la lectura general, después. Principio compartido con Raíces: <i>mucha lógica detrás, poca fricción delante.</i>", "A single initial admin with no technical background: orders to prepare, incidents and low stock (≤ 3 units) on top; the general overview after. A principle shared with Raíces: <i>lots of logic behind, little friction in front.</i>")}</div>
      </div>
    </div>
  </div>
</section>'''


@page
def gxk_arch(n):
    svc = ["catalog", "cart", "checkout", "orders", "payments", "inventory", "shipping", "emails", "familia", "outfits", "universe", "analytics"]
    chips = "".join(f'<span class="mono" style="font-size:6.2pt;border:1px solid var(--line-inv);padding:1mm 1.6mm;margin:0 1mm 1.2mm 0;display:inline-block">{s}</span>' for s in svc)
    dec = [
        (t("Stock por variante", "Stock per variant"), t("Producto + talle + color con restricción de unicidad. El producto no guarda stock total.", "Product + size + colour with a uniqueness constraint. The product holds no total stock.")),
        (t("Pedidos como fotografía", "Orders as snapshots"), t("Cada ítem guarda nombre, variante, SKU y precio del momento de compra.", "Each item stores name, variant, SKU and price at the moment of purchase.")),
        (t("Seguimiento sin cuenta", "Tracking without an account"), t("Acceso al pedido con un token impredecible; se guarda solo su hash.", "Order access via an unpredictable token; only its hash is stored.")),
        (t("Pago confirmado por servidor", "Server-confirmed payment"), t("El estado depende del webhook de Mercado Pago, no del retorno del navegador.", "Status depends on Mercado Pago’s webhook, not on the browser redirect.")),
        (t("Proveedores desacoplados", "Decoupled providers"), t("Andreani y Correo Argentino detrás de adaptadores: se pueden sumar o cambiar sin tocar el núcleo.", "Andreani and Correo Argentino sit behind adapters: they can be added or swapped without touching the core.")),
    ]
    drows = "".join(f'<tr><td>{a}</td><td class="muted">{b}</td></tr>' for a, b in dec)
    return f'''
<section class="page">
  {hdr("GXK12:2 · " + t("Arquitectura y desarrollo", "Architecture and development"), n)}
  <div class="roomy body grid">
    <div style="grid-column:1/7" class="col gap2">
      <div class="kicker">08 — {t("Arquitectura", "Architecture")}</div>
      <div class="panel-ink col" style="padding:6mm;flex:1;justify-content:space-around">
        <div class="row gap1">
          <div class="box flex1" style="padding:2.6mm"><div class="kicker">Storefront</div><div class="small">{t("tienda pública", "public store")}</div></div>
          <div class="box flex1" style="padding:2.6mm"><div class="kicker">Admin</div><div class="small">{t("panel privado", "private panel")}</div></div>
          <div class="box flex1" style="padding:2.6mm;border-style:dashed"><div class="kicker">Desktop</div><div class="small">{t("a futuro", "future")}</div></div>
        </div>
        <div class="mono" style="text-align:center;font-size:16pt;color:var(--peach);line-height:1">↓</div>
        <div class="box" style="padding:3mm;border-color:var(--peach)">
          <div class="row between"><div class="h-s" style="font-size:10.5pt">GXK Core</div><div class="cap">Next.js · TypeScript · {t("lógica de negocio en servidor", "server-side business logic")}</div></div>
          <div class="mt1">{chips}</div>
        </div>
        <div class="mono" style="text-align:center;font-size:16pt;color:var(--peach);line-height:1">↓</div>
        <div class="row gap1">
          <div class="box flex1" style="padding:2.6mm"><div class="kicker">Supabase</div><div class="small">PostgreSQL · Auth · Storage · RLS</div></div>
          <div class="box flex1" style="padding:2.6mm"><div class="kicker">Mercado Pago</div><div class="small">{t("pagos · webhook", "payments · webhook")}</div></div>
          <div class="box flex1" style="padding:2.6mm"><div class="kicker">{t("Logística", "Logistics")}</div><div class="small">Andreani · Correo Arg.</div></div>
        </div>
      </div>
      <div class="cap">{t("Tres superficies sobre un mismo backend y una misma lógica de negocio. Verificado en el repositorio (README, ARCHITECTURE.md y estructura de src/).", "Three surfaces on one backend and one set of business logic. Verified in the repository (README, ARCHITECTURE.md and src/ structure).")}</div>
    </div>
    <div style="grid-column:8/13" class="col gap2">
      <div class="kicker">09 — {t("Decisiones técnicas", "Technical decisions")}</div>
      <table class="t" style="font-size:8.8pt"><tbody>{drows}</tbody></table>
      <div class="kicker mt2">10 — {t("Herramientas confirmadas en el proyecto", "Tools confirmed in the project")}</div>
      <div class="small">Figma · Claude Design · Claude Code · GitHub · Linear · Obsidian · Supabase · Vercel (Preview)</div>
      <div class="small muted">{t("Calidad: pruebas unitarias, TypeScript, ESLint y pruebas de navegador como puerta antes de integrar.", "Quality: unit tests, TypeScript, ESLint and browser tests as a gate before merging.")}</div>
    </div>
  </div>
</section>'''


@page
def gxk_status(n):
    rows = [
        (status("ok", t("Aprobado", "Approved")), t("Diseño · Etapa 1", "Design · Stage 1"), t("Diseños aprobados consolidados en Figma: 14 áreas en desktop y mobile, de la tienda al Admin, incluidos estados de error y carga.", "Approved designs consolidated in Figma: 14 areas on desktop and mobile, from store to Admin, including error and loading states.")),
        (status("ok", t("Implementado", "Implemented")), "Home", t("En la rama principal del repositorio; la implementación es la fuente de verdad de la Home.", "On the repository’s main branch; the implementation is the Home’s source of truth.")),
        (status("wip", t("En rama", "On branch")), t("Compra y contenido", "Purchase and content"), t("Checkout, estado del pedido, páginas de contenido y cuenta, y lógica de disponibilidad del carrito: implementados en ramas de trabajo, sin integrar ni publicar.", "Checkout, order status, content and account pages, and cart availability logic: implemented on working branches, not yet merged or published.")),
        (status("pend", t("Pendiente", "Pending")), t("Integraciones reales", "Live integrations"), t("Mercado Pago y envíos en producción; los adaptadores de Andreani y Correo Argentino aún no hacen llamadas reales. Proveedor de email por definir.", "Mercado Pago and shipping in production; the Andreani and Correo Argentino adapters don’t make live calls yet. Email provider to be defined.")),
        (status("pend", t("Próximo", "Next")), t("Beta", "Beta"), t("QA integral y beta de presentación para el dueño de GXK (objetivo: 30/11/2026); luego beta comercial y lanzamiento.", "Full QA and a presentation beta for GXK’s owner (target: 30 Nov 2026); then a commercial beta and launch.")),
    ]
    tr = "".join(f'<tr><td style="width:30mm">{a}</td><td style="width:36mm">{b}</td><td class="muted" style="font-weight:400">{c}</td></tr>' for a, b, c in rows)
    learn = [
        (t("Diseñar antes de implementar.", "Design before implementing."), t("Un agente de IA rinde mejor como implementador cuando la dirección visual ya está decidida.", "An AI agent works best as an implementer once the visual direction is decided.")),
        (t("Una simulación no es una integración.", "A simulation isn’t an integration."), t("Lo probado contra datos simulados se reporta como tal, nunca como funcionalidad terminada.", "What’s tested against mocked data is reported as such, never as a finished feature.")),
        (t("Aprobado ≠ implementado ≠ publicado.", "Approved ≠ implemented ≠ published."), t("Separar estos estados evita confundir avance con entrega.", "Keeping these states apart avoids confusing progress with delivery.")),
    ]
    lr = "".join(f'<div style="border-top:1.5px solid var(--sand);padding-top:2.4mm"><div class="h-s" style="font-size:10.5pt">{a}</div><div class="small muted">{b}</div></div>' for a, b in learn)
    return f'''
<section class="page">
  {hdr("GXK12:2 · " + t("Estado y aprendizajes", "Status and learnings"), n)}
  <div class="roomy body grid">
    <div style="grid-column:1/8" class="col gap2">
      <div class="kicker">11 — {t("Estado actual · noviembre 2026", "Current status · November 2026")}</div>
      <h2 class="h-m">{t("Lo que está aprobado, lo que está construido <span class='ser wine-t'>y lo que falta.</span>", "What’s approved, what’s built <span class='ser wine-t'>and what’s left.</span>")}</h2>
      <table class="t mt1" style="font-size:9pt"><tbody>{tr}</tbody></table>
    </div>
    <div style="grid-column:9/13" class="panel-pet col gap3">
      <div class="kicker">12 — {t("Conclusiones y aprendizajes", "Conclusions and learnings")}</div>
      {lr}
      <div class="flex1"></div>
      <div class="cap">{t("Sin métricas comerciales: el producto todavía no está lanzado.", "No commercial metrics: the product hasn’t launched yet.")}</div>
    </div>
  </div>
</section>'''


# ================================================================ RAÍCES
@page
def raices_open(n):
    meta = [
        (t("Tipo", "Type"), t("Plataforma digital de turismo de aventura", "Digital platform for adventure travel")),
        (t("Rol", "Role"), t("Estrategia, arquitectura, UX/UI, diseño, desarrollo y documentación", "Strategy, architecture, UX/UI, design, development and documentation")),
        (t("Estado", "Status"), t("Sitio público operativo · Admin en desarrollo", "Public site live · Admin in development")),
        ("Stack", "HTML · CSS · JavaScript · Supabase"),
    ]
    return f'''
<section class="page petrol" style="background:#0f2d2b">
  <img src="img/raices/web-home-hero.jpg" class="abs" style="left:0;top:0;width:297mm;height:132mm;object-fit:cover;object-position:center 72%" alt="">
  <div class="abs" style="left:0;top:0;width:297mm;height:132mm;background:linear-gradient(180deg,rgba(15,45,43,.55) 0%,rgba(15,45,43,0) 22%)"></div>
  {hdr(t("05 · Caso de estudio", "05 · Case study"), n)}
  <div class="abs cap" style="right:14mm;top:126mm;color:#FFE7CE">{t("Home del sitio público — captura de proyectoraices.com.ar", "Public site home — screenshot of proyectoraices.com.ar")}</div>
  <div class="abs" style="left:14mm;top:137mm;right:14mm" >
    <div class="grid" style="height:auto">
      <div style="grid-column:1/7">
        <div class="kicker"><span class="n">05</span>{t("Caso 02", "Case 02")}</div>
        <h2 class="h-xl mt1" style="font-size:52pt">{t("Proyecto <span class='ser peach-t'>Raíces</span>", "Proyecto <span class='ser peach-t'>Raíces</span>")}</h2>
        <p class="small mt1" style="color:#FFE7CE">{t("“Viajes para conectar con cada lugar.” La evolución de una plataforma digital: de un sitio funcional a un sistema preparado para crecer.", "“Journeys to connect with every place.” The evolution of a digital platform: from a working site to a system ready to grow.")} <a class="u" href="{RAICES_URL}">proyectoraices.com.ar</a></p>
      </div>
      <div style="grid-column:7/13;display:grid;grid-template-columns:1fr 1fr;gap:3mm 5mm;align-content:start">{meta_row(meta, True)}</div>
    </div>
  </div>
</section>'''


@page
def raices_context(n):
    role = [t("Estrategia de producto", "Product strategy"), t("Conceptualización", "Concept"), t("Arquitectura", "Architecture"), t("Experiencia de usuario", "User experience"), t("Diseño", "Design"), t("Desarrollo", "Development"), t("Organización y documentación", "Organisation and documentation")]
    lis = "".join(f"<li>{r}</li>" for r in role)
    tree = lambda title, kind, lines, accent: f'''<div class="flex1 col" style="border:1px solid var(--line);padding:4mm">
        <div class="row between"><div class="h-s">{title}</div><div class="kicker" style="color:{accent}">{kind}</div></div>
        <div class="col mt2" style="gap:0">{"".join(f'<div class="row" style="align-items:center"><div class="mono" style="width:{4+i*4}mm;color:{accent};font-size:7pt;text-align:right;padding-right:1.5mm">{"└" if i else "●"}</div><div class="small">{l}</div></div>' for i, l in enumerate(lines))}</div></div>'''
    return f'''
<section class="page">
  {hdr(t("Proyecto Raíces · Contexto y arquitectura", "Proyecto Raíces · Context and architecture"), n)}
  <div class="roomy body grid">
    <div style="grid-column:1/5" class="col gap3">
      <div>
        <div class="kicker mb1">01 — {t("Presentación y contexto", "Overview and context")}</div>
        <p>{t("Proyecto Raíces propone tours, travesías y paquetes en Argentina y Perú que combinan naturaleza, aventura, cultura y encuentros, lejos del modelo tradicional de agencia.", "Proyecto Raíces offers tours, treks and packages in Argentina and Peru that combine nature, adventure, culture and encounters, far from the traditional agency model.")}</p>
      </div>
      <div>
        <div class="kicker mb1">02 — {t("Objetivo y oportunidad", "Goal and opportunity")}</div>
        <p class="small">{t("Que la web se sienta como una propuesta de experiencias y no como una agencia genérica: fotografía y relato trabajando juntos, navegación clara y un camino simple para consultar y reservar.", "A website that feels like a proposal of experiences rather than a generic agency: photography and storytelling working together, clear navigation and a simple path to ask and book.")}</p>
        <p class="small muted">{t("También fue el proyecto donde validé mi metodología de trabajo.", "It was also the project where I validated my working method.")}</p>
      </div>
      <div>
        <div class="kicker mb1">03 — {t("Mi rol", "My role")}</div>
        <ul class="l tight small" style="columns:2;column-gap:4mm">{lis}</ul>
      </div>
    </div>
    <div style="grid-column:6/13" class="col gap2">
      <div class="kicker">07 — {t("Arquitectura de información", "Information architecture")}</div>
      <h2 class="h-m">{t("Dos puertas, un solo catálogo. <span class='ser wine-t'>La separación es deliberada.</span>", "Two doors, one catalogue. <span class='ser wine-t'>The split is deliberate.</span>")}</h2>
      <div class="row gap2 mt1">
        {tree(t("Experiencias", "Experiences"), t("Catálogo", "Catalogue"), [t("Todas las experiencias", "All experiences"), t("Tours · Travesías · Paquetes", "Tours · Treks · Packages"), t("Filtros por destino", "Filter by destination"), t("Ficha de experiencia", "Experience page")], "#9E1F32")}
        {tree(t("Destinos", "Destinations"), "Editorial", [t("País", "Country"), t("Destino concreto", "Specific destination"), t("Relato e información del lugar", "Story and place information"), t("Experiencias relacionadas", "Related experiences")], "#1B5956")}
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:5mm" class="mt1">
        <div class="small"><b>{t("Sin duplicar.", "No duplication.")}</b> <span class="muted">{t("Destinos es una puerta editorial hacia el catálogo, no un segundo catálogo. Patagonia funciona como contexto geográfico, no como destino navegable.", "Destinations is an editorial door into the catalogue, not a second catalogue. Patagonia works as geographic context, not as a navigable destination.")}</span></div>
        <div class="small"><b>{t("Una plantilla, muchos destinos.", "One template, many destinations.")}</b> <span class="muted">{t("Una única página de destino reutilizada por parámetro de URL, alimentada desde la misma fuente de datos que el catálogo.", "A single destination page reused through a URL parameter, fed by the same data source as the catalogue.")}</span></div>
      </div>
      <div class="flex1"></div>
      {nfig("img/raices/web-experiencias.jpg", t("Catálogo de Experiencias implementado: filtros por tipo y por destino. Sitio público, desktop.", "Implemented Experiences catalogue: filters by type and destination. Public site, desktop."), w="125mm")}
    </div>
  </div>
</section>'''


@page
def raices_visual(n):
    pal = [("#8ba6b7", t("Azul", "Blue")), ("#8d4b12", t("Marrón", "Brown")), ("#ff5b28", t("Naranja", "Orange")), ("#e9e073", t("Amarillo", "Yellow")), ("#43612f", t("Verde", "Green")), ("#6a7133", t("Oliva", "Olive"))]
    sw = "".join(f'<div class="col" style="flex:1"><div style="height:9mm;background:{c}"></div><div class="cap mt1">{nme}<br>{c}</div></div>' for c, nme in pal)
    dirs = ["Territorio monumental", "Cartografía viva", "Atlas humano", "Secuencia de expedición", "Periódico de montaña", "Señal abierta"]
    return f'''
<section class="page">
  {hdr(t("Proyecto Raíces · Proceso de diseño", "Proyecto Raíces · Design process"), n)}
  <div class="body grid">
    <div style="grid-column:1/5" class="col gap3">
      <div>
        <div class="kicker mb1">04 — {t("Conceptualización", "Concept")} · 05 — {t("Proceso de diseño", "Design process")}</div>
        <h2 class="h-m">{t("“La web no tiene que parecer una web de turismo. <span class='ser wine-t'>Tiene que parecer Raíces.</span>”", "“The site shouldn’t look like a travel website. <span class='ser wine-t'>It should look like Raíces.</span>”")}</h2>
      </div>
      <p class="small">{t("Desde una biblioteca de referencias se extrajo un <b>ADN visual</b>: color, tipografía, fotografía, composición, navegación, recursos gráficos y movimiento. No es una página: son reglas para construir una Raíces propia.", "A <b>visual DNA</b> was distilled from a reference library: colour, type, photography, composition, navigation, graphic resources and motion. It isn’t a page: it’s a set of rules for building a Raíces of its own.")}</p>
      <div>
        <div class="kicker mb1">{t("Identidad vigente", "Current identity")}</div>
        <div class="row gap1">{sw}</div>
        <div class="small muted mt1">Alte Haas Grotesk · Cascadia Mono · Arial Rounded</div>
      </div>
      <div class="box">
        <div class="kicker mb1">{t("Seis direcciones exploradas para la Home", "Six directions explored for the Home")}</div>
        <div class="small">{" · ".join(dirs)}</div>
        <div class="mt1">{status("exp", t("Exploraciones · no aprobadas", "Explorations · not approved"))}</div>
      </div>
    </div>
    <div style="grid-column:5/9" class="col gap1">
      {nfig("img/raices/fig-visual-dna.jpg", t("Raíces / Visual DNA — tablero en Figma.", "Raíces / Visual DNA — Figma board."))}
    </div>
    <div style="grid-column:9/13" class="col gap1">
      <div class="flex1"></div>{nfig("img/raices/fig-exploracion-periodico.jpg", t("Dirección “Periódico de montaña” — exploración en Figma, no implementada. Textos y fechas de la maqueta son de muestra.", "“Mountain newspaper” direction — Figma exploration, not implemented. Mock copy and dates are placeholders."))}
    </div>
  </div>
</section>'''


@page
def raices_ui(n):
    dec = [
        (t("Contrato de la ficha", "Experience page contract"), t("Detalle = lo esencial para decidir. Itinerario = para imaginar el viaje. Los campos sin dato real se ocultan; nunca se completan por inferencia.", "Details = what you need to decide. Itinerary = what helps you imagine the trip. Fields without real data are hidden, never filled by inference.")),
        (t("Sistema de cards", "Card system"), t("Contenedor de imagen compartido con proporción constante. Las inconsistencias se resuelven en el sistema, no foto por foto.", "A shared image container with a constant ratio. Inconsistencies are fixed in the system, not photo by photo.")),
        (t("La foto manda", "Photography leads"), t("Paisajes y personas reales; sin overlays que tapen la imagen ni recortes que pierdan el punto focal.", "Real landscapes and people; no overlays hiding the image or crops that lose the focal point.")),
        (t("Un camino a la consulta", "One path to enquiry"), t("CTA principal “Reserva ahora”; las consultas van a WhatsApp con la experiencia ya nombrada. No es un e-commerce.", "Main CTA “Book now”; enquiries go to WhatsApp with the experience already named. It isn’t an e-commerce site.")),
    ]
    rows = "".join(f'<div style="border-top:1px solid var(--line);padding-top:2mm"><div class="h-s" style="font-size:10pt">{a}</div><div class="small muted">{b}</div></div>' for a, b in dec)
    return f'''
<section class="page sand">
  {hdr(t("Proyecto Raíces · UX/UI implementada", "Proyecto Raíces · Implemented UX/UI"), n)}
  <div class="body grid" style="grid-template-rows:auto auto;row-gap:6mm;align-content:space-between">
    <div style="grid-column:1/5;grid-row:1/3" class="col gap2">
      <div class="kicker">06 — {t("Decisiones de UX/UI", "UX/UI decisions")}</div>
      <h2 class="h-m">{t("Una experiencia de viaje clara y editorial, <span class='ser wine-t'>no una ficha técnica.</span>", "A clear, editorial travel experience, <span class='ser wine-t'>not a spec sheet.</span>")}</h2>
      <div class="col gap2 mt1">{rows}</div>
      <div class="flex1"></div>
      <div>{status("ok", t("Implementado · sitio público", "Implemented · public site"))}</div>
    </div>
    <div style="grid-column:5/13;grid-row:1" class="row gap3">
      <div style="flex:1.4">{nfig("img/raices/web-home-experiencias.jpg", t("Home · “Momentos para vivir distinto”: carrusel de experiencias filtrable por tipo.", "Home · “Moments to live differently”: experience carousel filtered by type."))}</div>
      <div class="col between" style="flex:.6"><div class="lead-ser" style="font-size:16pt">{t("“Mucha lógica detrás, poca fricción delante.”", "“Lots of logic behind, little friction in front.”")}</div><div class="small muted">{t("Principio de interfaz compartido con GXK12:2: la complejidad del modelo se resuelve por dentro.", "Interface principle shared with GXK12:2: the model’s complexity is solved on the inside.")}</div></div>
    </div>
    <div style="grid-column:5/13;grid-row:2" class="row gap2">
      <div style="flex:1.4">{nfig("img/raices/web-ficha.jpg", t("Ficha de experiencia · Travesía Salkantay Trek: detalle esencial, aviso de modalidad privada y un único CTA.", "Experience page · Salkantay Trek: essential details, private-option note and a single CTA."))}</div>
      <div class="col end" style="flex:.6">
        <div class="cap">{t("Capturas del sitio público proyectoraices.com.ar (desktop), aportadas por Ignacio.", "Screenshots of the public site proyectoraices.com.ar (desktop), provided by Ignacio.")}</div>
      </div>
    </div>
  </div>
</section>'''


@page
def raices_dev(n):
    tl = [
        (t("Sep 2026", "Sep 2026"), t("Datos a Supabase", "Data moves to Supabase"), t("El contenido deja archivos JS planos y pasa a una base de datos con una única capa de acceso.", "Content leaves flat JS files for a database with a single access layer.")),
        (t("Sep 2026", "Sep 2026"), t("Bilingüe y QA", "Bilingual and QA"), t("Textos ES/EN y pruebas end-to-end con Playwright.", "ES/EN copy and end-to-end tests with Playwright.")),
        ("28.09", t("Etapa funcional cerrada", "Functional stage closed"), t("Con la base estable, el foco pasa a UX/UI y dirección visual.", "With a stable base, focus shifts to UX/UI and visual direction.")),
        ("05.10", "System Reset", t("Foundation → Components → Patterns → Pages → Content. Se migra progresivamente; no se rehace.", "Foundation → Components → Patterns → Pages → Content. Migrate progressively; don’t rebuild.")),
        (t("Oct 2026", "Oct 2026"), "Admin / CMS", t("Admin → modelo de contenido → Supabase → DataAPI → páginas. El Admin gestiona entidades, no la presentación.", "Admin → content model → Supabase → DataAPI → pages. The Admin manages entities, not presentation.")),
        ("26.10", t("Revisión estratégica", "Strategic review"), t("Paquetes como prioridad comercial y guías locales como nuevo eje. Registrado; arquitectura nueva aún sin aprobar.", "Packages as the commercial priority and local guides as a new axis. Recorded; new architecture not yet approved.")),
    ]
    rows = "".join(f'''<div class="row gap2" style="border-top:1px solid var(--line-inv);padding:2mm 0">
        <div class="mono peach-t" style="width:15mm;font-size:6.6pt;padding-top:.6mm">{a}</div>
        <div style="width:36mm;font-size:12pt" class="h-s" >{b}</div><div class="muted flex1" style="font-size:8.8pt">{c}</div></div>''' for a, b, c in tl)
    st = [
        (status("ok", t("Operativo", "Live")), t("Sitio público", "Public site")),
        (status("wip", t("En desarrollo", "In development")), t("Admin / CMS de contenidos, en verificación", "Content Admin / CMS, under verification")),
        (status("pend", t("En pausa", "Paused")), t("Nuevas migraciones, hasta confirmar un respaldo restaurable de la base", "New migrations, until a restorable database backup is confirmed")),
        (status("pend", t("Por aprobar", "To approve")), t("Reestructuración: paquetes y guías locales", "Restructure: packages and local guides")),
    ]
    strow = "".join(f'<div class="col gap1" style="padding:1.6mm 0;border-top:1px solid var(--line)"><div>{a}</div><div class="small">{b}</div></div>' for a, b in st)
    learn = [t("Primero el modelo y el sistema; después el Admin.", "Model and system first; Admin second."), t("Preservar lo que funciona y migrar por capas.", "Preserve what works and migrate layer by layer."), t("Con datos reales, primero el respaldo.", "With real data, backups come first.")]
    return f'''
<section class="page">
  {hdr(t("Proyecto Raíces · Desarrollo y evolución", "Proyecto Raíces · Development and evolution"), n)}
  <div class="body grid">
    <div style="grid-column:1/8" class="panel-pet col gap2" style="">
      <div class="kicker">08 — {t("Desarrollo tecnológico y evolución", "Technical development and evolution")}</div>
      <div class="small" style="color:#FFE7CE">{t("HTML, CSS y JavaScript sin framework · Supabase · i18n ES/EN · Playwright. Una sola capa (<span class='mono'>data-api.js</span>) conoce la base de datos; el resto del sitio no.", "HTML, CSS and framework-free JavaScript · Supabase · ES/EN i18n · Playwright. A single layer (<span class='mono'>data-api.js</span>) knows the database; the rest of the site doesn’t.")}</div>
      <div class="col flex1" style="justify-content:space-evenly">{rows}</div>
    </div>
    <div style="grid-column:8/13" class="col gap2">
      <div class="kicker">11 — {t("Estado actual · noviembre 2026", "Current status · November 2026")}</div>
      <div class="col">{strow}</div>
      <div class="kicker mt2">12 — {t("Aprendizajes", "Learnings")}</div>
      <ul class="l small">{"".join(f"<li>{x}</li>" for x in learn)}</ul>
      <div class="flex1"></div>
      <div class="cap">{t("Fuentes: documentación del proyecto (Obsidian), repositorio proyecto-raices y archivo Figma. Herramientas confirmadas: Figma, Claude Design, Claude Code, GitHub, Linear, Supabase, Playwright, Cloudflare.", "Sources: project documentation (Obsidian), proyecto-raices repository and Figma file. Confirmed tools: Figma, Claude Design, Claude Code, GitHub, Linear, Supabase, Playwright, Cloudflare.")}</div>
    </div>
  </div>
</section>'''


# ================================================================ LAB
@page
def lab(n):
    layers = [("Obsidian", t("conocimiento", "knowledge")), ("Linear", t("trabajo", "work")), ("Figma", t("fuente visual", "visual source")), ("GitHub", t("código", "code")), ("Claude Design", t("exploración", "exploration")), ("Claude Code", t("ejecución", "execution"))]
    lay = "".join(f'<div class="row between" style="border-top:1px solid var(--line-inv);padding:1.6mm 0"><span class="small"><b>{a}</b></span><span class="mono" style="font-size:6.4pt;color:var(--peach)">{b}</span></div>' for a, b in layers)
    slots = [(t("Exploración 3D", "3D exploration")), (t("Exploración audiovisual", "Audiovisual exploration")), (t("Experimentos con IA", "AI experiments"))]
    sl = "".join(f'<div class="col between" style="border:1px dashed var(--ink2);padding:3mm;flex:1;min-height:30mm"><div class="kicker" style="color:var(--ink2)">{t("Espacio reservado", "Reserved space")}</div><div class="h-s" style="color:var(--ink2)">{s}</div></div>' for s in slots)
    return f'''
<section class="page">
  {hdr(t("06 · Laboratorio", "06 · Lab"), n)}
  <div class="body grid">
    <div style="grid-column:1/5" class="col between">
      <div>
        <div class="kicker"><span class="n">06</span>{t("Laboratorio creativo", "Creative lab")}</div>
        <h2 class="h-l mt3">{t("Curiosidad <span class='ser wine-t'>con método.</span>", "Curiosity <span class='ser wine-t'>with a method.</span>")}</h2>
        <p class="mt2">{t("La experimentación no vive aparte: aparece dentro de los proyectos —seis direcciones para una Home, un laboratorio de reglas visuales, prototipos de interacción— y en la forma de trabajar.", "Experimentation doesn’t live apart: it shows up inside the projects —six directions for one Home, a visual-rules lab, interaction prototypes— and in the way I work.")}</p>
      </div>
      <div class="small muted">{t("Exploraciones documentadas en los casos: Raíces (Visual DNA y direcciones de Home) y GXK12:2 (Visual Rules Lab V0.2, prototipos de motion en Figma).", "Explorations documented in the cases: Raíces (Visual DNA and Home directions) and GXK12:2 (Visual Rules Lab V0.2, motion prototypes in Figma).")}</div>
    </div>
    <div style="grid-column:5/9" class="panel-ink col gap2">
      <div class="kicker">{t("Experimento en curso", "Ongoing experiment")} · MACARIO</div>
      <div class="h-m" style="font-size:17pt">{t("Un sistema propio para construir productos digitales con IA.", "My own system for building digital products with AI.")}</div>
      <div class="small muted">{t("Organiza el ciclo idea → research → producto → visual → UX/UI → arquitectura → desarrollo → QA → lanzamiento → iteración, y define qué decide una persona y qué ejecuta un agente. La autonomía del agente cubre <i>cómo</i> ejecutar lo aprobado, nunca <i>qué</i> se construye; integrar, publicar o tocar datos reales requiere autorización explícita.", "It organises the cycle idea → research → product → visual → UX/UI → architecture → development → QA → release → iteration, and defines what a person decides and what an agent executes. Agent autonomy covers <i>how</i> to execute what’s approved, never <i>what</i> gets built; merging, publishing or touching real data needs explicit authorisation.")}</div>
      <div class="col flex1" style="justify-content:flex-end">{lay}</div>
    </div>
    <div style="grid-column:9/13" class="col gap2">
      <div class="kicker">{t("Próximas exploraciones", "Upcoming explorations")}</div>
      <div class="small muted">{t("Este espacio está preparado para sumar trabajo nuevo a medida que exista. No contiene piezas todavía.", "This space is ready to hold new work as it happens. It contains no pieces yet.")}</div>
      <div class="col gap2 flex1">{sl}</div>
    </div>
  </div>
</section>'''


# ================================================================ FORMACIÓN
@page
def education(n):
    ic = [t("Desarrollo y diseño conceptual de videojuegos", "Game development and concept design"), t("Diseño de experiencias interactivas, incluido diseño UX/UI", "Interactive experience design, including UX/UI"), t("Documentación para facilitar la comunicación del equipo", "Documentation to support team communication"), t("Trabajo colaborativo en equipos multidisciplinarios", "Collaboration in multidisciplinary teams"), t("Procesos iterativos basados en feedback del equipo y del cliente", "Iterative processes driven by team and client feedback"), t("Organización y planificación de tareas en proyectos grupales", "Task organisation and planning in group projects"), t("Foco en la experiencia del cliente y la interacción con el producto", "Focus on customer experience and product interaction")]
    return f'''
<section class="page">
  {hdr(t("07 · Formación", "07 · Education"), n)}
  <div class="roomy body grid">
    <div style="grid-column:1/4" class="col between">
      <div>
        <div class="kicker"><span class="n">07</span>{t("Formación", "Education")}</div>
        <h2 class="h-l mt3">{t("Diseñar <span class='ser wine-t'>experiencias</span> antes que pantallas.", "Designing <span class='ser wine-t'>experiences</span> before screens.")}</h2>
      </div>
      <div class="num">07</div>
    </div>
    <div style="grid-column:5/10" class="col gap2">
      <div class="coord">Image Campus · Buenos Aires, Monserrat</div>
      <div class="h-m">{t("Tecnicatura en Producción y Diseño Conceptual de Videojuegos", "Technical Degree in Video Game Production and Concept Design")}</div>
      <div class="kicker">Game Design</div>
      <div class="rule mt1 mb1"></div>
      <ul class="l">{"".join(f"<li>{x}</li>" for x in ic)}</ul>
    </div>
    <div style="grid-column:10/13" class="col gap3">
      <div class="panel col gap1">
        <div class="coord">{t("Formación complementaria", "Additional training")}</div>
        <div class="h-s">Branding</div>
        <div class="small muted">{t("Identidad de marca y disciplinas vinculadas al diseño y la comunicación visual.", "Brand identity and disciplines related to design and visual communication.")}</div>
      </div>
      <div class="box col gap1">
        <div class="coord">{t("Idiomas", "Languages")}</div>
        <div class="h-s">{t("Español · Inglés", "Spanish · English")}</div>
      </div>
    </div>
  </div>
</section>'''


@page
def tools(n):
    groups = [
        ("ux", t("Diseño y producción visual", "Design and visual production"), ["Figma", "Adobe Photoshop", "Adobe Premiere"]),
        ("pm", t("Gestión y organización", "Project management"), ["ClickUp", "Trello"]),
        ("sys", t("Análisis y visualización de datos", "Data analysis and visualisation"), ["Tableau"]),
        ("brand", t("Diseño y modelado de sistemas", "System design and modelling"), ["Machinations"]),
        ("tech", t("Inteligencia artificial", "Artificial intelligence"), ["Claude", t("Herramientas de IA aplicadas a diseño, desarrollo, investigación y procesos creativos", "AI tools for design, development, research and creative work")]),
    ]
    pos = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)]
    cards = ""
    for (k, g, items), (c, r) in zip(groups, pos):
        ch = "".join(f'<span class="chip">{x}</span>' for x in items)
        cards += f'''<div class="col gap1" style="grid-column:{c+1};grid-row:{r+1};border-top:1.5px solid var(--sand);padding-top:3mm">
            <div class="row between"><div class="h-s">{g}</div><div style="color:var(--peach)">{ICONS[k]}</div></div><div class="mt1">{ch}</div></div>'''
    return f'''
<section class="page petrol">
  {hdr(t("07 · Herramientas", "07 · Tools"), n)}
  <div class="body grid">
    <div style="grid-column:1/5" class="col between">
      <div>
        <div class="kicker">{t("Herramientas", "Tools")}</div>
        <h2 class="h-l mt3">{t("Herramientas por <span class='ser peach-t'>función,</span> no por logo.", "Tools by <span class='ser peach-t'>function,</span> not by logo.")}</h2>
        <p class="muted mt2">{t("Cada grupo cubre una parte del trabajo: imaginar y producir, organizar, entender datos, modelar sistemas y ampliar el proceso con IA. Se combinan según lo que pida cada proyecto.", "Each group covers part of the work: imagining and producing, organising, understanding data, modelling systems and extending the process with AI. They’re combined as each project requires.")}</p>
      </div>
      <div class="cap">{t("Herramientas de uso, sin niveles ni certificaciones. Las tecnologías de cada proyecto se detallan en sus casos.", "Tools I use, with no levels or certifications implied. Each project’s technologies are listed in its case.")}</div>
    </div>
    <div style="grid-column:6/13;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:auto auto;gap:9mm 6mm;align-content:center">
      {cards}
      <div class="col" style="grid-column:3;grid-row:2;justify-content:center"><div class="lead-ser" style="color:var(--peach);font-size:16pt">{t("Las herramientas cambian; el criterio para combinarlas se mantiene.", "Tools change; the judgement to combine them stays.")}</div></div>
    </div>
  </div>
</section>'''


@page
def contact(n):
    rows = [
        ("Email", EMAIL, f"mailto:{EMAIL}"),
        (t("Teléfono", "Phone"), PHONE_DISPLAY, PHONE_LINK),
        ("Instagram", IG_DISPLAY, IG),
    ]
    rr = "".join(f'<a href="{h}" class="row between" style="border-top:1px solid var(--line-inv);padding:3.4mm 0;align-items:baseline"><span class="kicker">{a}</span><span class="h-m" style="font-size:17pt">{b} <span class="peach-t">↗</span></span></a>' for a, b, h in rows)
    return f'''
<section class="page wine">
  {hdr(t("08 · Contacto", "08 · Contact"), n)}
  <div class="body grid">
    <div style="grid-column:1/7" class="col between">
      <div>
        <div class="kicker"><span class="n">08</span>{t("Contacto", "Contact")}</div>
        <h2 class="h-xxl mt3" style="font-size:80pt">{t("Conver<br>semos.", "Let’s<br>talk.")}</h2>
      </div>
      <p class="lead" style="max-width:115mm;color:#FFE7CE">{t("Estoy abierto a oportunidades laborales, proyectos freelance y colaboraciones creativas. Si tenés un proyecto donde diseño y tecnología necesitan hablar el mismo idioma, me encantaría conocerlo.", "I’m open to full-time roles, freelance projects and creative collaborations. If you have a project where design and technology need to speak the same language, I’d love to hear about it.")}</p>
    </div>
    <div style="grid-column:8/13" class="col end">
      <div class="h-s mb2" style="color:#FFE7CE">Ignacio Sconza</div>
      {rr}
      <div style="border-top:1px solid var(--line-inv)"></div>
      <div class="cap mt3" style="color:rgba(255,231,206,.75)">{t("Diseño · Desarrollo · Creatividad — Portfolio 2026", "Design · Development · Creativity — Portfolio 2026")}</div>
    </div>
  </div>
</section>'''


# ---------------------------------------------------------------- build
def build(lang):
    global LANG
    LANG = lang
    fonts = (HERE / "fonts" / "fonts.css").read_text()
    html_pages = [fn(i + 1) for i, fn in enumerate(PAGES)]
    total = len(html_pages)
    body = "\n".join(html_pages).replace("{TOTAL}", f"{total:02d}")
    title = "Ignacio Sconza — Portfolio" + (" (ES)" if lang == "es" else " (EN)")
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><title>{title}</title>
<meta name="author" content="Ignacio Sconza">
<style>{fonts}</style><link rel="stylesheet" href="styles.css"></head>
<body>{body}</body></html>'''


if __name__ == "__main__":
    import sys
    for lang in ("es", "en"):
        LANG = lang
        out = HERE / f"portfolio_{lang}.html"
        out.write_text(build(lang))
        print("wrote", out)

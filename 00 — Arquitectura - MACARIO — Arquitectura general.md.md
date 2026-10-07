# MACARIO — Arquitectura general

> Documento maestro de arquitectura.  
> Mapa general del sistema: qué es MACARIO, cómo se relacionan sus partes y cuál es la responsabilidad de cada capa.  
> No es un documento metodológico ni un catálogo de herramientas: la metodología vive en [[02 — Metodología - MACARIO — Flujo de trabajo]], el detalle de herramientas en [[03 — Herramientas - MACARIO — Herramientas y ecosistema]].

---

## 1. Qué es MACARIO

**MACARIO** es el sistema operativo interno desde el cual se diseñan, construyen, documentan, gestionan y evolucionan productos digitales.

No es una marca ni una herramienta: es el **System**.

MACARIO es agnóstico de plataforma. No está limitado a sitios web. Debe poder utilizarse para:

- Websites
- Web apps
- Mobile apps
- Dashboards
- Herramientas internas
- E-commerce
- Otros productos digitales

Es la combinación de:

- una arquitectura operativa (áreas y ciclo de vida);
- una metodología de trabajo;
- un sistema de documentación (capas transversales);
- bases técnicas reutilizables (**Foundations**), como Web-Base;
- y una colección de proyectos reales (**Projects**) que validan y mejoran el sistema.

La identidad externa con la que ese trabajo se presenta hacia afuera es **PRANA**. MACARIO organiza; PRANA muestra.

---

## 2. Relación PRANA / MACARIO / Foundation / Project

**Capa interna — cómo se organiza:**

```
                      MACARIO
                       System
                         │
                  organiza el trabajo
                         │
                         ▼
                    FOUNDATION
              (Web-Base, Mobile-Base…)
                         │
                  habilita técnicamente
                         │
                         ▼
                      PROJECT
                (Raíces, GXK, Onda…)
```

**Capa externa — lo que se ve:**

```
                      PROJECT
                         │
                    materializa
                         │
                         ▼
                       PRANA
            marca / negocio hacia afuera
          (casos públicos y portfolio propio)

       ITS  ──── autoría ────▶  PRANA
 autor / identidad personal     marca / negocio
    (superficie propia)        (superficie propia)
```

MACARIO no aparece hacia afuera: su arquitectura no se expone al público. Hacia afuera se ven dos superficies separadas: PRANA (marca / negocio) e ITS (autor / identidad personal). PRANA es una creación de autoría de ITS, pero no es una sección de ITS ni depende de ITS para funcionar públicamente. Ver [[PRANA — Estrategia]] y [[06 — ITS - ITS — Portfolio y posicionamiento]].

Los proyectos reales alimentan el sistema de vuelta:

```
PROJECTS → aprendizajes → MACARIO (metodología) + FOUNDATION (base técnica) → mejores proyectos
```

---

## 3. Principio central

> **MACARIO organiza → Foundation habilita → Project materializa.**

- **MACARIO organiza**: define áreas, ciclo de vida, principios, capas transversales y criterios de decisión — sin importar la plataforma del producto.
- **Foundation habilita**: convierte esa organización en una base técnica reutilizable para una plataforma concreta (Web-Base para websites y web apps; Mobile-Base para mobile, en el futuro).
- **Project materializa**: usa una Foundation para construir un producto real, con su propia identidad, repositorio y decisiones.

Ninguna capa reemplaza a la anterior. MACARIO no construye productos directamente; una Foundation no es un producto; un Project no es metodología.

---

## 4. Arquitectura del sistema

MACARIO organiza el trabajo en seis áreas. No son etapas estrictamente secuenciales ni exclusivas de un tipo de producto: son las funciones que cualquier producto digital necesita, sin importar la plataforma.

|Área|Responde a|
|---|---|
|**Research**|¿Qué problema resolvemos y para quién?|
|**Visual / Assets**|¿Qué identidad y recursos visuales usamos?|
|**UX / UI**|¿Cómo se experimenta y se ve el producto?|
|**Product Development**|¿Cómo se construye técnicamente? (incluye las Foundations)|
|**QA**|¿Funciona como fue definido?|
|**Analytics / Operations**|¿Cómo se mide y opera una vez publicado?|

El orden en que se recorren estas áreas durante un proyecto, y qué produce cada una, está definido en [[02 — Metodología - MACARIO — Flujo de trabajo]].

---

## 5. Capas transversales

Estas capas atraviesan las seis áreas: no pertenecen a un área específica, están disponibles en todas.

|Capa|Fuente de verdad para|
|---|---|
|**Obsidian**|conocimiento, contexto y decisiones|
|**Linear**|trabajo, tareas, milestones y estado|
|**Figma**|diseño visual, UX/UI y prototipos|
|**GitHub**|código y versiones|
|**Claude Code**|implementación y ejecución técnica|

Claude Code no es una fuente de verdad: trabaja sobre las fuentes correspondientes (código en GitHub, tareas de Linear, decisiones de Obsidian, diseño de Figma).

Otras herramientas (Playwright, Sentry, PostHog, Resend, n8n, Supabase, Cloudflare, ChatGPT, etc.) son especializadas dentro de un área concreta y no forman parte de esta capa transversal. Su responsabilidad y criterio de uso viven en [[03 — Herramientas - MACARIO — Herramientas y ecosistema]].

---

## 6. Foundations

Una **Foundation** es una base técnica reutilizable dentro de **Product Development**. Implementa, para una plataforma concreta, la metodología definida a nivel MACARIO.

Actualmente:

- **Web-Base** → foundation para websites y web apps. Ver [[04 — Web-Base - WEB-BASE — Metodología y estándares]].
- **Mobile-Base** → futura foundation para mobile apps.
- Otras foundations (dashboards, e-commerce, herramientas internas…) → futuras, según necesidad real y comprobada.

Una Foundation no es MACARIO completo. MACARIO es el sistema; cada Foundation es una pieza reutilizable dentro de una de sus áreas.

Una Foundation no contiene proyectos reales dentro de su propio repositorio: los proyectos la usan como punto de partida técnico, no como contenedor.

### Criterio para incorporar una nueva Foundation

Mobile-Base y otras futuras Foundations no se diseñan por adelantado: se incorporan solo cuando existe una necesidad real y comprobada. Antes de crear una:

1. ¿Existe una plataforma concreta (mobile, dashboards, e-commerce…) que hoy no tiene base técnica reutilizable?
2. ¿Hay evidencia de al menos un proyecto real que la necesita, no solo una hipótesis?
3. ¿El ciclo general de MACARIO ([[02 — Metodología - MACARIO — Flujo de trabajo]]) le alcanza sin modificarse, igual que le alcanza a Web-Base?
4. ¿Puede implementarse como Foundation independiente, sin absorber Research, Visual/Assets o UX/UI ni duplicar su metodología?

Toda Foundation nueva:

- implementa el mismo ciclo general de MACARIO, adaptado a su plataforma — no crea un ciclo propio;
- vive dentro de Product Development, igual que Web-Base;
- no contiene metodología general de MACARIO, solo su aplicación técnica acotada a esa plataforma;
- se distribuye y se relaciona con sus proyectos de la misma forma que Web-Base (ver [[04 — Web-Base - WEB-BASE — Metodología y estándares]] §18).

Si la respuesta a 1-3 no es clara y comprobada, la Foundation todavía no se crea.

---

## 7. Projects

Los **Projects** son donde se aplica y valida todo el sistema.

Actualmente, dentro del ecosistema activo de MACARIO:

- **GXK12:2** — proyecto activo;
- **Proyecto Raíces** — proyecto funcionalmente terminado; actualmente recibe iteración visual y ajustes puntuales;
- **Bresstore** — proyecto real pendiente de cierre;
- futuros proyectos.

Proyectos históricos o archivados conceptualmente:

- **Web-Base** — Foundation histórica/fundacional, congelada como línea de desarrollo independiente;
- **CONCRETO** — concepto histórico de marca;
- **tienda-ropa-demo** — repositorio histórico;
- **Onda** — fuera del ecosistema MACARIO actual.

No deben tratarse proyectos históricos, archivados o externos como trabajo activo por defecto.

Cada proyecto:

- se construye a partir de una Foundation;
- mantiene su propia identidad, contenido, repositorio y decisiones;
- no queda acoplado estructuralmente a la Foundation que lo originó;
- puede convertirse en caso, referencia o evidencia para PRANA (portfolio público) o para ITS (perspectiva del autor) cuando corresponde; puede documentarse internamente sin ser público.

---

## 8. Relación entre todas las capas

```
                         MACARIO
             (áreas + metodología + principios)
                            │
        ┌───────────┬───────┴───────┬───────────┐
        ▼           ▼               ▼           ▼
    Research   Visual/Assets     UX/UI      Analytics/Ops
        │           │               │           │
        └───────────┴───────┬───────┴───────────┘
                             ▼
                    PRODUCT DEVELOPMENT
                             │
                        FOUNDATION
                    (Web-Base, Mobile-Base…)
                             │
                             ▼
                           QA
                             │
                             ▼
                          PROJECT
                             │
                             ▼
                           PRANA
                  (muestra el resultado)
```

Durante todo el ciclo, las capas transversales quedan disponibles para cualquier área, con mayor peso relativo según corresponda:

```
Obsidian    ← conocimiento, en cualquier área
Linear      ← trabajo, en cualquier área
Figma       ← diseño, principalmente Visual/Assets y UX/UI
GitHub      ← código, principalmente Product Development
Claude Code ← ejecución técnica, principalmente Product Development y QA
```

MACARIO OS coordina esta relación entre capas sin reemplazar ninguna herramienta. Ver [[05 — MACARIO OS - MACARIO OS — Arquitectura y roadmap]].

---

## 9. Principio de no duplicación

Cada información debe tener un lugar principal:

|Información|Fuente principal|
|---|---|
|Arquitectura / decisiones|Obsidian|
|Metodología|Obsidian ([[02 — Metodología - MACARIO — Flujo de trabajo]], [[04 — Web-Base - WEB-BASE — Metodología y estándares]])|
|Tareas / estado del trabajo|Linear|
|Diseño / UX-UI|Figma|
|Código / historial técnico|GitHub|
|Implementación|GitHub + Claude Code|

El detalle completo de esta regla y sus criterios de decisión vive en [[01 — Principios y decisiones - MACARIO — Principios y decisiones]].

---

## 10. Estado actual

### Consolidado

- MACARIO como sistema general (System), agnóstico de plataforma.
- Seis áreas operativas: Research, Visual/Assets, UX/UI, Product Development, QA, Analytics/Operations.
- PRANA como marca / identidad externa.
- ITS como identidad personal, autoría y portfolio de Ignacio: superficie separada de PRANA (PRANA es una creación de su autoría).
- Web-Base como Foundation para websites y web apps.
- MACARIO OS como capa de orquestación.
- Linear, GitHub y Obsidian como capas transversales operativas.

### En construcción

- consolidación de la bóveda MACARIO;
- MACARIO OS como integración real;
- documentación maestra y gobierno operativo.

Las Foundations futuras se incorporan solamente cuando exista una necesidad real y comprobada.

### Proyectos actuales

- GXK12:2
- Proyecto Raíces
- Bresstore
- futuros proyectos

Web-Base queda como Foundation histórica/fundacional congelada: no es una línea activa de desarrollo independiente.

---

## 11. Documentos relacionados

- [[01 — Principios y decisiones - MACARIO — Principios y decisiones]]
- [[02 — Metodología - MACARIO — Flujo de trabajo]]
- [[03 — Herramientas - MACARIO — Herramientas y ecosistema]]
- [[04 — Web-Base - WEB-BASE — Metodología y estándares]]
- [[05 — MACARIO OS - MACARIO OS — Arquitectura y roadmap]]
- [[06 — ITS - ITS — Portfolio y posicionamiento]]
- [[PRANA — Estrategia]]

---

## 12. Regla final

**MACARIO no es una herramienta ni un sitio web.**

Es el sistema que permite que la marca (PRANA), la metodología, el conocimiento, las Foundations y los proyectos funcionen como una sola estructura sin perder la independencia de cada componente.

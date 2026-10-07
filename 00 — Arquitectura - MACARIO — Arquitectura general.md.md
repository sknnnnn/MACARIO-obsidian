# MACARIO — Arquitectura general

> Documento maestro de arquitectura.  
> Mapa general del sistema: qué es MACARIO, cómo se relacionan sus partes y cuál es la responsabilidad de cada capa.  
> No es un documento metodológico ni un catálogo de herramientas: la metodología vive en [[02 — Metodología - MACARIO — Flujo de trabajo.md|MACARIO — Flujo de trabajo]], el detalle de herramientas en [[03 — Herramientas - MACARIO — Herramientas y ecosistema.md|MACARIO — Herramientas y ecosistema]].

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
- bases técnicas reutilizables (**Foundations**); Web-Base fue la primera y hoy es una referencia histórica congelada (ver §6);
- y una colección de proyectos reales (**Projects**) que validan y mejoran el sistema.

MACARIO opera como **MACARIO ESTUDIO**: el estudio / estructura de trabajo desde la cual se organizan los proyectos, la metodología y la operación. Ver §2.

---

## 2. Jerarquía de identidad y relación MACARIO / Foundation / Project

> **Decisión vigente (2026-10-07).** Reemplaza versiones anteriores que equiparaban PRANA con la identidad externa de MACARIO o con "MACARIO STUDIO".

| Identidad | Qué es | Qué NO es |
|---|---|---|
| **MACARIO ESTUDIO** | El estudio / estructura de trabajo desde la cual se organizan proyectos, metodología y operación. | — |
| **PRANA** | Un proyecto / marca / posible futura empresa **independiente de MACARIO**, en evaluación. | No reemplaza a MACARIO ESTUDIO. No es sinónimo de MACARIO ni su canal público definitivo. |
| **ITS** | Identidad / proyecto personal de Ignacio, cuando corresponda. | No es sinónimo de PRANA ni de MACARIO ESTUDIO. |

- No usar "PRANA = MACARIO" ni "PRANA reemplazó a MACARIO ESTUDIO".
- El archivo de Figma llamado `PRANA STUDIOS` es solo el nombre de un recurso visual; no modifica esta jerarquía.

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
                (Raíces, GXK…)
```

**Superficies externas:** PRANA e ITS tienen superficies propias y separadas. Ver [[PRANA — Estrategia]] y [[06 — ITS - ITS — Portfolio y posicionamiento.md|ITS — Portfolio y posicionamiento]].

> ⚠️ **Decisión abierta — superficie pública:** versiones anteriores de este documento definían a PRANA como la superficie donde se publican los casos de los proyectos de MACARIO ("MACARIO organiza; PRANA muestra"). Regla actual (2026-10-07), mientras no se decida:
> - PRANA está en evaluación; MACARIO ESTUDIO es el estudio.
> - No asumir que PRANA es el canal público definitivo del estudio.
> - No mantener documentación interna de MACARIO publicada como si fuera contenido público.

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

El orden en que se recorren estas áreas durante un proyecto, y qué produce cada una, está definido en [[02 — Metodología - MACARIO — Flujo de trabajo.md|MACARIO — Flujo de trabajo]].

---

## 5. Capas fundamentales

> **Modelo vigente (2026-10-07).** Estas capas atraviesan las seis áreas: no pertenecen a un área específica, están disponibles en todas.

|Capa|Rol|Responsabilidad|
|---|---|---|
|**Obsidian**|Memory / Context|conocimiento permanente, contexto, decisiones, principios, metodología, arquitectura|
|**Linear**|Operations / Work|tareas, bugs, mejoras, prioridades, estados, planificación y seguimiento|
|**GitHub**|Implementation / Code|repositorios, código, ramas, commits, PRs, estado técnico|
|**Figma**|Visual Source|fuente de verdad visual: referencias, assets, reglas visuales y diseños aprobados|
|**Claude Design**|Creative Engine|exploración visual, composición, prototipado e iteración antes de la aprobación|
|**Claude Code**|Implementation Engine|implementación del diseño aprobado, desarrollo, integración, correcciones y mantenimiento|
|**Preview / QA**|Validación|validación del producto real|
|**Cowork**|Audit / Coordination / Cross-tool Operations|auditoría transversal, coordinación entre herramientas, detección de inconsistencias, informes y tareas transversales delegadas|

- **Fuentes de verdad:** Obsidian (conocimiento), Linear (trabajo), GitHub (código), Figma (visual).
- **Motores** (no son fuente de verdad; trabajan sobre las fuentes): Claude Design, Claude Code, Cowork.
- **Claude Design no reemplaza a Figma**, y Cowork no reemplaza ninguna herramienta: coordina, audita y ejecuta tareas transversales cuando corresponde.
- **Alcance de Figma como Visual Source (2026-10-07):** Figma es la fuente visual de verdad **cuando un proyecto tiene una definición visual que deba preservarse, explorarse, aprobarse o implementarse de forma sistemática**: un sistema visual, un diseño aprobado, referencias, assets o una dirección visual relevante. Los proyectos y cambios simples no necesitan crearse ni pasar por Figma. Claude Design no reemplaza a Figma.

### Flujo visual

```
Referencias + Figma
        ↓
Claude Design  (exploración / composición / prototipo)
        ↓
diseño aprobado
        ↓
Figma como Visual Source
        ↓
Claude Code
        ↓
producto
        ↓
Preview / QA
```

Otras herramientas (Playwright, Sentry, PostHog, Resend, n8n, Supabase, Cloudflare, etc.) son especializadas dentro de un área concreta y no forman parte de las capas fundamentales. ChatGPT, Gemini y Grok pueden usarse como herramientas auxiliares cuando corresponda, pero no son capas de la arquitectura ni dependencias estructurales. Ver [[03 — Herramientas - MACARIO — Herramientas y ecosistema.md|MACARIO — Herramientas y ecosistema]].

---

## 6. Foundations

> ⚠️ **Web-Base — HISTÓRICO / FUNDACIONAL / CONGELADO (decisión 2026-10-07).** Web-Base ya no es una línea activa de desarrollo ni un sistema obligatorio. MACARIO ESTUDIO absorbió sus aprendizajes útiles. El repositorio y esta documentación se conservan como referencia histórica.
>
> ⚠️ **Decisión abierta:** si el concepto de *Foundation* se mantiene como capa de MACARIO para bases futuras (Mobile-Base u otras). Las reglas de esta sección describen el modelo con el que se construyó Web-Base.

Una **Foundation** es una base técnica reutilizable dentro de **Product Development**. Implementa, para una plataforma concreta, la metodología definida a nivel MACARIO.

Actualmente:

- **Web-Base** → foundation histórica para websites y web apps, **congelada**: ya no se desarrolla. Ver [[04 — Web-Base - WEB-BASE — Metodología y estándares.md|WEB-BASE — Metodología y estándares]].
- **Mobile-Base** → futura foundation para mobile apps.
- Otras foundations (dashboards, e-commerce, herramientas internas…) → futuras, según necesidad real y comprobada.

Una Foundation no es MACARIO completo. MACARIO es el sistema; cada Foundation es una pieza reutilizable dentro de una de sus áreas.

Una Foundation no contiene proyectos reales dentro de su propio repositorio: los proyectos la usan como punto de partida técnico, no como contenedor.

### Criterio para incorporar una nueva Foundation

Mobile-Base y otras futuras Foundations no se diseñan por adelantado: se incorporan solo cuando existe una necesidad real y comprobada. Antes de crear una:

1. ¿Existe una plataforma concreta (mobile, dashboards, e-commerce…) que hoy no tiene base técnica reutilizable?
2. ¿Hay evidencia de al menos un proyecto real que la necesita, no solo una hipótesis?
3. ¿El ciclo general de MACARIO ([[02 — Metodología - MACARIO — Flujo de trabajo.md|MACARIO — Flujo de trabajo]]) le alcanza sin modificarse, igual que le alcanza a Web-Base?
4. ¿Puede implementarse como Foundation independiente, sin absorber Research, Visual/Assets o UX/UI ni duplicar su metodología?

Toda Foundation nueva:

- implementa el mismo ciclo general de MACARIO, adaptado a su plataforma — no crea un ciclo propio;
- vive dentro de Product Development, igual que Web-Base;
- no contiene metodología general de MACARIO, solo su aplicación técnica acotada a esa plataforma;
- se distribuye y se relaciona con sus proyectos de la misma forma que Web-Base (ver [[04 — Web-Base - WEB-BASE — Metodología y estándares.md|WEB-BASE — Metodología y estándares]] §18).

Si la respuesta a 1-3 no es clara y comprobada, la Foundation todavía no se crea.

---

## 7. Projects

Los **Projects** son donde se aplica y valida todo el sistema.

Ejemplos actuales: Proyecto Raíces, GXK, Bresstore, futuros proyectos y clientes. CONCRETO se conserva solo como concepto histórico / muestra (ver §10).

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
Obsidian      ← memoria / contexto, en cualquier área
Linear        ← trabajo, en cualquier área
Figma         ← fuente visual, principalmente Visual/Assets y UX/UI
Claude Design ← exploración visual, principalmente Visual/Assets y UX/UI
GitHub        ← código, principalmente Product Development
Claude Code   ← implementación, principalmente Product Development y QA
Preview / QA  ← validación del producto real, principalmente QA
Cowork        ← auditoría y coordinación transversal, en cualquier área
```

MACARIO OS coordina esta relación entre capas sin reemplazar ninguna herramienta. Ver [[05 — MACARIO OS - MACARIO OS — Arquitectura y roadmap.md|MACARIO OS — Arquitectura y roadmap]].

---

## 9. Principio de no duplicación

Cada información debe tener un lugar principal:

|Información|Fuente principal|
|---|---|
|Decisiones permanentes / principios / arquitectura|Obsidian|
|Metodología|Obsidian ([[02 — Metodología - MACARIO — Flujo de trabajo.md|MACARIO — Flujo de trabajo]]; Web-Base como referencia histórica)|
|Tareas / estado del trabajo / bugs / prioridades|Linear|
|Diseño aprobado / assets / reglas visuales|Figma|
|Exploración visual en curso|Claude Design (hasta su aprobación; lo aprobado pasa a Figma)|
|Código / historial técnico|GitHub|
|Implementación|GitHub + Claude Code|

Linear puede enlazar a Obsidian, pero no es una segunda wiki.

El detalle completo de esta regla y sus criterios de decisión vive en [[01 — Principios y decisiones - MACARIO — Principios y decisiones.md|MACARIO — Principios y decisiones]].

---

## 10. Estado actual

### Consolidado

- MACARIO como sistema general (System), agnóstico de plataforma, operado como **MACARIO ESTUDIO**.
- Seis áreas operativas: Research, Visual/Assets, UX/UI, Product Development, QA, Analytics/Operations.
- PRANA como marca / proyecto / negocio separado, en evaluación (ver §2).
- ITS como identidad personal, autoría y portfolio de Ignacio: superficie separada de PRANA y de MACARIO ESTUDIO.
- Capas fundamentales y flujo visual (§5).
- MACARIO OS como capa de orquestación (en pausa).

### Pendiente de decisión

- Si el concepto de *Foundation* se mantiene para bases futuras (ver §6).

### En construcción

- bóveda MACARIO completa;
- Mobile-Base y otras futuras foundations;
- MACARIO OS como integración real;
- documentación maestra terminada.

### Proyectos

El estado operativo de cada proyecto vive en Linear; la documentación permanente, en `07 — Proyectos/`.

- GXK12:2 — activo (principal).
- Proyecto Raíces — **Activo — fase de reorganización de código, documentación, arquitectura / modelo de datos y preparación del Admin/CMS**. Que el sitio público funcione no significa que el proyecto esté terminado.
- Bresstore — proyecto real pendiente, de menor prioridad.
- ITS Portfolio — pausado.
- MACARIO OS — conceptual / pausado.
- PRANA — estructura separada de MACARIO ESTUDIO (ver §2).

**Históricos / referencia (no operativos):**

- Web-Base — histórico / fundacional / congelado. MACARIO absorbió sus aprendizajes útiles.
- CONCRETO — concepto histórico de marca de ropa; se conserva como referencia / muestra.
- `tienda-ropa-demo` — repositorio histórico, no operativo.

**Fuera del ecosistema MACARIO:**

- Onda — no es proyecto, prospecto ni iniciativa de MACARIO.

---

## 11. Documentos relacionados

- [[01 — Principios y decisiones - MACARIO — Principios y decisiones.md|MACARIO — Principios y decisiones]]
- [[02 — Metodología - MACARIO — Flujo de trabajo.md|MACARIO — Flujo de trabajo]]
- [[03 — Herramientas - MACARIO — Herramientas y ecosistema.md|MACARIO — Herramientas y ecosistema]]
- [[04 — Web-Base - WEB-BASE — Metodología y estándares.md|WEB-BASE — Metodología y estándares]]
- [[05 — MACARIO OS - MACARIO OS — Arquitectura y roadmap.md|MACARIO OS — Arquitectura y roadmap]]
- [[06 — ITS - ITS — Portfolio y posicionamiento.md|ITS — Portfolio y posicionamiento]]
- [[PRANA — Estrategia]]

---

## 12. Regla final

**MACARIO no es una herramienta ni un sitio web.**

Es el sistema que permite que el estudio (MACARIO ESTUDIO), la metodología, el conocimiento, las Foundations y los proyectos funcionen como una sola estructura sin perder la independencia de cada componente.

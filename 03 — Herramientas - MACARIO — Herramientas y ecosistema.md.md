# MACARIO — Herramientas y ecosistema

> Mapa maestro de herramientas utilizadas por MACARIO.  
> Define qué responsabilidad tiene cada herramienta, a qué área del sistema sirve principalmente, cuándo utilizarla y qué información debe permanecer en ella.

---

# 1. Principio general

MACARIO no busca tener la mayor cantidad posible de herramientas.

Busca tener:

- las herramientas correctas;
- con responsabilidades claras;
- conectadas entre sí;
- sin duplicación innecesaria;
- y activadas solamente cuando aportan valor.

---

# 2. Mapa rápido

> **Modelo vigente (2026-10-07).** Ver [[00 — Arquitectura - MACARIO — Arquitectura general.md|MACARIO — Arquitectura general]] §5.

|Herramienta|Rol|Responsabilidad principal|Área principal|
|---|---|---|---|
|Obsidian|Memory / Context|conocimiento y documentación permanente|transversal|
|Linear|Operations / Work|ejecución y seguimiento|transversal|
|GitHub|Implementation / Code|código e historial|transversal|
|Figma|Visual Source|fuente de verdad visual: referencias, assets, reglas, diseños aprobados|transversal (Visual/Assets, UX/UI)|
|Claude Design|Creative Engine|exploración, composición, prototipado e iteración visual|Visual/Assets, UX/UI|
|Claude Code|Implementation Engine|implementación técnica del diseño aprobado|transversal|
|Preview / QA|Validación|validación del producto real|QA|
|Cowork|Audit / Coordination|auditoría, coordinación y operaciones entre herramientas|transversal|
|ChatGPT|auxiliar|análisis y razonamiento cuando corresponda|Research|
|Grok / Gemini|auxiliar|IA complementaria / segunda opinión cuando corresponda|Research|
|Banana|generación/edición de imágenes con IA|Visual / Assets|
|Artifact / Preview|revisión visual|Visual/Assets, UX/UI|
|Web-Base|histórico / fundacional / congelado|referencia|
|Supabase|backend / datos|Product Development|
|Playwright|QA automatizado|QA|
|Sentry|monitoreo de errores|Analytics / Operations|
|PostHog|analítica de producto|Analytics / Operations|
|Resend|email transaccional|Analytics / Operations|
|n8n|automatizaciones|Analytics / Operations|
|Cloudflare|infraestructura / deploy|Analytics / Operations (Release)|
|MACARIO OS|orquestación|coordinación (ver [[05 — MACARIO OS - MACARIO OS — Arquitectura y roadmap.md|MACARIO OS — Arquitectura y roadmap]])|

---

# 3. Capas fundamentales

Obsidian, Linear, GitHub y Figma son **fuentes de verdad**, cada una para un tipo de información. Claude Design, Claude Code y Cowork son **motores**: trabajan sobre esas fuentes y no las reemplazan. Preview / QA valida el producto real. Ver [[00 — Arquitectura - MACARIO — Arquitectura general.md|MACARIO — Arquitectura general]] para la relación entre capas y áreas.

## 3.1 Obsidian — Conocimiento

Fuente de conocimiento permanente de MACARIO.

Contiene: arquitectura, principios, decisiones, metodología, aprendizajes, documentación de proyectos, contexto, referencias, criterios reutilizables.

No debe contener una copia completa de las tareas de Linear.

**Acceso de los agentes:**
- **Local:** Claude Code consulta el vault mediante **Obsidian Agent MCP**, un servidor MCP local verificado como operativo (2026-09-12, PRO-71). Esta conexión ya no es trabajo pendiente; las futuras integraciones de MACARIO OS cubren capacidades nuevas.
- **Sesiones en la nube y Cowork:** leen el vault a través del repositorio de GitHub `MACARIO-obsidian`, que es privado (regla *private by default*).

> **¿Qué sabemos y por qué hacemos las cosas así?**

## 3.2 Linear — Trabajo

Sistema operativo del trabajo.

Contiene: issues, microtareas, bugs, prioridades, estados, dependencias, ciclos, proyectos, iniciativas, seguimiento operativo.

Linear organiza el trabajo alrededor de issues, proyectos e iniciativas; los proyectos agrupan trabajo alrededor de un resultado común, mientras que las iniciativas se sitúan por encima de proyectos para objetivos más amplios.

> **¿Qué tenemos que hacer?**

### Regla

Linear debe mantenerse operativo. No usarlo como wiki.

## 3.3 Figma — Visual Source

Fuente de verdad visual del producto.

Contiene: referencias visuales (colocadas en el tablero del proyecto), assets, sistema visual, reglas visuales consolidadas y diseños aprobados.

> **¿Cómo se ve el producto aprobado?**

### Regla

Figma es la fuente visual de verdad **cuando un proyecto tiene una definición visual que deba preservarse, explorarse, aprobarse o implementarse de forma sistemática**: un sistema visual, un diseño aprobado, referencias, assets o una dirección visual relevante. En ese caso, lo aprobado —incluido lo explorado en Claude Design— se consolida en Figma. Los proyectos y cambios simples no necesitan crearse ni pasar por Figma.

Figma no es el motor de exploración principal; ese rol es de Claude Design (3.6).

> Cambio respecto de la versión anterior (Figma *opt-in* genérico): decisión del 2026-10-07.

## 3.4 GitHub — Código

Fuente de verdad de la implementación.

Contiene: repositorios, código, ramas, commits, Pull Requests, historial, releases cuando corresponda.

> **¿Qué construimos realmente?**

### Regla

Si existe una diferencia entre una descripción antigua y el código real, el código real tiene prioridad.

## 3.5 Claude Code — Ejecución

Implementación y trabajo técnico asistido.

Puede utilizarse para: implementar features, corregir bugs, refactorizar, auditar, ejecutar QA, revisar estructura, generar documentación técnica, trabajar sobre repositorios.

Claude Code no es una fuente de verdad: debe seguir las decisiones documentadas en Obsidian, el scope de Linear, el código de GitHub y el diseño de Figma.

### Regla

Claude Code no debe tomar silenciosamente decisiones importantes de arquitectura, alcance o negocio, ni inventar la identidad visual en código: implementa diseño aprobado en Figma.

## 3.6 Claude Design — Creative Engine

Exploración visual, composición, prototipado, experimentación e iteración de conceptos antes de su aprobación.

> **¿Cómo podría verse?**

### Regla

Claude Design **no reemplaza a Figma**. Lo que se aprueba en Claude Design se consolida en Figma como Visual Source; Claude Code implementa desde ahí.

## 3.7 Preview / QA — Validación

Validación del producto real (previews, Artifacts de revisión, QA funcional y visual) antes de cerrar.

## 3.8 Cowork — Audit / Coordination / Cross-tool Operations

Auditoría transversal, coordinación entre herramientas, análisis del estado de los proyectos, detección de inconsistencias y gaps, preparación de informes y ejecución de tareas transversales que se le deleguen.

### Regla

Cowork no reemplaza ninguna herramienta ni es fuente de verdad: lee y coordina las fuentes, y propone cambios antes de ejecutarlos cuando no son reversibles.

---

# 4. Herramientas especializadas por área

Estas herramientas sirven principalmente a un área concreta del sistema (ver [[00 — Arquitectura - MACARIO — Arquitectura general.md|MACARIO — Arquitectura general]]) y son **opt-in**: se incorporan cuando el proyecto lo justifica, no por defecto.

## 4.1 Research

> ChatGPT, Grok y Gemini son **herramientas auxiliares**: pueden usarse cuando corresponda, pero no forman parte de las capas fundamentales ni son dependencias estructurales de MACARIO (decisión 2026-10-07).

### ChatGPT

Análisis, estrategia y razonamiento.

Puede utilizarse para: pensar arquitectura, analizar problemas, comparar alternativas, investigar, definir estrategia, revisar auditorías, interpretar resultados, diseñar procesos.

> **¿Qué deberíamos hacer y por qué?**

### Grok / Grokbot

IA complementaria. Se utiliza cuando aporta una ventaja específica frente a ChatGPT o Claude para exploración, comparación, investigación o generación de alternativas.

No reemplaza automáticamente a ChatGPT o Claude: debe usarse cuando exista una razón concreta.

## 4.2 Visual / Assets

### Banana

Generación y edición de imágenes con IA. Se incorpora cuando el proyecto necesita producir o iterar assets visuales que no provienen de fotografía o diseño manual.

> Nota: esta herramienta no tenía documentación previa en la bóveda; se incorpora aquí según el uso real del sistema. Confirmar y ampliar su criterio de uso cuando haya evidencia de proyectos concretos.

### Artifact / Preview

Validación visual y presentación del trabajo.

Cuando una herramienta permite generar un Artifact, preview, render, prototipo o resultado navegable, debe utilizarse cuando ayude a revisar el trabajo. Especialmente útil para UI, rediseños, landing pages, portfolios, componentes visuales, experiencias interactivas.

> El resultado debe poder verse, no solamente describirse.

## 4.3 UX / UI

Claude Design (exploración y prototipo), Figma (diseño aprobado) y Preview (ver secciones 3.3, 3.6 y 3.7) son las herramientas principales de esta área.

## 4.4 Product Development

### Web-Base (Foundation — histórico, congelado)

> ⚠️ **Web-Base — HISTÓRICO / FUNDACIONAL / CONGELADO (decisión 2026-10-07).** Web-Base ya no es una línea activa de desarrollo ni un sistema obligatorio. MACARIO ESTUDIO absorbió sus aprendizajes útiles. El repositorio y esta documentación se conservan como referencia histórica.

Base técnica reutilizable de MACARIO para websites y web apps.

No es una herramienta externa: es el punto de partida técnico desde el que nace cada proyecto de ese tipo, e implementa etapas, quality gates, templates, skills, commands, estándares y criterios de QA.

> **¿Desde qué base partimos?**

Ver [[04 — Web-Base - WEB-BASE — Metodología y estándares.md|WEB-BASE — Metodología y estándares]].

### Supabase

Backend y datos cuando el proyecto lo necesita: PostgreSQL, autenticación, storage, APIs, funciones, realtime.

### Regla

Supabase no es obligatorio. Un sitio estático simple no necesita una base de datos solo porque Supabase esté disponible.

## 4.5 QA

### Playwright

QA y testing automatizado del navegador: E2E, navegación, formularios, flujos críticos, regresión, validaciones responsive, smoke tests.

### Regla

Playwright no es obligatorio para todos los proyectos. Se incorpora cuando existe un flujo crítico, hay suficiente complejidad, existe riesgo de regresión, o el proyecto justifica automatizar QA.

## 4.6 Analytics / Operations

### Sentry

Monitoreo de errores en producción: excepciones, errores frontend/backend, trazas, contexto de errores, alertas.

### Regla

Sentry es opt-in. Tiene sentido especialmente cuando el proyecto está en producción, tiene usuarios reales, tiene suficiente complejidad, o necesita observabilidad.

### PostHog

Analítica y comportamiento del producto: eventos, funnels, comportamiento, conversiones, feature usage, experimentación cuando corresponda.

### Regla

No instalar analytics simplemente porque sí. Primero definir: ¿qué queremos medir y qué decisión tomaremos con ese dato? Si no existe respuesta, PostHog probablemente todavía no sea necesario.

### Resend

Email transaccional: formularios, emails de contacto, confirmaciones, notificaciones, workflows de email.

### Regla

No usar Resend si un proyecto no necesita envío de email real. Los formularios deben tener una estrategia explícita de destino y procesamiento.

### n8n

Automatización entre sistemas. Puede conectar Linear, GitHub, email, formularios, APIs, bases de datos, analítica, servicios externos.

```
Formulario
    ↓
n8n
    ↓
Linear
    ↓
notificación
    ↓
Obsidian / documentación cuando corresponda
```

### Regla

Automatizar solamente procesos repetitivos, suficientemente estables y con beneficio real. No automatizar procesos que todavía están cambiando constantemente.

### Cloudflare

Infraestructura y publicación (Release): hosting, Pages, Workers, DNS, dominios, CDN, seguridad, servicios edge.

### Regla

La infraestructura debe ser proporcional al proyecto. No introducir complejidad de infraestructura si un hosting estático simple resuelve correctamente la necesidad.

---

# 5. MACARIO OS — Coordinación

MACARIO OS no es una herramienta más: es la capa que conecta a todas las anteriores sin duplicar sus funciones.

> **¿Cómo hacemos que todo el sistema funcione coordinadamente?**

Su arquitectura y roadmap completos viven en [[05 — MACARIO OS - MACARIO OS — Arquitectura y roadmap.md|MACARIO OS — Arquitectura y roadmap]].

---

# 6. Integraciones entre herramientas

La arquitectura ideal busca enlaces, no duplicaciones.

```
                    OBSIDIAN
                 conocimiento
                       │
                       ▼
                 MACARIO OS
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
      LINEAR         GITHUB        CLAUDE CODE
      tareas         código        implementación
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                    PROYECTO
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
         Playwright  Sentry    PostHog
             │         │         │
             └─────────┼─────────┘
                       ▼
                    PRODUCCIÓN
                       │
                 Cloudflare
```

---

# 7. Estado de integración

## Capas fundamentales

- Obsidian
- Linear
- GitHub
- Figma
- Claude Design
- Claude Code
- Preview / QA
- Cowork

## Auxiliares

- ChatGPT
- Grok / Gemini

## Integraciones / herramientas disponibles según necesidad

- Playwright
- Sentry
- Resend
- PostHog
- n8n
- Supabase
- Cloudflare
- Banana

## Futuro

- MACARIO OS como capa real de orquestación;
- contexto unificado;
- automatizaciones;
- integración más profunda entre documentación, tareas y código.

---

# 8. Criterio para agregar una herramienta

Antes de incorporar una nueva herramienta:

1. **Problema** — ¿Qué problema concreto resuelve?
2. **Frecuencia** — ¿Ese problema aparece una vez o repetidamente?
3. **Beneficio** — ¿Cuánto tiempo, calidad o claridad aporta?
4. **Complejidad** — ¿Qué mantenimiento agrega?
5. **Integración** — ¿A qué área de MACARIO sirve?
6. **Fuente de verdad** — ¿Qué información va a manejar?
7. **Reversibilidad** — ¿Podemos quitarla fácilmente si deja de aportar valor?

---

# 9. Herramientas obligatorias vs. optativas

### Base mínima

Todo proyecto puede comenzar solamente con:

```
Obsidian
Linear
GitHub
Claude Code
Preview / QA
```

Cuando el proyecto tiene una definición visual que preservar, explorar, aprobar o implementar sistemáticamente, se suman **Figma** (Visual Source) y **Claude Design** (exploración). Cowork se suma para auditoría y coordinación transversal. Web-Base ya no forma parte de la base: está congelado como referencia histórica.

### Según necesidad

```
Playwright
Sentry
PostHog
Resend
n8n
Supabase
Cloudflare
Banana
ChatGPT / Grok / Gemini (auxiliares)
```

La metodología no debe obligar a activar herramientas que el proyecto no necesita.

---

# 10. Principio de evolución

El stack no está cerrado para siempre. Puede cambiar. Una herramienta puede incorporarse, reemplazarse, eliminarse, quedar experimental o convertirse en estándar.

Cada cambio importante debe documentarse en [[01 — Principios y decisiones - MACARIO — Principios y decisiones.md|MACARIO — Principios y decisiones]] y reflejarse aquí.

---

# 11. Regla final

> **No buscamos tener todas las herramientas. Buscamos que cada herramienta que usamos tenga una razón clara para existir, y que sirva a un área concreta de MACARIO.**

El valor de MACARIO no está en la cantidad de herramientas. Está en cómo se conectan para producir mejores proyectos.

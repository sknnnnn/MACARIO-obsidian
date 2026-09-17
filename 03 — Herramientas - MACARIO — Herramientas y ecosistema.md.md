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

|Herramienta|Responsabilidad principal|Área principal|
|---|---|---|
|Obsidian|conocimiento y documentación permanente|transversal|
|Linear|ejecución y seguimiento|transversal|
|GitHub|código e historial|transversal|
|Claude Code|implementación técnica|transversal|
|Figma|diseño y referencias visuales|transversal (Visual/Assets, UX/UI)|
|ChatGPT|análisis, estrategia y razonamiento|Research|
|Grok|IA complementaria|Research|
|Banana|generación/edición de imágenes con IA|Visual / Assets|
|Artifact / Preview|revisión visual|Visual/Assets, UX/UI|
|Web-Base|Foundation — base técnica reutilizable|Product Development|
|Supabase|backend / datos|Product Development|
|Playwright|QA automatizado|QA|
|Sentry|monitoreo de errores|Analytics / Operations|
|PostHog|analítica de producto|Analytics / Operations|
|Resend|email transaccional|Analytics / Operations|
|n8n|automatizaciones|Analytics / Operations|
|Cloudflare|infraestructura / deploy|Analytics / Operations (Release)|
|MACARIO OS|orquestación|coordinación (ver [[MACARIO OS — Arquitectura y roadmap]])|

---

# 3. Capas transversales (fuente de verdad)

Estas cinco herramientas atraviesan las seis áreas de MACARIO y cada una es fuente principal de verdad para un tipo de información. Ver [[MACARIO — Arquitectura general]] para la relación entre capas y áreas.

## 3.1 Obsidian — Conocimiento

Fuente de conocimiento permanente de MACARIO.

Contiene: arquitectura, principios, decisiones, metodología, aprendizajes, documentación de proyectos, contexto, referencias, criterios reutilizables.

No debe contener una copia completa de las tareas de Linear.

> **¿Qué sabemos y por qué hacemos las cosas así?**

## 3.2 Linear — Trabajo

Sistema operativo del trabajo.

Contiene: issues, microtareas, bugs, prioridades, estados, dependencias, ciclos, proyectos, iniciativas, seguimiento operativo.

Linear organiza el trabajo alrededor de issues, proyectos e iniciativas; los proyectos agrupan trabajo alrededor de un resultado común, mientras que las iniciativas se sitúan por encima de proyectos para objetivos más amplios.

> **¿Qué tenemos que hacer?**

### Regla

Linear debe mantenerse operativo. No usarlo como wiki.

## 3.3 Figma — Diseño

Diseño visual, UX/UI y prototipos.

Puede utilizarse para: exploración visual, wireframes, UI, identidad, referencias, handoff.

> **¿Cómo se ve y se experimenta el producto?**

### Regla

Figma es **opt-in**. No todos los proyectos lo necesitan. Una dirección visual clara y un Artifact/preview pueden ser suficientes para proyectos simples.

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

Claude Code no debe tomar silenciosamente decisiones importantes de arquitectura, alcance o negocio.

---

# 4. Herramientas especializadas por área

Estas herramientas sirven principalmente a un área concreta del sistema (ver [[MACARIO — Arquitectura general]]) y son **opt-in**: se incorporan cuando el proyecto lo justifica, no por defecto.

## 4.1 Research

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

Figma y Artifact/Preview (ver secciones 3.3 y 4.2) son las herramientas principales de esta área.

## 4.4 Product Development

### Web-Base (Foundation)

Base técnica reutilizable de MACARIO para websites y web apps.

No es una herramienta externa: es el punto de partida técnico desde el que nace cada proyecto de ese tipo, e implementa etapas, quality gates, templates, skills, commands, estándares y criterios de QA.

> **¿Desde qué base partimos?**

Ver [[WEB-BASE — Metodología y estándares]].

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

Su arquitectura y roadmap completos viven en [[MACARIO OS — Arquitectura y roadmap]].

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

## Ya forman parte del sistema

- Linear
- GitHub
- Claude Code
- ChatGPT
- Obsidian
- Web-Base

## Integraciones / herramientas disponibles según necesidad

- Figma
- Playwright
- Sentry
- Resend
- PostHog
- n8n
- Supabase
- Cloudflare
- Grok
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
Linear
GitHub
Claude Code
Obsidian
ChatGPT
Web-Base (o la Foundation correspondiente)
```

### Según necesidad

```
Figma
Playwright
Sentry
PostHog
Resend
n8n
Supabase
Cloudflare
Grok
Banana
```

La metodología no debe obligar a activar herramientas que el proyecto no necesita.

---

# 10. Principio de evolución

El stack no está cerrado para siempre. Puede cambiar. Una herramienta puede incorporarse, reemplazarse, eliminarse, quedar experimental o convertirse en estándar.

Cada cambio importante debe documentarse en [[MACARIO — Principios y decisiones]] y reflejarse aquí.

---

# 11. Regla final

> **No buscamos tener todas las herramientas. Buscamos que cada herramienta que usamos tenga una razón clara para existir, y que sirva a un área concreta de MACARIO.**

El valor de MACARIO no está en la cantidad de herramientas. Está en cómo se conectan para producir mejores proyectos.

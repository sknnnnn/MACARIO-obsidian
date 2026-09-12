# MACARIO — Herramientas y ecosistema

> Mapa maestro de herramientas utilizadas por MACARIO.  
> Define qué responsabilidad tiene cada herramienta, cuándo utilizarla y qué información debe permanecer en ella.

---

# 1. Principio general

MACARIO no busca tener la mayor cantidad posible de herramientas.

Busca tener:

- las herramientas correctas;
    
- con responsabilidades claras;
    
- conectadas entre sí;
    
- sin duplicación innecesaria;
    
- y activadas solamente cuando aportan valor.
    

```
                    MACARIO OS
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
   CONOCIMIENTO       EJECUCIÓN        IMPLEMENTACIÓN
       │                 │                 │
    Obsidian           Linear           GitHub
       │                 │                 │
       └─────────────────┼─────────────────┘
                         │
                  Claude / ChatGPT
                         │
                    PROYECTOS
```

---

# 2. Mapa rápido

|Herramienta|Responsabilidad principal|
|---|---|
|Obsidian|conocimiento y documentación permanente|
|Linear|ejecución y seguimiento|
|GitHub|código e historial|
|Claude Code|implementación técnica|
|ChatGPT|análisis, estrategia y razonamiento|
|Web-Base|metodología|
|MACARIO OS|orquestación|
|Figma|diseño y referencias visuales|
|Playwright|QA automatizado|
|Sentry|monitoreo de errores|
|PostHog|analítica de producto|
|Resend|email transaccional|
|n8n|automatizaciones|
|Supabase|backend / datos|
|Cloudflare|infraestructura / deploy|
|Grok|herramienta complementaria de IA|
|Artifact / Preview|revisión visual|

---

# 3. Obsidian

## Responsabilidad

**Fuente de conocimiento permanente de MACARIO.**

Contiene:

- arquitectura;
    
- principios;
    
- decisiones;
    
- metodología;
    
- aprendizajes;
    
- documentación de proyectos;
    
- contexto;
    
- referencias;
    
- criterios reutilizables.
    

No debe contener una copia completa de las tareas de Linear.

### Pregunta que responde

> **¿Qué sabemos y por qué hacemos las cosas así?**

### Uso

Obsidian es especialmente importante para información que debe seguir siendo útil meses o años después.

---

# 4. Linear

## Responsabilidad

**Sistema operativo del trabajo.**

Contiene:

- issues;
    
- microtareas;
    
- bugs;
    
- prioridades;
    
- estados;
    
- dependencias;
    
- ciclos;
    
- proyectos;
    
- iniciativas;
    
- seguimiento operativo.
    

Linear organiza el trabajo alrededor de issues, proyectos, iniciativas y ciclos; los proyectos agrupan trabajo alrededor de un resultado común, mientras que las iniciativas se sitúan por encima de proyectos para objetivos más amplios. citeturn0search5turn0search6

### Pregunta que responde

> **¿Qué tenemos que hacer?**

### Regla MACARIO

Linear debe mantenerse operativo.

No usarlo como wiki.

---

# 5. GitHub

## Responsabilidad

**Fuente de verdad de la implementación.**

Contiene:

- repositorios;
    
- código;
    
- ramas;
    
- commits;
    
- Pull Requests;
    
- historial;
    
- releases cuando corresponda.
    

### Pregunta que responde

> **¿Qué construimos realmente?**

### Regla

Si existe una diferencia entre una descripción antigua y el código real, el código real tiene prioridad.

---

# 6. Claude Code

## Responsabilidad

**Implementación y trabajo técnico asistido.**

Puede utilizarse para:

- implementar features;
    
- corregir bugs;
    
- refactorizar;
    
- auditar;
    
- ejecutar QA;
    
- revisar estructura;
    
- generar documentación técnica;
    
- trabajar sobre repositorios.
    

Claude Code debe seguir:

- las decisiones documentadas;
    
- el scope;
    
- WEB-BASE;
    
- las reglas del proyecto;
    
- y las restricciones de Git.
    

### Regla

Claude Code no debe tomar silenciosamente decisiones importantes de arquitectura, alcance o negocio.

---

# 7. ChatGPT

## Responsabilidad

**Análisis, estrategia y razonamiento.**

Puede utilizarse para:

- pensar arquitectura;
    
- analizar problemas;
    
- comparar alternativas;
    
- investigar;
    
- definir estrategia;
    
- revisar auditorías;
    
- interpretar resultados;
    
- diseñar procesos;
    
- coordinar el ecosistema.
    

### Pregunta que responde

> **¿Qué deberíamos hacer y por qué?**

---

# 8. WEB-BASE

## Responsabilidad

**Metodología reutilizable de MACARIO.**

No es una herramienta externa.

Es el sistema que define:

- etapas;
    
- quality gates;
    
- templates;
    
- skills;
    
- commands;
    
- estándares;
    
- criterios de QA;
    
- flujo de nuevos proyectos.
    

WEB-BASE responde:

> **¿Cómo trabajamos?**

---

# 9. MACARIO OS

## Responsabilidad

**Orquestación.**

MACARIO OS conecta:

- Obsidian;
    
- Linear;
    
- GitHub;
    
- Claude Code;
    
- ChatGPT;
    
- herramientas de QA;
    
- infraestructura;
    
- analítica;
    
- automatizaciones.
    

No debe duplicar funcionalidades que ya existen en estas herramientas.

### Pregunta que responde

> **¿Cómo hacemos que todo el sistema funcione coordinadamente?**

MACARIO OS es una capa que se construye progresivamente.

No necesita estar completamente implementado desde el inicio.

---

# 10. Figma

## Responsabilidad

**Diseño visual y referencia.**

Puede utilizarse para:

- exploración visual;
    
- wireframes;
    
- UI;
    
- identidad;
    
- referencias;
    
- handoff.
    

### Regla

Figma es **opt-in**.

No todos los proyectos necesitan Figma.

Una dirección visual clara y un Artifact/preview pueden ser suficientes para proyectos simples.

---

# 11. Playwright

## Responsabilidad

**QA y testing automatizado del navegador.**

Puede utilizarse para:

- E2E;
    
- navegación;
    
- formularios;
    
- flujos críticos;
    
- regresión;
    
- validaciones responsive;
    
- smoke tests.
    

### Regla

Playwright no es obligatorio para todos los proyectos.

Se incorpora cuando:

- existe un flujo crítico;
    
- hay suficiente complejidad;
    
- existe riesgo de regresión;
    
- o el proyecto justifica automatizar QA.
    

---

# 12. Sentry

## Responsabilidad

**Monitoreo de errores en producción.**

Puede utilizarse para:

- excepciones;
    
- errores frontend;
    
- errores backend;
    
- trazas;
    
- contexto de errores;
    
- alertas.
    

### Regla

Sentry es **opt-in**.

Tiene sentido especialmente cuando el proyecto:

- está en producción;
    
- tiene usuarios reales;
    
- tiene suficiente complejidad;
    
- o necesita observabilidad.
    

---

# 13. PostHog

## Responsabilidad

**Analítica y comportamiento del producto.**

Puede utilizarse para:

- eventos;
    
- funnels;
    
- comportamiento;
    
- conversiones;
    
- feature usage;
    
- experimentación cuando corresponda.
    

### Regla

No instalar analytics simplemente porque sí.

Primero definir:

> ¿Qué queremos medir y qué decisión tomaremos con ese dato?

Si no existe respuesta, PostHog probablemente todavía no sea necesario.

---

# 14. Resend

## Responsabilidad

**Email transaccional.**

Puede utilizarse para:

- formularios;
    
- emails de contacto;
    
- confirmaciones;
    
- notificaciones;
    
- workflows de email.
    

### Regla

No usar Resend si un proyecto no necesita envío de email real.

Los formularios deben tener una estrategia explícita de destino y procesamiento.

---

# 15. n8n

## Responsabilidad

**Automatización entre sistemas.**

Puede conectar:

- Linear;
    
- GitHub;
    
- email;
    
- formularios;
    
- APIs;
    
- bases de datos;
    
- analítica;
    
- servicios externos.
    

Ejemplo:

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

Automatizar solamente procesos:

- repetitivos;
    
- suficientemente estables;
    
- y con beneficio real.
    

No automatizar procesos que todavía están cambiando constantemente.

---

# 16. Supabase

## Responsabilidad

**Backend y datos cuando el proyecto lo necesita.**

Puede utilizarse para:

- PostgreSQL;
    
- autenticación;
    
- storage;
    
- datos;
    
- APIs;
    
- funciones;
    
- realtime;
    
- backend de aplicaciones.
    

### Regla

Supabase no es obligatorio.

Un sitio estático simple no necesita una base de datos solo porque Supabase esté disponible.

---

# 17. Cloudflare

## Responsabilidad

**Infraestructura y publicación.**

Puede utilizarse para:

- hosting;
    
- Pages;
    
- Workers;
    
- DNS;
    
- dominios;
    
- CDN;
    
- seguridad;
    
- servicios edge.
    

### Regla

La infraestructura debe ser proporcional al proyecto.

No introducir complejidad de infraestructura si un hosting estático simple resuelve correctamente la necesidad.

---

# 18. Grok / Grokbot

## Responsabilidad

**IA complementaria.**

Puede utilizarse cuando aporte una ventaja específica frente a las herramientas principales.

Posibles usos:

- exploración;
    
- comparación;
    
- investigación;
    
- generación de alternativas;
    
- análisis complementario.
    

### Regla

Grok no reemplaza automáticamente a ChatGPT o Claude.

Debe utilizarse cuando exista una razón concreta para hacerlo.

---

# 19. Artifact / Preview

## Responsabilidad

**Validación visual y presentación del trabajo.**

Cuando una herramienta permite generar un:

- Artifact;
    
- preview;
    
- render;
    
- prototipo;
    
- resultado navegable;
    

debe utilizarse cuando ayude a revisar el trabajo.

Especialmente útil para:

- UI;
    
- rediseños;
    
- landing pages;
    
- portfolios;
    
- componentes visuales;
    
- experiencias interactivas.
    

### Principio

> El resultado debe poder verse, no solamente describirse.

---

# 20. Integraciones entre herramientas

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

# 21. Estado de integración

## Ya forman parte del sistema

- Linear
    
- GitHub
    
- Claude Code
    
- ChatGPT
    
- Obsidian
    
- WEB-BASE
    

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
    

## Futuro

- MACARIO OS como capa real de orquestación;
    
- contexto unificado;
    
- automatizaciones;
    
- integración más profunda entre documentación, tareas y código.
    

---

# 22. Criterio para agregar una herramienta

Antes de incorporar una nueva herramienta:

### 1. Problema

¿Qué problema concreto resuelve?

### 2. Frecuencia

¿Ese problema aparece una vez o repetidamente?

### 3. Beneficio

¿Cuánto tiempo, calidad o claridad aporta?

### 4. Complejidad

¿Qué mantenimiento agrega?

### 5. Integración

¿Dónde encaja dentro de MACARIO?

### 6. Fuente de verdad

¿Qué información va a manejar?

### 7. Reversibilidad

¿Podemos quitarla fácilmente si deja de aportar valor?

---

# 23. Herramientas obligatorias vs. optativas

### Base mínima

Todo proyecto puede comenzar solamente con:

```
Linear
GitHub
Claude Code
Obsidian
ChatGPT
WEB-BASE
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
```

La metodología no debe obligar a activar herramientas que el proyecto no necesita.

---

# 24. Principio de evolución

El stack no está cerrado para siempre.

Puede cambiar.

Una herramienta puede:

- incorporarse;
    
- reemplazarse;
    
- eliminarse;
    
- quedar experimental;
    
- convertirse en estándar.
    

Pero cada cambio importante debe documentarse en:

`**MACARIO — Principios y decisiones**`

y reflejarse aquí.

---

# 25. Regla final

> **No buscamos tener todas las herramientas. Buscamos que cada herramienta que usamos tenga una razón clara para existir.**

El valor de MACARIO no está en la cantidad de herramientas.

Está en cómo se conectan para producir mejores proyectos.
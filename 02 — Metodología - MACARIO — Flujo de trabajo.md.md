# MACARIO — Flujo de trabajo

> Define cómo MACARIO transforma una idea en un producto digital terminado, documentado y reutilizable — sin importar la plataforma (website, web app, mobile app, dashboard, herramienta interna, e-commerce, etc.).  
> La implementación concreta y granular de este ciclo para websites y web apps vive en la Foundation correspondiente: [[WEB-BASE — Metodología y estándares]].

---

## 1. Ciclo general

```
        IDEA
          ↓
      RESEARCH
          ↓
  PRODUCT DEFINITION
          ↓
       VISUAL
          ↓
       UX / UI
          ↓
TECHNICAL ARCHITECTURE
          ↓
     DEVELOPMENT
          ↓
         QA
          ↓
      RELEASE
          ↓
ANALYTICS / OPERATIONS
          ↓
      ITERATION
          ↺ (vuelve a alimentar Research / Product Definition)
```

Las etapas no siempre son estrictamente lineales. Puede existir iteración interna, por ejemplo:

```
Research ↔ Product Definition
Visual ↔ UX/UI
Technical Architecture ↔ Development
Development ↔ QA
```

Pero **QA → Release → Analytics/Operations → Iteration** funciona como tramo final: no se salta.

---

## 2. Qué ocurre en cada etapa

|Etapa|Recibe|Produce|Continúa hacia|
|---|---|---|---|
|**Idea**|Un pedido informal (mensaje, reunión, problema, cliente)|Una necesidad identificada, sin convertirla todavía en solución|Research|
|**Research**|La idea/necesidad|Contexto de negocio, usuario, problema, competencia, restricciones, información faltante marcada como pendiente|Product Definition|
|**Product Definition**|El research|Alcance: qué entra, qué no entra, qué queda pendiente; objetivos verificables|Visual|
|**Visual**|El alcance definido|Dirección visual: identidad, referencias, paleta, tipografía, tono, assets|UX / UI|
|**UX / UI**|La dirección visual + el alcance|Flujos, wireframes, interacciones, pantallas — validados en Figma, Artifact o preview|Technical Architecture|
|**Technical Architecture**|UX/UI aprobado + alcance|Solución técnica: estructura, componentes, datos, integraciones, stack|Development|
|**Development**|La arquitectura técnica aprobada|Una versión funcional del producto|QA|
|**QA**|La versión funcional|Verificación funcional, responsive, accesibilidad y técnica; hallazgos clasificados (bloqueante / importante / mejora)|Release|
|**Release**|La versión validada por QA|El producto publicado en producción|Analytics / Operations|
|**Analytics / Operations**|El producto en producción|Datos de uso, errores, métricas, aprendizaje operativo|Iteration|
|**Iteration**|Los aprendizajes de Analytics/Operations|Nuevas ideas o ajustes de alcance, que vuelven a alimentar Research o Product Definition|Idea / Research (siguiente ciclo)|

### Regla

> No inventar información faltante. Si algo no está confirmado en Research o Product Definition, se documenta como pendiente y se pregunta antes de avanzar.

---

## 3. Sistema de capas por etapa

Cada etapa utiliza las capas transversales necesarias, no todas por defecto.

|Etapa|Capas principales|
|---|---|
|Idea|Linear + Obsidian|
|Research|Obsidian + GitHub (contexto existente)|
|Product Definition|Linear + Obsidian|
|Visual|Figma + Obsidian + Artifact/preview|
|UX / UI|Figma + Obsidian + Artifact/preview|
|Technical Architecture|Obsidian + GitHub|
|Development|Claude Code + GitHub|
|QA|Claude Code + Playwright cuando corresponda|
|Release|GitHub + infraestructura del proyecto (Cloudflare u otra)|
|Analytics / Operations|PostHog + Sentry + Obsidian|
|Iteration|Linear + Obsidian|

MACARIO OS coordina estas relaciones. Ver [[MACARIO OS — Arquitectura y roadmap]]. El detalle de cada herramienta vive en [[MACARIO — Herramientas y ecosistema]].

---

## 4. Linear vs Obsidian

### Linear

Linear representa el trabajo.

Contiene: estado, prioridad, responsable, dependencias, subtareas, seguimiento, bloqueos.

### Obsidian

Obsidian representa el conocimiento.

Contiene: contexto del negocio, decisiones, estructura, aprendizajes, referencias, criterios permanentes.

### Regla

> Si mañana necesitamos volver a entender algo, probablemente pertenece en Obsidian.  
> Si necesitamos hacer algo, probablemente pertenece en Linear.

---

## 5. GitHub

GitHub representa la implementación real.

Cada proyecto debería tener: repositorio, rama principal, ramas de trabajo cuando corresponda, commits, Pull Requests, historial.

Antes de modificar un repositorio:

1. comprobar estado;
2. comprobar rama;
3. comprobar cambios locales;
4. comprobar estado remoto;
5. comprobar PRs relevantes;
6. identificar posibles conflictos.

Nunca asumir que el estado local está actualizado.

---

## 6. Quality gates

Cada etapa debe producir una condición verificable.

```
IDEA
↓
¿Entendemos el pedido?

RESEARCH
↓
¿Entendemos el negocio/problema/usuario?

PRODUCT DEFINITION
↓
¿Sabemos qué entra y qué no?

VISUAL
↓
¿Sabemos cómo debe verse?

UX / UI
↓
¿Sabemos cómo se experimenta?

TECHNICAL ARCHITECTURE
↓
¿Sabemos cómo construirlo?

DEVELOPMENT
↓
¿Existe una versión funcional?

QA
↓
¿Funciona correctamente?

RELEASE
↓
¿La producción funciona?

ANALYTICS / OPERATIONS
↓
¿Sabemos cómo se está usando y comportando?

ITERATION
↓
¿Identificamos qué mejorar en el próximo ciclo?
```

---

## 7. Flujo de aprobación

### Claude puede avanzar solo

Cuando la decisión ya está tomada y documentada. Ejemplos: implementar un componente aprobado, corregir un bug, ejecutar una auditoría, generar un reporte, ejecutar QA, hacer refactors internos.

### Claude debe consultar

Cuando aparece: cambio importante de scope, nueva arquitectura, nueva dependencia significativa, cambio de identidad, migración destructiva, decisión comercial.

### Ignacio aprueba siempre

Commit final, push, merge, deploy, decisiones comerciales, publicación definitiva.

---

## 8. Flujo de revisión visual

Cuando el trabajo tiene impacto visual:

```
DEVELOPMENT
    ↓
ARTIFACT / PREVIEW
    ↓
REVISIÓN HUMANA
    ↓
¿APROBADO?
   ↙       ↘
 NO         SÍ
 ↓           ↓
CORREGIR   CONTINUAR
             ↓
             QA
```

La revisión visual humana tiene prioridad sobre la percepción del agente.

---

## 9. Aprendizaje posterior al proyecto

Después de cerrar un proyecto (fin de un ciclo de Release/Analytics-Operations):

1. identificar problemas repetidos;
2. identificar soluciones reutilizables;
3. documentarlas en Obsidian;
4. decidir si alguna debe entrar en la Foundation correspondiente (Web-Base u otra);
5. actualizar la metodología solamente si existe evidencia suficiente.

No toda experiencia se convierte en una nueva regla.

---

## 10. Evolución de MACARIO

```
PROYECTOS REALES
       ↓
experiencia
       ↓
aprendizaje
       ↓
Obsidian
       ↓
patrones repetibles
       ↓
FOUNDATION correspondiente
       ↓
mejor ejecución
       ↓
mejores proyectos
```

MACARIO OS aparece por encima de este ciclo para coordinarlo.

---

## 11. Regla de eficiencia

Antes de comenzar una tarea:

1. verificar qué ya existe;
2. reutilizar lo existente;
3. trabajar solamente sobre el scope necesario;
4. evitar cambios colaterales;
5. evitar documentación duplicada;
6. evitar nuevas herramientas sin necesidad.

El objetivo no es hacer más. El objetivo es **resolver mejor con menos fricción**.

---

## 12. Relación con las Foundations

Este documento describe el ciclo general de MACARIO, válido para cualquier plataforma.

Cada Foundation implementa este ciclo con más granularidad para su plataforma concreta. Por ejemplo, Web-Base traduce este ciclo general en doce etapas específicas para websites y web apps (Intake, Context, Discovery, Scope, Architecture, Visual Direction, Implementation, QA, Audit, Deploy, Documentation, Close) — ver [[WEB-BASE — Metodología y estándares]].

Cuando una Foundation cambie su implementación, este documento debe revisarse para mantener alineados: principios, metodología general, herramientas y MACARIO OS.

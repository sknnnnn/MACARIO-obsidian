# MACARIO — Flujo de trabajo

> Define cómo MACARIO transforma una idea en un producto digital terminado, documentado y reutilizable — sin importar la plataforma (website, web app, mobile app, dashboard, herramienta interna, e-commerce, etc.).  
> La implementación concreta y granular de este ciclo para websites y web apps vive en la Foundation correspondiente: [[WEB-BASE — Metodología y estándares]].

---

## 1. Ciclo general

```
        IDEA
          ↓
      RESEARCH
       (Discovery)
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

> Research se ejecuta mediante el proceso formal de **Discovery** — ver sección 3.

### Regla

> No inventar información faltante. Si algo no está confirmado en Research o Product Definition, se documenta como pendiente y se pregunta antes de avanzar.

---

## 3. Discovery: el proceso detrás de Research

> Discovery es el proceso formal mediante el cual la etapa Research transforma una idea, pedido, brief, problema o proyecto existente en información suficientemente clara para pasar a Product Definition **sin inventar requisitos**.

Discovery no es una etapa aparte en el ciclo general: es el nombre formal del proceso con el que se ejecuta Research, inmediatamente antes de Product Definition.

### 3.1 Proceso

1. Preguntar
2. Investigar (incluye cruzar fuentes — ver 3.4)
3. Organizar
4. Detectar faltantes, contradicciones e incertidumbres
5. Convertir la información en decisiones

Este ciclo se repite tantas veces como sea necesario hasta cumplir el gate (3.7). Discovery no es un cuestionario fijo.

### 3.2 Mapa de información

Discovery cubre, según lo que cada proyecto realmente necesite:

- problema / necesidad
- objetivo
- usuarios / audiencia
- producto o servicio
- alcance inicial
- modelo de negocio
- contenido y datos disponibles
- funcionalidades conocidas
- referencias
- marca y restricciones
- canales y contexto de uso
- recursos disponibles
- restricciones técnicas
- tiempo y presupuesto
- criterios de éxito

Esto es un **mapa de información, no un cuestionario fijo**. MACARIO no pregunta siempre las mismas áreas: pregunta únicamente lo necesario según el proyecto, lo que ya se sabe y los gaps detectados.

### 3.3 Estados de la información

Cada dato de Discovery se clasifica, cuando corresponda, en uno de estos estados:

- **Confirmado** — verificado directamente en una fuente confiable del propio proyecto (documentación MACARIO, repositorio, cliente).
- **Confirmado en otra fuente** — la información existe y puede verificarse en otra fuente del proyecto (repositorio, README, `PROJECT-CONTEXT` o equivalente, documentación de marca, código/configuración), pero todavía no fue incorporada ni reconciliada en la documentación correspondiente de MACARIO. No equivale a `Faltante`: el dato existe, solo falta traerlo — ver 3.4 y 3.5.
- **Decisión** — ya fue resuelto explícitamente por elección deliberada, no es un hecho externo a verificar.
- **Hipótesis** — suposición razonable, todavía no confirmada ni decidida.
- **Faltante** — no existe en ninguna fuente disponible del proyecto. Se pregunta antes de avanzar; no se inventa.
- **No aplica** — el área no es relevante para este proyecto puntual.

No forzar un dato a un estado si realmente no existe.

### 3.4 Cruce de fuentes

Antes de marcar un dato como `Faltante`, se revisan las fuentes del proyecto razonablemente relevantes para ese dato puntual — no todo el repositorio de forma indiscriminada. Según corresponda:

- documentación de MACARIO del proyecto;
- repositorio del proyecto;
- README, `PROJECT-CONTEXT` o equivalente;
- documentación de marca;
- código o configuración, cuando sea relevante para el dato buscado.

Si el dato aparece en alguna de estas fuentes pero no en la documentación de MACARIO, se marca `Confirmado en otra fuente`, no `Faltante`.

Para datos y decisiones relevantes que puedan cambiar durante el desarrollo — no para cada dato menor — registrar, cuando corresponda:

- fuente;
- fecha o referencia temporal (commit, versión, fecha del documento);
- vigencia (¿sigue siendo cierto?);
- conflicto con otra fuente, si existe.

### 3.5 Reconciliación

Cuando otra fuente demuestra que algo que MACARIO tenía marcado como pendiente ya fue resuelto, se reconcilia en vez de dejarlo como pendiente:

```
MACARIO dice "pendiente"
        ↓
otra fuente demuestra que ya fue resuelto
        ↓
reconciliar
        ↓
registrar la decisión
        ↓
actualizar la fuente canónica correspondiente
```

Reconciliar no reabre todo el Discovery: solo actualiza el dato puntual afectado y, si corresponde, registra la decisión permanente en la nota de decisiones del proyecto.

### 3.6 Tres capas

1. **Discovery interno de MACARIO** — determina qué necesitamos conocer, qué ya está confirmado, qué es hipótesis, qué falta, qué contradicciones existen y qué decisiones están bloqueadas.
2. **Discovery con cliente** — traduce esas necesidades internas en preguntas naturales y fáciles de responder, sin jerga técnica innecesaria.
3. **Procesamiento** — convierte las respuestas más la investigación en decisiones, requisitos, alcance, riesgos, preguntas pendientes y próximos pasos.

### 3.7 Discovery Gate

> ¿Tenemos suficiente información para pasar a Product Definition sin inventar requisitos?

El gate admite tres estados:

- **Sí** — la información disponible alcanza para pasar a Product Definition sin inventar requisitos.
- **Parcial** — hay base suficiente para avanzar, pero con gaps conocidos que se aceptan conscientemente como riesgo. Para declarar Parcial se registra:
  - qué está resuelto;
  - qué falta;
  - qué de eso bloquea Product Definition;
  - qué riesgo se acepta si se continúa.
- **No** — falta información necesaria para definir el producto. Discovery continúa hasta resolver los gaps que bloquean Product Definition (no todos los gaps posibles).

No todo gap es bloqueante: la diferencia entre información necesaria para definir el producto y riesgo aceptado conscientemente es la que decide si algo impide pasar a Product Definition o no.

**Chequeos obligatorios.** El gate revisa explícitamente estas tres áreas, incluso si el resultado es que no aplican:

- objetivo medible;
- modelo de negocio / monetización;
- tiempo / presupuesto.

Si alguna no aplica al proyecto, se registra como `No aplica` con su justificación — nunca se omite en silencio ni se inventa un valor.

### 3.8 Discovery continuo

El Discovery inicial establece una base suficiente para pasar a Product Definition, pero no es una verdad inmutable del proyecto. Durante el desarrollo pueden aparecer nuevos datos, decisiones, restricciones, cambios de alcance o contradicciones.

Cuando aparecen, se reconcilian y documentan con las herramientas correspondientes (ver 3.5), sin reabrir artificialmente todo el Discovery. Que algo nuevo aparezca después no significa que el Discovery original haya sido incorrecto: significa que el proyecto avanzó y generó información que no existía antes.

### 3.9 Relación con Web-Base

Web-Base traduce Research en tres sub-etapas propias: Intake, Context y Discovery (ver [[WEB-BASE — Metodología y estándares]]). La sub-etapa "Discovery" de Web-Base es la aplicación técnica y acotada de este proceso general para websites y web apps (investigación de referencias, competencia, contenido existente, stack) — no una definición paralela ni un sistema distinto.

### 3.10 Qué documentar

Lo que Discovery deja resuelto para un proyecto se documenta en `07 — Proyectos/_Plantilla/01 — Contexto y Brief`, incluidos su Discovery Gate y los estados/fuentes relevantes. Las reconciliaciones y decisiones permanentes se registran en `11 — Decisiones y Changelog` del proyecto. La metodología general de Discovery vive únicamente acá.

---

## 4. Sistema de capas por etapa

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

## 5. Linear vs Obsidian

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

## 6. GitHub

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

## 7. Quality gates

Cada etapa debe producir una condición verificable.

```
IDEA
↓
¿Entendemos el pedido?

RESEARCH (DISCOVERY)
↓
¿Tenemos suficiente información para pasar a Product Definition sin inventar requisitos?

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

## 8. Flujo de aprobación

### Claude puede avanzar solo

Cuando la decisión ya está tomada y documentada. Ejemplos: implementar un componente aprobado, corregir un bug, ejecutar una auditoría, generar un reporte, ejecutar QA, hacer refactors internos.

### Claude debe consultar

Cuando aparece: cambio importante de scope, nueva arquitectura, nueva dependencia significativa, cambio de identidad, migración destructiva, decisión comercial.

### Ignacio aprueba siempre

Commit final, push, merge, deploy, decisiones comerciales, publicación definitiva.

---

## 9. Flujo de revisión visual

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

## 10. Aprendizaje posterior al proyecto

Después de cerrar un proyecto (fin de un ciclo de Release/Analytics-Operations):

1. identificar problemas repetidos;
2. identificar soluciones reutilizables;
3. documentarlas en Obsidian;
4. decidir si alguna debe entrar en la Foundation correspondiente (Web-Base u otra);
5. actualizar la metodología solamente si existe evidencia suficiente.

No toda experiencia se convierte en una nueva regla.

---

## 11. Evolución de MACARIO

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

## 12. Regla de eficiencia

Antes de comenzar una tarea:

1. verificar qué ya existe;
2. reutilizar lo existente;
3. trabajar solamente sobre el scope necesario;
4. evitar cambios colaterales;
5. evitar documentación duplicada;
6. evitar nuevas herramientas sin necesidad.

El objetivo no es hacer más. El objetivo es **resolver mejor con menos fricción**.

---

## 13. Relación con las Foundations

Este documento describe el ciclo general de MACARIO, válido para cualquier plataforma.

Cada Foundation implementa este ciclo con más granularidad para su plataforma concreta. Por ejemplo, Web-Base traduce este ciclo general en doce etapas específicas para websites y web apps (Intake, Context, Discovery, Scope, Architecture, Visual Direction, Implementation, QA, Audit, Deploy, Documentation, Close) — ver [[WEB-BASE — Metodología y estándares]].

Cuando una Foundation cambie su implementación, este documento debe revisarse para mantener alineados: principios, metodología general, herramientas y MACARIO OS.

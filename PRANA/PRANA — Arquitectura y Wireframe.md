# PRANA — Arquitectura y Wireframe v0.1

> **v0.1 — Arquitectura de información y wireframe conceptual** de la web pública de PRANA.
> Se apoya en [[PRANA — Presence Blueprint]] (contenido y copy base), [[PRANA — Brand Core]] y [[PRANA — Estrategia]]. No los redefine.
> **No es diseño visual ni implementación.** Es el plano de la web antes de llevarla a Figma.
> **Copy operativo:** ante diferencias con el Blueprint, manda este documento (p. ej. "Quiero mejorar algo" en lugar de "Necesito mejorar algo").

---

## 1. Mapa del sitio

| Página | Función | Pregunta que responde |
|---|---|---|
| **Home** | Puerta de entrada. Recorre de la idea a la conversación. | ¿Qué es PRANA y por qué hablar con ellos? |
| **Proyectos** | Evidencia. Casos concretos. | ¿Qué hicieron realmente? |
| ↳ **Caso individual** | Profundidad de un proyecto. | ¿Cómo lo resolvieron? |
| **Proceso** | Cómo se trabaja. | ¿Cómo sería trabajar juntos? |
| **Nosotros** | Qué es PRANA y quién está detrás. | ¿Quién hace esto y con qué criterio? |
| **Contacto** | Inicio de la conversación. | ¿Cómo empiezo? |

- **Navegación principal:** Proyectos · Proceso · Nosotros · Contacto.
- **Logo PRANA** → Home. "PRANA" no aparece como ítem de navegación.
- **Footer** común a todas las páginas.
- No hay páginas por servicio ni por tipo de proyecto.

---

## 2. Home

**Recorrido:** idea → necesidad/problema → qué podemos producir → evidencia → criterio → proceso → conversación.

### Hero

- Mensaje + apoyo (copy en el Blueprint).
- **"Contanos qué querés construir →"** → Contacto.
- **"Ver proyectos"** → página Proyectos.

### Entrada por problema

**Decisión:** cada opción lleva a **Contacto con esa opción preseleccionada**.

- Las opciones expresan una intención, no una categoría de servicio. Tratarlas como navegación obligaría a crear páginas por intención, que la arquitectura no contempla.
- Llevarlas a Contacto con contexto hace que la persona no tenga que repetir lo que ya eligió: la conversación empieza donde la dejó.
- En Contacto la opción se puede cambiar; nada queda bloqueado.

| Opción en Home | Opción preseleccionada en Contacto |
|---|---|
| Tengo una idea | Tengo una idea |
| Quiero mejorar algo | Quiero mejorar algo |
| Necesito construir algo | Necesito construir algo |
| No estoy seguro | No estoy seguro |

"Quiero explorar una posibilidad" existe solo en Contacto.

### Capacidades

**Función:** orientar, no vender. Le muestra a la persona que lo que necesita probablemente entra en algo que PRANA produce.

- Cuatro grupos (Experiencias digitales, Productos digitales, Sistemas, Identidad y contenido), cada uno con sus ejemplos como texto.
- **Los ejemplos no son links** y no hay página por servicio.
- Cierre: "Si no sabés dónde encaja lo que necesitás, podemos empezar por ahí." → Contacto con **"No estoy seguro"** preseleccionado.

### Proyectos (preview)

- Título: "Hecho, no solamente pensado." + texto del Blueprint.
- 2–4 cards seleccionadas.
- **Card mínima:** visual · nombre · etiqueta (PROYECTO / CREACIÓN PRANA / EXPERIMENTO PRANA) · qué es / para quién (1 línea) · qué hicimos (1 línea).
- Cada card → su caso individual.
- **"Ver todos los proyectos →"** → Proyectos.

### Criterio

- Título: "No empezamos por la solución." + "Primero entendemos qué está pasando. Después decidimos qué vale la pena construir."
- **En Home:** los 4 principios cortos (Entender antes de ejecutar · Resolver antes que decorar · Lo simple también puede estar muy bien hecho · Los detalles importan), sin desarrollo.
- **En Nosotros:** los 6 principios completos, más el de identidad/criterio de ejecución.
- Sin CTA propio: la sección da contexto y lleva al Proceso, que viene a continuación.

### Proceso (teaser)

- 01 Entender → 02 Definir → 03 Diseñar → 04 Construir → 05 Evolucionar, solo con los nombres (o una línea por etapa como máximo).
- **"Conocé nuestro proceso →"** → Proceso.

### CTA final

- "¿Qué querés construir?" + "No necesitás saber qué solución necesitás. Solo necesitás saber qué querés lograr."
- **"Empezar una conversación →"** → Contacto (sin preselección).

---

## 3. Proyectos

### Página general

- **Hero:** "Cosas que hicimos realidad."
- **Introducción:** "Cada proyecto empieza en un contexto diferente. Entendemos el problema, encontramos una dirección y construimos la solución."
- **Cards:** misma card mínima que en Home. Las tres etiquetas conviven en un único listado, con la etiqueta visible en cada card.
- **Sin filtros** en v0.1: con pocos proyectos, un filtro dejaría vistas casi vacías. Se reevalúa cuando haya suficiente volumen.
- **CTA final:** "¿Qué podríamos construir juntos?" → **"Contanos qué querés resolver →"** → Contacto.

### Caso individual

Estructura base, **flexible**:

1. **Encabezado:** nombre · etiqueta · qué es / para quién · qué hicimos · visual principal.
2. **Contexto:** situación de partida.
3. **Desafío:** qué había que resolver.
4. **Enfoque:** cómo se pensó.
5. **Solución:** qué se construyó.
6. **Resultado:** solo si hay información real. **Si no la hay, la sección se omite.** No se completa con suposiciones.
7. **Galería.**
8. **Otros proyectos:** 1–2 cards → sus casos.
9. **CTA:** "¿Qué podríamos construir juntos?" → Contacto.

**Reglas:**

- Las secciones se pueden fusionar u omitir según el caso. Un EXPERIMENTO PRANA puede no tener "Resultado".
- No inventar métricas, resultados, testimonios ni datos faltantes.

### Información a recopilar antes de publicar cada caso

- Nombre y etiqueta correcta.
- Qué es / para quién (1 línea).
- Qué hizo PRANA concretamente (alcance real).
- Contexto y desafío, en palabras propias y verificables.
- Decisiones de enfoque relevantes.
- Descripción de la solución entregada / construida.
- Resultado: solo si existe y es verificable.
- Visuales: capturas, fotos o video con calidad suficiente.
- Permiso del cliente para publicar (en los PROYECTO).
- Link público, si existe y puede mostrarse.

| Proyecto | Etiqueta tentativa | Estado |
|---|---|---|
| Proyecto Raíces | A confirmar | Recopilar información |
| Bresstore | A confirmar | Recopilar información |
| ITS Portfolio | A confirmar | Recopilar información |
| Creaciones / experimentos PRANA | CREACIÓN / EXPERIMENTO | A definir |

---

## 4. Proceso

- **Hero:** "No empezamos por la solución. Empezamos por entender."
- **Nota introductoria:** el proceso se adapta a cada proyecto. No es rígido ni necesariamente lineal: se puede volver a etapas anteriores y no todos los proyectos pasan por todo con la misma profundidad.

Lo que obtiene el proyecto en cada etapa es una propuesta derivada del Blueprint. Validar antes de publicar.

| Etapa | Objetivo | Qué hacemos | Qué obtiene el proyecto | Contenido visual útil |
|---|---|---|---|---|
| **01 — Entender** | Entender qué se produce y por qué. | Explorar contexto, objetivos, problema y audiencia. | Una comprensión compartida del punto de partida. | Preguntas de entrada, notas y mapas de contexto. |
| **02 — Definir** | Decidir qué vale la pena construir. | Decidir qué resolver, qué no resolver y qué debería producir la solución. | Una definición clara de qué se va a construir y qué queda afuera. | Definición del alcance, prioridades. |
| **03 — Diseñar** | Diseñar la solución antes de convertirla en producto. | Explorar experiencia, estructura, interacción, contenido, identidad y dirección visual cuando corresponda. No siempre en Figma. | La dirección de cómo va a funcionar y verse la solución. | Wireframes, estructuras, exploraciones visuales. |
| **04 — Construir** | Algo que funcione fuera de la idea. | Desarrollo, integración, contenido, automatización, implementación y QA. | La solución construida y revisada. "Funciona" ≠ "está bien hecho". | Detalles de construcción, antes/después, revisión. |
| **05 — Evolucionar** | Una solución no termina necesariamente al publicarse. | Observar, aprender y mejorar. | Mejoras basadas en el uso real y el feedback. | Iteraciones, versiones. |

- **Cierre:** "No buscamos hacer más. Buscamos hacer lo que tiene sentido."
- **CTA:** "Empezar una conversación →" → Contacto.

---

## 5. Nosotros

- **Hero:** "PRANA es una forma de producir." + "Un espacio para convertir ideas, necesidades y problemas en soluciones digitales."
- **Introducción:** breve (2–3 líneas). PRANA parte de entender qué se quiere lograr, no de una solución predeterminada (Brand Core).
- **Principios:** los 6 del Blueprint, cada uno con una línea de desarrollo como máximo.
- **Quién está detrás:**
  - "PRANA fue creado por Ignacio Tomás Sconza."
  - ITS dirige la visión, el criterio y la producción, y experimenta continuamente nuevas formas de crear soluciones digitales.
  - Breve y sin autobiografía. No se presenta un equipo ficticio ni una gran empresa.
- **Relación con ITS:** PRANA es la marca de producción y ITS es la persona detrás. **"Conocé ITS →"** lleva al portfolio de ITS (URL pendiente).
- **MACARIO / Web-Base:** **se omiten en v0.1 pública.** Es arquitectura interna y el Blueprint la marca como secundaria. Si más adelante se incluye, será como mención mínima al final, nunca como protagonista.
- **CTA:** "Empezar una conversación →" → Contacto.

---

## 6. Contacto

- **Hero:** "¿Qué querés construir o qué querés resolver?" + apoyo del Blueprint.
- **Opciones de entrada** (selección única, opcional):
  Tengo una idea · Quiero mejorar algo · Necesito construir algo · Quiero explorar una posibilidad · No estoy seguro
  - Si se llega desde una opción de Home (o desde Capacidades), la opción aparece preseleccionada y se puede cambiar.
  - Si se llega desde otro CTA, no hay preselección.
- **Formulario:**

| Campo | Obligatorio |
|---|---|
| Nombre | Sí |
| Email | Sí |
| ¿Qué querés construir o resolver? | Sí |
| Contanos un poco más | No |
| ¿Hay algo que podamos ver? (web / Instagram / referencia / documento) | No |

- Sin presupuesto obligatorio y sin selección de servicio.
- **Éxito:** el formulario se reemplaza por el mensaje del Blueprint. No se afirma que el proyecto esté iniciado ni confirmado.
- **Después del envío:** link discreto a Proyectos, para seguir explorando si quiere.

---

## 7. Navegación y CTA

- **CTA principal global:** conversar. En Hero y en CTAs finales aparece como "Contanos qué querés construir →" o "Empezar una conversación →", y siempre lleva a Contacto.
- **CTA secundario:** ver evidencia: "Ver proyectos" / "Ver todos los proyectos →" → Proyectos.
- **Navegación principal:** Proyectos · Proceso · Nosotros · Contacto. Contacto está en la navegación y no se duplica como botón extra en el header.

### Recorridos esperados

| Desde | Recorrido esperado | Alternativas |
|---|---|---|
| **Home** | Scroll completo → CTA final → Contacto | Opción de entrada → Contacto (preseleccionado) · card → Caso · Proceso |
| **Proyectos** | Card → Caso → CTA → Contacto | Caso → Otros proyectos · navegación |
| **Proceso** | Lectura → cierre → Contacto | Proyectos para ver el proceso aplicado (vía navegación) |
| **Nosotros** | Lectura → Contacto | "Conocé ITS →" (externo) · Proyectos |
| **Contacto** | Envío → mensaje de éxito | Link a Proyectos |

Cada página termina en una invitación a conversar, pero ninguna obliga: la navegación está siempre disponible y no hay pasos forzados ni pop-ups.

---

## 8. Wireframe conceptual

### HOME

```
[HEADER]
logo PRANA (→ Home) · Proyectos · Proceso · Nosotros · Contacto

[HERO]
Creamos soluciones digitales para ideas que quieren convertirse en realidad.
Transformamos ideas, necesidades y problemas en productos, experiencias y sistemas digitales.
[Contanos qué querés construir →] (Contacto)   [Ver proyectos] (Proyectos)

[ENTRADA POR PROBLEMA]
¿Qué querés construir o qué querés resolver?
( Tengo una idea ) ( Quiero mejorar algo ) ( Necesito construir algo ) ( No estoy seguro )
→ cada una: Contacto con opción preseleccionada

[CAPACIDADES]
Experiencias digitales | Productos digitales | Sistemas | Identidad y contenido
  ejemplos en texto (sin links)
Si no sabés dónde encaja lo que necesitás, podemos empezar por ahí. → Contacto ("No estoy seguro")

[PROYECTOS]
Hecho, no solamente pensado.
Cada proyecto parte de un contexto diferente. La solución también.
[card] [card] [card]   (2–4: visual · nombre · etiqueta · qué es · qué hicimos)
[Ver todos los proyectos →]

[CRITERIO]
No empezamos por la solución.
Primero entendemos qué está pasando. Después decidimos qué vale la pena construir.
· Entender antes de ejecutar  · Resolver antes que decorar
· Lo simple también puede estar muy bien hecho  · Los detalles importan

[PROCESO]
01 Entender → 02 Definir → 03 Diseñar → 04 Construir → 05 Evolucionar
[Conocé nuestro proceso →]

[CTA FINAL]
¿Qué querés construir?
No necesitás saber qué solución necesitás. Solo necesitás saber qué querés lograr.
[Empezar una conversación →]

[FOOTER]
```

### PROYECTOS

```
[HEADER]

[HERO]
Cosas que hicimos realidad.
Cada proyecto empieza en un contexto diferente. Entendemos el problema,
encontramos una dirección y construimos la solución.

[LISTADO]
[card] [card] [card] ...
(visual · nombre · ETIQUETA · qué es / para quién · qué hicimos)  → Caso

[CTA FINAL]
¿Qué podríamos construir juntos?
[Contanos qué querés resolver →]

[FOOTER]
```

### CASO INDIVIDUAL

```
[HEADER]

[ENCABEZADO]
ETIQUETA
Nombre
qué es / para quién · qué hicimos
visual principal

[CONTEXTO]      (opcional)
[DESAFÍO]       (opcional)
[ENFOQUE]       (opcional)
[SOLUCIÓN]
[RESULTADO]     (solo con información real)
[GALERÍA]

[OTROS PROYECTOS]
[card] [card]

[CTA]
¿Qué podríamos construir juntos?
[Contanos qué querés resolver →]

[FOOTER]
```

### PROCESO

```
[HEADER]

[HERO]
No empezamos por la solución. Empezamos por entender.
nota: el proceso se adapta; no es rígido ni necesariamente lineal

[01 — ENTENDER]    objetivo · qué hacemos · qué obtiene el proyecto · visual
[02 — DEFINIR]     ídem
[03 — DISEÑAR]     ídem (no todos los proyectos necesitan Figma)
[04 — CONSTRUIR]   ídem ("Funciona" ≠ "está bien hecho")
[05 — EVOLUCIONAR] ídem

[CIERRE]
No buscamos hacer más. Buscamos hacer lo que tiene sentido.
[Empezar una conversación →]

[FOOTER]
```

### NOSOTROS

```
[HEADER]

[HERO]
PRANA es una forma de producir.
Un espacio para convertir ideas, necesidades y problemas en soluciones digitales.

[INTRODUCCIÓN]
2–3 líneas

[PRINCIPIOS]
6 principios, una línea cada uno como máximo

[QUIÉN ESTÁ DETRÁS]
PRANA fue creado por Ignacio Tomás Sconza.
ITS dirige la visión, el criterio y la producción de PRANA...
[Conocé ITS →] (externo)

[CTA]
[Empezar una conversación →]

[FOOTER]
```

### CONTACTO

```
[HEADER]

[HERO]
¿Qué querés construir o qué querés resolver?
No necesitás saber qué solución necesitás. Contanos qué querés lograr
y vemos juntos por dónde empezar.

[OPCIONES]  (selección única, opcional; preseleccionada si viene de Home)
( Tengo una idea ) ( Quiero mejorar algo ) ( Necesito construir algo )
( Quiero explorar una posibilidad ) ( No estoy seguro )

[FORMULARIO]
Nombre*
Email*
¿Qué querés construir o resolver?*
Contanos un poco más
¿Hay algo que podamos ver? (links)
[Enviar]

[ÉXITO]  (reemplaza el formulario)
Recibimos tu mensaje. Gracias por contarnos sobre el proyecto.
Vamos a revisarlo y te contactamos para seguir la conversación.
→ Ver proyectos

[FOOTER]
```

### FOOTER (global)

```
PRANA
Creamos soluciones digitales para ideas que quieren convertirse en realidad.
Proyectos · Proceso · Nosotros · Contacto
ITS — Ignacio Tomás Sconza
[links sociales / contacto: pendiente]
```

---

## 9. Estado

### Ya definido

- Páginas, navegación y función de cada página.
- Secciones y orden de cada página.
- Destino de cada CTA.
- Entrada por problema → Contacto con preselección.
- Capacidades como orientación, sin páginas de servicio.
- Proyectos sin filtros, con etiquetas en un único listado.
- Estructura flexible de caso individual.
- Estructura del formulario y del mensaje de éxito.
- Copy base (en el Blueprint).

### Pendiente de contenido

- Información completa de Proyecto Raíces, Bresstore e ITS Portfolio (ver checklist en §3), más su etiqueta definitiva.
- Selección de los 2–4 proyectos de Home.
- Visuales de cada proyecto y permisos de publicación.
- Introducción de Nosotros (2–3 líneas) y desarrollo de una línea por principio.
- Validación de "qué obtiene el proyecto" en cada etapa del Proceso.
- URL de "Conocé ITS →".
- Links sociales / contacto del footer.

### Pendiente de Figma

- Dirección visual completa: logo, color, tipografía, sistema visual.
- Tratamiento de cards, etiquetas y opciones de entrada.
- Representación visual del proceso (lineal / cíclica / no lineal).
- Composición de Capacidades.
- Header y footer, y comportamiento mobile.
- Movimiento / animación.

### Pendiente de implementación

- Mecanismo de preselección en Contacto (p. ej. parámetro en la URL).
- Destino y envío del formulario, validación y protección anti-spam.
- Estructura de URLs de los casos.
- Gestión del contenido de proyectos.
- SEO, metadatos y analítica.

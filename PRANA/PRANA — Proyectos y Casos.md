# PRANA — Proyectos y Casos v0.1

> **Documentación interna.** Base factual para futuros casos de estudio de PRANA. **No es copy público.**
> Se apoya en [[PRANA — Estrategia]] (§8 Proyectos y casos), [[PRANA — Presence Blueprint]] y [[PRANA — Arquitectura y Wireframe]].
> No inventa resultados, métricas, fechas, permisos ni responsabilidades. Lo que no está documentado figura como pendiente.

**Fuentes de la información:**

- **[I]:** aportado directamente por Ignacio (relevamiento).
- **[R]:** verificable en la documentación del repositorio / vault.
- **[A]:** reconstruido por un audit técnico (a verificar).

**Separación de identidades:**

- **ITS:** autoría personal.
- **PRANA:** producción externa / marca.
- **MACARIO:** sistema interno.

---

## 1. Propósito

- Reunir en un solo lugar los proyectos que pueden formar parte de la primera presencia pública de PRANA.
- Dejar claro qué se puede afirmar públicamente sobre cada uno y qué no.
- Servir de base para redactar los casos definitivos, según la estructura de caso definida en [[PRANA — Arquitectura y Wireframe]] §3.

---

## 2. Criterio de clasificación

| Etiqueta | Significado |
|---|---|
| `PROYECTO` | Proyecto externo / realizado para un cliente. |
| `CREACIÓN PRANA` | Producción propia de PRANA, más terminada. |
| `EXPERIMENTO PRANA` | Exploración, prueba o concepto todavía abierto. |

---

## 3. Estado general de la base de casos

| Proyecto | Clasificación | Estado | Publicado | Permiso para mostrar | Métricas |
|---|---|---|---|---|---|
| Raíces | `CREACIÓN PRANA` | Activo | Sí (desde principios de agosto 2026) | Sí (proyecto propio) | No hay |
| Bresstore | `PROYECTO` | Activo, en preview | No | Sí | No hay |
| ITS Portfolio | `EXPERIMENTO PRANA` | En desarrollo | — | Proyecto propio; requiere adaptación | No aplica |

Ningún proyecto tiene hoy resultados cuantitativos documentados.

---

## 4. Raíces

**Clasificación:** `CREACIÓN PRANA`

- **Naturaleza:** proyecto propio de turismo aventura. [I]
- **Contexto:**
  - Proyecto orientado a mostrar y comercializar experiencias turísticas por Sudamérica. [I]
  - Comenzó prácticamente desde cero: no había web, redes ni una identidad de marca desarrollada. [I]
  - La marca y el proyecto se construyeron a la par de la web. [I]
- **Necesidad:** crear una presencia digital desde cero para un proyecto que todavía no tenía marca ni canales. [I]
- **Objetivo:** [I]
  - Mostrar y comercializar experiencias turísticas.
  - Presentar la marca.
  - Ordenar la oferta.
  - Permitir que el proyecto crezca con nuevos destinos y experiencias.
- **Alcance:** trabajo realizado íntegramente por Ignacio. Incluyó creación de marca, estrategia, arquitectura, UX, UI/diseño, desarrollo, contenido, infraestructura e integraciones. [I]
- **Decisiones / solución:**
  - Entre las herramientas e integraciones figuran Supabase y Resend. [I]
  - El detalle vive en la documentación del proyecto: [[07 — Proyectos/Proyecto Raíces/00 — Índice|Proyecto Raíces]] (arquitectura, UX-UI, datos e integraciones, decisiones). [R]
- **Resultado:**
  - Web publicada desde principios de agosto de 2026. [I]
  - El feedback disponible es positivo. [I]
  - No hay métricas de negocio, tráfico, conversiones ni reservas. [I]
- **Estado:** activo. [I]
- **Evidencia disponible:**
  - Sitio publicado: https://proyectoraices.com.ar [R]
  - Documentación del proyecto en `07 — Proyectos/Proyecto Raíces/`. [R]
- **Qué podemos afirmar públicamente:**
  - Que es una creación propia de PRANA.
  - Que partió desde cero, sin web, redes ni marca.
  - Que marca y web se construyeron en paralelo.
  - El alcance del trabajo, que el sitio está publicado y que el proyecto sigue activo.
- **Qué todavía no podemos afirmar:**
  - Métricas o resultados comerciales (ventas, reservas, tráfico, conversiones).
  - Cualquier mejora cuantitativa respecto de una situación anterior: no había web previa.
  - Detalle o fuente del feedback positivo, hasta documentarlo.

---

## 5. Bresstore

**Clasificación:** `PROYECTO`

- **Naturaleza:** proyecto para un tercero (un amigo que vende camisetas). [I]
- **Contexto:**
  - El dueño necesitaba una página para vender camisetas y contactó a Ignacio. [I]
  - Bresstore no tenía web al comenzar. [I]
  - No hay documentada una infraestructura digital previa relevante. [I]
- **Necesidad:** vender camisetas online. [I]
- **Objetivo:** crear la página de venta y darle al vendedor un proceso sencillo para recibir pedidos. [I]
- **Alcance:** Ignacio tomó todas las decisiones y realizó todo el trabajo: estructura, UX/UI, diseño y desarrollo. [I]
- **Decisiones / solución:** flujo de compra por WhatsApp, porque le resulta más sencillo al vendedor. [I]
- **Audit técnico:** hay un audit técnico del proyecto, pero **no está en este vault**. Antes de incorporar datos suyos, marcarlos como [A] y separarlos de lo documentado en el repositorio del proyecto.
- **Resultado:** el dueño vio el proyecto y le gusta. No hay resultados comerciales documentados. [I]
- **Estado:** activo; en preview, todavía sin publicar. [I]
- **Evidencia disponible:** preview del proyecto (link pendiente de registrar).
- **Permiso:** hay permiso para mostrarlo públicamente como proyecto de PRANA. [I]
- **Qué podemos afirmar públicamente:**
  - Que es un proyecto para un cliente que no tenía web.
  - Que PRANA hizo estructura, UX/UI, diseño y desarrollo.
  - Que el flujo de compra por WhatsApp se eligió por simplicidad para el vendedor.
- **Qué todavía no podemos afirmar:**
  - Que está publicado o en funcionamiento.
  - Ventas, pedidos o cualquier resultado comercial.
  - Datos técnicos que solo provengan del audit, hasta verificarlos.

---

## 6. ITS Portfolio

**Clasificación:** `EXPERIMENTO PRANA`

> **Separación ITS / PRANA:** el proyecto nació como portfolio personal de ITS. Para PRANA se usa **solo como prueba de solución de portfolio**. **No se presenta como el portfolio personal de Ignacio** y su contenido personal queda fuera de la presentación pública.

- **Naturaleza:** pieza de demostración, no proyecto de cliente. [I]
- **Contexto original:** [I]
  - Creado para mostrar las creaciones personales de Ignacio y comunicar quién es y qué hace.
  - No existía un portfolio ni una web personal previa.
- **Necesidad original:** organizar y priorizar la información. Fue uno de los problemas principales del proyecto. [I]
- **Alcance:** Ignacio hizo todo el trabajo. Las decisiones de estructura, contenido, diseño y desarrollo fueron propias. [I]
- **Adaptación para PRANA:** [I]
  - Eliminar el contenido personal de ITS y la información personal innecesaria.
  - Reemplazarlo por contenido neutro o ficticio cuando haga falta para demostrar la solución.
  - Conservar la estructura y la solución de portfolio.
  - Demostrar estructura, organización de la información, jerarquía, experiencia y ejecución.
  - No mezclarlo con la identidad personal de Ignacio.
- **Resultado:** sin resultados comerciales. [I]
- **Estado:** en desarrollo. [I]
- **Evidencia disponible:** pendiente, hasta tener la versión adaptada.
- **Qué podemos afirmar públicamente:**
  - Que es un experimento / demostración de PRANA sobre cómo resolver un portfolio.
  - Lo relacionado con estructura, organización de la información y jerarquía.
- **Qué todavía no podemos afirmar:**
  - Nada que lo presente como portfolio personal de ITS.
  - Resultados, uso real o clientes.
  - Si se usa contenido ficticio, presentarlo como real.

---

## 7. Selección inicial para la presencia pública de PRANA

| Proyecto | Rol propuesto | Condición para publicarlo |
|---|---|---|
| Raíces | Caso principal | Tener visuales y el caso redactado. |
| Bresstore | Caso de cliente | Que haya suficiente nivel de terminación, según [[PRANA — Estrategia]] §8. Ver pendientes. |
| ITS Portfolio | Experimento | Tener la versión adaptada, sin contenido personal. |

Con estos tres proyectos se cubren las tres etiquetas y el rango de 2–4 proyectos definido para Home ([[PRANA — Arquitectura y Wireframe]]).

---

## 8. Información pendiente para convertir cada proyecto en caso público

### Raíces

- Visuales: capturas, fotos y video.
- Registro concreto del feedback positivo, si se quiere mencionar.
- Decisiones clave a destacar, tomadas de la documentación del proyecto.
- Redacción del caso: Contexto → Desafío → Enfoque → Solución → Resultado (cualitativo) → Galería.

### Bresstore

- Link de preview / URL definitiva.
- Fecha de publicación, cuando ocurra.
- Separar lo verificado en el repositorio de lo reconstruido por el audit.
- Visuales.
- Cómo nombrar al cliente en el caso (marca solamente / sin datos personales).
- Confirmar si se publica como caso antes o después de que el sitio salga de preview.

### ITS Portfolio

- Versión adaptada, sin contenido personal.
- Definir el contenido neutro / ficticio de demostración.
- Nombre con el que se presenta, que no puede ser "ITS Portfolio" en público si remite a lo personal.
- Visuales de la versión adaptada.

---

## Decisiones pendientes

- **Bresstore público:** [[PRANA — Estrategia]] §8 dice que todavía no es caso público y que solo podría serlo con suficiente nivel de terminación. El relevamiento agrega que hay permiso y que está en preview. Hay que decidir si entra en la primera presencia pública estando en preview, o recién cuando se publique. Estrategia no se modificó.
- **Raíces:** [[PRANA — Estrategia]] §8 lo lista como "Proyecto real" y caso público principal. Acá se clasifica como `CREACIÓN PRANA`. No hay contradicción de fondo, pero conviene alinear la terminología de Estrategia cuando se revise.

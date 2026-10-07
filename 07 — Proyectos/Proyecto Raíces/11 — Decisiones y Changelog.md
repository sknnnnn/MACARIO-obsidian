# Proyecto Raíces — Decisiones y Changelog

> Registro permanente de decisiones importantes e hitos del proyecto.
> Esta nota registra únicamente decisiones permanentes y hitos importantes.
> No registrar cambios menores, tareas, sprints ni actividad cotidiana — eso vive en Linear/GitHub.
> Se agrega, no se reescribe.
> Regla transversal: una fuente por tipo de información — enlazar, no copiar. Ver [[07 — Proyectos/Proyecto Raíces/00 — Índice]].

---

## Cómo usar esta nota

Cada entrada nueva se agrega arriba, con fecha. No se borran entradas anteriores. Las entradas migradas desde el documento original no tenían fecha registrada; se marcan explícitamente como "Fecha: no registrada" en vez de inventar una.

---

## Decisiones

> Las entradas del 2026-09-07 al 2026-10-05 se migraron desde Linear el 2026-10-07 (doc "Roadmap — MACARIO STUDIO + WEB-BASE + RAÍCES", doc "PRO-40 — Contrato técnico maestro de experiencias" y la descripción del proyecto "Rediseño y lanzamiento Web"). Linear conserva los originales como referencia.

### Fecha: 2026-10-07 — Estado del proyecto

**Decisión:** Proyecto Raíces sigue **activo**. Su fase actual es reorganización de código, documentación, arquitectura / modelo de datos y preparación del Admin/CMS. Que el sitio público funcione no significa que el proyecto esté terminado.

### Pendiente de decisión — Destino de `comentarios.html`

**Estado:** ⚠️ requiere decisión de Ignacio.
**Contexto:** `comentarios.html` existe, pero no forma parte del Page System aprobado el 2026-10-05.
**Hipótesis preferida (no decidida):** convertir comentarios / testimonios en contenido contextual dentro de Home, Destino, Experiencia u otras páginas.
**Mientras tanto:** no se elimina; queda como legacy.

### Fecha: 2026-10-05 — System Reset: arquitectura Foundation → Components → Patterns → Pages → Content

**Decisión:** la arquitectura de Raíces se consolida como Foundation → Components → Patterns → Pages → Content, migrando progresivamente la base funcional existente, sin rehacer el proyecto desde cero.
**Razón:** ordenar el sistema visual y de contenido, y preparar un futuro Admin / CMS simple.
**Consecuencias:** principio de preservación de lo funcional ([[07 — Proyectos/Proyecto Raíces/08 — Desarrollo|Desarrollo]] §5); el Admin se construye después de estabilizar el modelo ([[07 — Proyectos/Proyecto Raíces/04 — Arquitectura|Arquitectura]] §6–§7).
**Alternativas descartadas:** rehacer el proyecto desde cero.

### Fecha: 2026-10-05 — Principio "mucha lógica detrás, poca fricción delante" y motion

**Decisión:** Raíces (junto con GXK12:2) adopta "simple por defecto → potente cuando hace falta". El motion se define como orgánico, editorial y cinematográfico. Ver [[07 — Proyectos/Proyecto Raíces/05 — UX-UI|UX-UI]] §7–§8.

### Fecha: 2026-09-30 — Decisiones de contenido previas al rediseño

**Decisión:** quitar el contenido de Covid / mascarilla; no mostrar Choquequirao como "Próximamente" cuando tiene una experiencia cargada; reemplazar las fotos solo a mano y con imágenes reales (las generadas, únicamente como preview). Ver [[07 — Proyectos/Proyecto Raíces/06 — Contenido|Contenido]] §1. (Fuente: PRO-115.)

### Fecha: 2026-09-30 — Hito: revisión de seguridad

Revisión de seguridad realizada, con deuda pendiente documentada. Ver [[07 — Proyectos/Proyecto Raíces/09 — QA|QA]] §4. (Fuente: PRO-153.)

### Fecha: 2026-09-28 — Hito: etapa funcional cerrada (estado histórico)

> Estado vigente (2026-10-07): el proyecto sigue **activo**, en reorganización de código, documentación, arquitectura / modelo de datos y preparación del Admin/CMS. Esta entrada registra el estado del 2026-09-28.

Arquitectura, funcionalidad, datos y QA se dan por cerrados. El proyecto sigue abierto para el cierre de UX/UI y dirección visual, trabajados con referencias dentro de Figma. La etapa funcional ya estaba mergeada a `main`.

> Nota 2026-10-07: el cierre de QA convive con una contradicción abierta sobre Sentry ([[07 — Proyectos/Proyecto Raíces/10 — Deploy y Monitoring|Deploy y Monitoring]] §4).

### Fecha: 2026-09 — CTA principal "Reserva ahora" y retiro de Guías

**Decisión:** el CTA principal vigente es "Reserva ahora", con el código y `PROJECT-CONTEXT.md` sincronizados (PRO-85; commits `6c3fc16` / `9857f89`). `guias.html` y `guias-data.js` se retiraron como legacy (PRO-86). Las fechas exactas no quedaron registradas en las issues.

### Fecha: 2026-09-10 — Salidas programadas como fuente del calendario

**Decisión:** las fechas se modelan como salidas concretas en `experiencia_salidas`, que es la única fuente del Calendario de viajes, y el calendario es solo para Travesías. Ver [[07 — Proyectos/Proyecto Raíces/07 — Datos e Integraciones|Datos e Integraciones]] §1. (Fuente: PRO-42.)
**Alternativas descartadas:** temporadas genéricas; usar `detalle.fechas` como fuente.

### Fecha: 2026-09-10 — Contrato técnico y de presentación de experiencias

**Decisión:** el modelo de experiencias es núcleo común + `detalle` JSONB por tipo + tablas relacionales para imágenes, actividades y paquetes. La ficha pública muestra solo la información esencial por tipo.
**Razón:** la auditoría del esquema mostró que ya cubría casi todo el contrato; no convenía una migración grande.
**Detalle:** [[07 — Proyectos/Proyecto Raíces/07 — Datos e Integraciones|Datos e Integraciones]] §1 y [[07 — Proyectos/Proyecto Raíces/05 — UX-UI|UX-UI]] §6.
**Alternativas descartadas:** convertir todos los atributos de `detalle` en columnas o tablas separadas.

### Fecha: 2026-09-08 — Secuencia de incorporación de herramientas

**Decisión registrada en su momento:** Playwright y Sentry se implementan primero en Raíces y luego se generalizan en Web-Base; Archify se valida primero en Web-Base; PostHog y n8n no se incorporan sin una necesidad concreta; Resend se incorpora cuando los formularios reales estén definidos.
**Estado al 2026-10-07:** Playwright y Resend están en uso; Sentry está integrado pero sin DSN; la generalización a Web-Base ya no aplica: Web-Base quedó congelado como referencia histórica (2026-10-07).

### Fecha: 2026-09-07 — Supabase como fuente central de datos

**Decisión:** migrar el frontend a Supabase como fuente de datos (PRO-44, PRO-47; commit `ed0b829`), con `data-api.js` como única capa de acceso.
**Consecuencias:** los archivos de datos JS planos quedaron obsoletos y se eliminaron el 2026-09-30 (commit `5decc72`).

### Fecha: 2026-09-04 — Separación de Patagonia en 5 destinos navegables reales

**Decisión:** El destino agregado "Patagonia" se reemplaza por 5 destinos concretos: Bariloche, Ushuaia, San Martín de los Andes, Villa Pehuenia y Norte Neuquino.
**Razón:** "Patagonia" agrupaba 19 experiencias reales de lugares distintos bajo un único destino navegable, lo cual era geográficamente impreciso (confirmado por commit `3dbc890` del repositorio).
**Alternativas descartadas:** No registradas.

### Fecha: no registrada — Buenos Aires dejó de ofrecerse como destino

**Decisión:** Buenos Aires se retiró de la lista de destinos ofrecidos.
**Razón:** No registrada explícitamente; confirmado por comentario en el código (`assets/js/destinos-data.js`) que indica que puede reincorporarse en el futuro reutilizando la imagen ya conservada.
**Alternativas descartadas:** No registradas.

### Fecha: 2026-09-04 — Plantilla única para páginas de destino

**Decisión:** Se usa una sola plantilla (`catalogo.html`) para los 12 destinos, en vez de una página HTML por destino, accedida vía `?destino=slug`.
**Razón:** Reutilizar el mismo dataset y lógica de filtros ya existente, evitando duplicar código y manteniendo consistencia (confirmado por commits `6cfd3a2` y `4864db2`).
**Alternativas descartadas:** No registradas.

### Fecha: no registrada — Separación de función entre Experiencias y Destinos

**Decisión:** Experiencias funciona como catálogo principal de descubrimiento y venta de experiencias; Destinos funciona como contenido editorial e informativo, sin duplicar el catálogo.
**Razón:** No registrada explícitamente en el documento original.
**Alternativas descartadas:** No registradas en el documento original.

### Fecha: no registrada — Patagonia no es un destino navegable independiente

**Decisión:** Patagonia se usa como referencia geográfica, categoría o agrupación conceptual, pero la navegación debe llevar a destinos concretos (ej. Bariloche, El Chaltén, Ushuaia).
**Razón:** No registrada explícitamente en el documento original.
**Alternativas descartadas:** No registradas.

---

## Hitos

### Fecha: 2026-09-04 — Carga de contenido real de las 11 Travesías

Se reemplazó el placeholder de ejemplo por las 11 Travesías reales del catálogo (Perú y Patagonia), con ficha técnica uniforme (distancia, dificultad, alojamiento, fechas) y CTA unificado a WhatsApp (commits del repositorio).

### Fecha: 2026-09-04 — Unificación de CTA de detalle a un solo botón por experiencia

Los detalles de Tours y Travesías pasan a tener un único botón de contacto directo a WhatsApp, eliminando botones duplicados ("Consultar disponibilidad", "Solicitar información").

### Fecha: no registrada — Eliminación de duplicación de catálogo

Se eliminó la duplicación de catálogo entre Experiencias y Destinos. Destinos quedó orientado hacia contenido editorial/informativo, con posibilidad de enlazar experiencias desde ahí.

### Fecha: no registrada — Las experiencias pueden enlazarse desde Destinos

Las experiencias pueden enlazarse desde Destinos (registrado como consolidado en el documento original).

---

## Documentos relacionados

- [[07 — Proyectos/Proyecto Raíces/00 — Índice]]

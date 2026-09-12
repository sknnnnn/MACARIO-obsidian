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

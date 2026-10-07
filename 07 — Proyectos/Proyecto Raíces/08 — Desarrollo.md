# Proyecto Raíces — Desarrollo

> Decisiones técnicas estables del proyecto.
> No es lista de tareas (Linear) ni el README (GitHub).
> Regla transversal: una fuente por tipo de información — enlazar, no copiar. Ver [[07 — Proyectos/Proyecto Raíces/00 — Índice]].

---

## 1. Stack técnico

Confirmado por inspección directa del repositorio (actualizado 2026-10-07):
- Frontend: HTML + CSS + JavaScript vanilla, sin framework.
- **Datos en Supabase** desde el 2026-09-07 (commit `ed0b829`, PRO-47). Ver [[07 — Proyectos/Proyecto Raíces/07 — Datos e Integraciones|Datos e Integraciones]].
- **i18n ES / EN** (`assets/js/i18n.js`, desde el 2026-09-19).
- **Playwright** para QA (`package.json` y `playwright.config.js` existen desde el 2026-09-08; se usan solo para tests, no como build del sitio).
- **Sentry**: código presente, sin DSN configurado (ver [[07 — Proyectos/Proyecto Raíces/10 — Deploy y Monitoring|Deploy y Monitoring]] §4).

> La versión anterior de esta sección (2026-09-12) describía un sitio sin base de datos y sin `package.json`; quedó superada por los cambios de septiembre.

---

## 2. Estructura de datos

El contenido dinámico vive en Supabase y se lee a través de una única capa:
- `assets/js/supabase-client.js` — inicializa el cliente (URL + clave *publishable*).
- `assets/js/data-api.js` — **única** capa de acceso a Supabase.
- `assets/js/main.js` — render, filtros y navegación.
- `assets/js/i18n.js` — textos ES / EN.
- `assets/js/comentarios-data.js` — comentarios / testimonios (todavía como archivo local).

**Histórico:** hasta septiembre de 2026 los datos vivían en archivos JS planos (`destinos-data.js`, `propuestas-data.js`, `guias-data.js`, `site-config.js`). Se eliminaron en la limpieza técnica del 2026-09-30 (commit `5decc72`).

---

## 3. Convenciones

Pendiente de documentar. No hay convenciones de código formalizadas más allá de la estructura de datos de la sección anterior.

---

## 4. Entornos

Pendiente de documentar. Ver también [[07 — Proyectos/Proyecto Raíces/10 — Deploy y Monitoring]].

---

## 5. Decisiones técnicas relevantes

- Una única plantilla de página de destino (`catalogo.html`), reutilizada por los 12 destinos vía parámetro de URL (`?destino=slug`), en vez de una página HTML por destino. Reduce duplicación y mantiene consistencia de filtros/navegación entre destinos.
- El árbol de navegación País → Destino en Experiencias y en Destinos se arma desde el mismo dataset (`DESTINOS`), evitando dos fuentes distintas de la misma pregunta ("¿qué destinos existen?").
- El botón "volver" en el detalle de una experiencia respeta el destino/filtro de origen cuando se llega desde `catalogo.html` o desde Tours/Travesías/Paquetes con `?destino=...`.
- **`data-api.js` es la única capa de acceso a Supabase.** Ningún otro archivo conoce la URL ni la clave directamente.
- Cambios pequeños, reversibles y verificables; evitar refactors innecesarios; cada cambio relevante se valida visual y funcionalmente.

### Principio de preservación (decisión 2026-10-05, System Reset)

Durante la migración hacia la nueva arquitectura ([[07 — Proyectos/Proyecto Raíces/04 — Arquitectura|Arquitectura]] §6) **no se rehacen ni reemplazan innecesariamente**: Supabase, DataAPI, el modelo Destination / Experience, Tour / Travesía / Paquete, i18n, contacto, disponibilidad, Calendar funcional, Gallery funcional, Sentry, Playwright, `imagen_pos` / foco, ni la relación imagen principal = imagen de card.

- Arquitectura JS: modularización progresiva de `main.js`, sin rewrite masivo.
- CSS: migración progresiva por capas (Foundation → Global → Editorial → Content → Experience → Calendar → Contact).

Fuente: doc Linear [Roadmap](https://linear.app/proyecto-raices/document/roadmap-macario-studio-web-base-raices-3beb4db4f227) §2 y §12, migrado el 2026-10-07.

---

## Documentos relacionados

- [[07 — Proyectos/Proyecto Raíces/00 — Índice]]
- [[07 — Proyectos/Proyecto Raíces/07 — Datos e Integraciones]]
- [[07 — Proyectos/Proyecto Raíces/12 — Enlaces (Linear y GitHub)]]

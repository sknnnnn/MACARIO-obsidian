# Proyecto Raíces — Desarrollo

> Decisiones técnicas estables del proyecto.
> No es lista de tareas (Linear) ni el README (GitHub).
> Regla transversal: una fuente por tipo de información — enlazar, no copiar. Ver [[07 — Proyectos/Proyecto Raíces/00 — Índice]].

---

## 1. Stack técnico

Confirmado por inspección directa del repositorio:
- Sitio estático: HTML + CSS + JavaScript vanilla.
- Sin framework de frontend.
- Sin build system ni gestor de paquetes (no existe `package.json` en el repositorio).

---

## 2. Estructura de datos

El contenido dinámico se gestiona mediante archivos de datos en JavaScript plano (arrays/objetos), sin base de datos ni CMS:
- `assets/js/destinos-data.js` — destinos (array `DESTINOS`).
- `assets/js/propuestas-data.js` — Tours, Travesías y Paquetes.
- `assets/js/comentarios-data.js` — comentarios/testimonios.
- `assets/js/guias-data.js` — datos de la sección Guías.
- `assets/js/site-config.js` — configuración general del sitio.
- `assets/js/main.js` — lógica de render, filtros y navegación (consume los datasets anteriores).

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

---

## Documentos relacionados

- [[07 — Proyectos/Proyecto Raíces/00 — Índice]]
- [[07 — Proyectos/Proyecto Raíces/07 — Datos e Integraciones]]
- [[07 — Proyectos/Proyecto Raíces/12 — Enlaces (Linear y GitHub)]]

# Proyecto Raíces — Datos e Integraciones

> Modelo de datos conceptual e integraciones externas. No duplica esquemas ni código real.
> Regla transversal: una fuente por tipo de información — enlazar, no copiar. Ver [[07 — Proyectos/Proyecto Raíces/00 — Índice]].

---

## 1. Modelo de datos conceptual

**Supabase es la fuente central de datos** desde el 2026-09-07 (PRO-44 / PRO-47; commit `ed0b829` del repositorio). Las páginas no contienen datos duplicados de experiencias.

Contrato del modelo de experiencias (definido el 2026-09-10, PRO-40):

- **`experiencias` — núcleo común:** identificación (`slug`, `nombre`, `tipo_producto` = `tour` / `travesia` / `paquete`, `destino_id`), `resumen`, `descripcion`, `duracion`, `modalidad`, `ubicacion`, `precio` (opcional; solo si existe y es publicable), control de publicación (`publicado`, `activo`, `destacada`, `orden`), imagen principal (`imagen`, `imagen_pos`), `incluye` / `no_incluye` (JSONB) e `info_importante`.
- **`detalle` (JSONB) — atributos específicos por tipo:** se mantiene como contenedor para lo que todavía no justifica tabla propia. No se crean campos ficticios para completar la estructura: si un dato no existe, queda ausente.
- **`experiencia_imagenes`:** galería independiente (`experiencia_id`, `url`, `orden`, `foco`, `alt`). La imagen principal puede seguir en `experiencias.imagen`.
- **`actividades` + `experiencia_actividades`:** actividades normalizadas, relación many-to-many. Se conservan para filtros y automatizaciones.
- **`paquete_experiencias`:** composición de paquetes en relación separada; no se inventan relaciones.
- **Salidas programadas — `experiencia_salidas`** (decisión e implementación del 2026-09-10, PRO-42): el modelo se centra en **salidas concretas**, no en temporadas genéricas: `experiencia → muchas salidas → calendario`. Campos: `experiencia_id`, `fecha_inicio`, `fecha_fin`, `estado` (`programada` / `a_confirmar` / `completa` / `cancelada`), `tipo_salida`, `nota`, `activo`, `orden`. Tiene RLS con lectura pública solo de las salidas activas. Es la forma concreta de la dirección `Experience → Occurrence / Date → Calendar` ([[07 — Proyectos/Proyecto Raíces/04 — Arquitectura|Arquitectura]] §7).
  - Una experiencia sin salida registrada **no está incompleta**: simplemente no tiene fecha programada.
  - El Calendario de viajes se alimenta **exclusivamente** de `experiencia_salidas`. No se usa `detalle.fechas` como fuente, no se duplican fechas en HTML/JS y no se inventan fechas.
  - El calendario es **solo para Travesías**. Los Tours quedan fuera por su reserva flexible y los Paquetes, por ahora.
  - Transición: todavía pueden existir fechas históricas en `detalle.fechas` / `fechasNota`, pero la fuente de verdad de las salidas es `experiencia_salidas`.

Conclusión de arquitectura (auditoría del esquema, 2026-09-10): no hace falta convertir todos los atributos en columnas; la estructura es núcleo común + `detalle` JSONB + tablas relacionales para imágenes, actividades y paquetes.

Fuente: doc Linear [PRO-40 — Contrato técnico maestro de experiencias](https://linear.app/proyecto-raices/document/pro-40-contrato-tecnico-maestro-de-experiencias-6f54d70eb333), migrado el 2026-10-07. El esquema real en Supabase es la referencia técnica ante cualquier diferencia.

---

## 2. Integraciones activas

Confirmado en el repositorio (2026-10-07):

- **Supabase** — datos (acceso únicamente vía `assets/js/data-api.js`; cliente en `assets/js/supabase-client.js` con la clave *publishable*, pública por diseño; la protección la da RLS).
- **Resend** — envío de emails de contacto y fotos, vía funciones de Supabase (referenciado en `assets/js/main.js`; el código de esas funciones no está en el repositorio).
- **Playwright** — QA E2E y regresión (`tests/`).
- **Sentry** — integración presente en el código, pero **no activa**: `SENTRY_DSN = "COMPLETAR"` en `assets/js/sentry-init.js`. Ver contradicción en [[07 — Proyectos/Proyecto Raíces/10 — Deploy y Monitoring|Deploy y Monitoring]] §4.

---

## 3. Fuentes externas

- **Google Drive** (carpeta "Proyecto Raíces"): fuente editorial real para las descripciones de destinos, branding, minutas y banco de imágenes.

---

## 4. Reglas de sincronización

- Supabase es la única fuente de datos de experiencias y destinos; el frontend no duplica datos.
- Toda lectura pasa por `data-api.js` (ver [[07 — Proyectos/Proyecto Raíces/08 — Desarrollo|Desarrollo]] §5).

---

## Documentos relacionados

- [[07 — Proyectos/Proyecto Raíces/00 — Índice]]
- [[07 — Proyectos/Proyecto Raíces/04 — Arquitectura]]
- [[07 — Proyectos/Proyecto Raíces/08 — Desarrollo]]


---

## Implicaciones del nuevo modelo de producto — 2026-11-05 (decisión aprobada; implementación pendiente)

### Destinos
- Ushuaia, Cusco y Ubatuba son los tres destinos principales de esta etapa.
- País deja de ser entidad jerárquica de navegación/alta y permanece como atributo del destino.
- Choquequirao debe convertirse en lugar/área/punto de interés asociado a Cusco. Antes de fusionar, inventariar referencias, experiencias, imágenes, slugs y enlaces; preservar datos y preparar redirecciones. No borrar registros sin plan reversible.

### Guías
- Se necesita una entidad/perfil público de guía, con relaciones hacia destinos y paquetes/experiencias.
- La gestión es exclusiva del Admin; no existe publicación autónoma por parte de los guías.
- El esquema actual no debe asumirse suficiente: auditar tablas y relaciones existentes antes de proponer migración.
- El modelo económico de guías permanece sin definir y no debe codificarse por inferencia.

### Calendario
- La decisión de producto pasa a ser calendario general + disponibilidad individual por propuesta.
- Auditar `experiencia_salidas` como fuente existente y única de fechas programadas. Su alcance histórico exclusivo para Travesías debe revisarse para incluir Paquetes y los tipos que realmente tengan salidas.
- Calendario general y fichas individuales deben consumir la misma fuente; no crear listas paralelas ni duplicar fechas en JSONB/HTML/JS.
- Mantener modalidades de consulta flexible cuando una propuesta no tenga una salida programada. No inventar fechas ni cupos.
- Cualquier ampliación del esquema requiere inventario, plan de migración y pruebas; no aplicar SQL ni modificar producción como parte de esta decisión.

### Consultas
- Formulario contextual y WhatsApp deben coexistir como vías de consulta.
- La consulta debe identificar la propuesta y el destino de origen cuando sea posible.
- No implica checkout, cobro online ni reserva confirmada.

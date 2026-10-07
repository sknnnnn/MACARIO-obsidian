# Proyecto Raíces — Arquitectura

> Estructura de información y producto. Decisiones de estructura ya tomadas.
> No es el código — eso vive en GitHub.
> Regla transversal: una fuente por tipo de información — enlazar, no copiar. Ver [[07 — Proyectos/Proyecto Raíces/00 — Índice]].

---

## 1. Estructura general

```
EXPERIENCIAS
    ↓
catálogo principal de experiencias
    ↓
Tours / Travesías / Paquetes
    ↓
filtros por destino
```

```
DESTINOS
    ↓
contenido editorial e informativo
    ↓
información del lugar
    ↓
accesos a experiencias relacionadas
```

**Documentado en el original:** "Esta separación es deliberada."

**Síntesis derivada** de las reglas documentadas en las secciones 5 y 6 del documento original: Experiencias funciona como catálogo principal; Destinos funciona como contenido editorial/informativo (ver detalle en las secciones 3 y 4 de esta nota).

**Documentado en el original (sección 5):** el catálogo de Experiencias debe permitir explorar Todos, Tours, Travesías, Paquetes y destinos. El usuario puede llegar a una experiencia desde el catálogo y desde filtros.

---

## 2. Jerarquía de información

Jerarquía geográfica:

```
País
  ↓
Destino
  ↓
Experiencias
```

Patagonia no funciona como destino navegable independiente. Se usa como referencia geográfica, categoría, contexto o agrupación conceptual. La navegación debe llevar a destinos concretos.

**Destinos concretos reales confirmados en el código** (`assets/js/destinos-data.js`), 12 en total:

- **Argentina:** Bariloche, Ushuaia, San Martín de los Andes, Villa Pehuenia, Norte Neuquino (contenido real cargado); Norte Argentino (en preparación).
- **Perú:** tarjeta general "Perú" (contenido real); Choquequirao, Paracas, Huacachina, Arequipa, Lima (en preparación — ver detalle de estado por destino en [[07 — Proyectos/Proyecto Raíces/06 — Contenido]]).

**Nota:** `PROJECT-CONTEXT.md` del repositorio todavía lista "Patagonia" y "Norte Argentino" como los destinos de Argentina — quedó desactualizado frente al código, que ya separó Patagonia en sus 5 destinos concretos (confirmado por commit `3dbc890`, ver [[07 — Proyectos/Proyecto Raíces/11 — Decisiones y Changelog]]). Se prioriza el código como fuente de verdad.

Relación Destinos → Experiencias:

```
DESTINO
   │
   ├── información
   ├── contexto
   ├── contenido editorial
   └── experiencias relacionadas
             │
             ▼
        ficha de experiencia
```

Esto permite que Destinos funcione como puerta editorial hacia determinadas experiencias sin duplicar el catálogo.

---

## 3. Decisiones de estructura

- Experiencias es el catálogo principal de descubrimiento y venta de experiencias; Destinos es contenido editorial e informativo, sin duplicar el catálogo. (Registrada también en [[07 — Proyectos/Proyecto Raíces/11 — Decisiones y Changelog]].)
- No crear un segundo catálogo de experiencias dentro de Destinos.
- Destinos no es la principal vía de descubrimiento del catálogo — esa función la cumple Experiencias.

---

## 4. Reglas de navegación

- No duplicar el catálogo de experiencias entre Experiencias y Destinos.
- Regla de navegación geográfica: ver "2. Jerarquía de información" en esta misma nota (la navegación debe llevar a destinos concretos, no a agrupaciones regionales amplias como Patagonia).

---

## 5. Páginas y estructura de navegación real

Confirmado por inspección directa del código.

**Navegación principal (header):** Experiencias, Destinos, Nosotros, Galería, Contacto. CTA fijo "Reserva ahora" → Contacto (CTA principal vigente, PRO-85).

**Páginas secundarias** (enlazadas desde el pie de página en todo el sitio): Tours, Travesías, Paquetes, Comentarios — cada una existe como página propia además de como filtro dentro de Experiencias.

**Plantillas reutilizadas por parámetro de URL** (no son una página por destino/experiencia):
- `catalogo.html?destino=slug` — plantilla única de página de destino, usada por los 12 destinos.
- `propuesta.html` — plantilla de ficha de detalle de experiencia.

**Guías — retirada:** `guias.html` era una página legacy sin enlaces. Se retiró del repositorio junto con `assets/js/guias-data.js` y su CSS exclusivo, tras confirmar que no tenía dependencias vigentes. `PROJECT-CONTEXT.md` documenta la retirada. **Hoy no existe una sección pública de Guías.** (Fuente: PRO-86, migrada el 2026-10-07.)

---

## 6. Arquitectura de sistema — System Reset (decisión 2026-10-05)

La arquitectura de Raíces se consolida como:

```
Foundation → Components → Patterns → Pages → Content
```

- **No se rehace el proyecto desde cero:** la base funcional existente migra progresivamente hacia este sistema.
- **Foundation:** tipografía, color, grid, spacing, breakpoints, aspect ratios, motion y estados.
- **Componentes globales:** header, header mobile, footer, button, link, selector de idioma, breadcrumb.
- **Componentes editoriales:** hero, section header, bloque editorial, imagen, imagen + texto, quote / manifiesto, galería, content card.
- **Experience System:** tipo de experiencia, metadata, itinerario, incluye / no incluye, disponibilidad, próximas fechas, CTA de experiencia.
- **Calendar:** calendario, filtros, grupo de fechas, ítem de experiencia, estado de disponibilidad.
- **Páginas del Page System aprobado:** Home → Experiencia → Destino → Calendario → Galería → Nosotros → Contacto.

El orden de implementación y su avance son trabajo operativo y viven en Linear. Las reglas técnicas de preservación están en [[07 — Proyectos/Proyecto Raíces/08 — Desarrollo|Desarrollo]] §5.

> ⚠️ **Pendiente de decisión:** `comentarios.html` existe pero no forma parte del Page System aprobado. No se elimina todavía; la hipótesis preferida es convertir comentarios / testimonios en contenido contextual dentro de Home, Destino o Experiencia. Ver [[07 — Proyectos/Proyecto Raíces/11 — Decisiones y Changelog|Decisiones]].

## 7. Preparación para un Admin / CMS (decisión 2026-10-05)

La arquitectura de sistema también se adopta para que un futuro Admin de contenido sea simple. Separación fundamental:

```
ADMIN → CONTENT MODEL → SUPABASE → DATA API → PAGES / COMPONENTS / PATTERNS
```

- El Admin **no controla la presentación visual**: administra entidades y relaciones del producto.
- **Entidades administrables:** Destinos (nombre, descripción, imagen principal, galería, experiencias y contenido editorial relacionados), Experiencias (nombre, tipo, destino, descripción, duración, logística, itinerario, incluye / no incluye, fotografías, fechas, disponibilidad, estado, CTA), Fotografías (imagen, destino, experiencia, personas, momento, historia) y Calendario (experiencia, fecha / ocurrencia, disponibilidad, estado).
- **Modelo de fechas:** `Experience → Occurrence / Date → Calendar`. No se crea una experiencia duplicada por cada fecha.
- **Regla:** primero el modelo y el sistema, después el Admin. No construir el Admin sobre una arquitectura que todavía está cambiando.

Modelo de datos actual de experiencias: [[07 — Proyectos/Proyecto Raíces/07 — Datos e Integraciones|Datos e Integraciones]].

Fuente de §6–§7: doc Linear [Roadmap](https://linear.app/proyecto-raices/document/roadmap-macario-studio-web-base-raices-3beb4db4f227) §12, migrado el 2026-10-07.

---

## Documentos relacionados

- [[07 — Proyectos/Proyecto Raíces/00 — Índice]]
- [[07 — Proyectos/Proyecto Raíces/05 — UX-UI]]
- [[07 — Proyectos/Proyecto Raíces/07 — Datos e Integraciones]]

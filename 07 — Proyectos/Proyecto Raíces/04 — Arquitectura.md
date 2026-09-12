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

**Navegación principal (header):** Experiencias, Destinos, Nosotros, Galería, Contacto. CTA fijo "Reservá ahora" → Contacto.

**Páginas secundarias** (enlazadas desde el pie de página en todo el sitio): Tours, Travesías, Paquetes, Comentarios — cada una existe como página propia además de como filtro dentro de Experiencias.

**Plantillas reutilizadas por parámetro de URL** (no son una página por destino/experiencia):
- `catalogo.html?destino=slug` — plantilla única de página de destino, usada por los 12 destinos.
- `propuesta.html` — plantilla de ficha de detalle de experiencia.

**Página huérfana detectada:** `guias.html` existe en el repositorio pero no está enlazada desde ninguna otra página del sitio. Su función no está documentada ni en Obsidian ni en `PROJECT-CONTEXT.md` — pendiente de confirmar con Ignacio si sigue vigente.

---

## Documentos relacionados

- [[07 — Proyectos/Proyecto Raíces/00 — Índice]]
- [[07 — Proyectos/Proyecto Raíces/05 — UX-UI]]
- [[07 — Proyectos/Proyecto Raíces/07 — Datos e Integraciones]]

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

Patagonia no funciona como destino navegable independiente. Se usa como referencia geográfica, categoría, contexto o agrupación conceptual. La navegación debe llevar a destinos concretos (ej. Bariloche, El Chaltén, Ushuaia).

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

## Documentos relacionados

- [[07 — Proyectos/Proyecto Raíces/00 — Índice]]
- [[07 — Proyectos/Proyecto Raíces/05 — UX-UI]]
- [[07 — Proyectos/Proyecto Raíces/07 — Datos e Integraciones]]

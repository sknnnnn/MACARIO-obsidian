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

> Nota 2026-10-07: `destinos-data.js` se eliminó el 2026-09-30 al migrar a Supabase. La lista siguiente refleja ese archivo y hay que re-verificarla contra Supabase.


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


---

## Revisión estratégica — 2026-10-26 (propuesta, pendiente de aprobación de arquitectura)

### Cambio confirmado de orientación comercial

Proyecto Raíces pasa a priorizar comercialmente los **paquetes de viaje**. Tours y travesías continúan formando parte de la oferta; no se eliminan ni se consideran productos obsoletos.

Raíces también desarrollará una propuesta de visibilidad y comercialización para guías locales. La dirección deseada contempla perfiles propios de guías, con información real y experiencias asociadas a los destinos donde trabajan.

### Implicaciones para la arquitectura

- Evaluar Paquetes y Guías como ejes principales de descubrimiento y propuesta de valor.
- Mantener Tours y Travesías como categorías vigentes dentro del sistema de experiencias.
- Mantener Destinos como contenido editorial que conecta territorio, guías y propuestas.
- Diseñar una experiencia integrada: no convertir cada categoría en un sitio separado.
- Reemplazar la jerarquía histórica Experiencias → Tours/Travesías/Paquetes solo después de aprobar un mapa de navegación nuevo.

### Límites y decisiones pendientes

- La estructura exacta del menú y las rutas de navegación todavía no están aprobadas.
- El modelo de datos actual contempla experiencias y composición de paquetes, pero la existencia de un modelo completo de perfiles de guías no está verificada.
- No está definido el modelo económico del servicio a guías (suscripción, comisión, cobros u otro).
- No asumir pagos en línea, reserva automática ni cambios de datos sin definición y autorización.

Esta revisión registra la nueva orientación y abre la revisión de la arquitectura anterior; no modifica por sí sola el código ni declara implementadas nuevas funcionalidades.


---

## Pausa y secuencia de reestructuración — 2026-10-26

Raíces queda en pausa al cerrar esta sesión. La orientación estratégica ya está documentada arriba; no se crean documentos paralelos ni se considera aprobada una nueva arquitectura.

### Próxima fase: avanzar sin mezclar diseño y operación

1. **Inventario real del sitio:** páginas, componentes, assets, tokens, datos disponibles y relaciones existentes. Es el primer paso de la reestructuración y puede comenzar sin esperar a cerrar todos los pendientes operativos.
2. **Propuesta de arquitectura:** jerarquía de navegación, relación entre Paquetes, Guías locales, Tours, Travesías y Destinos; qué se conserva, evoluciona o propone retirar. Destinos conecta editorialmente y no duplica el catálogo.
3. **Propuesta de dirección visual:** parte de la identidad orgánica, aventurera, humana, editorial y natural vigente. No cambia automáticamente Brand Bible, paleta ni tipografías.
4. **Aprobación explícita:** no implementar pantallas finales ni cambiar modelo de datos antes de aprobar arquitectura y dirección visual.
5. **Implementación por etapas:** solo después de la aprobación, con pruebas y sin merge/deploy sin autorización.

### Dependencias y límites

- PRO-172 (respaldo real y restauración aislada) **no bloquea el inventario ni la propuesta conceptual**. Sí es requisito previo para cambios sensibles/destructivos en datos o producción, nuevas migraciones o pruebas reales que puedan alterar datos.
- PRO-165 (calendario), PRO-166 (subida de imágenes) y PRO-162/163/164 (escrituras y datos de prueba) siguen pendientes de diagnóstico/evidencia; se pueden resolver en paralelo al inventario.
- Reconciliar el Loop 2 del Admin (etapas B–F) según la nueva estrategia; la etapa A sigue cerrada en `ef6b175` y no se repite.
- No inventar guías, biografías, destinos, experiencias, imágenes ni testimonios. El modelo económico para guías sigue sin decidirse; no presuponer pagos ni reservas automáticas.

La pausa no cierra estos pendientes ni autoriza cambios en código, datos, producción o despliegue.

# Proyecto Raíces — Contenido

> Reglas editoriales y de contenido del proyecto.
> Regla transversal: una fuente por tipo de información — enlazar, no copiar. Ver [[07 — Proyectos/Proyecto Raíces/00 — Índice]].

---

## 1. Reglas editoriales

- El contenido debe ser real. No inventar: experiencias, destinos, precios, fechas, servicios, testimonios, datos comerciales, información geográfica específica.
- Los placeholders deben eliminarse antes del cierre del proyecto.

Flujo ante dato faltante (según el documento original):

```
dato faltante
    ↓
registrar pendiente
    ↓
obtener información real
    ↓
incorporar
```

### Guía editorial de descripciones de experiencias (2026-09-10)

Toda descripción debe poder organizarse conceptualmente en: 1) qué es; 2) qué experiencia ofrece; 3) qué se hace o recorre; 4) qué la hace especial; 5) para quién está pensada, cuando corresponda; 6) información / logística relevante. Es una guía editorial, no una plantilla de texto literal. (Fuente: doc Linear PRO-40 §7.)

### Decisiones de contenido (2026-09-30, PRO-115)

- El contenido de **Covid / mascarilla** se elimina de la propuesta pública.
- **Choquequirao** no se muestra como "Próximamente" cuando existe una experiencia cargada para ese destino.
- **Fotografías:** no hay reemplazos automáticos ni imágenes inventadas. La selección y el reemplazo se hacen a mano, revisando las imágenes reales una por una. Las fotos finales tienen que ser reales de Raíces; las imágenes generadas sirven solo como preview / referencia, nunca como contenido final.
- No se introducen contenidos ni secciones no definidas para el rediseño.

### Fuente editorial real

Las descripciones de destinos se actualizan desde la fuente real disponible en Google Drive (carpeta "Proyecto Raíces"); no se inventa contenido cuando existe una fuente editorial real. (Fuente: doc Linear Roadmap §2, fase C.)

> Nota 2026-10-07: el estado por destino de la sección 4 se tomó de `destinos-data.js`, archivo eliminado el 2026-09-30 al migrar a Supabase. Hay que re-verificarlo contra Supabase.

---

## 2. Tono y voz

Pendiente de definir explícitamente. No documentado en el original más allá de los principios de dirección de producto (ver [[07 — Proyectos/Proyecto Raíces/05 — UX-UI]]).

---

## 3. Tipos de contenido

**Tours:** experiencias organizadas, generalmente de menor duración y con una propuesta concreta.

**Travesías:** experiencias de aventura y exploración (trekking, senderismo, MTB, buceo, entre otras), de uno o varios días, que pueden ofrecerse como experiencia, experiencia con servicios incluidos o propuesta integral.

**Paquetes:** propuestas integrales que combinan distintos componentes de una experiencia. Esta categoría debe utilizarse solo cuando exista realmente una propuesta de paquete.

**Destinos (contenido editorial e informativo):** puede incluir información del destino, características, naturaleza, cultura, atractivos, contexto, contenido editorial, referencias visuales y experiencias relacionadas.

---

## 4. Pendientes de contenido

Estado real confirmado en el código (`assets/js/destinos-data.js`), 12 destinos en total:

**Con contenido real cargado:**
- Argentina: Bariloche, Ushuaia, San Martín de los Andes, Villa Pehuenia, Norte Neuquino.
- Perú: tarjeta general "Perú".

**Pendientes / en preparación** (marcados explícitamente en el código como tales, sin contenido inventado):
- Norte Argentino (Argentina) — tiene imagen y resumen cargados, pero el destino sigue marcado como en preparación.
- Choquequirao (Perú) — imagen y resumen reales ya cargados (reutilizados de la Travesía "Choquequirao Trekking"), pero el destino sigue marcado como en preparación.
- Paracas, Huacachina, Arequipa, Lima (Perú) — sin imagen ni contenido real; el código muestra "Imagen pendiente" / "En preparación" en vez de contenido inventado o prestado de otro destino.

Definir y completar el contenido editorial e informativo de estos destinos pendientes (estructura, imágenes, narrativa, información útil) sigue siendo trabajo pendiente. Esta sección documenta qué información falta, únicamente a fines de conocimiento del proyecto. No reemplaza ni sustituye el seguimiento operativo: cualquier tarea de seguimiento para completar este contenido debe crearse y trackearse en Linear.

---

## Documentos relacionados

- [[07 — Proyectos/Proyecto Raíces/00 — Índice]]
- [[07 — Proyectos/Proyecto Raíces/09 — QA]]

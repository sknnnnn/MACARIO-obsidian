# Proyecto Raíces — UX/UI

> Dirección de producto y visual. Principios que guían decisiones de diseño.
> Regla transversal: una fuente por tipo de información — enlazar, no copiar. Ver [[07 — Proyectos/Proyecto Raíces/00 — Índice]].

---

## 1. Dirección de producto

El sitio debe sentirse como una propuesta de experiencias y aventura, no como una agencia de turismo tradicional genérica. La experiencia debe priorizar: descubrimiento, inspiración, claridad, fotografía, narrativa, confianza y acceso sencillo a las experiencias. El contenido y las imágenes deben trabajar juntos.

---

## 2. Principios de UX

Pendiente de definir como lista independiente. En el documento original estos principios están integrados dentro de la dirección de producto (sección 1) y no se separan en principios de interacción/navegación propios.

---

## 3. Dirección visual

La referencia general busca una estética de turismo de aventura con personalidad (ver referencias en [[07 — Proyectos/Proyecto Raíces/03 — Identidad y Referencias]]). Debe evitarse una estética genérica de template. La interfaz debe permitir que:

- las fotografías tengan protagonismo;
- el contenido respire;
- la navegación sea clara;
- las experiencias se sientan concretas.

---

## 4. Componentes clave

Confirmado por `PROJECT-CONTEXT.md` del repositorio y por el código implementado.

### CTA
- CTA principal implementado en la navegación: **"Reservá ahora"** (enlaza a Contacto).
- En la home, CTAs del hero: "Ver experiencias" y "Reservá por WhatsApp".
- En el detalle de Tours y Travesías: un único botón de CTA ("Consultar este Tour"/"Consultar esta Travesía") que enlaza directo a WhatsApp con el nombre de la experiencia — se eliminaron botones duplicados como "Consultar disponibilidad"/"Solicitar información" (confirmado por commits del repositorio).
- Las consultas/reservas derivan a WhatsApp y, según el contexto, a Google Forms u otros mecanismos (`PROJECT-CONTEXT.md`).
- El sitio no funciona como e-commerce (regla explícita de `PROJECT-CONTEXT.md`).

**Nota de discrepancia:** `PROJECT-CONTEXT.md` describe el CTA principal como "Consultar" (con "Reservar ahora" como secundario). El código implementado usa "Reservá ahora" como CTA principal de navegación y "Consultar este Tour/esta Travesía" en el detalle. Se documenta acá el comportamiento real del código, confirmado por inspección directa; queda pendiente de decisión si `PROJECT-CONTEXT.md` debe actualizarse para reflejarlo.

### Reglas fotográficas
Confirmado por `PROJECT-CONTEXT.md`:
- Priorizar paisajes reales, personas viviendo las experiencias, montaña, naturaleza, aventura y elementos característicos de cada destino.
- Evitar overlays verdes excesivos, filtros que oculten la fotografía, crops arbitrarios, imágenes deformadas y proporciones inconsistentes entre cards similares.
- Si una fotografía tiene un elemento protagonista, evitar recortarlo innecesariamente.

Regla aplicada activamente en el código: se corrigieron encuadres de cards donde se cortaba la cabeza o el sombrero de una persona (Travesías "Cruce Andino x Lagos a Chile" y "Domuyo").

### Reglas de hero
Confirmado por `PROJECT-CONTEXT.md` y aplicado en el código:
- El hero debe priorizar la fotografía; el overlay no debe cubrirla en exceso ni el contenido tapar elementos importantes.
- El recorte no debe eliminar el punto focal de la imagen.
- Al modificar un hero, revisar desktop, mobile, posición del contenido, crop y legibilidad del texto.

Implementado: la página de destino (`catalogo.html`) migró de un hero casi de pantalla completa a un formato compacto (imagen + kicker + título + resumen), igual al de Nosotros/Galería, reduciendo la altura del hero en mobile de ~73% a ~53% del viewport.

### Reglas de cards
Confirmado por `PROJECT-CONTEXT.md` y aplicado en el código:
- Evitar textos cortados, títulos truncados, alturas inconsistentes en grillas, botones desplazados, imágenes con proporciones distintas sin intención.
- Priorizar responsive y comportamiento natural del contenido antes que truncar texto agresivamente.

Implementado: en `catalogo.html`, todas las cards de experiencias tienen el mismo alto exacto independientemente del destino, tipo o imagen.

---

## 5. Decisiones visuales implementadas (registro)

- Fondo con textura compartido entre Experiencias, Tours, Travesías, Paquetes, Nosotros, Galería, Contacto, Propuesta y (ahora) `catalogo.html`.
- Sistema de contenido "en preparación": pill visual punteada con el texto "En preparación" / "Imagen pendiente", usado de forma consistente en destinos sin contenido real y en perfiles de equipo sin datos confirmados (reemplaza textos repetidos como "Rol pendiente"/"Descripción pendiente").
- Fix de overflow horizontal en mobile/tablet (el menú lateral fuera de pantalla inflaba el ancho de scroll del documento).

---

## Documentos relacionados

- [[07 — Proyectos/Proyecto Raíces/00 — Índice]]
- [[07 — Proyectos/Proyecto Raíces/03 — Identidad y Referencias]]
- [[07 — Proyectos/Proyecto Raíces/04 — Arquitectura]]

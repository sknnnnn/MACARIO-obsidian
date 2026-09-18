# [Nombre del proyecto] — Contexto y Brief

> Salida de Discovery: contexto estable del proyecto — de dónde viene, para quién es, qué problema resuelve y qué se sabe con certeza antes de pasar a Product Definition. Ver el proceso de Discovery en [[MACARIO — Flujo de trabajo]].
> No incluye tareas ni estado operativo — eso vive en Linear.
> Completar solo lo que aplique al proyecto: Discovery pregunta lo necesario, no todo siempre.
> Antes de marcar algo como faltante, cruzar las fuentes del proyecto que correspondan (repo, README, PROJECT-CONTEXT o equivalente, documentación de marca). Si el dato existe ahí pero no acá, es `Confirmado en otra fuente`, no `Faltante` — ver los estados de Discovery en [[MACARIO — Flujo de trabajo]].
> Regla transversal: una fuente por tipo de información — enlazar, no copiar. Ver [[00 — Índice]].

---

## 1. Origen del proyecto

[Cómo y por qué surge este proyecto: idea, pedido, brief, problema o proyecto existente.]

---

## 2. Cliente / Stakeholder

**Nombre:** [nombre]
**Contacto:** [email / whatsapp]
**Rol en el proyecto:** [cliente directo / interno MACARIO / etc.]

---

## 3. Problema que resuelve

[Qué necesidad real atiende el proyecto.]

---

## 4. Usuarios / audiencia

[Quién usa o consume el producto o servicio. Distinguir de quién lo pide, si son personas distintas.]

---

## 5. Producto o servicio

[Qué es concretamente lo que se va a construir u operar, en una descripción breve. El detalle de alcance vive en [[02 — Objetivos y Alcance]].]

---

## 6. Modelo de negocio

[Cómo genera valor o ingresos el proyecto, si aplica. NO CONFIRMADO si todavía no se sabe.]

---

## 7. Funcionalidades conocidas

[Funcionalidades que ya se saben necesarias, aunque no estén detalladas todavía. El detalle técnico vive en [[04 — Arquitectura]] y [[07 — Datos e Integraciones]].]

---

## 8. Canales y contexto de uso

[Dónde y cómo se usa el producto: web, mobile, presencial, redes, etc.]

---

## 9. Recursos disponibles

[Qué existe ya y se puede reutilizar: repositorio, contenido, assets, integraciones, equipo.]

---

## 10. Restricciones técnicas conocidas

[Restricciones de stack, hosting, integraciones u otras condiciones técnicas ya conocidas antes de definir arquitectura. Las decisiones técnicas ya tomadas viven en [[04 — Arquitectura]] y [[08 — Desarrollo]].]

---

## 11. Tiempo y presupuesto

[Plazos y presupuesto conocidos, si existen. NO CONFIRMADO si no se sabe todavía.]

---

## 12. Contexto relevante

[Cualquier antecedente, restricción o condición adicional que afecte cómo se piensa el proyecto.]

---

## 13. Incertidumbres pendientes

[Qué preguntas siguen abiertas y qué falta confirmar, a nivel general del proyecto. No inventar esta información: si no está confirmada, se marca como NO CONFIRMADO y se pregunta antes de avanzar. Los pendientes específicos de contenido viven en [[06 — Contenido]], no acá.

Si una incertidumbre listada acá se resuelve más adelante en otra fuente (repo, código, cliente), reconciliar: actualizar este dato acá y registrar la decisión en [[11 — Decisiones y Changelog]], en vez de dejarla pendiente sin actualizar.]

---

## 14. Discovery Gate

> ¿Tenemos suficiente información para pasar a Product Definition sin inventar requisitos?

**Estado:** [Sí / Parcial / No]

**Si es "Sí":** justificación breve. Registrar el cierre de Discovery como hito en [[11 — Decisiones y Changelog]].

**Si es "Parcial":**
- Qué está resuelto: [...]
- Qué falta: [...]
- Qué de eso bloquea Product Definition: [...]
- Qué riesgo se acepta si se continúa: [...]

**Si es "No":** el proyecto permanece en Discovery hasta resolver los gaps que bloquean Product Definition (no todos los gaps posibles).

### Chequeos obligatorios

Completar los tres, aunque el resultado sea "No aplica" (con justificación) — no omitir en silencio ni inventar un valor.

- **Objetivo medible:** [Confirmado / Confirmado en otra fuente / Decisión / Hipótesis / Faltante / No aplica — detalle. Ver [[02 — Objetivos y Alcance]]]
- **Modelo de negocio / monetización:** [ídem. Ver sección 6 de esta nota]
- **Tiempo / presupuesto:** [ídem. Ver sección 11 de esta nota]

---

## Documentos relacionados

- [[00 — Índice]]
- [[02 — Objetivos y Alcance]]
- [[03 — Identidad y Referencias]]
- [[04 — Arquitectura]]
- [[06 — Contenido]]
- [[07 — Datos e Integraciones]]
- [[08 — Desarrollo]]
- [[11 — Decisiones y Changelog]]

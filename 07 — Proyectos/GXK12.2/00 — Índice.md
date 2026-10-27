# GXK12:2 — Índice

> Nota de entrada del proyecto dentro de MACARIO.
> Fuentes: Linear = ejecución/tareas · GitHub = código · Obsidian = documentación · Brand & E-commerce Bible = verdad de marca/UX/contenido · Dirección Visual = traducción visual aprobada · Figma Pro = exploración y validación visual.

---

## Resumen

GXK 12:2 es un espacio de exploración y transformación a través de la ropa (slogan: NO TE CONFORMES. TRANSFORMATE.). Su soporte es un e-commerce completo de indumentaria para GXK: tienda pública con catálogo, variantes (talles/colores) y stock reducido por variante, carrito, checkout como invitado, pagos con Mercado Pago, envíos (Andreani / Correo Argentino), seguimiento de pedido sin cuenta, y un panel administrativo privado (único administrador inicial) para gestionar productos, fotografías, stock, pedidos y outfits/selecciones editoriales.

---

## Estado general

**Estado:** Proyecto activo. El Preview de la rama candidata `claude/bold-cerf-sj4d8y` volvió a funcionar tras corregir el alcance de las variables de entorno de Preview en Vercel. La siguiente etapa es completar QA y verificar el aislamiento de Supabase antes de preparar una integración; todavía no está autorizado hacer merge. La Brand & E-commerce Bible y la Dirección Visual aprobada siguen siendo obligatorias.

**Última actualización:** 2026-10-27.

**Checkpoint actual (2026-10-27) — recorrido de compra en diseño:**
- **Terminado hoy:** Tienda v22, B3 Carrito y B4 Checkout están en Figma (PRANA STUDIOS, página `GxK12.2`: Tienda `509:1114`, B3 `533:1567`, B4 `548:2482`, índice del recorrido `526:1505`) como capas nativas editables, con la auditoría de coherencia con la Biblia aplicada. B4 fue aceptado en Claude Design v28; la v30 solo sincroniza B3 con Figma y suma la decisión sobre efectivo. Detalle: [[07 — Proyectos/GXK12.2/09 — GXK12.2 — Decisiones y Changelog|Decisiones y Changelog]] (27/10).
- **Pendiente:** decisiones comerciales (costos de entrega, cuotas, alcance del Camino, política de precio) y dependencias técnicas (precio del resumen, resumen siempre visible, doble envío y reintento, Mercado Pago y envíos en producción). Todo el recorrido sigue sin implementar.
- **No repetir:** la auditoría integral de coherencia, las decisiones aceptadas de B3 y B4 ni su traspaso a Figma.
- **Próximo bloque (28/10):** B5 — Resultado / confirmación (`/checkout/retorno`): estados del panel de pedido (esperando pago, pago confirmado, rechazado, incidencia, cancelado, punto de encuentro con saldo, pedido no encontrado), con Claude Design primero y después Figma. Condición de inicio: abrir el índice `526:1505` (fila «7 Confirmación» y tabla de dependencias), la sección B4 (estados de resultado y conexión con B5), el código de `src/app/(storefront)/checkout/retorno` y `OrderStatusPanel` en `6be7d02`, y la Biblia §32–33. No hay bloqueos de diseño.

**Estado del recorrido de compra (27/10).** «Aceptado» = revisión visual aceptada por el usuario; no significa funcionalidad implementada. Nada del recorrido está implementado todavía.
| Bloque | Diseñado | Aceptado | Pendiente de definición | Pendiente de implementación |
|---|---|---|---|---|
| Home V0.4 y Ficha (D1b) | Sí (Figma) | Ficha: aprobada el 26/10 (Claude Design v19) | D7, D8, D10 (ver índice de Figma) | Sí |
| Tienda v22 y /buscar | Sí | Sí | D1 (2.ª línea de /buscar sin término), D2 (paginación) | Sí |
| B3 Carrito | Sí | A página completa: sí. Confirmación al agregar, A5 y nota de stock: propuestas, no aprobadas | Ubicación y redacción final de la nota de stock | Sí, incluida accesibilidad del panel |
| B4 Checkout | Sí | Sí (Claude Design v28) | Costos de entrega, cuotas, alcance del Camino, política de precio | Sí |
| B5 Confirmación (`/checkout/retorno`) | **No comenzó** | No | A confirmar con las fuentes canónicas | Sí |

**Mapa de fuentes vigentes (27/10):** Claude Design v30 (https://claude.ai/artifact/3CjPmcc7Hp7QRau2yw6rKi); Figma PRANA STUDIOS, página `GxK12.2`: índice `526:1505`, Tienda `509:1114`, B3 `533:1567`, B4 `548:2482`; código en `sknnnnn/GxK12-2` (referencia `6be7d02`): `src/app/(storefront)/checkout/CheckoutFlow.tsx`, `src/app/(storefront)/checkout/retorno/page.tsx`, `src/components/storefront/orders/OrderStatusPanel.tsx`; Linear (sin cambios): PRO-124 (Mercado Pago), PRO-125 y PRO-126 (Andreani y Correo), PRO-127 (peso y dimensiones), PRO-128 (flujo real de envíos), PRO-129 (liberación de reservas vencidas: revisar contra Biblia §17 antes de ejecutar).

**Tarea inicial de la próxima sesión (única):** B5 — Resultado / confirmación del checkout (`/checkout/retorno`). Fuentes: índice `526:1505`, B4 `548:2482`, Biblia §32–33, Claude Design v30 y el código citado, solo como referencia del comportamiento real. Estados a confirmar con las fuentes: pago pendiente, confirmado, rechazado, incidencia o cancelación, punto de encuentro con saldo, pedido no encontrado. No se inventan políticas comerciales. La auditoría de qué se administra desde el Admin (por ejemplo efectivo) se hace después de completar diseño e implementación.

**Checkpoint anterior (2026-10-26):** D1b de storefront sigue aprobado en Claude Design v19: https://claude.ai/artifact/3CjPmcc7Hp7QRau2yw6rKi. **Nueva decisión (26/10): trasladar el diseño aprobado a Figma en frames editables para que el usuario pueda retocarlo; hacerlo antes de implementar D1b, sin sobrescribir diseños existentes.** La rama `claude/bold-cerf-sj4d8y` está 21 commits por delante de `master` y 3 por delante de `fix/home-v04-visual`; Vercel reportó `READY` y el usuario confirmó que el Preview volvió a funcionar tras corregir el alcance de variables de entorno para Preview. URL: https://gx-k12-2-314cw1oto-proyecto-travesia.vercel.app/. Próximo paso para el 27/10: comprobar aislamiento de Supabase (bloqueante para pruebas de escritura), hacer QA de Home V0.4 y Admin Lote 1, verificar tests/migraciones por entorno y preparar PR sin hacer merge. No tocar `master` ni producción sin autorización explícita. Detalle: [[07 — Proyectos/GXK12.2/09 — GXK12.2 — Decisiones y Changelog|Decisiones y Changelog]].

> **Registro histórico — Home V0.3 (2026-10-07):** la implementación estaba presente en master, pero su presencia no equivalía a aprobación ni QA. El checkpoint operativo actual es el Admin Lote 1 descrito arriba; el diseño público permanece pausado.
> - El código ya está en `master` del repositorio (commit `950c566`, 2026-10-06, "apply Home V0.3 visual direction from approved docs"), aplicado sin rama de implementación.
> - Esta nota y Linear (PRO-158 "Implementación Home V0.3", *Backlog*) lo siguen mostrando como pendiente.
> - **No se considera terminado** por la sola existencia del commit. Para resolverlo hace falta Preview / QA contra el diseño aprobado, según el flujo Figma → Claude Design → aprobación → Claude Code → producto → Preview / QA.

---

## Estado visual de storefront — referencia del 2026-10-07

- **Hero Home V0.3:** NO APROBADO.
- **Sistema A:** referencia compositiva útil.
- **Concepto G × K de B:** dirección conceptual interesante, no cierre de Hero.
- **Ideas de Outfits:** misma proporción, dimensiones visuales, alineación y línea de piso para todos los contenedores.
- **Rokkā / G/K:** assets provisionales.
- **Spacing & Layout Foundations V0.1:** aprobada y vigente como base estructural.
- **Composición GXK:** CONTROL → TENSIÓN → RUPTURA → CONTROL.

## Estado del Admin GXK — 2026-10-17

- **Loop 1:** auditoría y propuesta visual disponibles como base; no equivalen a aprobación final.
- **Estado:** pausado mientras Claude termina el trabajo pendiente de Proyecto Raíces.
- **Próximo paso:** Loop 2: refinar la propuesta existente en Claude Design y consolidar las pantallas aprobables en Figma.
- **Fuente visual definitiva:** Figma, una vez actualizados y revisados los frames. No se autoriza implementación hasta una aprobación explícita.
- **Decisiones a validar:** navegación («Home y tienda» en Contenido; «Analíticas» en Operación), interfaz en español, aclaración de `is_featured`, aviso aproximado de posibles imágenes duplicadas, temas claro/oscuro, accesibilidad y revisión del riesgo de listados extensos.
- **Fuera de alcance del Loop 2:** cambios de código/datos, migraciones, reglas comerciales, rutas/contratos y paginación.
- **Registro permanente:** [[07 — Proyectos/GXK12.2/09 — GXK12.2 — Decisiones y Changelog|Decisiones y Changelog]].
- **Criterios UX:** [[07 — Proyectos/GXK12.2/10 — GXK12.2 — UX e interacción|UX e interacción]].

## Documentación del proyecto

- [[07 — Proyectos/GXK12.2/01 — GXK12.2 — Requerimientos|Requerimientos]]
- [[07 — Proyectos/GXK12.2/02 — GXK12.2 — Arquitectura funcional|Arquitectura funcional]]
- [[07 — Proyectos/GXK12.2/03 — GXK12.2 — Arquitectura técnica|Arquitectura técnica]]
- [[07 — Proyectos/GXK12.2/04 — GXK12.2 — Brand & E-commerce Bible|Brand & E-commerce Bible]] — fuente de verdad de marca, UX y contenido
- [[07 — Proyectos/GXK12.2/05 — GXK12.2 — Roadmap de producto|Roadmap de producto]] — 6 bloques y metodología Figma → implementación → QA
- [[07 — Proyectos/GXK12.2/06 — GXK12.2 — Dirección visual — Reglas aprobadas|Dirección Visual — Reglas aprobadas]] — síntesis aprobada V0.1 + V0.2
- [[07 — Proyectos/GXK12.2/07 — GXK12.2 — V0.3 Home|V0.3 Home]] — dirección visual de Home consolidada en Figma
- [[07 — Proyectos/GXK12.2/08 — GXK12.2 — Spacing & Layout Foundations V0.1|Spacing & Layout Foundations V0.1]] — sistema espacial aprobado para implementación
- [[07 — Proyectos/GXK12.2/09 — GXK12.2 — Decisiones y Changelog|Decisiones y Changelog]] — hitos y decisiones permanentes fechadas
- [[07 — Proyectos/GXK12.2/10 — GXK12.2 — UX e interacción|UX e interacción]] — criterios de UX / interacción y auditoría post-funcional
- [[07 — Proyectos/GXK12.2/12 — GXK12.2 — Admin Lote 1 — Cierre y continuidad 2026-10-19|Admin Lote 1 — cierre y continuidad (2026-10-19)]] — estado del artefacto corregido, validación pendiente y próximo paso

---

## Gobernanza y limpieza transversal

- [[07 — Proyectos/Inventario cero — Raíces + GXK12.2 — 2026-10-19|Inventario cero — Raíces + GXK12.2]] — estado de limpieza, fuentes revisadas y candidatos pendientes. Seguimiento operativo en [Linear PRO-161](https://linear.app/proyecto-raices/issue/PRO-161/gobernanza-feature-freeze-y-limpieza-del-inventario-raices-gxk122).

## Enlaces externos

**Sitio:** Pendiente de completar.
**Repositorio:** https://github.com/sknnnnn/GxK12-2
**Proyecto en Linear:** [GxK12.2 — Construcción y lanzamiento de marca](https://linear.app/proyecto-raices/project/gxk122-construccion-y-lanzamiento-de-marca-ba4a28ef0c6a)
**Figma:** PRANA STUDIOS — laboratorio y dirección visual GXK.

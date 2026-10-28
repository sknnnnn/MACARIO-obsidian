# GXK12:2 — Índice

> Nota de entrada del proyecto dentro de MACARIO.
> Fuentes: Linear = ejecución/tareas · GitHub = código · Obsidian = documentación · Brand & E-commerce Bible = verdad de marca/UX/contenido · Dirección Visual = traducción visual aprobada · Figma Pro = exploración y validación visual.

---

## Resumen

GXK 12:2 es un espacio de exploración y transformación a través de la ropa (slogan: NO TE CONFORMES. TRANSFORMATE.). Su soporte es un e-commerce completo de indumentaria para GXK: tienda pública con catálogo, variantes (talles/colores) y stock reducido por variante, carrito, checkout como invitado, pagos con Mercado Pago, envíos (Andreani / Correo Argentino), seguimiento de pedido sin cuenta, y un panel administrativo privado (único administrador inicial) para gestionar productos, fotografías, stock, pedidos y outfits/selecciones editoriales.

---

## Estado general

**Estado:** Proyecto activo. El Preview de la rama candidata `claude/bold-cerf-sj4d8y` volvió a funcionar tras corregir el alcance de las variables de entorno de Preview en Vercel. La siguiente etapa es completar QA y verificar el aislamiento de Supabase antes de preparar una integración; todavía no está autorizado hacer merge. La Brand & E-commerce Bible y la Dirección Visual aprobada siguen siendo obligatorias.

**Última actualización:** 2026-10-28.

**Checkpoint actual (2026-10-28) — cierre de la etapa de diseño del recorrido de compra, antes de la pasada de motion.** Fuente visual: Figma PRANA STUDIOS, página `GxK12.2` (índice del recorrido `526:1505`). Se distingue lo aprobado, lo no cerrado, lo implementado y lo pendiente:
- **A. Diseño aprobado (no se reabre sin una nueva decisión):**
  - **PDP** (desktop y mobile `501:1032`, `501:1151`, `505:1072`, `505:1172`): header del sistema y títulos en ABC Favorit Bold (la escala tipográfica sigue abierta).
  - **Confirmación al agregar** (`542:2410` panel desktop de 421 px con velo suave; `538:2435` hoja inferior mobile; vistas en la PDP B): es la confirmación principal y reemplaza a «Agregado ✓» y al aviso en línea. No se cierra sola, no se apila, muestra la cantidad real de la línea y el contador del header es solo un indicador persistente. Foco, Escape, anuncio accesible y `prefers-reduced-motion` están especificados. El estado de error del agregado es comportamiento futuro: hoy agregar es local y síncrono.
  - **B3 Carrito** (`533:1567`): A página completa, desktop y mobile. Los **selectores desplegables** de talle y color son la solución vigente (los chips quedaron **descartados** y marcados así en Figma); las variantes agotadas no se pueden elegir. El contador del header se oculta con el carrito vacío o cargando y suma las cantidades cuando hay productos.
  - **Disponibilidad** (Desktop 6–7 `603:4702` y `603:4826`; Mobile A7–A8 `603:5028` y `603:5106`; Desktop 2 / Mobile A2 para la falta de stock confirmada): el carrito sigue visible mientras se verifica, «Iniciar compra» permanece bloqueado mientras se verifica y ante un error, el error usa exactamente «No pudimos verificar la disponibilidad.» con una acción «Reintentar» que vuelve a consultar, y un error de consulta no equivale a falta de stock («Ya no está disponible. Quitalo o elegí otra variante.» solo cuando la consulta lo confirma). La compra se habilita solo tras una verificación exitosa y sin productos confirmados como no disponibles. El texto «Verificando disponibilidad…» sigue siendo provisional.
- **B. Diseño existente todavía no cerrado:**
  - La interfaz del carrito diseñada en Figma **no está aplicada** al carrito real del código (la vista actual usa estilos propios simples).
  - **A5** (`537:2183`, barra fija mobile «Iniciar compra») sigue pendiente de revisión manual del usuario: no está aprobada ni lista para implementar. La barra fija del PDP (`505:1167`) también es una propuesta pendiente.
  - La **política comercial y la redacción sobre reserva de stock** siguen pendientes (Biblia §17: el carrito no reserva; gana el primer pago confirmado). La nota de stock no se muestra en la interfaz hasta que se apruebe.
  - **B5** (`568:3323`) fue transferido desde Claude Design v36 y está pendiente de revisión conjunta; discrepancias documentales abiertas: rechazo como estado del pedido o del pago, 5 estados de pago documentados frente a 9 admitidos por el código, seguimiento de la Biblia §33 frente a Arquitectura técnica §12, y el vencimiento de 20 minutos, que depende de PRO-129.
- **C. Lógica implementada (no equivale a carrito terminado ni publicado):** la lógica de disponibilidad del carrito está en el commit `88fe72e` de la rama `claude/bold-cerf-sj4d8y` (publicada en GitHub; no mergeada a `master`; sin despliegue). Un error de consulta ya no se interpreta como falta de stock, «Iniciar compra» queda bloqueado mientras se verifica o ante un error, y «Reintentar» vuelve a consultar. Se ejecutaron 192 pruebas (todas pasan), `tsc` sin errores y 29 comprobaciones de navegador contra una base simulada local. No se ejecutó `next build` ni se validó contra Supabase real.
- **D. Pendiente para una sesión posterior de implementación:** aplicar a la interfaz real del carrito el diseño aprobado de Figma; ejecutar el build y la validación integrada del carrito y el checkout; verificar en el entorno adecuado (Preview aislado) lo que solo se probó con la base simulada; aprobar los textos definitivos de verificación; definir A5 y la política de reserva de stock; revisar B5.
- **E. Próxima etapa — pasada integral de motion (no comenzó):** se hará en Figma, después de este cierre, sobre todo el recorrido de compra: PDP, selección de variantes, agregado al carrito, panel de confirmación, carrito, disponibilidad, checkout y retorno. Incluirá transiciones, overlays, hoja inferior, feedback, carga, errores y recuperación, diferencias desktop y mobile, y `prefers-reduced-motion`. No implica iniciar la implementación y no se anticipa ninguna decisión de motion todavía no revisada.

**Checkpoint anterior (2026-10-27) — recorrido de compra en diseño:**
- **Terminado hoy:** Tienda v22, B3 Carrito y B4 Checkout están en Figma (PRANA STUDIOS, página `GxK12.2`: Tienda `509:1114`, B3 `533:1567`, B4 `548:2482`, índice del recorrido `526:1505`) como capas nativas editables, con la auditoría de coherencia con la Biblia aplicada. B4 fue aceptado en Claude Design v28; la v30 solo sincroniza B3 con Figma y suma la decisión sobre efectivo. Detalle: [[07 — Proyectos/GXK12.2/09 — GXK12.2 — Decisiones y Changelog|Decisiones y Changelog]] (27/10).
- **Pendiente:** decisiones comerciales (costos de entrega, cuotas, alcance del Camino, política de precio) y dependencias técnicas (precio del resumen, resumen siempre visible, doble envío y reintento, Mercado Pago y envíos en producción). Todo el recorrido sigue sin implementar.
- **No repetir:** la auditoría integral de coherencia, las decisiones aceptadas de B3 y B4 ni su traspaso a Figma.
- **Próximo bloque (28/10):** B5 — Resultado / confirmación (`/checkout/retorno`): estados del panel de pedido (esperando pago, pago confirmado, rechazado, incidencia, cancelado, punto de encuentro con saldo, pedido no encontrado), con Claude Design primero y después Figma. Condición de inicio: abrir el índice `526:1505` (fila «7 Confirmación» y tabla de dependencias), la sección B4 (estados de resultado y conexión con B5), el código de `src/app/(storefront)/checkout/retorno` y `OrderStatusPanel` en `6be7d02`, y la Biblia §32–33. No hay bloqueos de diseño.

**Estado del recorrido de compra (28/10).** «Aceptado» = revisión visual aceptada por el usuario; no significa funcionalidad implementada. Salvo la lógica de disponibilidad del carrito (ver C arriba), nada del recorrido está implementado todavía.
| Bloque | Diseñado | Aceptado | Pendiente de definición | Pendiente de implementación |
|---|---|---|---|---|
| Home V0.4 y Ficha (D1b) | Sí (Figma) | Ficha: aprobada el 26/10 (Claude Design v19) | D7, D8, D10 (ver índice de Figma) | Sí |
| Tienda v22 y /buscar | Sí | Sí | D1 (2.ª línea de /buscar sin término), D2 (paginación) | Sí |
| B3 Carrito | Sí | A página completa, selectores desplegables, panel y hoja de confirmación y decisiones funcionales de disponibilidad: sí. A5 y nota de stock: pendientes | Texto definitivo de los avisos de disponibilidad, A5 y política y redacción de reserva de stock | Interfaz con el diseño de Figma pendiente; lógica de disponibilidad implementada en la rama (`88fe72e`) |
| B4 Checkout | Sí | Sí (Claude Design v28) | Costos de entrega, cuotas, alcance del Camino, política de precio | Sí |
| B5 Confirmación (`/checkout/retorno`) | Sí (Figma `568:3323`, desde Claude Design v36) | Pendiente de revisión conjunta | Discrepancias documentales abiertas (ver B arriba) | Sí |

**Mapa de fuentes vigentes (27/10):** Claude Design v30 (https://claude.ai/artifact/3CjPmcc7Hp7QRau2yw6rKi); Figma PRANA STUDIOS, página `GxK12.2`: índice `526:1505`, Tienda `509:1114`, B3 `533:1567`, B4 `548:2482`; código en `sknnnnn/GxK12-2` (referencia `6be7d02`): `src/app/(storefront)/checkout/CheckoutFlow.tsx`, `src/app/(storefront)/checkout/retorno/page.tsx`, `src/components/storefront/orders/OrderStatusPanel.tsx`; Linear (sin cambios): PRO-124 (Mercado Pago), PRO-125 y PRO-126 (Andreani y Correo), PRO-127 (peso y dimensiones), PRO-128 (flujo real de envíos), PRO-129 (liberación de reservas vencidas: revisar contra Biblia §17 antes de ejecutar). **Agregado el 28/10:** la lógica de disponibilidad del carrito está en `sknnnnn/GxK12-2`, rama `claude/bold-cerf-sj4d8y`, commit `88fe72e` (`src/lib/cart/availability.ts`, `src/lib/cart/verify.ts`, `src/app/(storefront)/carrito/`); Figma: PDP `496:1401`, B3 `533:1567`, B5 `568:3323`.

**Próxima etapa (28/10):** pasada integral de motion en Figma sobre todo el recorrido de compra (punto E del checkpoint del 28/10), sin iniciar la implementación. Después, una sesión de implementación (punto D). B5 ya está transferido a Figma (`568:3323`) y su revisión conjunta sigue pendiente; la auditoría de qué se administra desde el Admin (por ejemplo efectivo) se hace después de completar diseño e implementación. No se inventan políticas comerciales.

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

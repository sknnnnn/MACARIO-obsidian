# GXK12:2 — Índice

> Nota de entrada del proyecto dentro de MACARIO.
> Fuentes: Linear = ejecución/tareas · GitHub = código · Obsidian = documentación · Brand & E-commerce Bible = verdad de marca/UX/contenido · Dirección Visual = traducción visual aprobada · Figma Pro = exploración y validación visual.
> **Ejecución con agentes:** aplicar [[02 — Metodología - MACARIO — Flujo de trabajo|MACARIO — Flujo de trabajo]] §8.1–8.4. Este protocolo regula autonomía, ramas, verificaciones y cierres; la Bible, las decisiones aprobadas y la Dirección Visual siguen gobernando el producto.

---

## Resumen

GXK 12:2 es un espacio de exploración y transformación a través de la ropa (slogan: NO TE CONFORMES. TRANSFORMATE.). Su soporte es un e-commerce completo de indumentaria para GXK: tienda pública con catálogo, variantes (talles/colores) y stock reducido por variante, carrito, checkout como invitado, pagos con Mercado Pago, envíos (Andreani / Correo Argentino), seguimiento de pedido sin cuenta, y un panel administrativo privado (único administrador inicial) para gestionar productos, fotografías, stock, pedidos y outfits/selecciones editoriales.

---

## Estado general

### Plan global por etapas (marco vigente)

- **Etapa 1 — Diseño integral en Figma: CERRADA el 05/11/2026.** Referencia visual central: página de Figma `GXK12.2 — Etapa 1 — Diseños aprobados`. Cierre documental: nota 13, sección 10. (Texto original del marco:) Fue la etapa en curso. Incluye completar y revisar los diseños, aprobarlos, consolidar el sistema visual y preparar el traspaso ordenado a implementación. El Periodo 1 (04/11–09/11) es un tramo de trabajo dentro de esta etapa, no una etapa independiente.
- **Etapa 2 — Implementación integral: ABIERTA (09/11/2026).** PRO-185 In Progress. PRO-186 y PRO-187 Done; PRO-188 In Review; PRO-189 In Progress; PRO-190 Todo. Implementación del inventario Figma 764:70 completa en alcance local; cierre formal no declarado (falta aprobación de PRO-188 y validación real de PRO-189). PRO-192 es el único backlog de correcciones (Etapas 1–4).
- **Etapa 3 — QA integral y estabilización: COMPLETADA (confirmación del responsable, 09/11/2026).** Trabajo: PRO-189 Loops 1–4, diagnóstico de rendimiento, optimización técnica inicial y diagnóstico real de `/outfits`. Criterios de cierre no estaban escritos; validaciones reales pendientes quedan diferidas, no perdidas.
- **Etapa 4 — Beta presentable: NO INICIADA según las fuentes.** Sin issue ni criterios de aceptación definidos.
- **Siguiente bloque previsto:** PRO-189 · Loop 6 (Admin → Preview de Universo, Eventos, Nosotros y Legales), no iniciado ni autorizado. Detalle, contradicciones abiertas y pendientes diferidos: [[07 — Proyectos/GXK12.2/05 — GXK12.2 — Roadmap de producto|Roadmap]] §«Reconciliación de etapas — 09/11/2026».
- **Hito objetivo:** beta el 30/11/2026.

**Fuente de verdad de Home:** la Home ya está implementada y validada en producción (`master`, commit `30a1054`). Las propuestas anteriores de Home en Figma son historial, no la referencia vigente. El usuario incorporará manualmente la Home implementada a la página consolidada para reunir todo en un único lugar; esa tarea de organización visual no es un pendiente de implementación ni condiciona el cierre de Etapa 1. Ver nota 13, §10.4 y §10.9.

**Lectura del estado vigente (05/11):** la Etapa 1 está CERRADA. El cierre confirma que se cumplieron los objetivos y entregables acordados; no congela los diseños. Cualquier pantalla o decisión aprobada puede revisitarse en una etapa posterior si existe una razón fundamentada (implementación, QA, inconsistencia UX/UI o necesidad de producto), con alcance, evidencia y aprobación documentados.

**Estado:** Proyecto activo. LOOP 1 Producto / NUEVO / Early Access en QA final parcial. Las migraciones de producción y los archivos de la rama `claude/gxk-loop1-producto-early-access` están reconciliados; la Preview más reciente está READY y el build/TypeScript finalizaron correctamente. Por decisión explícita, Preview continúa conectada a Supabase producción y el QA se limita a lectura. No hay registros positivos para probar NUEVO ni Early Access. Analytics no registra eventos en Preview porque no tiene `SUPABASE_SERVICE_ROLE_KEY`; se mantiene así para no habilitar escrituras privilegiadas desde Preview. No hay merge ni deploy a producción autorizados. La Brand & E-commerce Bible y la Dirección Visual aprobada siguen siendo obligatorias.

**Última actualización:** 2026-11-09.

**Estructura del archivo de Figma (reorganizado el 04/11/2026, Periodo 1 · Etapa 1 · Subfase 1).** Archivo PRANA STUDIOS (`RqXlNyOZPYDsJFtX9Kk6dj`). Las referencias anteriores a «página `GxK12.2`» siguen siendo válidas por **ID de nodo** (no cambió ninguno); el contenido de esa página se distribuyó por área y lo que no es diseño de producto quedó en el archivo histórico, sin eliminar nada. Índice navegable con vínculos y estado de cada diseño: página `00 · Índice general`, frame `703:70` (regenerado en cada loop; versiones anteriores `684:70` y `691:2141`).

**Cierre vigente de Unificación UX/UI (05/11/2026):** Etapa 1 CERRADA. La página `GXK12.2 — Etapa 1 — Diseños aprobados` reúne 89 pantallas y variantes aprobadas, más los marcos de referencia para Home implementada. La dirección consolidada de la página 18 y el detalle de Outfit comercial, iteración 2 de la página 20, fueron aprobados por el responsable. Las páginas 16–20 y 99 conservan el historial del proceso; no se sobrescribieron los originales. La nota 13, sección 10, contiene el inventario, fuentes de verdad, verificaciones y transición. La distribución del sistema a las páginas originales (PRO-182) queda como trabajo posterior, no como condición para cerrar la Etapa 1.

**Estructura histórica del archivo:** `00 · Índice general` · `01 · Marca y sistema visual` · `02 · Home` · `03 · Navegación y componentes compartidos` · `04 · Tienda y Buscar` · `05 · Ficha de producto` · `06 · Carrito` · `07 · Checkout` · `08 · Estado del pedido y Seguimiento` · `09 · Familia, Mi Casa y Mi Camino` · `10 · Favoritos` · `11 · Nosotros y Help` · `12 · Universo, Aventuras y Eventos` · `13 · Outfits` · `14 · Admin` · `15 · Estados globales, errores y cargas` · `99 · Archivo — exploraciones, versiones previas y referencias (ex GxK12.2)` (id `37:26`). Los estados de aprobación y las notas de trabajo del Periodo 1 que aparecen en los checkpoints posteriores son registros históricos; la aprobación y consolidación final del 05/11 prevalecen.

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
- **E. Pasada integral de motion — iniciada y PARCIAL (cierre de sesión 28/10, Figma bloqueado por el límite de llamadas del MCP del plan Starter):**
  - **Hecho en Figma (verificado leyendo la configuración, no recorrido visualmente):** 12 reacciones de prototipo nuevas (19 → 31) y puntos de inicio de flujo de 2 a 7. Recorridos: Desktop carrito `536:2049` → `603:4702` → `536:1742`; Desktop reintento `603:4826` → `603:4702`; Desktop carrito → checkout `536:1742` → D1 `550:2482`; Mobile carrito `537:2152` → `603:5028` → `537:1966`; Mobile reintento `603:5106` → `603:5028`; Checkout desktop D1 `550:2561` → D3 `550:2662` → D5 `551:2792` → D7 procesando `551:2995`; Checkout mobile M2 `552:3167` → M3 `552:3223` → M4 procesando `552:3298`. Transición DISSOLVE solo de opacidad, `cubic-bezier(0.2, 0, 0, 1)`, 160 ms entre pasos y 120 ms hacia «Procesando»; los tiempos de 0,6 s y 1,2 s son ilustrativos. Tres flujos quedaron con nombre por defecto (Flow 3, 4, 5) porque el renombrado falló.
  - **NO completado:** bloque «Sistema de motion» del índice `526:1516`; anotaciones de motion (`586:4577`, `586:4578`, `586:4579`, fila «Movimiento» de `542:2479`, anotaciones del carrito `603:5188` a `603:5192`, anotaciones de checkout, nota de B5, texto del índice `532:1811`); renombrado de flujos; capturas y verificación visual; validación de interrupciones, colapso de altura y `prefers-reduced-motion` (Figma no los representa fielmente). **Las anotaciones de Figma NO están actualizadas con el motion: la sincronización visual queda pendiente de recuperar la cuota.**
  - **Especificación preservada:** el borrador completo (principios, tokens, T1–T22, reduced-motion, límites y pendientes) está en [[07 — Proyectos/GXK12.2/10 — GXK12.2 — UX e interacción|10 — UX e interacción]] §6, como **propuesta sin aprobar**. Ningún valor de duración o easing está aprobado.
  - **Decisiones pendientes que afectan el motion:** demora (~300 ms) del aviso «Verificando…»; estado de «Reintentar» durante una nueva consulta; indicador de actividad de «Procesando…»; transiciones hacia y dentro de B5 (revisión conjunta); cierre por clic en el velo (no aprobado). No se reabren: panel como confirmación principal, sin apilar paneles, foco vuelve al CTA, sin cierre por swipe, contador persistente, sin «Agregado ✓».
  - **Orden del próximo loop (cuando vuelva la cuota; no iniciado, sin cambios de código):** (1) recuperar y revisar la especificación preservada; (2) completar anotaciones y el bloque «Sistema de motion»; (3) renombrar los flujos; (4) revisar visualmente el prototipo en desktop y mobile y capturar evidencia; (5) revisar las propuestas y obtener aprobación antes de dar el motion por cerrado.

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
- [[07 — Proyectos/GXK12.2/13 — GXK12.2 — Unificación UX-UI — Propuesta|Unificación UX/UI y cierre de Etapa 1]] — historial y fuente de continuidad; §10 registra el cierre de Etapa 1 (05/11/2026) y §11.15 el estado vigente y la reanudación de Etapa 2 (06/11/2026).

---

## Gobernanza y limpieza transversal

- [[07 — Proyectos/Inventario cero — Raíces + GXK12.2 — 2026-10-19|Inventario cero — Raíces + GXK12.2]] — estado de limpieza, fuentes revisadas y candidatos pendientes. Seguimiento operativo en [Linear PRO-161](https://linear.app/proyecto-raices/issue/PRO-161/gobernanza-feature-freeze-y-limpieza-del-inventario-raices-gxk122).

## Enlaces externos

**Sitio:** Pendiente de completar.
**Repositorio:** https://github.com/sknnnnn/GxK12-2
**Proyecto en Linear:** [GxK12.2 — Construcción y lanzamiento de marca](https://linear.app/proyecto-raices/project/gxk122-construccion-y-lanzamiento-de-marca-ba4a28ef0c6a)
**Figma:** PRANA STUDIOS — laboratorio y dirección visual GXK.


---
## Registro operativo histórico — 2026-11-03 (no representa el estado vigente)

- **LOOP 1:** migraciones de `products.is_new` y teaser Early Access aplicadas y verificadas en Supabase producción. Snapshot descriptivo de esquema/RLS guardado en [GXK12-2 — snapshot producción 2026-11-03](https://github.com/sknnnnn/GxK12-2/blob/master/supabase/snapshots/2026-11-03-production-schema.md). Es una referencia de consulta, no un backup restaurable ni contiene filas. Detalle técnico: [[07 — Proyectos/GXK12.2/03 — GXK12.2 — Arquitectura técnica|Arquitectura técnica]] §24.
- **Preview:** se acepta continuar conectada a Supabase producción. No se creó un segundo proyecto ni se modificaron variables. QA de lectura permitido; sin compras, pagos, envíos, emails ni escrituras de prueba.
- **Datos para QA:** reconsulta SQL read-only: 6 productos totales, 4 publicados, 0 NUEVO, 0 Early Access activo y 0 vencido. Los cuatro publicados son registros `test-*`; no existe un caso positivo real para probar NUEVO/Early Access. Los escenarios positivos quedan pendientes hasta disponer de datos de prueba autorizados.
- **Home:** estados sin contenido de Outfits y Universo **rediseñados** (Claude Design v51, artboard 31, para revisión). La versión anterior y su implementación en `claude/gxk-loop2-outfits` (`96375df`) quedaron **descartadas** por dirección visual no aprobada; no se implementa nada hasta aprobar el nuevo diseño. Ver [[07 — Proyectos/GXK12.2/10 — GXK12.2 — UX e interacción|UX e interacción]].
- **LOOP 2 (Ideas de outfits):** funcionalidad hecha en la rama `claude/gxk-loop2-outfits` (filtro por los cinco estilos, OUTFITS de header y footer hacia la página, estilos de Home como enlaces), sin PR ni merge. **Dirección visual no aprobada** (03/11): `/outfits` y los estados vacíos se rediseñaron (artboards 30 y 31, v51) como continuación de la Home. Pendiente: revisión del usuario, luego adaptar el código al diseño aprobado. Detalle: [[07 — Proyectos/GXK12.2/09 — GXK12.2 — Decisiones y Changelog|Decisiones y Changelog]] (03/11, LOOP 2).
- **Seguimiento:** [Linear PRO-174 — completar QA de NUEVO y Early Access en Preview](https://linear.app/proyecto-raices/issue/PRO-174/gxk122-loop-1-completar-qa-de-nuevo-y-early-access-en-preview).
- **Reconciliación final de LOOP 1 (2026-11-03):** `supabase_migrations.schema_migrations` y `list_migrations` coinciden con los archivos `20261103152134_products_is_new.sql` y `20261103152140_early_access_teaser.sql` de la rama. La última Preview (`dpl_FhGp4ASB8TkHHGpa8kYNZVqDBkdr`, commit `8e4f251`) está READY; build y TypeScript correctos. La falta de `SUPABASE_SERVICE_ROLE_KEY` en Preview explica el descarte no bloqueante de analytics; no se agrega esa credencial. El QA positivo de NUEVO/Early Access sigue bloqueado por ausencia de datos elegibles y la comprobación HTTP de la última Preview queda pendiente por la protección SSO y la falta de una sesión de navegador conectada. PRO-174 permanece In Progress. Las pruebas unitarias no se ejecutaron: el deployment de Vercel solo corrió `next build` (TypeScript y build), sin `npm test`. Los scripts de QA de navegador requieren una base local/de pruebas y `requireLocalDatabase()` rechaza explícitamente URLs `supabase.co`; no deben ejecutarse contra producción.

**Etapa 1 · CERRADA (05/11/2026).** Referencia única: página de Figma `GXK12.2 — Etapa 1 — Diseños aprobados` (89 pantallas y variantes + Home implementada). Las páginas 16–20 quedan como historial del proceso. **Antecedente — Dirección visual consolidada (05/11/2026).** Página de Figma `18 · Etapa 1 — Presentación integral consolidada (propuesta)` (84 pantallas D/M, comparación con Figma AI, superficies medidas, QA y cierre). Fue la presentación de trabajo que recibió aprobación del responsable el 05/11; la referencia visual operativa final es la página `GXK12.2 — Etapa 1 — Diseños aprobados`. Nota 13, secciones 9–10.




## Etapa 2 — Estado vigente al 07/11/2026

- **Etapa 1:** cerrada el 05/11/2026.
- **Etapa 2:** en curso; no se declara cerrada. PRO-188 está In Review; PRO-189 sigue Todo y requiere QA integrado en Preview; PRO-190 sigue Todo y depende de PRO-189. PRO-185 permanece In Progress.
- **Implementación:** rama `claude/gxk-etapa1-integracion`, commit `371487c`; inventario Figma 764:70 recorrido según `docs/etapa1-loop-progreso.md`. Resultado reportado: 418/418 tests, lint/typecheck/build OK y QA local del demo.
- **Preview:** deployment Vercel READY para el commit exacto `371487c`: https://gx-k12-2-9umrwje5f-proyecto-travesia.vercel.app. Falta QA visual/funcional en navegador, capturas y recorridos.
- **GitHub:** 19 commits desde checkpoint `ed26be3`; frente a `master` `30a1054`, rama 75 commits adelante y 1 detrás. El único commit que falta es el snapshot documental de esquema. No hay PR abierto; no sincronizar ni integrar sin autorización.
- **Backlog:** PRO-192 es el único backlog de correcciones para Etapas 1–4. Los pendientes no bloqueantes se consolidan allí; las excepciones de migraciones, legales, galería y SMTP quedan explícitas.
- **Próximo gate:** PRO-189, QA de Preview con evidencia desktop/mobile y estados críticos. Después PRO-190. Etapa 3 solo empieza tras el cierre de implementación y QA.
- **Guardas:** sin PR, merge, deploy ni cambios en producción.

Detalle: [[07 — Proyectos/GXK12.2/13 — GXK12.2 — Unificación UX-UI — Propuesta|nota 13]] §11.16 y [[07 — Proyectos/GXK12.2/05 — GXK12.2 — Roadmap de producto|Roadmap]] §Auditoría de implementación 07/11/2026.
## Etapa 2 — Implementación integral y estado al 06/11/2026 (histórico; superado por el corte 07/11/2026) (histórico; superado por el corte 07/11/2026)

- **Etapa 1:** Diseño integral en Figma, cerrada el 05/11/2026. La referencia vigente son las 89 pantallas/variantes aprobadas; Home conserva su implementación validada en producción.
- **Etapa 2:** iniciada el 06/11/2026 y temporalmente pausada por límite de uso de Claude. Sigue abierta; no es cierre de ciclo ni habilita Etapa 3.
- **Primer ciclo:** PRO-186 preflight cerrado → PRO-187 fundamentos visuales aprobados (sin integrar) → PRO-188 primer lote abierto y pausado → PRO-189 QA Preview → PRO-190 cierre/siguiente ciclo.
- **PRO-188:** Pago B4 aprobado (`96c552c`); Confirmación B5 aprobada y completada (`4d7a64c`); Outfit B6 implementado (`90e7a39`, corrección `8d93f97`) pero pendiente de aprobación visual, copy, datos reales y QA staging; estados vacíos implementados funcionalmente (`2e7a5f1`) pero pendientes de diseño visual general.
- **Checkpoint actual:** código `sknnnnn/GxK12-2`, rama `claude/gxk-etapa1-integracion`, commit `ed26be3`; registro operativo `docs/etapa1-loop-progreso.md`, commit inicial `663e6d1`; la aclaración de jerarquía y el título interno del registro se corrigieron en `c752521`. El nombre histórico de archivo/rama no cambia la etapa global.
- **Verificación:** 391/391 tests; lint y typecheck limpios; build pendiente. Navegación, Tienda, Buscar y Ficha verificadas en 1440/390 px. Familia Ingresar/Registro/Recuperar implementada, pendiente de QA visual en navegador.
- **Reanudación exacta:** QA visual de Familia contra Figma 764:1005, 1023, 1041, 1055, 1069 y 1078 en desktop/mobile; revisar también Nueva contraseña, Mi Casa → Mis datos y «Sumarme». Después continuar con Figma 764:1108–1503 y el inventario aprobado restante, sin repetir auditorías cerradas.
- **Guardas:** Home excluida; PRO-192 fuera del alcance de esta reanudación; Legales no se implementa sin textos aprobados; `418c85a` permanece fuera hasta disponer de migraciones. No integrar ramas, PR, merge a `master`, deploy ni cambios de producción.
- **Método:** loops pequeños de 4–5 tareas; cada bloque se contrasta con Figma, se implementa solo en sus brechas, se vuelve a verificar y se registra. Registrar pendientes transversales en PRO-192 solo cuando correspondan, sin duplicar ni ampliar alcance.

Detalle: nota 13 §11.15 y [registro operativo de checkpoint](https://github.com/sknnnnn/GxK12-2/blob/claude/gxk-etapa1-integracion/docs/etapa1-loop-progreso.md).

### Resolución de PRO-186 — 2026-11-05

- Preflight y matriz de 89 pantallas revisados y aprobados por el responsable; PRO-186 cerrada.
- Base de trabajo aprobada: `claude/gxk-loop2-completar`; recuperación selectiva desde `experiment` según nota 13 §11.3, commit por commit.
- Migraciones de stock/pagos postergadas en producción. Staging Supabase independiente + pagos de prueba es el entorno objetivo; Preview actual sigue siendo solo lectura contra producción.
- ABC Favorit no está disponible con licencia verificada: Archivo queda como sustituto provisional.
- Primer lote aprobado: fundamentos visuales → recorrido de compra → Outfit comercial. PRO-187 implementada y aprobada (06/11/2026), sin integrar. PRO-188 abierta: Pago y Confirmación aprobados; Outfit y estados vacíos implementados pero con aprobación visual pendiente según el alcance descrito arriba.
- Sin creación de infraestructura, migraciones, cambios de código, integración de ramas ni deploys en esta preparación. Detalle y límites: nota 13 §11.11; Linear PRO-186/187.

**Corte 07/11/2026 — PRO-189:** se completó Loop 1 de diagnóstico en modo solo lectura. PRO-189 sigue In Progress; Loop 2 propuesto, todavía no autorizado/iniciado. Preview compartido: https://gx-k12-2-9umrwje5f-proyecto-travesia.vercel.app/ . Próxima acción: comprobar acceso desde navegador del responsable y después acordar alcance del Loop 2. Diagnóstico y hallazgos detallados en nota 13, nuevo registro de cierre del 07/11/2026. Etapa 2 sigue en curso; PRO-188 In Review; PRO-190 Todo; PRO-192 backlog único. No merge/PR/deploy ni cambios de producción.

**Corte 09/11/2026 — PRO-189 (Loops 2–4):** PRO-189 sigue ABIERTA (In Progress). Loops 1–4 completados en su alcance técnico local (Loop 4: checkpoint `1e04880`, código `5c1f5bd`, rama `claude/pro-189-loop4-loading-estabilidad`); falta el QA real de Preview y la validación de rendimiento real (no validado en producción). Feedback de carga en navegación trasladado a PRO-192 §B10.1. Detalle: nota 13 «Cierre documental del Loop 4».

**Corte 09/11/2026 (reconciliación de etapas):** Etapa 1 cerrada · Etapa 2 abierta · Etapa 3 completada (confirmación del responsable) · Etapa 4 no iniciada. PRO-189 sigue ABIERTA: Loops 1–4 completados; diagnóstico de rendimiento y de `/outfits` realizado; optimización avanzada DIFERIDA (pool frío, caché, rondas, región, doble `getUser`). Rendimiento real no validado. Registro: Roadmap «Reconciliación de etapas», nota 13 «PRO-189 · Diagnóstico de rendimiento…» y `docs/etapa1-loop-progreso.md` (`claude/bold-cerf-sj4d8y`, `2f78cfd`).

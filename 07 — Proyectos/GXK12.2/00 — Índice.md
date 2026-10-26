# GXK12:2 — Índice

> Nota de entrada del proyecto dentro de MACARIO.
> Fuentes: Linear = ejecución/tareas · GitHub = código · Obsidian = documentación · Brand & E-commerce Bible = verdad de marca/UX/contenido · Dirección Visual = traducción visual aprobada · Figma Pro = exploración y validación visual.

---

## Resumen

GXK 12:2 es un espacio de exploración y transformación a través de la ropa (slogan: NO TE CONFORMES. TRANSFORMATE.). Su soporte es un e-commerce completo de indumentaria para GXK: tienda pública con catálogo, variantes (talles/colores) y stock reducido por variante, carrito, checkout como invitado, pagos con Mercado Pago, envíos (Andreani / Correo Argentino), seguimiento de pedido sin cuenta, y un panel administrativo privado (único administrador inicial) para gestionar productos, fotografías, stock, pedidos y outfits/selecciones editoriales.

---

## Estado general

**Estado:** Proyecto activo con una pausa operativa temporal por límite de uso de Claude. La base técnica de e-commerce sigue en el repo de aplicación; la dirección visual de páginas públicas avanzó por separado. La Brand & E-commerce Bible y la Dirección Visual aprobada siguen siendo obligatorias. El estado vigente y los próximos pasos de storefront se registran en el checkpoint D1b de 2026-10-26, en [[07 — Proyectos/GXK12.2/09 — GXK12.2 — Decisiones y Changelog|Decisiones y Changelog]].

**Última actualización:** 2026-10-26.

**Checkpoint actual (2026-10-26):** D1b de storefront aprobado por el usuario en Claude Design versión 19: https://claude.ai/artifact/3CjPmcc7Hp7QRau2yw6rKi. La ficha de producto desktop/móvil ya tiene galería con miniaturas seleccionables y guía de talles junto al selector. **Pausa temporal por límite de uso de Claude; no iniciar implementación todavía.** Al retomar: decidir si se registra el diseño en Figma, diagnosticar el preview fallido `a0d500e` o elegir una base verificada, y planificar un loop de implementación de 4–5 tareas. Referencia visual confirmada: preview `6be7d02` en `fix/home-v04-visual`. Detalle y bloqueos: [[07 — Proyectos/GXK12.2/09 — GXK12.2 — Decisiones y Changelog|Decisiones y Changelog]].

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

# GXK12:2 — Índice

> Nota de entrada del proyecto dentro de MACARIO.
> Fuentes: Linear = ejecución/tareas · GitHub = código · Obsidian = documentación · Brand & E-commerce Bible = verdad de marca/UX/contenido · Dirección Visual = traducción visual aprobada · Figma Pro = exploración y validación visual.

---

## Resumen

GXK 12:2 es un espacio de exploración y transformación a través de la ropa (slogan: NO TE CONFORMES. TRANSFORMATE.). Su soporte es un e-commerce completo de indumentaria para GXK: tienda pública con catálogo, variantes (talles/colores) y stock reducido por variante, carrito, checkout como invitado, pagos con Mercado Pago, envíos (Andreani / Correo Argentino), seguimiento de pedido sin cuenta, y un panel administrativo privado (único administrador inicial) para gestionar productos, fotografías, stock, pedidos y outfits/selecciones editoriales.

---

## Estado general

**Estado:** Proyecto activo. Existe una base técnica de e-commerce funcional (Storefront, Admin Web, Supabase/schema/RLS, catálogo, variantes e inventario, stock y operaciones atómicas, carrito, guest checkout, base de Mercado Pago, arquitectura de shipping con Andreani / Correo Argentino preparados a nivel técnico, sistema de pedidos y estados, outfits a nivel de modelo de datos). Ahora comienza la evolución hacia el producto GXK completo, guiada por la [[07 — Proyectos/GXK12.2/04 — GXK12.2 — Brand & E-commerce Bible|Brand & E-commerce Bible]], la [[07 — Proyectos/GXK12.2/06 — GXK12.2 — Dirección visual — Reglas aprobadas|Dirección Visual — Reglas aprobadas]] y el [[07 — Proyectos/GXK12.2/05 — GXK12.2 — Roadmap de producto|Roadmap de producto]] (6 bloques). **Bloque actual: 4 — Dirección de páginas**, con V0.1 + V0.2 de dirección visual cerradas, Spacing & Layout Foundations V0.1 aprobada y **Home V0.3 Híbrido en checkpoint visual para implementación**.

**Última actualización:** 2026-10-06.

**Checkpoint actual:** Home V0.3 Híbrido cerrado como dirección visual; artefacto Claude Design: https://claude.ai/artifact/Whoah9UyMMkk9CviL9GyEb. Próximo paso: revisión de gaps → aprobación → rama de implementación → Claude Code → QA.

> ⚠️ **Contradicción de estado (2026-10-07) — Home V0.3: implementación presente en código; aprobación / QA visual pendiente.**
> - El código ya está en `master` del repositorio (commit `950c566`, 2026-10-06, "apply Home V0.3 visual direction from approved docs"), aplicado sin rama de implementación.
> - Esta nota y Linear (PRO-158 "Implementación Home V0.3", *Backlog*) lo siguen mostrando como pendiente.
> - **No se considera terminado** por la sola existencia del commit. Para resolverlo hace falta Preview / QA contra el diseño aprobado, según el flujo Figma → Claude Design → aprobación → Claude Code → producto → Preview / QA.

---

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

---

## Enlaces externos

**Sitio:** Pendiente de completar.
**Repositorio:** https://github.com/sknnnnn/GxK12-2
**Proyecto en Linear:** [GxK12.2 — Construcción y lanzamiento de marca](https://linear.app/proyecto-raices/project/gxk122-construccion-y-lanzamiento-de-marca-ba4a28ef0c6a)
**Figma:** PRANA STUDIOS — laboratorio y dirección visual GXK.

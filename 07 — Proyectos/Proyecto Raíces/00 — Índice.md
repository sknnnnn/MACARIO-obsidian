## Estado operativo actualizado — 2026-11-11

**Etapa 0 cerrada documentalmente.** Registro: [PRO-194](https://linear.app/proyecto-raices/issue/PRO-194/etapa-0-preparacion-y-continuidad-cierre-2026-11-11). Próxima etapa: [Etapa 1 — Discovery y auditoría integral (PRO-191)](https://linear.app/proyecto-raices/issue/PRO-191/etapa-1-raices-discovery-y-auditoria-integral).

**Fuentes canónicas:** Obsidian = contexto y decisiones; Linear = etapas, tareas, estados y dependencias; GitHub = código, ramas y PRs; Figma = diseño aprobado; Claude Design = exploración; Claude Code = implementación; Cloudflare Preview/Dev = QA previo.

**Estado de repositorios y ramas:**
- Aplicación `sknnnnn/proyecto-raices`: rama por defecto `main`. La rama `docs/raices-nueva-arquitectura-20261105` permanece sin integrar respecto de `main`; revisar la comparación actual antes de cualquier PR o merge.
- Obsidian `sknnnnn/MACARIO-obsidian`: la rama `docs/raices-nueva-arquitectura-20261105` está divergida respecto de `master`. Se conserva sin merge ni actualización forzada hasta reconciliar el historial.
- Aplicación: `feature/admin` tiene 26 commits adicionales; `claude/proyecto-raices-visual-language-q04g3y` tiene 115; `chore/technical-hardening` y `dev` están divergentes. PR #23 fue mergeado, pero no integró todo el trabajo posterior de la rama visual. No borrar ni fusionar ramas por antigüedad.

**Estado Linear:** PRO-194 = Etapa 0 Done; PRO-191 = Etapa 1 en Backlog y preparada; PRO-172 y PRO-160 siguen In Progress; PRO-161 continúa como inventario transversal.

**Dependencias y límites:** PRO-172 conserva pendiente el backup real de Supabase y la restauración aislada. La simulación local no los reemplaza. Las migraciones v6–v11 figuran como ejecutadas el 2026-10-22; no repetir SQL. PRO-172 no bloquea la auditoría de solo lectura de Etapa 1, pero sí operaciones sensibles sobre datos reales. No se modificaron código, datos, Supabase, producción, permisos, ramas, deploys ni merges.

**Verificaciones no disponibles en este checkpoint:** worktrees y ramas locales de la PC; estado live de servicios y entornos productivos. La documentación registra el sitio público y el flujo `GitHub main → Cloudflare Dev`, pero no se afirma una comprobación live de Admin o integraciones.

- [Cierre Etapa 0 — Linear PRO-194](https://linear.app/proyecto-raices/issue/PRO-194/etapa-0-preparacion-y-continuidad-cierre-2026-11-11).
- [Etapa 1 — Linear PRO-191](https://linear.app/proyecto-raices/issue/PRO-191/etapa-1-raices-discovery-y-auditoria-integral).
- [Plan maestro — Linear](https://linear.app/proyecto-raices/document/proyecto-raices-plan-maestro-de-rediseno-integral-ac57209593ba).
- [Estado y continuidad técnica — corte 2026-11-03](https://github.com/sknnnnn/proyecto-raices/blob/docs/raices-metodologia-pausa-20261103/docs/operacion/estado-y-continuidad-2026-11-03.md).

---

# Proyecto Raíces — Índice

> Nota de entrada del proyecto dentro de MACARIO.
> Resume el estado general y enlaza el resto de la documentación permanente.
>
> Las tareas operativas viven en Linear.
> El código vive en GitHub.
> Esta nota es el punto de partida para orientarse en el proyecto.
>
> **Ejecución con agentes:** aplicar [[02 — Metodología - MACARIO — Flujo de trabajo|MACARIO — Flujo de trabajo]] §8.1–8.4. La autonomía técnica no resuelve decisiones de negocio pendientes ni habilita cambios destructivos, migraciones o acciones sobre producción sin autorización específica.

---

## Regla transversal de la plantilla

> **Una fuente por tipo de información.**
> Si una información ya tiene un sistema propietario (Linear, GitHub, README, etc.), esta documentación debe enlazarla, no copiarla.

---

## Resumen

Proyecto Raíces es un proyecto de turismo de aventura y experiencias (tours, travesías y paquetes) que combina naturaleza, aventura, cultura, encuentros, exploración y experiencias compartidas, alejándose del modelo tradicional de agencia.

---

## Estado general

**Estado:** plan maestro de rediseño integral adoptado el 2026-11-05. Próxima secuencia: Etapa 0 — Preparación y continuidad → Etapa 1 — Discovery y auditoría integral (PRO-191). No se inicia implementación ni se autorizan operaciones sensibles por la aprobación del plan. El sitio público existe; el Admin y sus integraciones conservan validaciones pendientes. El seguimiento operativo vive en Linear.

**Última actualización:** 2026-11-05. Plan maestro de ocho etapas adoptado y registrado en Linear. Las migraciones v6–v11 figuran como ejecutadas en Linear el 2026-10-22; no repetir SQL. El respaldo real de producción y la restauración aislada siguen pendientes. La orientación estratégica prioriza paquetes y visibilidad de guías; la remuneración de guías no está definida. Ver el plan maestro y la continuidad vigente.

### Estado histórico — 2026-10-16 (superado por el checkpoint del 2026-10-19)

- Admin E1: la issue **PRO-160** continúa **In Progress**. La migración v5 figura aplicada y verificada en producción según el registro operativo.
- **Refinamiento visual del Admin:** tramo cerrado en la rama `claude/proyecto-raices-visual-language-q04g3y`, con 176/176 pruebas Playwright y `node --check` sin errores. D21 se resolvió respetando `CLAUDE.md §9`; responsive revisado en 390, 768, 1024 y 1280 px. Esto no equivale a validar escrituras reales, Supabase Auth/PostgREST o lectores de pantalla.
- **Registro técnico de cierre:** [nota de cierre en el repositorio de aplicación](https://github.com/sknnnnn/proyecto-raices/blob/claude/proyecto-raices-visual-language-q04g3y/docs/admin/cierre-sesion-2026-10-16.md). Commit documental `87ef3ff`.
- **Sin integración/publicación:** no hubo merge a `feature/admin`, `main` o `master`, despliegue a producción ni migraciones remotas.
- **Próximo orden de trabajo:** (1) auditar D15: seis claves de `site_config` editables desde Admin pero no usadas por el frontend; (2) clasificar el inventario §11.7; (3) diagnosticar D19 usando el lienzo existente de Claude y la Home real; presentar la propuesta antes de implementar.
- **D19 — bloques de Home:** Portada (la foto ya se puede editar; falta verificar el resto), Momentos para vivir distinto (carrusel de 10 experiencias), Principales destinos, Tours, Travesías, Paquetes, Quiénes somos, Comentarios y comunidad, Cierre. Tours/Travesías/Paquetes son cards editoriales que llevan a sus respectivas secciones, no listados de experiencias. No existe actualmente “experiencia destacada” en Home y no se incorpora como requisito.
- **Principio de administrabilidad:** contenido editorial que deba mantener una persona sin código debería gestionarse desde Admin cuando corresponda; reutilizar fuentes de verdad existentes y evitar duplicación. Estilos, reglas de negocio, permisos y configuración técnica no se convierten automáticamente en contenido editable.
- **Límites:** no modificar código, datos, permisos, Supabase remoto ni producción; no publicar ni hacer merge sin autorización explícita.

Seguimiento operativo: [PRO-160](https://linear.app/proyecto-raices/issue/PRO-160/raices-admin-de-contenidos-e1-v5-aplicada-y-verificada-falta-publicar).
---

## Plan maestro de rediseño integral — aprobado 2026-11-05

**Estado:** plan adoptado. La ejecución se organiza en ocho etapas secuenciales. Amplía el alcance para incluir un rediseño visual integral. No implica que las etapas estén ejecutadas ni autoriza cambios en producción.

| Etapa | Nombre | Resultado esperado |
|---|---|---|
| 0 | Preparación y continuidad | Estado real reconciliado, fuentes canónicas, dependencias, entorno seguro y reglas de trabajo definidos. |
| 1 | Discovery y auditoría integral | Inventario funcional, técnico, editorial y visual de web, Admin, datos, contenido, responsive e integraciones, con evidencia y brechas priorizadas. |
| 2 | Arquitectura del producto | Navegación, sitemap, entidades, relaciones, recorridos y reglas funcionales aprobados. |
| 3 | Dirección visual | Concepto visual integral aprobado: identidad digital, referencias, fotografía, tipografía, color, composición, componentes, motion, responsive y accesibilidad. |
| 4 | UX/UI y diseño en Figma | Flujos, wireframes, pantallas finales, componentes y estados diseñados y aprobados en Figma como fuente visual definitiva. |
| 5 | Arquitectura técnica y preparación | Modelo de datos, Admin, integraciones, estrategia de migración reversible, seguridad, entornos y pruebas preparados. |
| 6 | Implementación | Desarrollo por bloques aprobados, en ramas aisladas, con QA continuo y sin cambios directos no autorizados en producción. |
| 7 | QA, migración y lanzamiento | Validación funcional/visual, responsive, accesibilidad, contenido, SEO, rendimiento, integridad de datos, migración y lanzamiento controlado. |

### Orden y dependencias

- Etapa 0 ordena el contexto y las condiciones de trabajo; no bloquea el análisis de solo lectura.
- Etapa 1 audita en paralelo las dimensiones funcional, técnica, editorial y visual. No se diseña una Home aislada antes de comprender el sistema completo.
- Etapa 2 define la arquitectura de producto a partir de la auditoría. Las decisiones funcionales aprobadas el 2026-11-05 son restricciones de partida.
- Etapa 3 define la dirección visual; Etapa 4 la traduce a flujos y pantallas completas en Figma.
- Etapa 5 prepara la base técnica y los cambios de datos antes de implementar. PRO-172 (backup real y restauración aislada) es prerequisito para operaciones sensibles sobre datos reales.
- Etapa 6 implementa en bloques coherentes. Etapa 7 valida el conjunto y controla migración/publicación.

### Método de ejecución y cierre

- Obsidian + GitHub: contexto, documentación canónica, decisiones y continuidad.
- Linear: etapas, subfases, tareas, dependencias, criterios de aceptación y estados.
- GitHub: código, ramas, commits y PRs.
- Claude Design: exploración visual y prototipos; Figma conserva la fuente visual aprobada y editable.
- Claude Code: implementación.
- Preview/staging: validación antes de producción.
- Trabajar en loops de aproximadamente 4–5 tareas relacionadas. Cada loop cierra con evidencia, pruebas, pendientes explícitos y actualización documental.
- Diferenciar propuesta, decisión aprobada, diseño, implementación, preview y producción.
- No duplicar auditorías ya cerradas: recuperar evidencia vigente y auditar solo brechas o aspectos afectados por el nuevo alcance.
- No avanzar de etapa sin criterios de cierre cumplidos o bloqueos documentados y aceptados.

### Alcance visual transversal

El rediseño visual no se limita a una nueva Home. La auditoría cubre web pública y Admin; la dirección visual abarca lenguaje de marca, fotografía, tipografía, color, composición, navegación, componentes, responsive, accesibilidad y estados. Figma contiene las pantallas y estados aprobados antes de su implementación.

### Límites de seguridad

La aprobación del plan no autoriza migraciones, borrados, escrituras destructivas, cambios de permisos, operaciones sobre datos reales, merge a ramas principales, deploy ni publicación. Cada operación sensible requiere preflight, respaldo/restauración cuando corresponda, estrategia reversible, pruebas y autorización explícita.

---

## Plan y seguimiento operativo

- [Linear — Plan maestro de rediseño integral](https://linear.app/proyecto-raices/document/proyecto-raices-plan-maestro-de-rediseno-integral-ac57209593ba)
- [Linear — Etapa 1: Discovery y auditoría integral (PRO-191)](https://linear.app/proyecto-raices/issue/PRO-191/etapa-1-raices-discovery-y-auditoria-integral)
- Proyecto Linear: [Rediseño y lanzamiento Web](https://linear.app/proyecto-raices/project/rediseno-y-lanzamiento-web-2a37c58672be)

## Documentación del proyecto

- [[07 — Proyectos/Proyecto Raíces/01 — Contexto y Brief]]
- [[07 — Proyectos/Proyecto Raíces/02 — Objetivos y Alcance]]
- [[07 — Proyectos/Proyecto Raíces/03 — Identidad y Referencias]]
- [[07 — Proyectos/Proyecto Raíces/04 — Arquitectura]]
- [[07 — Proyectos/Proyecto Raíces/05 — UX-UI]]
- [[07 — Proyectos/Proyecto Raíces/06 — Contenido]]
- [[07 — Proyectos/Proyecto Raíces/07 — Datos e Integraciones]]
- [[07 — Proyectos/Proyecto Raíces/08 — Desarrollo]]
- [[07 — Proyectos/Proyecto Raíces/09 — QA]]
- [[07 — Proyectos/Proyecto Raíces/10 — Deploy y Monitoring]]
- [[07 — Proyectos/Proyecto Raíces/11 — Decisiones y Changelog]]
- [[07 — Proyectos/Proyecto Raíces/12 — Enlaces (Linear y GitHub)]]

---

## Enlaces externos

**Sitio:** https://proyectoraices.com.ar
**Repositorio:** https://github.com/sknnnnn/proyecto-raices.git
**Proyecto en Linear:** [Rediseño y lanzamiento Web](https://linear.app/proyecto-raices/project/rediseno-y-lanzamiento-web-2a37c58672be)
**Figma:** [tablero de referencias y dirección visual](https://www.figma.com/design/RqXlNyOZPYDsJFtX9Kk6dj/PRANA-STUDIOS?node-id=54-26) (archivo `PRANA STUDIOS`)

## Estado operativo actualizado — 2026-11-03

**Estado: PAUSADO.** Por decisión del usuario, no se retoman funcionalidades, arreglos, rediseño ni cambios técnicos. La intervención actual se limita a ordenar y reconciliar documentación.

- [Estado y continuidad técnica en el repositorio de aplicación](https://github.com/sknnnnn/proyecto-raices/blob/docs/raices-metodologia-pausa-20261103/docs/operacion/estado-y-continuidad-2026-11-03.md).
- [[07 — Proyectos/Proyecto Raíces/Continuidad — Respaldo de producción y migraciones]] — respaldo real/restauración pendiente y orden de retoma.
- [[07 — Proyectos/Proyecto Raíces/11 — Decisiones y Changelog]] — decisión estratégica y pausa del 2026-11-03.
- [[02 — Metodología - MACARIO — Flujo de trabajo]] — metodología general vigente.
- Linear: [Rediseño y lanzamiento Web](https://linear.app/proyecto-raices/project/rediseno-y-lanzamiento-web-2a37c58672be).

**Orientación estratégica:** paquetes como oferta comercial prioritaria y mayor visibilidad para los perfiles de guías. El modelo de remuneración de guías permanece sin definir. Tours y Travesías existentes no se eliminan por esta decisión. No se deriva de esto autorización para implementar.

**Próxima secuencia cuando el usuario reactive el proyecto:** PRO-172 (preflight, backup real y restauración aislada) → PRO-165 (validación funcional del calendario/salidas) → PRO-166 (prueba real de subida) → PRO-162/PRO-163 (reconciliación de migraciones registradas y verificación autorizada de escrituras E1). Las migraciones v6–v11 figuran como ejecutadas el 2026-10-22 en Linear; no repetir SQL. La simulación local no sustituye al backup real.

**GitHub:** rama por defecto main. PR #23 sí fue mergeado; la rama visual sigue con 115 commits adicionales frente a main. feature/admin tiene 26 commits adicionales. También existen ramas divergentes chore/technical-hardening y dev. No fusionar ni borrar ramas sin inventario y autorización.

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

**Estado:** PAUSADO por decisión del usuario al 2026-11-03. No avanzar con funcionalidades, arreglos, rediseño ni operaciones técnicas. El alcance actual es exclusivamente documental. El sitio público existe; el Admin y sus integraciones conservan validaciones pendientes. El seguimiento operativo vive en Linear.

**Última actualización:** 2026-11-03. Las migraciones v6–v11 figuran como ejecutadas en Linear el 2026-10-22; no repetir SQL. El respaldo real de producción y la restauración aislada siguen pendientes. La orientación estratégica prioriza paquetes y visibilidad de guías; la remuneración de guías no está definida. Ver el bloque de estado al inicio de esta nota y la continuidad vigente.

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

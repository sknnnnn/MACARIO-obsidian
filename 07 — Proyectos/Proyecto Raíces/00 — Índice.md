## Estado operativo actualizado — cierre técnico previo a producción (2026-10-19)

**Estado actual: PAUSADO hasta la próxima sesión.** La nota histórica del 2026-10-16 que sigue más abajo ya no representa el estado operativo actual; para detalles, consultar las fuentes técnicas enlazadas aquí.

- [Cierre técnico completo en el repositorio de Proyecto Raíces](https://github.com/sknnnnn/proyecto-raices/blob/claude/proyecto-raices-visual-language-q04g3y/docs/operacion/cierre-tecnico-produccion-2026-10-19.md).
- [[07 — Proyectos/Proyecto Raíces/13 — Continuidad previa a producción — 2026-10-19]] — resumen y orden para retomar.
- [Continuidad operativa en el repositorio](https://github.com/sknnnnn/proyecto-raices/blob/claude/proyecto-raices-visual-language-q04g3y/docs/operacion/continuidad-cierre-tecnico-2026-10-19.md).

**Bloqueo principal:** no se confirmó un backup restaurable de Supabase. No aplicar v6–v11 hasta verificar respaldo/recuperación y revisar el plan técnico. Ninguna migración se aplicó; no se modificaron datos de producción, no hubo borrados, deploy ni merge a `main`.

**Siguiente sesión:** (1) verificar Supabase → Database → Backups o PITR; (2) revisar el procedimiento §3.5 del cierre técnico; (3) solo con respaldo confirmado, autorizar y ejecutar migraciones por tramos, una por una; (4) después de v10 y con autorización específica, probar una subida real desde Admin. Los pendientes de contenido y decisiones se detallan en el documento técnico.

---

# Proyecto Raíces — Índice

> Nota de entrada del proyecto dentro de MACARIO.
> Resume el estado general y enlaza el resto de la documentación permanente.
>
> Las tareas operativas viven en Linear.
> El código vive en GitHub.
> Esta nota es el punto de partida para orientarse en el proyecto.

---

## Regla transversal de la plantilla

> **Una fuente por tipo de información.**
> Si una información ya tiene un sistema propietario (Linear, GitHub, README, etc.), esta documentación debe enlazarla, no copiarla.

---

## Resumen

Proyecto Raíces es un proyecto de turismo de aventura y experiencias (tours, travesías y paquetes) que combina naturaleza, aventura, cultura, encuentros, exploración y experiencias compartidas, alejándose del modelo tradicional de agencia.

---

## Estado general

**Estado:** **Activo — fase de reorganización de código, documentación, arquitectura / modelo de datos y preparación del Admin/CMS**. El proyecto **no está terminado**: el sitio público funciona, pero el trabajo actual es reorganizar el código y la documentación, consolidar la arquitectura y el modelo de datos (System Reset, [[07 — Proyectos/Proyecto Raíces/04 — Arquitectura|Arquitectura]] §6–§7) y preparar el Admin/CMS, que todavía debe implementarse sobre esa base. El seguimiento operativo vive en Linear.

> Estado histórico: el 2026-09-28, Linear registró la "etapa funcional cerrada", con el foco puesto en UX/UI y dirección visual. Ese estado quedó superado.
**Última actualización:** 2026-10-16 — refinamiento visual del Admin cerrado en la rama de trabajo; próxima etapa: auditoría D15 e inventario de contenidos, seguida por diagnóstico D19 de Home.

### Estado operativo — 2026-10-16

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

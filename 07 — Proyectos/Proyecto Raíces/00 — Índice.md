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
**Última actualización:** 2026-10-16 — rediseño visual del Admin aprobado como base; refinamiento y auditoría de administrabilidad pendientes.

### Estado operativo — 2026-10-16

- Admin E1: la issue **PRO-160** continúa **In Progress**. La migración v5 figura aplicada y verificada en producción según el registro operativo.
- **Dirección visual:** aprobado como base el rediseño de Claude Design, preview versión 18, con 15 pantallas: https://claude.ai/artifact/FcUCMgXa7z3dQzMNKBa5Hn. La aprobación no autoriza implementación ni publicación.
- **Orden de trabajo:** (1) retomar el refinamiento sobre la misma preview, sin empezar de cero; (2) revisar y aprobar la preview refinada e identificar puntos a validar en código; (3) auditar la administrabilidad actual —metadata, imágenes, card, vista rápida, detalle, fechas, recorrido y campos innecesarios—; (4) diseñar el Admin espejo del frontend editable, combinando edición contextual y controles operativos; (5) implementar y validar antes de autorizar cualquier publicación.
- **Límites:** no ampliar el trabajo pausado ni modificar ahora el repositorio de aplicación, Supabase o producción. El Admin espejo es posterior al refinamiento y a la auditoría. No hay autorización implícita para merge a `main`, despliegues ni escrituras remotas.
- Fechas de Travesías: comprobar cómo conectar las fechas gestionadas desde Admin con el calendario público existente. No crear un calendario paralelo; Tours quedan excluidos.
- Experiencia destacada en Home: diferida para otra etapa.
- Otros pendientes operativos: escrituras reales de E1, pruebas Deno de Edge Functions, resolver la experiencia E0 de prueba en producción con autorización y continuar decisiones D7–D18.

Seguimiento operativo: [PRO-160](https://linear.app/proyecto-raices/issue/PRO-160/raices-admin-de-contenidos-e0-validada-e1-en-planificacion).
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

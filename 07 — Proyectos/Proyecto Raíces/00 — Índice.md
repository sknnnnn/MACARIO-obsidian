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
**Última actualización:** 2026-10-15 — estado del Admin E1, dirección visual en exploración y próximos pasos operativos.

### Estado operativo — 2026-10-15

- Admin E1: migración v5 aplicada y verificada en producción según el registro operativo. La issue **PRO-160** sigue **In Progress**.
- Dirección visual: existe una preview privada de Claude Design con 15 pantallas. El refinamiento quedó pausado por límite diario; continuar desde la preview existente, sin reiniciar la exploración.
- Próximo trabajo: validar la preview y después implementar en `feature/admin`, preservando la lógica existente. No hay autorización implícita para merge a `main` ni para desplegar.
- Fechas de Travesías: comprobar cómo conectar las fechas gestionadas desde Admin con el calendario público existente. No crear un calendario paralelo; Tours quedan excluidos.
- Experiencia destacada en Home: diferida para otra etapa.
- Pendientes de cierre: escrituras reales de E1, pruebas Deno de Edge Functions, resolver la experiencia E0 de prueba en producción con autorización y continuar decisiones D7–D18.

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

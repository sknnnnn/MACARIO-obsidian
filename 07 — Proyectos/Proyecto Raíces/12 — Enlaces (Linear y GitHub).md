# Proyecto Raíces — Enlaces (Linear y GitHub)

> Solo pointers a los sistemas de ejecución. No se copia ni resume contenido acá.
> Regla transversal: una fuente por tipo de información — enlazar, no copiar. Ver [[07 — Proyectos/Proyecto Raíces/00 — Índice]].

---

## Linear

**Proyecto:** [Rediseño y lanzamiento Web](https://linear.app/proyecto-raices/project/rediseno-y-lanzamiento-web-2a37c58672be) (verificado 2026-10-07). El nombre del proyecto no menciona "Raíces"; por eso la verificación del 2026-09-12 no lo encontró.

**Documentos de Linear con conocimiento de Raíces** (migrado a esta documentación el 2026-10-07; se conservan como referencia histórica):
- [Roadmap — MACARIO STUDIO + WEB-BASE + RAÍCES](https://linear.app/proyecto-raices/document/roadmap-macario-studio-web-base-raices-3beb4db4f227) — §12–13 (System Reset, Admin/CMS, motion).
- [PRO-40 — Contrato técnico maestro de experiencias](https://linear.app/proyecto-raices/document/pro-40-contrato-tecnico-maestro-de-experiencias-6f54d70eb333).

---

## GitHub

**Repositorio:** https://github.com/sknnnnn/proyecto-raices.git (confirmado por auditoría de Git, 2026-09-12).

Nota: al momento de esta auditoría, el checkout local del repositorio tenía activa la rama `claude/proyecto-raices-visual-language-q04g3y`, con trabajo de rediseño visual/contenido que todavía no está en `main`. El seguimiento del estado de ramas y PRs vive en GitHub, no se documenta acá.

---

## Sitio en producción

**URL:** https://proyectoraices.com.ar

---

## Figma

[Tablero de referencias y dirección visual](https://www.figma.com/design/RqXlNyOZPYDsJFtX9Kk6dj/PRANA-STUDIOS?node-id=54-26) — archivo `PRANA STUDIOS` (el nombre del archivo no implica relación de identidad con PRANA).

## Otros enlaces

- Google Drive: carpeta "Proyecto Raíces" (branding, minutas, banco de imágenes, fuente real de descripciones de destinos).

---

## Documentos relacionados

- [[07 — Proyectos/Proyecto Raíces/00 — Índice]]


## Seguimiento operativo — 2026-10-19

- **Cierre técnico previo a producción:** [documento completo en GitHub](https://github.com/sknnnnn/proyecto-raices/blob/claude/proyecto-raices-visual-language-q04g3y/docs/operacion/cierre-tecnico-produccion-2026-10-19.md).
- **Continuidad para la próxima sesión:** [plan y bloqueos](https://github.com/sknnnnn/proyecto-raices/blob/claude/proyecto-raices-visual-language-q04g3y/docs/operacion/continuidad-cierre-tecnico-2026-10-19.md).
- **Estado:** pausado. No se aplicaron migraciones, no hubo cambios de datos, borrados, deploy ni merge a `main`.
- **Bloqueo principal:** backup/restauración de Supabase sin confirmar. No avanzar con v6–v11 hasta verificarlo.
- **Próximo paso:** revisar Supabase → Database → Backups/PITR; después revisar el procedimiento técnico y autorizar por tramos, una migración por vez. Prueba real de Storage solo después de v10 y con autorización específica.
- **Linear:** PRO-160 y PRO-166 comentadas con la evidencia del cierre; ninguna issue se cerró.

---

## Seguimiento operativo — 2026-10-16

- **Linear PRO-160:** [estado y continuidad](https://linear.app/proyecto-raices/issue/PRO-160/raices-admin-de-contenidos-e1-v5-aplicada-y-verificada-falta-publicar).
- **Nota técnica de cierre:** [GitHub — cierre-sesion-2026-10-16.md](https://github.com/sknnnnn/proyecto-raices/blob/claude/proyecto-raices-visual-language-q04g3y/docs/admin/cierre-sesion-2026-10-16.md).
- **Rama de trabajo:** [claude/proyecto-raices-visual-language-q04g3y](https://github.com/sknnnnn/proyecto-raices/tree/claude/proyecto-raices-visual-language-q04g3y).
- **Siguiente paso:** auditar D15 y el inventario §11.7; luego diagnosticar D19 (Home). Sin merge, publicación, despliegue o migraciones remotas sin autorización explícita.

---

## Seguimiento operativo — 2026-10-15

- **Admin E1 / estado actual:** [Linear PRO-160](https://linear.app/proyecto-raices/issue/PRO-160/raices-admin-de-contenidos-e0-validada-e1-en-planificacion) — In Progress.
- **Especificación funcional del Admin:** [GitHub](https://github.com/sknnnnn/proyecto-raices/blob/feature/admin/docs/admin/especificacion-funcional.md).
- **Guía operativa Admin v5:** [GitHub](https://github.com/sknnnnn/proyecto-raices/blob/feature/admin/docs/operacion/admin-v5-guia-operativa.md).
- **Preview privada del rediseño (15 pantallas):** https://claude.ai/artifact/FcUCMgXa7z3dQzMNKBa5Hn. Retomar desde esta preview; no reiniciar exploración.

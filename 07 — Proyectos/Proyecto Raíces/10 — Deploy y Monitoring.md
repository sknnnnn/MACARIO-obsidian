# Proyecto Raíces — Deploy y Monitoring

> Proceso de deploy y herramientas de analítica/monitoreo usadas en este proyecto.
> Regla transversal: una fuente por tipo de información — enlazar, no copiar. Ver [[07 — Proyectos/Proyecto Raíces/00 — Índice]].

---

## 1. Proceso de deploy

**Confirmado en otra fuente (`PROJECT-CONTEXT.md` del repositorio, 2026-10-07):** flujo real `GitHub main → Cloudflare`. No existe pipeline de CI/CD adicional.

- **Hosting:** Cloudflare, conectado al repositorio de GitHub.
- **Rama que dispara el deploy:** `main`.
- **No usa GitHub Pages:** el repositorio no tiene `CNAME` ni workflows de GitHub Actions.
- **Cambio de visibilidad del repositorio a privado (regla *private by default*, 2026-10-07):** el deploy depende de que la integración de Cloudflare con GitHub tenga acceso al repositorio privado. Después del cambio, verificar que un push a `main` siga disparando el deploy.

> Nota: desde la sesión de auditoría no fue posible acceder al sitio publicado (bloqueo de red del entorno), así que el proveedor se confirmó por el repositorio y no por inspección del sitio.

Nota histórica (2026-09-12): no se encontró ningún archivo de configuración de deploy en el repositorio (sin `netlify.toml`, `vercel.json` ni workflows de GitHub Actions al momento de esta auditoría). Esto no confirma el proveedor de deploy — solo indica que no está configurado como código dentro del propio repositorio. El proveedor y el proceso real de deploy siguen pendientes de confirmar con Ignacio.

---

## 2. Entornos

Pendiente de documentar. Ver también [[07 — Proyectos/Proyecto Raíces/08 — Desarrollo]].

---

## 3. Analítica

Pendiente de documentar. No hay herramientas de analítica específicas de Proyecto Raíces registradas en la documentación original.

---

## 4. Monitoreo de errores

**Sentry** — integración presente en el código (`assets/js/sentry-init.js`, commit `2800b63`, 2026-09-08).

> ⚠️ **Contradicción técnica abierta (detectada 2026-10-07):** en Linear, PRO-52 ("Integrar Sentry…") figura como *Done*, pero en el código `SENTRY_DSN = "COMPLETAR"`. **Sentry no está activo en producción.** No asumir que PRO-52 está terminado; queda para resolverse en Linear / GitHub.

---

## 5. Alertas

Pendiente de documentar.

---

## Documentos relacionados

- [[07 — Proyectos/Proyecto Raíces/00 — Índice]]
- [[07 — Proyectos/Proyecto Raíces/08 — Desarrollo]]

# Inventario — Consolidación transversal Loop 1 — 2026-10-22

> Nota de enlace. El detalle verificable (ramas, evidencia, comandos de solo lectura para ambas PC, lista de candidatas a limpiar) está en el repositorio de aplicación: [inventario-consolidacion-2026-10-22.md](https://github.com/sknnnnn/proyecto-raices/blob/claude/proyecto-raices-visual-language-q04g3y/docs/operacion/inventario-consolidacion-2026-10-22.md) (actualizado en el commit `bd186a7`).

## Estado verificado (desde la nube, historial completo; no desde las PC)

- **Raíces:** la rama de trabajo contiene `main` y `feature/admin`. `chore/technical-hardening`, `dev` y las tres `docs/…20261009` tienen su contenido en la rama de trabajo, pero no son ancestras: se conservan. No se borró nada.
- **GXK12:2:** 6 ramas; `chore/gxk-local-staging-safe` tiene 2 commits publicados no integrados (conservar). Tres `feat/home-v04-*` están contenidas en `fix/home-v04-visual`, con previews de Vercel.
- **Este vault (`master` 8b6ad8a):** 9 ramas `docs/…` sin líneas ausentes; `docs/gxk-admin-loop2-decisions-2026-10-17` y `claude/obsidian-fix-broken-links-20261007` tienen contenido que `master` no repite: conservar hasta decidir qué se rescata.

## Contradicción abierta

La nota 13 y Linear PRO-161 dicen que «19 experiencias sin imagen principal / 26 sin galería» están superadas. Lectura de solo lectura a producción el 2026-10-22: 54 publicadas, **19 sin imagen principal, 26 sin galería, 0 fotos con texto alternativo**. Las cifras siguen vigentes; la afirmación del vault necesita revisión.

## Pendiente (sin ejecutar)

- Verificar en la PC personal y en la laboral (`git status`, ramas, worktrees, stashes, archivos ignorados): **sin evidencia, ninguna se considera sincronizada**.
- Respaldo real de Supabase y prueba de restauración (PRO-172, Loop 2): **no existe todavía**. Migraciones v6–v11 sin aplicar.
- Aprobación de la lista de ramas a limpiar.


## Cierre de la etapa de consolidación local — 2026-10-22

La consolidación y publicación de los cambios autorizados en Raíces y MACARIO quedó completada y verificada desde la PC personal.

- **Raíces:** `feature/admin` sincronizada con GitHub en `64c059bea0ab9172d99f816e549a76a657357d4a`; working tree limpio. El commit de Codex conserva 232 archivos y el respaldo local `backup/codex-pre-rebase-9b7b565` sigue disponible. Admin E1 y Codex están publicados; no se tocó producción ni Supabase.
- **MACARIO/Obsidian:** `master` sincronizada con GitHub en `9178382f952a14f0b02d97f0f0230219b61d8f4f`; working tree limpio. Publicados los tres commits de decisiones/contexto GXK y esta nota de enlace.
- Las tres ramas originales de Obsidian siguen intactas en `origin/*`. La rama de enlaces rotos no se integró porque su cambio quedó superado por la versión de enlaces que ya está corregida en `master`.
- No se hizo push de otras ramas, no se borraron ramas ni se reorganizaron archivos del vault.

**Alcance:** esto cierra la etapa de consolidación local y publicación de Raíces + MACARIO, no toda PRO-161. La PC laboral sigue pendiente de inspección; también quedan la conciliación final de referencias locales, las decisiones de limpieza de ramas y la revisión del deployment ERROR antiguo de Vercel. GXK no se modificó durante esta etapa.

**Siguiente loop operativo:** PRO-172 — respaldo real de producción de Raíces y prueba de restauración aislada. Todavía no existe un respaldo real validado ni una restauración probada; las migraciones v6–v11 siguen sin aplicar. No avanzar a migraciones hasta cumplir y verificar los criterios de PRO-172.


## GXK12:2 — estado previo a la consolidación local (2026-10-22)

**Repositorio:** `sknnnnn/GxK12-2`; rama por defecto `master`. La conexión de GitHub confirma seis ramas remotas:

- `master`
- `fix/home-v04-visual`
- `feat/home-v04-approved`
- `feat/home-v04-cierre`
- `feat/home-v04-preview-safe`
- `chore/gxk-local-staging-safe`

### Hechos remotos ya conocidos

- `chore/gxk-local-staging-safe` conserva dos commits propios frente a la sucesora visual: `7982038` (documentación de staging local) y `e066783` (seed SQL intencionalmente vacío). No integrarlos ni descartarlos sin revisar el clon local y confirmar su necesidad.
- `fix/home-v04-visual` es la rama sucesora visual conocida; está 18 commits por delante de `master`.
- `feat/home-v04-approved`, `feat/home-v04-cierre` y `feat/home-v04-preview-safe` están integradas por ancestría en la sucesora según el inventario remoto previo. Había previews READY de Vercel asociados a esas ramas; preservar sus referencias hasta verificar URLs, uso y configuración actual.
- El Admin Lote 1 está aprobado visualmente en Figma; su implementación funcional corresponde al Loop 4 transversal. Las pantallas públicas continúan pausadas para el Loop 5.
- `docs/staging-local.md` exige staging local aislado: no enlazar ni ejecutar comandos contra Supabase alojado; no copiar secretos de producción; seed vacío; pruebas con datos sintéticos.

### Trabajo requerido para cerrar la parte local de GXK

1. En la PC personal, inspeccionar el clon real de GXK: ruta, rama actual, `git status`, archivos ignorados, ramas locales, worktrees, stashes, remotos y commits no publicados. No asumir que coincide con la foto remota.
2. Identificar cambios de trabajo, artefactos de staging, `.env.local`, `supabase/.temp/`, volúmenes/dumps y cualquier contenido ignorado; nunca publicar secretos ni datos locales.
3. Conciliar la rama local `chore/gxk-local-staging-safe` y sus dos commits propios con el remoto; preservar ambos y cualquier trabajo adicional. No rebasear, resetear, limpiar ni borrar por inferencia.
4. Comparar el estado local de las ramas activas de Home V0.4 con GitHub y Vercel; no tocar previews READY ni publicar un cambio visual a producción.
5. Solo si el contenido es revisado, seguro y el árbol está entendido, publicar cambios autorizados mediante push normal de la rama correcta; verificar SHA local/remoto y árbol limpio. No usar force push ni integrar a `master` sin autorización.
6. Documentar resultado y próxima acción en Obsidian y PRO-161.

**Límites:** esta etapa es consolidación y trazabilidad, no implementación del Admin GXK, no continuación del storefront, no migraciones ni cambios en producción. La verificación local de GXK y su publicación siguen pendientes; no se deben considerar cerradas por la auditoría remota.

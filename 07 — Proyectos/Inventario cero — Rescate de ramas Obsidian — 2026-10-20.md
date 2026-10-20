# Rescate selectivo de ramas Obsidian — 2026-10-20

> **Estado:** auditoría remota de solo lectura; no autoriza borrados ni merges.
> **Alcance:** ramas documentales de `sknnnnn/MACARIO-obsidian`.
> **Seguimiento:** [Linear PRO-161 — Inventario y limpieza](https://linear.app/proyecto-raices/issue/PRO-161/gobernanza-feature-freeze-y-limpieza-del-inventario-raices-gxk122) · [PR #16 — auditoría documental](https://github.com/sknnnnn/MACARIO-obsidian/pull/16).

## Criterio

No conservar una rama únicamente porque tenga commits exclusivos, ni borrarla porque esté atrasada. Comparar archivos concretos contra `master`, identificar contenido que siga vigente y revisar worktrees/referencias locales antes de cualquier eliminación. Las ramas históricas no se integran completas si contienen decisiones o estados superados.

## Resultado por rama

### Candidatas a limpieza después de verificación local

- `docs/conciliacion-estado-2026-10-20`: el roadmap de GXK y el inventario tienen los mismos blob SHA que `master`. Los dos archivos cambiados ya están reflejados en la rama principal; no se encontró contenido documental vigente exclusivo en los archivos comparados.
- `docs/cleanup-pointers-and-branch-audit-2026-10-19`: el índice GXK y `Proyecto Raíces/12 — Enlaces (Linear y GitHub).md` coinciden por SHA con `master`. Su inventario es una versión anterior/superada frente al de `master`.
- `docs/gxk-admin-lote1-cierre-2026-10-19`: la nota `12 — Admin Lote 1 — Cierre y continuidad 2026-10-19.md` y el changelog coinciden exactamente con `master`; el índice de la rama es anterior y no contiene la sección de gobernanza presente en `master`.
- `claude/obsidian-content-cleanup-20261007`: el comparador informa cero commits exclusivos y la rama está muy atrasada. Candidata solo tras comprobar PRs, worktrees y referencias locales.
- `claude/trusting-feynman-sm520n`: la revisión de los 32 archivos no encontró contenido vigente exclusivo; 22 blobs son idénticos a `master` y los 10 restantes son versiones antiguas. Candidata tras verificación local.
- `claude/obsidian-structural-cleanup-20261007`: los cambios comparados están superados por `master`; la auditoría histórica ya está en `master` en una versión más completa, y la eliminación del antiguo archivo raíz de principios ya está reflejada. Candidata tras verificación local.
- `claude/obsidian-fix-broken-links-20261007`: los seis archivos cambiados son versiones antiguas con enlaces/definiciones superados por `master`. Candidata tras verificación local.

**Acción:** no borrar desde esta sesión. Confirmar primero desde la PC personal que no haya worktrees, ramas locales sin publicar, automatizaciones o URLs activas que dependan de ellas.

### Mantener temporalmente para rescate selectivo

- `docs/gxk-admin-loop2-decisions-2026-10-17`: la entrada del 17/10 falta en el changelog de `master`, pero es un snapshot de planificación, no una lista de decisiones para copiar en bloque. La contrasté con el changelog y el cierre del 19/10:
  - **No rescatar como estado actual:** Loop 2 pausado esperando a Raíces; Figma aún pendiente de aprobación; revisión de navegación presentada como futura; propuesta de aviso de duplicados; «ABC Favorit conserva prioridad documental» si contradice la jerarquía de fuentes vigente.
  - **Conservar solo donde siga vigente y esté confirmado por las fuentes actuales:** `is_featured` no tiene efecto operativo y no debe conectarse al hero por inferencia; Figma sigue siendo la fuente visual aprobada y Claude Design un motor de exploración/validación; la interfaz debe priorizar español, accesibilidad y baja fricción. Estos principios ya están reflejados en documentos vigentes, por lo que no requieren copiar la entrada histórica entera al changelog.
  - **No rescatar:** la detección de duplicados por nombre/tamaño; el cierre del 19/10 la retiró porque el modelo no persiste el nombre original ni ofrece hashes/comparación visual.
  - **Conclusión:** no integrar el changelog de esa rama tal cual. Retenerla temporalmente solo hasta confirmar que los criterios vigentes están cubiertos en fuentes actuales y revisar referencias/worktrees locales.

### Otras ramas documentales

- `docs/branch-audit-2026-10-20`: rama de trabajo del PR #16. La contradicción sobre el PR #5 fue corregida y verificada en el inventario (commit `a26ddc5d2411951b1ea4c0bdd95602dbffc86f49`); el PR #16 sigue abierto, no mergeado. La identificación de E0 como `prueba` en PRO-164 no autoriza a borrar ninguno de los cinco borradores.

## Estado de seguridad

- No se borraron ramas ni deployments.
- No se integraron commits en `master`.
- No se modificaron código, datos de producción, Supabase, Figma ni artefactos de Claude Design.
- La verificación de worktrees y referencias locales queda pendiente hasta usar la PC personal.
- Este documento registra la auditoría; no reemplaza las fuentes de verdad de los proyectos ni autoriza acciones destructivas.

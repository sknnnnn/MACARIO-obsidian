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

**Acción:** no borrar desde esta sesión. Confirmar primero desde la PC personal que no haya worktrees, ramas locales sin publicar, automatizaciones o URLs activas que dependan de ellas.

### Mantener temporalmente para rescate selectivo

- `docs/gxk-admin-loop2-decisions-2026-10-17`: su entrada del 17/10 no está en el encabezado del changelog de `master`. Revisar por decisión, no copiar la entrada completa:
  - conservar como criterios a revisar la interfaz del Admin en español, la organización de navegación, la distinción entre Familia GXK y Members Only, accesibilidad/temas y el principio de Figma como fuente visual aprobada;
  - mantener `is_featured` sin efecto operativo hasta una decisión explícita;
  - no rescatar la supuesta detección de duplicados de imágenes por nombre/tamaño: el cierre del 19/10 la retiró porque el modelo no persiste el nombre original ni ofrece hashes/comparación visual;
  - no mantener como estado actual que Loop 2 estaba pausado esperando a Raíces; es una fotografía histórica del 17/10 y fue superada por el cierre del Admin Lote 1 del 19/10.
- `claude/trusting-feynman-sm520n`: 10 commits exclusivos y cambios en 32 archivos, incluidos documentos de GXK, Raíces, MACARIO, PRANA y Bresstore. No hacer merge global. La mayoría de los estados requieren contraste con fuentes más recientes; el índice de Bresstore revisado tiene el mismo SHA que `master`.
- `claude/obsidian-structural-cleanup-20261007`: la auditoría del 07/10 ya existe en `master` como versión actualizada que la etiqueta como histórica/superada. Las versiones de arquitectura e ITS en la rama mantienen formulaciones antiguas sobre PRANA/MACARIO; no rescatar esos archivos completos.
- `claude/obsidian-fix-broken-links-20261007`: las versiones revisadas de arquitectura, metodología, herramientas, Web-Base, MACARIO OS y PRANA son más antiguas que `master`, con wikilinks y formulaciones superadas. No integrar la rama completa.

### Otras ramas documentales

- `docs/gxk-admin-lote1-cierre-2026-10-19`: la nota de cierre está integrada en `master` con blob SHA `7b9014bbe9c941bdbb579e23fba5e72358821f50`. La copia antigua de la rama de origen afirma que solo existía allí; ese dato de sincronización quedó obsoleto.
- `docs/branch-audit-2026-10-20`: sigue siendo la rama de trabajo del PR #16. Antes del merge hay que reconciliar la contradicción interna sobre el estado del PR #5: las instrucciones antiguas hablan de cerrarlo en el futuro, mientras otra sección ya lo registra como cerrado sin merge. La identificación de E0 como `prueba` en PRO-164 no autoriza a borrar ninguno de los cinco borradores.

## Estado de seguridad

- No se borraron ramas ni deployments.
- No se integraron commits en `master`.
- No se modificaron código, datos de producción, Supabase, Figma ni artefactos de Claude Design.
- La verificación de worktrees y referencias locales queda pendiente hasta usar la PC personal.
- Este documento registra la auditoría; no reemplaza las fuentes de verdad de los proyectos ni autoriza acciones destructivas.

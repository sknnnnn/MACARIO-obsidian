# Inventario cero — Proyecto Raíces + GXK12:2

> **Fecha:** 2026-10-19  
> **Estado:** barrido iniciado; clasificación y limpieza selectiva en curso. No equivale a permiso para borrar datos de producción.  
> **Issue rectora:** [Linear PRO-161 — Gobernanza, Feature Freeze y limpieza del inventario](https://linear.app/proyecto-raices/issue/PRO-161/gobernanza-feature-freeze-y-limpieza-del-inventario-raices-gxk122).

## Principio

Una cosa vieja no es necesariamente obsoleta. Antes de borrar un archivo, rama, issue, artefacto o registro hay que demostrar que no está en uso, que su información útil está preservada y que no es fuente de verdad ni contiene una decisión vigente. Si falta evidencia, se clasifica como candidato y no se elimina.

## Fuentes revisadas

- **Linear:** issues de GXK12.2 y Rediseño y lanzamiento Web (Raíces), proyectos, documentos y PRO-161.
- **GitHub:** ramas, PRs y árboles de sknnnnn/GxK12-2, sknnnnn/proyecto-raices y sknnnnn/MACARIO-obsidian.
- **Obsidian:** índices, changelogs y notas de continuidad de ambos proyectos.
- **Supabase:** dos proyectos activos y saludables: Proyecto Raices y GxK12-2. No se modificaron tablas, datos, migraciones ni ramas.
- **Vercel:** el proyecto relevante para GXK es gx-k12-2. Raíces documenta sus despliegues en Cloudflare Pages; no apareció un proyecto Vercel llamado Raíces en el inventario consultado.
- **Figma / Claude Design:** se preservan las fuentes visuales conocidas. No estuvo disponible un listado completo de artefactos de Claude Design ni se verificaron todos los archivos de Figma; el inventario de esas herramientas es parcial. No se borraron diseños.

## Limpieza ya aplicada

1. **Linear PRO-158 — Home V0.4:** pasó de In Progress a Backlog; se documentó la pausa hasta cerrar el Admin Lote 1 y se añadió dependencia de PRO-173. No se canceló.
2. **Linear PRO-159 — Experiencia & Motion de Home:** se mantiene en Backlog, con pausa explícita y dependencia de PRO-173.
3. **Linear PRO-161:** pasó a In Progress para reflejar que el inventario se está auditando.
4. **Documentación:** la rama de limpieza consolida dos notas de continuidad de Raíces, corrige el estado del índice y agrega este inventario. La revisión de los criterios de duplicados se registra aquí porque la propuesta sin soporte técnico solo aparece en el PR #5 aún no integrado.

## Linear — clasificación inicial

### GXK12:2

| Issue | Clasificación | Próxima acción |
|---|---|---|
| [PRO-173](https://linear.app/proyecto-raices/issue/PRO-173/gxk122-admin-lote-1-revisar-correcciones-y-preparar-aprobacion) | Prioridad actual | Revisar el artefacto v4 en el visor real, contrastar con Figma y aprobar o pedir correcciones; no avanzar al Lote 2. |
| [PRO-158](https://linear.app/proyecto-raices/issue/PRO-158/gxk122-home-v04-cierre-visual-y-preparacion-de-integracion) | Pausada / Backlog | Retomar después de cerrar Admin Lote 1; conservar las notas de QA e integración histórica. |
| [PRO-159](https://linear.app/proyecto-raices/issue/PRO-159/gxk122-direccion-de-experiencia-and-motion-de-home) | Pausada / Backlog | Retomar cuando se reabra diseño público; no explorar motion ahora. |
| [PRO-128](https://linear.app/proyecto-raices/issue/PRO-128/gxk122-shipping-implementar-flujo-real-de-envios) | Mantener en backlog | Integración real de envíos pendiente; verificar decisiones y credenciales antes de ejecutar. |
| [PRO-129](https://linear.app/proyecto-raices/issue/PRO-129/gxk122-stock-automatizar-liberacion-de-reservas-vencidas) | Mantener en backlog | Automatización pendiente; no es duplicada del trabajo visual del Admin. |
| [PRO-124](https://linear.app/proyecto-raices/issue/PRO-124/gxk122-mercado-pago-completar-configuracion-y-pruebas-reales) | Mantener en backlog | Depende de credenciales reales y pruebas autorizadas. |
| [PRO-127](https://linear.app/proyecto-raices/issue/PRO-127/gxk122-shipping-agregar-peso-y-dimensiones-al-catalogo) | Mantener en backlog | Datos logísticos pendientes; no cerrar sin evidencia. |
| [PRO-125](https://linear.app/proyecto-raices/issue/PRO-125/gxk122-shipping-completar-integracion-andreani) | Reabierta a Backlog por descripción/estado contradictorios | El adapter existe, pero credenciales/endpoints de Andreani no están verificados; no declarar integración real completada. Relacionada con PRO-128. |
| [PRO-126](https://linear.app/proyecto-raices/issue/PRO-126/gxk122-shipping-completar-integracion-correo-argentino) | Reabierta a Backlog por descripción/estado contradictorios | Faltan credenciales, valores de contrato y validación real de Correo Argentino; relacionada con PRO-128. |

### Proyecto Raíces

| Issue | Clasificación | Próxima acción |
|---|---|---|
| [PRO-172](https://linear.app/proyecto-raices/issue/PRO-172/raices-respaldar-produccion-y-probar-restauracion-antes-de-migraciones) | Bloqueante / prioridad alta | Desde la PC personal, confirmar backup restaurable, Storage y prueba de restauración; no migrar antes. |
| [PRO-160](https://linear.app/proyecto-raices/issue/PRO-160/raices-admin-de-contenidos-e1-v5-aplicada-y-verificada-falta-publicar) | Mantener In Progress | Verificar rama de trabajo y requisitos de publicación; no asumir que los cambios están integrados. |
| [PRO-166](https://linear.app/proyecto-raices/issue/PRO-166/admin-carga-de-imagenes-d8-y-alt-publico-d13-implementado-y-probado-en) | Mantener / bloqueada por v10 | No probar Storage real ni publicar hasta cumplir prerequisitos y obtener autorización. |
| [PRO-162](https://linear.app/proyecto-raices/issue/PRO-162/admin-aplicar-migraciones-v6-y-v7-en-produccion-requiere-autorizacion) | Bloqueada | Solo después de backup restaurable y autorización explícita; migraciones por tramos. |
| [PRO-163](https://linear.app/proyecto-raices/issue/PRO-163/admin-verificar-escrituras-reales-de-e1-con-datos-descartables-req-01) | Mantener / no ejecutar aún | Pruebas con datos descartables cuando exista entorno seguro y se autorice. |
| [PRO-164](https://linear.app/proyecto-raices/issue/PRO-164/admin-eliminar-la-experiencia-e0-y-los-borradores-de-prueba-req-04) | No limpiar por descarte | E0 sigue sin identificar. No borrar E0 ni los cinco borradores hasta verificar historial/dependencias y recibir autorización. |
| [PRO-165](https://linear.app/proyecto-raices/issue/PRO-165/admin-decision-fuente-unica-de-fechas-salidas-globalcalendario-y) | Mantener / conciliar alcance | La fuente única de salidas está decidida; comprobar qué pasos siguen abiertos antes de cerrar. |
| [PRO-167](https://linear.app/proyecto-raices/issue/PRO-167/admin-destacada-unica-por-destino-req-16-home-momentos-independiente-y) | Mantener / bloqueada por v6 | Implementado localmente según la issue; no dar por aplicado en producción. |
| [PRO-168](https://linear.app/proyecto-raices/issue/PRO-168/df-01-cards-publicas-metadata-con-duracion-y-actividad-req-29) | Mantener | Implementar y verificar metadata pública de cards según intención aprobada. |
| [PRO-169](https://linear.app/proyecto-raices/issue/PRO-169/df-02-orden-de-experiencias-definir-alcance-y-verificar-que-el-sitio) | Mantener / verificar | Comprobar el comportamiento real de orden en web antes de decidir si está resuelta. |
| [PRO-170](https://linear.app/proyecto-raices/issue/PRO-170/df-04-paquetes-no-se-publican-sin-experiencias-asociadas-req-32req-13) | Mantener In Progress | DF-04 aprobado; falta aplicar v8 tras los prerequisitos de respaldo y autorización. |
| [PRO-171](https://linear.app/proyecto-raices/issue/PRO-171/df-05-destinos-el-contador-n-publicadas-de-m-lleva-a-experiencias) | Mantener | Implementar el enlace al listado de experiencias filtradas y probarlo. |
| [PRO-115](https://linear.app/proyecto-raices/issue/PRO-115/raices-refinar-contenido-y-ux-antes-del-rediseno-visual) | Revalidar estado | Sigue In Progress desde el 07/10; revisar si su alcance fue absorbido o si conserva acciones concretas. |
| [PRO-152](https://linear.app/proyecto-raices/issue/PRO-152/raices-repaso-del-contenido-en-ingles) | Mantener en backlog | Trabajo de contenido futuro; no bloquea el backup. |
| [PRO-13](https://linear.app/proyecto-raices/issue/PRO-13/futuro-automatizar-carga-y-distribucion-de-actividades) | Mantener como futuro | No bloquea el cierre actual; no ejecutar por la prioridad heredada. |
| [PRO-52](https://linear.app/proyecto-raices/issue/PRO-52/raices-completar-sentry-para-monitoreo-de-errores-en-produccion) | Mantener en backlog | Deuda de monitoreo independiente; no cerrar sin evidencia. |
| [PRO-81](https://linear.app/proyecto-raices/issue/PRO-81/raices-corregir-flechas-e-interaccion-de-todos-los-carruseles) | Revalidar contra código | Puede haber sido parcialmente resuelta por cambios posteriores; verificar antes de cancelar o cerrar. |
| [PRO-60](https://linear.app/proyecto-raices/issue/PRO-60/ux-acceso-al-catalogo-completo-desde-inicio) | Revalidar contra código | Confirmar si el acceso existe y cumple el requisito. |
| [PRO-150](https://linear.app/proyecto-raices/issue/PRO-150/raices-corregir-bug-del-hero) | Revalidar contra sitio vigente | Comprobar si el bug sigue presente antes de cancelar o cerrar. |
| [PRO-151](https://linear.app/proyecto-raices/issue/PRO-151/raices-revisar-fotos-no-correspondientes) | Mantener / revisar contenido | Revisar asignaciones reales; no sustituir por imágenes inventadas. |
| [PRO-41](https://linear.app/proyecto-raices/issue/PRO-41/14-unificar-footer-y-accesos-secundarios) | Ya marcada Duplicate | Preservar el rastro; comprobar que apunta a la issue canónica. |

## GitHub — ramas y PRs

### GXK12:2

Ramas detectadas: master, fix/home-v04-visual, feat/home-v04-approved, feat/home-v04-cierre, feat/home-v04-preview-safe y chore/gxk-local-staging-safe.

- master está en 950c566; fix/home-v04-visual está en 6be7d02 y contiene documentación de cierre que todavía se había registrado como no publicada. No borrar ninguna sin comparar commits y working tree local.
- feat/home-v04-preview-safe se conserva hasta confirmar que sigue siendo la ruta segura para QA; no usar una Preview que haya escrito eventos en Supabase de producción.
- PR #1 está mergeado; PR #2 está cerrado sin merge. Conservar historial hasta revisar diferencias.

### Proyecto Raíces

Ramas detectadas: main, master, dev, feature/admin, feature/i18n-es-en, ramas claude/*, chore/technical-hardening, reorg/base-tecnica y ramas docs/*.

- main es la rama por defecto y recibió PRs #31–#35. master, dev, feature/admin, feature/i18n-es-en y las ramas Claude no se borran por nombre/antigüedad: comparar SHA, PRs, cambios únicos y estado local.
- PRs #31–#35 están mergeados. Sus ramas técnicas/documentales son candidatas a limpieza tras confirmar que no hay trabajo único no integrado.
- claude/proyecto-raices-visual-language-q04g3y contiene el cierre técnico más reciente según la documentación; no eliminar ni reemplazar por main sin conciliar pendientes.

### MACARIO-obsidian

- PR #7 (cierre GXK) y PR #6 (continuidad Raíces) están mergeados.
- PR #5 sigue abierto y no mergeable. Mezcla decisiones útiles del Loop 2 con estados superados y una propuesta de avisos de duplicados descartada por falta de soporte. Incorporar selectivamente lo vigente y después cerrar el PR como supersedido; no mergear el diff antiguo íntegro.
- Las ramas claude/obsidian-content-cleanup-20261007, claude/obsidian-fix-broken-links-20261007, claude/obsidian-structural-cleanup-20261007 y claude/trusting-feynman-sm520n requieren comparación de commits y contenido antes de decidir.

## Obsidian — limpieza documental

- Las notas «13 — Continuidad previa a producción — 2026-10-19» y «Continuidad — Respaldo de producción y migraciones» se solapaban. La primera se convierte en puntero histórico; la segunda queda como fuente vigente, con pendientes únicos preservados y conteos antiguos invalidados.
- «12 — Cierre técnico Supabase y deploys — 2026-10-09» no se elimina: documenta una migración realmente aplicada y hechos históricos de despliegue.
- «12 — Enlaces (Linear y GitHub)» contiene seguimientos fechados antiguos. No recortar todavía: verificar que cada detalle quedó en Linear o GitHub.
- En GXK, la Biblia y el spacing aprobado de storefront no se sustituyen por la escala del Admin. El artefacto Admin v4 no está aprobado y Figma original permanece intacto.

## Datos y entornos — no limpiar automáticamente

- **Raíces:** no borrar E0 ni ninguno de los cinco borradores. E0 sigue sin identificar; hay dependencias y decisiones pendientes.
- **Supabase:** no borrar filas, objetos Storage, migraciones ni ramas durante este barrido. La migración supabase/pendiente/20261009_endurecimiento.sql se conserva por trazabilidad, aunque esté aplicada.
- **GXK Supabase:** no tocar catálogo de prueba ni migraciones pendientes; no ejecutar SQL de limpieza.
- **Vercel / Cloudflare:** no borrar proyectos, deployments, dominios ni entornos por antigüedad.
- **Figma / Claude Design:** no borrar previews o frames históricos que preservan decisiones. El listado completo de artefactos Claude Design no estuvo disponible; ese inventario es parcial.

## Próximas acciones

1. Integrar esta clasificación y la consolidación documental mediante PR de Obsidian.
2. Cerrar PR #5 como supersedido solo después de integrar las decisiones vigentes.
3. Comparar ramas candidatas contra sus bases y revisar cambios únicos; luego decidir cuáles se pueden eliminar.
4. Conciliar las issues de backlog/In Progress con el código y su próxima acción; no cancelar por antigüedad.
5. Limpiar código temporal solo tras demostrar que no está usado. Cualquier borrado de datos de producción requiere autorización separada.

## Registro de cambios

- 2026-10-19: PRO-158 y PRO-159 pausadas y bloqueadas por PRO-173; PRO-161 pasa a In Progress.
- 2026-10-19: se identifica el solapamiento de notas de continuidad de Raíces y la propuesta de duplicados sin soporte técnico en GXK.
- 2026-10-19: barrido inicial de GitHub, Linear, Obsidian, Supabase, Vercel y fuentes visuales; los candidatos no verificados permanecen intactos.
## Decisiones recuperadas del PR #5 de Obsidian — estado que debe conservarse

El PR #5 contiene contexto útil, pero no debe mergearse íntegro porque el índice y algunas propuestas quedaron superados. Al cerrarlo, conservar explícitamente:

- Mantener la Biblia GXK y la Dirección Visual aprobada como fuentes superiores; no convertir una propuesta de Admin en regla aprobada.
- El Admin debe conservar la estructura y navegación existentes salvo decisión explícita; los cambios de organización visual no deben cambiar comportamiento ni contratos.
- Mantener la interfaz del Admin en español, conservando nombres propios GXK.
- Conservar is_featured y explicar que actualmente no tiene efecto en el storefront; no conectarlo al hero ni eliminarlo por intuición.
- No implementar paginación en el Loop 2 salvo que la auditoría demuestre un bloqueo real y se apruebe el cambio.
- Mantener Universo, Aventuras G&K y Eventos diferenciados.
- Claude Design refina; Figma consolida las pantallas aprobadas como fuente visual; implementación y QA vienen después de aprobación explícita.
- **Descartar la propuesta de alertas por posibles duplicados por nombre/tamaño:** el modelo actual no conserva nombre original ni hash/comparación visual. No se debe describir una detección que no existe.
- Los tokens, tipografía, acentos naranjas, reglas de confirmación reforzada y nuevos patrones del Admin permanecen pendientes hasta revisión del artefacto v4; no se aprueban por estar escritos en el PR antiguo.
## Comparación de ramas — evidencia del 2026-10-19

### GXK12:2

- fix/home-v04-visual está 18 commits adelante de master y no está detrás. Es la rama más completa entre las comparadas.
- Las ramas feat/home-v04-approved (6 commits adelante), feat/home-v04-cierre (8) y feat/home-v04-preview-safe (11) forman una cadena de antecesores: approved → cierre (+2) → preview-safe (+3) → fix/home-v04-visual (+7). Las ramas approved y cierre no muestran commits exclusivos frente a la rama sucesora y son **candidatas a borrar después de comprobar referencias locales**. Aunque preview-safe también es antecesora, se **conserva provisionalmente** hasta verificar que ningún deployment/QA depende de esa ruta segura.
- chore/gxk-local-staging-safe diverge de preview-safe: tiene 2 commits exclusivos y queda 3 commits detrás, con docs/staging-local.md y supabase/seed.sql. **Conservar** hasta revisar y rescatar esos elementos.
- No hay PRs abiertos en el repositorio GXK. PR #1 está mergeado; PR #2 está cerrado sin merge.

### Proyecto Raíces

- main es la rama por defecto. master está 178 commits detrás de main y no tiene commits exclusivos según compare; **candidato**, pero no borrar hasta comprobar si algún deploy/configuración externa todavía lo referencia.
- reorg/base-tecnica está 5 commits detrás de main y no tiene commits exclusivos; PR #31 está mergeado. **Candidato a limpieza** tras confirmar que no quedan referencias externas.
- feature/admin está 25 commits adelante de main. claude/proyecto-raices-visual-language-q04g3y está 86 commits adelante de main y 61 adelante de feature/admin, sin commits detrás. **Conservar ambas** mientras PRO-160 y el cierre técnico sigan dependiendo de ese trabajo.
- dev diverge de main (4 commits exclusivos y 20 detrás); **conservar** hasta revisar sus cambios exclusivos.
- chore/technical-hardening diverge de main (11 commits exclusivos y 4 detrás) pese a PR #32 mergeado; **no borrar** sin revisar commits posteriores y diferencias.
- PRs #31–#35 están mergeados; las ramas docs/* asociadas son candidatas a limpieza tras verificar que el contenido quedó en main y que no existen referencias de deploy.

### MACARIO-obsidian

- claude/obsidian-content-cleanup-20261007 está 28 commits detrás de master y no tiene commits exclusivos; **candidato claro a borrar** tras confirmar que no hay PR o proceso local que lo necesite.
- claude/obsidian-fix-broken-links-20261007 (9 commits exclusivos / 30 detrás), claude/obsidian-structural-cleanup-20261007 (5 exclusivos / 29 detrás) y claude/trusting-feynman-sm520n (10 exclusivos / 28 detrás) contienen cambios propios en documentación central; **no borrar** hasta revisar sus diffs y rescatar o descartar cada cambio.
- docs/gxk-admin-loop2-decisions-2026-10-17 conserva 3 commits no integrados; PR #5 está cerrado sin merge. Las decisiones vigentes se registraron en el inventario, pero la rama aún no se eliminó.
- Las ramas docs/* de PRs ya mergeados son candidatas a limpieza, pero la conexión actual no ofrece una acción de eliminación de referencias; se dejan identificadas para la limpieza final manual.

Estos resultados describen relaciones de commits, no sustituyen la verificación de referencias locales, deploys externos o worktrees. Ninguna rama fue eliminada en este barrido.
## Segunda pasada de Linear — contradicciones en tareas Done

- **PRO-125 y PRO-126:** estaban en Done, pero su descripción decía que la integración real con Andreani/Correo Argentino seguía pendiente. La documentación técnica de GXK confirma que hay adapters, pero faltan credenciales/endpoints/valores de contrato verificados. Se reclasificaron a Backlog, se reescribió el alcance real y se relacionaron con PRO-128.
- **PRO-138 y PRO-139:** estaban en Done, pero conservaban una descripción que empezaba con «Pendiente». Se conservaron como Done y se actualizó el texto para que el alcance original quede como referencia histórica, enlazado al cierre de PRO-144.
- Este cambio evita tanto el falso cierre de integraciones externas como la falsa reapertura de módulos ya cerrados. No se cambió código ni configuración de proveedores.
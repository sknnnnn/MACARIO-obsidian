# Proyecto Raíces — Decisiones y Changelog

> Registro permanente de decisiones importantes e hitos del proyecto.
> Esta nota registra únicamente decisiones permanentes y hitos importantes.
> No registrar cambios menores, tareas, sprints ni actividad cotidiana — eso vive en Linear/GitHub.
> Se agrega, no se reescribe.
> Regla transversal: una fuente por tipo de información — enlazar, no copiar. Ver [[07 — Proyectos/Proyecto Raíces/00 — Índice]].

---

## Cómo usar esta nota

Cada entrada nueva se agrega arriba, con fecha. No se borran entradas anteriores. Las entradas migradas desde el documento original no tenían fecha registrada; se marcan explícitamente como "Fecha: no registrada" en vez de inventar una.


## Hito: 2026-10-26 — Pausa y orden de retoma de la reestructuración

**Decisión de proceso:** pausar Raíces al cierre de la sesión y dejar documentados tanto los pendientes operativos como la reestructuración propuesta. No se crean documentos nuevos: se actualizan las notas canónicas existentes y el punto de continuidad del repositorio.

**Próximo trabajo de reestructuración:** inventariar la aplicación real (páginas, componentes, assets, tokens y datos); proponer arquitectura de navegación; proponer dirección visual; obtener aprobación explícita antes de implementar. Esta fase de análisis puede comenzar sin haber cerrado todos los pendientes técnicos.

**Pendientes que siguen abiertos:** PRO-172 (respaldo/restauración), PRO-165 (calendario público), PRO-166 (carga real de imágenes), PRO-162/163/164 (escrituras y datos de prueba), y reconciliación del Loop 2 Admin (B–F; etapa A cerrada). PRO-172 no bloquea inventario ni diseño conceptual, pero sí operaciones sensibles/destructivas sobre datos o producción y nuevas migraciones.

**Límites:** no se modificó código funcional, Supabase, datos, producción, Linear ni despliegue como parte de esta pausa. No se considera aprobado el nuevo mapa de navegación ni la dirección visual. Se mantienen Paquetes como prioridad, Guías locales como eje a desarrollar y Tours/Travesías como oferta vigente; Destinos conecta editorialmente sin duplicar el catálogo.

---

## Hito: 2026-10-19 — Cierre técnico preparado y pausa antes de producción

**Estado:** se completa la preparación técnica previa a producción, pero se pausa la ejecución hasta la próxima sesión. No se aplicaron migraciones remotas, no se modificaron datos, no se borraron archivos ni registros, no hubo deploy ni merge a `main`.

**Fuente técnica única:** [cierre técnico previo a producción](https://github.com/sknnnnn/proyecto-raices/blob/claude/proyecto-raices-visual-language-q04g3y/docs/operacion/cierre-tecnico-produccion-2026-10-19.md). El detalle de hashes, validadores SQL, riesgos, inventario de imágenes y decisiones pendientes permanece allí para evitar duplicación.

**Bloqueo para avanzar:** no está confirmada una copia restaurable de Supabase ni una restauración viable. Antes de autorizar v6–v11 hay que verificar Database → Backups o PITR, revisar el plan técnico y aplicar las migraciones de forma escalonada, una por una. Storage necesita recuperación aparte de la base de datos.

**Estado relevante:** 436/436 tests Playwright Chromium en la última corrida completa; v6–v11 preparadas, ninguna aplicada; carga de imágenes Admin implementada localmente, depende de v10 y falta prueba real. Las notas de continuidad están enlazadas desde [[07 — Proyectos/Proyecto Raíces/00 — Índice]] y [[07 — Proyectos/Proyecto Raíces/13 — Continuidad previa a producción — 2026-10-19]].

**Pendientes que no se resuelven hoy:** elegir una de las dos experiencias destacadas de Cusco; decidir D3/D9 y D14; modelo de experiencias internas de paquetes; autorización para unificar los dos grupos de referencias duplicadas y para limpiar borradores; obtener material real para las experiencias sin imagen/galería y completar alt; verificar entrega de correo, accesibilidad y otros navegadores.

---

## Decisiones

### Fecha: 2026-10-16 — Cierre del refinamiento visual y continuidad funcional

**Hito:** se cierra el tramo de refinamiento visual del Admin en la rama de trabajo `claude/proyecto-raices-visual-language-q04g3y`. La rama está publicada en GitHub; el registro técnico está en [la nota de cierre](https://github.com/sknnnnn/proyecto-raices/blob/claude/proyecto-raices-visual-language-q04g3y/docs/admin/cierre-sesion-2026-10-16.md), commit documental `87ef3ff`.

**Validación registrada:** Playwright 176/176 y `node --check` sin errores; responsive revisado en 390, 768, 1024 y 1280 px. D21 se resolvió respetando `CLAUDE.md §9`. Siguen pendientes las verificaciones con Supabase Auth/PostgREST reales, escrituras reales y lectores de pantalla.

**Decisiones de continuidad:**
1. Auditar D15 (seis claves `site_config` editables en Admin que no se usan en frontend), sin implementar todavía.
2. Clasificar el inventario §11.7 por contenido ya editable/desconectado, nueva estructura necesaria, elemento que debe permanecer en código o decisión pendiente.
3. Diagnosticar D19 usando el lienzo existente de Claude y la Home real, y revisar la propuesta antes de implementar.

**Definición de Home para D19:** Portada (la foto ya es editable; verificar el resto), Momentos para vivir distinto (carrusel de 10 experiencias), Principales destinos, Tours, Travesías, Paquetes, Quiénes somos, Comentarios y comunidad, Cierre. Tours, Travesías y Paquetes son cards editoriales de acceso a sus secciones, no listados. Actualmente no existe “experiencia destacada” en Home; no se considera requisito.

**Límites:** no se hizo merge a `feature/admin`, `main` o `master`; no se publicó ni desplegó a producción ni se ejecutaron migraciones remotas. No autorizar esos pasos implícitamente.

---


### Fecha: 2026-10-16 — Aprobación del rediseño visual del Admin y orden de trabajo

**Decisión:** se aprueba como base de trabajo el rediseño visual del Admin de Proyecto Raíces en la preview de Claude Design, versión 18, con 15 pantallas: https://claude.ai/artifact/FcUCMgXa7z3dQzMNKBa5Hn.

**Alcance de la aprobación:** queda aprobada la dirección visual propuesta, no la implementación ni su publicación. La preview sigue siendo el punto de partida; no se reinicia la exploración ni se amplía el trabajo pausado.

**Orden acordado:**
1. Retomar el refinamiento visual pendiente sobre las mismas 15 pantallas de la preview existente.
2. Revisar y aprobar la preview refinada, anotando los aspectos que requieran validación durante la implementación.
3. Auditar la administrabilidad del sistema actual: metadata, imágenes, tarjeta (card), vista rápida, detalle, fechas, recorrido y campos innecesarios.
4. Diseñar la propuesta de Admin espejo del frontend editable, combinando edición visual contextual con controles específicos para la gestión operativa.
5. Implementar y validar los cambios antes de autorizar cualquier publicación.

**Límites:** por ahora no se modifican el repositorio de aplicación, Supabase ni producción. La propuesta de Admin espejo es posterior al cierre del refinamiento visual y la auditoría. No hay autorización implícita para desplegar, publicar o aplicar cambios remotos.

**Seguimiento operativo:** issue [PRO-160](https://linear.app/proyecto-raices/issue/PRO-160/raices-admin-de-contenidos-e0-validada-e1-en-planificacion).

---

### Fecha: 2026-10-15 — Seguimiento Admin E1, rediseño y calendario

**Estado:** E1 implementada; migración v5 aplicada y verificada en producción según el registro operativo. La issue [PRO-160](https://linear.app/proyecto-raices/issue/PRO-160/raices-admin-de-contenidos-e0-validada-e1-en-planificacion) continúa In Progress.

**Dirección visual:** existe una preview privada de Claude Design con 15 pantallas: https://claude.ai/artifact/FcUCMgXa7z3dQzMNKBa5Hn. Se pausó el refinamiento por límite diario. Retomar desde esa preview, sin reiniciar la exploración. Antes de implementar, validar estados vacíos/carga/error, responsive, accesibilidad, formularios, selector de fotos y guardado.

**Decisiones y límites:**
- Implementar el rediseño sobre `feature/admin`, preservando la lógica existente; validar en Preview.
- No hay autorización implícita para merge a `main`, despliegues, migraciones ni nuevas escrituras en producción.
- Verificar la integración de las fechas de `experiencia_salidas` con el calendario público existente (`calendario.html`). No crear un calendario paralelo; Tours quedan excluidos.
- La opción de seleccionar una experiencia destacada para Home se difiere a otra etapa. El campo `destacada` actual no implica selección de portada.
- Siguen pendientes las escrituras reales de los módulos E1, las pruebas Deno de Edge Functions, la resolución autorizada de la experiencia E0 de prueba en producción y las decisiones D7–D18 que correspondan.

---

### Fecha: 2026-10-14 — Estado del Admin: E0 validada, E1 sin autorizar

**Estado:** E0 del Admin está validada funcionalmente: Inicio con tareas pendientes, editor de Experiencias por pasos y Traducciones ES/EN lado a lado. Admin Auth v4 fue aplicada en producción y verificada.

**Referencia de código:** repositorio [proyecto-raices](https://github.com/sknnnnn/proyecto-raices), rama `feature/admin`, commit `d26219a` (`docs(admin): estado de E0 y próximos pasos (E1 sin autorizar)`). La especificación funcional vigente está en `docs/admin/especificacion-funcional.md`, §9.

**Próxima fase propuesta — E1:** investigar y planificar la gestión de destinos, actividades, fechas de salida, equipo, contacto y contenido del sitio, galerías y paquetes. E1 está pendiente de investigación y planificación; **no está autorizada para implementar ni para aplicar migraciones remotas**. Antes de considerar la migración de permisos v5, probarla en PostgreSQL 17 local con verificador de seguridad y reversión comprobada. No desplegar ni modificar datos de producción sin autorización.

**Decisión de proceso:** postergar la revisión visual integral hasta completar las funcionalidades. La experiencia de prueba que permanece en producción solo se eliminará con autorización explícita.


> Las entradas del 2026-09-07 al 2026-10-05 se migraron desde Linear el 2026-10-07 (doc "Roadmap — MACARIO STUDIO + WEB-BASE + RAÍCES", doc "PRO-40 — Contrato técnico maestro de experiencias" y la descripción del proyecto "Rediseño y lanzamiento Web"). Linear conserva los originales como referencia.

### Fecha: 2026-10-07 — Estado del proyecto

**Decisión:** Proyecto Raíces sigue **activo**. Su fase actual es reorganización de código, documentación, arquitectura / modelo de datos y preparación del Admin/CMS. Que el sitio público funcione no significa que el proyecto esté terminado.

### Pendiente de decisión — Destino de `comentarios.html`

**Estado:** ⚠️ requiere decisión de Ignacio.
**Contexto:** `comentarios.html` existe, pero no forma parte del Page System aprobado el 2026-10-05.
**Hipótesis preferida (no decidida):** convertir comentarios / testimonios en contenido contextual dentro de Home, Destino, Experiencia u otras páginas.
**Mientras tanto:** no se elimina; queda como legacy.

### Fecha: 2026-10-05 — System Reset: arquitectura Foundation → Components → Patterns → Pages → Content

**Decisión:** la arquitectura de Raíces se consolida como Foundation → Components → Patterns → Pages → Content, migrando progresivamente la base funcional existente, sin rehacer el proyecto desde cero.
**Razón:** ordenar el sistema visual y de contenido, y preparar un futuro Admin / CMS simple.
**Consecuencias:** principio de preservación de lo funcional ([[07 — Proyectos/Proyecto Raíces/08 — Desarrollo|Desarrollo]] §5); el Admin se construye después de estabilizar el modelo ([[07 — Proyectos/Proyecto Raíces/04 — Arquitectura|Arquitectura]] §6–§7).
**Alternativas descartadas:** rehacer el proyecto desde cero.

### Fecha: 2026-10-05 — Principio "mucha lógica detrás, poca fricción delante" y motion

**Decisión:** Raíces (junto con GXK12:2) adopta "simple por defecto → potente cuando hace falta". El motion se define como orgánico, editorial y cinematográfico. Ver [[07 — Proyectos/Proyecto Raíces/05 — UX-UI|UX-UI]] §7–§8.

### Fecha: 2026-09-30 — Decisiones de contenido previas al rediseño

**Decisión:** quitar el contenido de Covid / mascarilla; no mostrar Choquequirao como "Próximamente" cuando tiene una experiencia cargada; reemplazar las fotos solo a mano y con imágenes reales (las generadas, únicamente como preview). Ver [[07 — Proyectos/Proyecto Raíces/06 — Contenido|Contenido]] §1. (Fuente: PRO-115.)

### Fecha: 2026-09-30 — Hito: revisión de seguridad

Revisión de seguridad realizada, con deuda pendiente documentada. Ver [[07 — Proyectos/Proyecto Raíces/09 — QA|QA]] §4. (Fuente: PRO-153.)

### Fecha: 2026-09-28 — Hito: etapa funcional cerrada (estado histórico)

> Estado vigente (2026-10-07): el proyecto sigue **activo**, en reorganización de código, documentación, arquitectura / modelo de datos y preparación del Admin/CMS. Esta entrada registra el estado del 2026-09-28.

Arquitectura, funcionalidad, datos y QA se dan por cerrados. El proyecto sigue abierto para el cierre de UX/UI y dirección visual, trabajados con referencias dentro de Figma. La etapa funcional ya estaba mergeada a `main`.

> Nota 2026-10-07: el cierre de QA convive con una contradicción abierta sobre Sentry ([[07 — Proyectos/Proyecto Raíces/10 — Deploy y Monitoring|Deploy y Monitoring]] §4).

### Fecha: 2026-09 — CTA principal "Reserva ahora" y retiro de Guías

**Decisión:** el CTA principal vigente es "Reserva ahora", con el código y `PROJECT-CONTEXT.md` sincronizados (PRO-85; commits `6c3fc16` / `9857f89`). `guias.html` y `guias-data.js` se retiraron como legacy (PRO-86). Las fechas exactas no quedaron registradas en las issues.

### Fecha: 2026-09-10 — Salidas programadas como fuente del calendario

**Decisión:** las fechas se modelan como salidas concretas en `experiencia_salidas`, que es la única fuente del Calendario de viajes, y el calendario es solo para Travesías. Ver [[07 — Proyectos/Proyecto Raíces/07 — Datos e Integraciones|Datos e Integraciones]] §1. (Fuente: PRO-42.)
**Alternativas descartadas:** temporadas genéricas; usar `detalle.fechas` como fuente.

### Fecha: 2026-09-10 — Contrato técnico y de presentación de experiencias

**Decisión:** el modelo de experiencias es núcleo común + `detalle` JSONB por tipo + tablas relacionales para imágenes, actividades y paquetes. La ficha pública muestra solo la información esencial por tipo.
**Razón:** la auditoría del esquema mostró que ya cubría casi todo el contrato; no convenía una migración grande.
**Detalle:** [[07 — Proyectos/Proyecto Raíces/07 — Datos e Integraciones|Datos e Integraciones]] §1 y [[07 — Proyectos/Proyecto Raíces/05 — UX-UI|UX-UI]] §6.
**Alternativas descartadas:** convertir todos los atributos de `detalle` en columnas o tablas separadas.

### Fecha: 2026-09-08 — Secuencia de incorporación de herramientas

**Decisión registrada en su momento:** Playwright y Sentry se implementan primero en Raíces y luego se generalizan en Web-Base; Archify se valida primero en Web-Base; PostHog y n8n no se incorporan sin una necesidad concreta; Resend se incorpora cuando los formularios reales estén definidos.
**Estado al 2026-10-07:** Playwright y Resend están en uso; Sentry está integrado pero sin DSN; la generalización a Web-Base ya no aplica: Web-Base quedó congelado como referencia histórica (2026-10-07).

### Fecha: 2026-09-07 — Supabase como fuente central de datos

**Decisión:** migrar el frontend a Supabase como fuente de datos (PRO-44, PRO-47; commit `ed0b829`), con `data-api.js` como única capa de acceso.
**Consecuencias:** los archivos de datos JS planos quedaron obsoletos y se eliminaron el 2026-09-30 (commit `5decc72`).

### Fecha: 2026-09-04 — Separación de Patagonia en 5 destinos navegables reales

**Decisión:** El destino agregado "Patagonia" se reemplaza por 5 destinos concretos: Bariloche, Ushuaia, San Martín de los Andes, Villa Pehuenia y Norte Neuquino.
**Razón:** "Patagonia" agrupaba 19 experiencias reales de lugares distintos bajo un único destino navegable, lo cual era geográficamente impreciso (confirmado por commit `3dbc890` del repositorio).
**Alternativas descartadas:** No registradas.

### Fecha: no registrada — Buenos Aires dejó de ofrecerse como destino

**Decisión:** Buenos Aires se retiró de la lista de destinos ofrecidos.
**Razón:** No registrada explícitamente; confirmado por comentario en el código (`assets/js/destinos-data.js`) que indica que puede reincorporarse en el futuro reutilizando la imagen ya conservada.
**Alternativas descartadas:** No registradas.

### Fecha: 2026-09-04 — Plantilla única para páginas de destino

**Decisión:** Se usa una sola plantilla (`catalogo.html`) para los 12 destinos, en vez de una página HTML por destino, accedida vía `?destino=slug`.
**Razón:** Reutilizar el mismo dataset y lógica de filtros ya existente, evitando duplicar código y manteniendo consistencia (confirmado por commits `6cfd3a2` y `4864db2`).
**Alternativas descartadas:** No registradas.

### Fecha: no registrada — Separación de función entre Experiencias y Destinos

**Decisión:** Experiencias funciona como catálogo principal de descubrimiento y venta de experiencias; Destinos funciona como contenido editorial e informativo, sin duplicar el catálogo.
**Razón:** No registrada explícitamente en el documento original.
**Alternativas descartadas:** No registradas en el documento original.

### Fecha: no registrada — Patagonia no es un destino navegable independiente

**Decisión:** Patagonia se usa como referencia geográfica, categoría o agrupación conceptual, pero la navegación debe llevar a destinos concretos (ej. Bariloche, El Chaltén, Ushuaia).
**Razón:** No registrada explícitamente en el documento original.
**Alternativas descartadas:** No registradas.

---

## Hitos

### Fecha: 2026-09-04 — Carga de contenido real de las 11 Travesías

Se reemplazó el placeholder de ejemplo por las 11 Travesías reales del catálogo (Perú y Patagonia), con ficha técnica uniforme (distancia, dificultad, alojamiento, fechas) y CTA unificado a WhatsApp (commits del repositorio).

### Fecha: 2026-09-04 — Unificación de CTA de detalle a un solo botón por experiencia

Los detalles de Tours y Travesías pasan a tener un único botón de contacto directo a WhatsApp, eliminando botones duplicados ("Consultar disponibilidad", "Solicitar información").

### Fecha: no registrada — Eliminación de duplicación de catálogo

Se eliminó la duplicación de catálogo entre Experiencias y Destinos. Destinos quedó orientado hacia contenido editorial/informativo, con posibilidad de enlazar experiencias desde ahí.

### Fecha: no registrada — Las experiencias pueden enlazarse desde Destinos

Las experiencias pueden enlazarse desde Destinos (registrado como consolidado en el documento original).

---

## Documentos relacionados

- [[07 — Proyectos/Proyecto Raíces/00 — Índice]]


---

## Hito: 2026-10-26 — Nueva orientación estratégica de Proyecto Raíces

**Decisión confirmada por el usuario:** la propuesta comercial de Raíces pasa a priorizar paquetes de viaje. Tours y travesías permanecen en la oferta. Además, Raíces busca ofrecer a guías locales un servicio de visibilidad de sus destinos y propuestas, con perfiles propios y experiencias asociadas.

**Consecuencia:** revisar la arquitectura histórica del sitio y elaborar una nueva dirección visual de mayor calidad, coordinada con este modelo. La identidad y la dirección visual existentes son base de trabajo, no se reemplazan automáticamente.

**Pendiente:** aprobar el mapa de navegación, definir el alcance funcional de los perfiles de guía, comprobar el modelo de datos actual y decidir el modelo económico del servicio a guías. No se ha decidido suscripción, comisión ni mecanismo de cobro.

**Alcance de este hito:** registra la orientación de negocio. No implica cambios en código, base de datos, despliegue, ni aprobación de pantallas o de una nueva Biblia. El detalle arquitectónico y el brief UX/UI se registran en las notas [[07 — Proyectos/Proyecto Raíces/04 — Arquitectura]] y [[07 — Proyectos/Proyecto Raíces/05 — UX-UI]].

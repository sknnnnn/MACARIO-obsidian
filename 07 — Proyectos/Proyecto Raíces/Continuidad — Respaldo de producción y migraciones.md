---
tipo: proyecto
proyecto: Proyecto Raíces
estado: pausa preventiva
actualizado: 2026-11-03
---

# Continuidad — respaldo de producción y migraciones

## Estado al 03/11/2026

- **Estado del proyecto:** pausado por decisión del usuario. Esta nota conserva la continuidad técnica; no autoriza ejecutar tareas.
- **Respaldo real de producción:** pendiente.
- **Prueba simulada local:** completada con resultado TODO OK; no demuestra restauración real de Supabase Auth ni Storage.
- **Migraciones v6–v11:** Linear registra que fueron ejecutadas el 2026-10-22. No volver a ejecutar SQL. La validación funcional posterior es una tarea separada.
- **Decisión:** no avanzar con funcionalidades, arreglos, migraciones, cambios de datos ni despliegues hasta nueva indicación.
- **Próximo punto técnico cuando se reactive:** PRO-172, preflight de solo lectura desde la PC personal, seguido por respaldo real y prueba de restauración aislada.
- **No modificar BitLocker, permisos ni políticas de la PC laboral.** No desinstalar PostgreSQL local antes de completar el respaldo y la restauración reales.

## Documentación técnica vigente

- [[07 — Proyectos/Inventario cero — Raíces + GXK12.2 — 2026-10-19]] — clasificación transversal y candidatos de limpieza.

- [Procedimiento de respaldo manual de Supabase](https://github.com/sknnnnn/proyecto-raices/blob/claude/proyecto-raices-visual-language-q04g3y/docs/operacion/respaldo-manual-supabase.md)
- [Cierre técnico de producción — 19/10/2026](https://github.com/sknnnnn/proyecto-raices/blob/claude/proyecto-raices-visual-language-q04g3y/docs/operacion/cierre-tecnico-produccion-2026-10-19.md)
- [Linear PRO-172 — Respaldar producción y probar restauración antes de migraciones v6–v11](https://linear.app/proyecto-raices/issue/PRO-172/raices-respaldar-produccion-y-probar-restauracion-aislada)

## Próxima secuencia cuando se reactive

Esta secuencia es documental; **no se ejecuta durante la pausa**.

1. **PRO-172 — preflight, respaldo real y restauración aislada.** Desde la PC personal, verificar herramientas y destino seguro sin conectar/exportar datos hasta revisar el preflight. Luego realizar respaldo real de base de datos, Auth, metadatos y archivos de Storage; verificar hashes/integridad y probar restauración aislada. La simulación previa no sustituye este proceso.
2. **PRO-165 — calendario y salidas.** Validar con evidencia funcional la fuente única experiencia_salidas, calendario público y semántica de estados. No crear un calendario paralelo.
3. **PRO-166 — carga real de imágenes.** La v10 figura como ejecutada; queda pendiente una prueba real de subida desde Admin, en entorno autorizado.
4. **PRO-162 / PRO-163 — migraciones y escrituras E1.** Las v6/v7 figuran como ejecutadas; no repetir SQL. Reconciliar efectos y ejecutar el protocolo de escrituras reales con datos descartables solo con autorización expresa y prerequisitos satisfechos.

El orden es secuencial. Si el respaldo/restauración falla, detenerse antes de avanzar. PRO-165/166/162/163 no se ejecutan antes de que el usuario reactive el proyecto y se cumplan sus autorizaciones específicas.

## Límites y decisiones

- La prueba simulada ya realizada no debe repetirse sin una razón concreta.
- No aplicar v6–v11 antes de completar el respaldo real, validar la restauración y recibir autorización explícita.
- No guardar contraseñas, claves de servicio ni otros secretos en esta nota.
- Esta nota registra continuidad y decisiones; el procedimiento técnico completo vive en el repositorio de Proyecto Raíces y el seguimiento operativo en Linear.

## Pendientes heredados de la nota de continuidad anterior — revalidar antes de ejecutar

La nota 13 contenía detalles que no deben perderse, pero sus conteos de imágenes quedaron obsoletos. Se preservan aquí como pendientes históricos sujetos a verificación, no como inventario vigente:

- Revalidar si siguen pendientes dos reexportaciones manuales de imágenes.
- Reconciliar los dos grupos de referencias duplicadas mencionados en el registro anterior con la auditoría actual de coincidencias por nombre; no asumir que son los mismos grupos.
- Confirmar si sigue pendiente elegir una sola experiencia destacada de Cusco.
- Revalidar las decisiones D3/D9, D14 y el modelo de experiencias internas de paquetes contra Linear y la documentación más reciente.
- No reutilizar los conteos antiguos de 19 experiencias publicadas sin imagen principal y 26 sin galería: la auditoría posterior registró 12 publicadas sin imagen y 13 sin galería. Antes de cualquier acción, volver a consultar el inventario actual.

La lista anterior se mantiene para trazabilidad; cualquier resolución debe registrarse en Linear y el detalle técnico en el repositorio de Proyecto Raíces.
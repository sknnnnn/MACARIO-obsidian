---
tipo: proyecto
proyecto: Proyecto Raíces
estado: pausa preventiva
actualizado: 2026-10-19
---

# Continuidad — respaldo de producción y migraciones

## Estado al 19/10/2026

- **Respaldo real de producción:** pendiente.
- **Prueba simulada local:** completada con resultado `TODO OK`. Validó el procedimiento sobre una copia simulada, pero no prueba la restauración real de Supabase Auth ni de los archivos de Storage.
- **Migraciones v6–v11:** pendientes; no se aplicaron en producción.
- **Decisión:** pausar hasta retomar desde la PC personal. No modificar BitLocker, políticas ni permisos de la PC laboral.
- **PostgreSQL local:** no desinstalarlo hasta completar y verificar el respaldo real y la prueba de restauración.

## Documentación técnica vigente

- [Procedimiento de respaldo manual de Supabase](https://github.com/sknnnnn/proyecto-raices/blob/claude/proyecto-raices-visual-language-q04g3y/docs/operacion/respaldo-manual-supabase.md)
- [Cierre técnico de producción — 19/10/2026](https://github.com/sknnnnn/proyecto-raices/blob/claude/proyecto-raices-visual-language-q04g3y/docs/operacion/cierre-tecnico-produccion-2026-10-19.md)
- [Linear PRO-172 — Respaldar producción y probar restauración antes de migraciones v6–v11](https://linear.app/proyecto-raices/issue/PRO-172/raices-respaldar-produccion-y-probar-restauracion-antes-de-migraciones)

## Próxima secuencia de trabajo

1. Desde la PC personal, definir un destino seguro y una segunda copia en un medio separado.
2. Seguir el procedimiento documentado para generar respaldos reales de esquema/datos, Auth, metadatos de Storage e inventarios.
3. Descargar y verificar los archivos reales de Storage; el último inventario registrado tenía 17 archivos en `envios-fotos`, con 5.573.691 bytes. Confirmar nuevamente antes de aceptar el respaldo.
4. Verificar hashes, inventarios y consistencia de integridad antes/después.
5. Probar la restauración en una instancia local aislada; nunca restaurar sobre producción.
6. Confirmar todos los criterios de aceptación y que existan dos copias protegidas.
7. Revisar v6–v11 y solicitar autorización explícita antes de aplicar cualquier migración en producción.

Si falla cualquier comprobación, detenerse y resolverla antes de avanzar.

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
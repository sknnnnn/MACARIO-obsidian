---
tipo: cierre-tecnico
proyecto: Proyecto Raíces
fecha: 2026-10-09
estado: verificado-parcialmente
---

# Proyecto Raíces — Cierre técnico de Supabase y deploys

## Resultado confirmado

### Supabase
- Se aplicó en producción desde SQL Editor la migración `supabase/pendiente/20261009_endurecimiento.sql`.
- Verificación SQL posterior: **25 controles, 0 fallidos**; 3 filas informativas.
- Se endurecieron permisos `TRUNCATE`, políticas RLS de imágenes/actividades, inserción en Storage `envios-fotos`, esquema privado y RPCs de control de envíos/notificación.
- Las Edge Functions `contact-form` y `submit-photos` están activas en versión 4 con `verify_jwt=true`.
- Los logs revisados mostraron `POST 200` para ambas funciones y la cabecera `CF-Connecting-IP`. El usuario confirmó que los formularios funcionan.
- No se observaron errores relevantes en los logs revisados. Esto no constituye monitoreo continuo ni prueba independiente de entrega en bandeja de entrada.
- Los PR [#33](https://github.com/sknnnnn/proyecto-raices/pull/33) y [#34](https://github.com/sknnnnn/proyecto-raices/pull/34) documentan el resultado en el repo de Raíces.

### Cloudflare Pages
- El usuario confirmó que en el panel de Cloudflare ve deploys de **Preview** y **Producción**.
- La documentación operativa quedó en [`docs/operacion/despliegues-cloudflare.md`](https://github.com/sknnnnn/proyecto-raices/blob/main/docs/operacion/despliegues-cloudflare.md), PR [#35](https://github.com/sknnnnn/proyecto-raices/pull/35), mergeado en `main`.
- **No se verificaron directamente** los SHA, ramas de origen ni estados exactos de build de los deploys de Preview y Producción. No afirmar que ambos apuntan al mismo commit.
- No se hicieron cambios de configuración ni redeploys en Cloudflare como parte de este cierre.

## Deuda y seguimiento

- La migración está registrada dentro de `supabase/pendiente/` por decisión de trazabilidad; no volver a ejecutarla en producción para sincronizar documentación.
- Quedan hallazgos no bloqueantes de performance de Supabase documentados en `supabase/README.md`: tres FKs sin índice, tabla técnica sin PK y tres índices reportados como no usados. Revisarlos en una tarea separada con métricas, sin cambios preventivos.
- La revisión exacta de SHA de Preview/Producción queda opcional/pendiente. Hacerla sólo cuando sea necesario; no modificar el entorno productivo sólo para completar la auditoría.
- Sentry sigue siendo una deuda separada ya registrada en Linear (`PRO-52`); no confundirla con el cierre de formularios/Supabase.

## Fuentes de verdad

- Código y notas técnicas del proyecto: `sknnnnn/proyecto-raices`.
- Estado de producción de Supabase: [`supabase/README.md`](https://github.com/sknnnnn/proyecto-raices/blob/main/supabase/README.md).
- SQL aplicado: [`20261009_endurecimiento.sql`](https://github.com/sknnnnn/proyecto-raices/blob/main/supabase/pendiente/20261009_endurecimiento.sql).
- Deploys: [`docs/operacion/despliegues-cloudflare.md`](https://github.com/sknnnnn/proyecto-raices/blob/main/docs/operacion/despliegues-cloudflare.md).
- Trabajo operativo y seguimiento: Linear, proyecto **Rediseño y lanzamiento Web**, issues `PRO-153` y `PRO-88`.

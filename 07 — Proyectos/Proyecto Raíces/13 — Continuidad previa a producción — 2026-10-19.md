# Continuidad — Proyecto Raíces — 2026-10-19

> Estado: **pausado hasta la próxima sesión**. No ejecutar cambios de producción hasta retomar y confirmar el respaldo.

## Fuente técnica de verdad

- [Cierre técnico previo a producción (detalle completo)](https://github.com/sknnnnn/proyecto-raices/blob/claude/proyecto-raices-visual-language-q04g3y/docs/operacion/cierre-tecnico-produccion-2026-10-19.md)
- [Continuidad y próximos pasos](https://github.com/sknnnnn/proyecto-raices/blob/claude/proyecto-raices-visual-language-q04g3y/docs/operacion/continuidad-cierre-tecnico-2026-10-19.md)

El documento del repositorio contiene hashes, verificaciones SQL, riesgos de cada migración, evidencia de imágenes, registros de prueba y decisiones pendientes. Esta nota solo resume el estado y el orden para retomar, para evitar duplicar información técnica.

## Estado al cerrar la sesión

- Migraciones v6–v11 preparadas y verificadas por hashes; **ninguna aplicada en producción**.
- La producción solo se consultó en modo lectura; no hubo cambios de datos, borrados, deploy ni merge a `main`.
- No está confirmado que exista un backup restaurable. **No autorizar ni aplicar migraciones hasta verificarlo.**
- La carga de imágenes del Admin está implementada y probada localmente; depende de v10 y falta comprobar Storage real.
- Se optimizaron 100 imágenes; siguen pendientes dos reexportaciones manuales y la decisión sobre dos grupos de referencias duplicadas.
- No agregar imágenes provisorias: hay 19 experiencias publicadas sin imagen principal, 26 sin galería y faltan textos alternativos.
- Cusco tiene dos experiencias destacadas publicadas; hay que decidir cuál conservar.
- Quedaron decisiones abiertas D3/D9, D14 y el modelo de experiencias internas de paquetes.
- Linear: PRO-160 y PRO-166 recibieron comentarios con evidencia; no se cerraron issues.
- Se preparó documentación de continuidad en el repositorio de Proyecto Raíces. Esta nota enlaza a esa fuente técnica.

## Próxima sesión — orden acordado

1. Abrir Supabase → Database → Backups y verificar la fecha/hora de la última copia o si PITR está habilitado. Considerar Storage por separado: el backup de base no incluye los archivos de Storage.
2. Revisar el plan técnico y su §3.5. Si no hay recuperación viable confirmada, resolver ese bloqueo antes de migrar.
3. Con respaldo confirmado, autorizar explícitamente un tramo de migraciones y ejecutarlas **una por una**, con hash y verificadores antes/después. No ejecutar v6–v11 como un único bloque.
4. Tras v10 y con autorización específica, probar una subida real desde el Admin.
5. Después resolver por separado la sincronización de notas, decisiones de contenido, duplicados y limpieza autorizada de borradores.
6. Deploy y merge a `main` requieren autorización independiente.

## Límites vigentes

No aplicar migraciones remotas, modificar datos de producción, borrar archivos/registros, desplegar ni hacer merge a `main` mientras el trabajo permanezca pausado.
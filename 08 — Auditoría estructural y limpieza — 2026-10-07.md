# Auditoría estructural y limpieza de Obsidian — 2026-10-07

> ⚠️ **AUDITORÍA HISTÓRICA — superada.** Esta nota registra una auditoría intermedia del 2026-10-07 y se conserva como registro. **No describe el estado vigente:**
> - **Raíces:** la descripción "funcionalmente terminado, con iteración visual" quedó superada. Estado vigente: **activo**, en reorganización de código, documentación, arquitectura / modelo de datos y preparación del Admin/CMS (ver [[07 — Proyectos/Proyecto Raíces/00 — Índice|Proyecto Raíces — Índice]]).
> - **Bresstore:** "pendiente de cierre" quedó superado. Estado vigente: pendiente, de menor prioridad.
> - **Wikilinks:** el conteo y el estado de los links de esta auditoría quedaron superados por la limpieza posterior (0 links rotos). Los links con forma corta que usó esta auditoría no resolvían con los archivos de doble extensión `.md.md`.
> - El estado vigente se toma de la documentación actual, empezando por [[00 — Arquitectura - MACARIO — Arquitectura general.md|MACARIO — Arquitectura general]] §10.

> Registro de la auditoría estructural realizada después de la reparación puntual de wikilinks.
>
> Objetivo: ordenar la bóveda según el estado real de MACARIO sin borrar decisiones históricas válidas ni convertir Obsidian en un espejo de Linear.

## Resultado

### 1. Estructura actual

La bóveda queda organizada en:

- documentos maestros de MACARIO en la raíz;
- documentación específica de proyectos en `07 — Proyectos`;
- documentación específica de PRANA en `PRANA`;
- `_Plantilla` como plantilla de proyecto.

La estructura es funcional y no requiere una reorganización física mayor en este momento.

### 2. Limpieza realizada

- Se eliminaron referencias de proyectos que ya no representan trabajo activo en la arquitectura general de MACARIO.
- Se dejó **GXK12:2** como proyecto activo principal.
- **Proyecto Raíces** queda como proyecto funcionalmente terminado con iteración visual/ajustes puntuales.
- **Bresstore** queda como proyecto real pendiente de cierre.
- **Web-Base** queda explícitamente clasificado como Foundation histórica/fundacional congelada, no como línea de desarrollo independiente.
- **CONCRETO**, `tienda-ropa-demo` y **Onda** quedan fuera del conjunto de proyectos activos de MACARIO.
- Se eliminó el archivo raíz vacío y duplicado `MACARIO — Principios y decisiones.md`.
- Se alineó la lista de proyectos de ITS con el ecosistema vigente.

### 3. Qué NO se hizo

No se eliminaron documentos históricos completos solamente por estar viejos.

Tampoco se trasladaron documentos a una carpeta Archive todavía: antes de archivar físicamente conviene completar la auditoría de contenido y confirmar qué documentación sigue siendo útil como referencia histórica.

No se modificaron decisiones de producto de GXK ni de Raíces.

### 4. Wikilinks

La reparación anterior corrigió un conjunto concreto de enlaces rotos.

**Pendiente:** realizar una extracción y resolución exhaustiva de todos los `[[...]]` de la bóveda para distinguir:

1. enlaces válidos;
2. enlaces a documentos renombrados;
3. enlaces históricos/obsoletos;
4. referencias a documentos que realmente faltan.

No se declara todavía que la bóveda tenga cero enlaces rotos.

### 5. Próxima fase

La siguiente revisión debe concentrarse en **contenido redundante/obsoleto**, especialmente:

- contradicciones entre documentos maestros y estado actual;
- duplicación de decisiones entre documentos;
- documentos que deberían pasar a histórico;
- referencias antiguas a herramientas/proyectos;
- coherencia entre índices y documentos reales.

La regla es conservar conocimiento útil y eliminar ruido, no borrar historia por antigüedad.

## Fuente de verdad

- **Obsidian:** conocimiento, contexto y decisiones.
- **Linear:** trabajo operativo.
- **GitHub:** código e historial técnico.

Esta auditoría no reemplaza esas fuentes ni convierte Obsidian en un registro operativo.

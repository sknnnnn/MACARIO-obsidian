# Portfolio Ignacio Sconza — Relevamiento de fuentes

Fecha: 2026-11-05. Relevamiento **de solo lectura**: no se modificaron archivos de Figma, repositorios de proyecto, documentación ni datos.

## 1. Fuentes consultadas

| Fuente | Proyecto | Acceso | Qué se obtuvo |
|---|---|---|---|
| Vault MACARIO (Obsidian, este repo) | Ambos | ✅ | Brief, arquitectura, UX/UI, decisiones, estado, metodología, Brand Bible de GXK, dirección visual |
| `sknnnnn/GxK12-2` (rama `master`, `30a1054`) | GXK12:2 | ✅ | Stack (Next.js 16, React 19, TypeScript, Supabase), estructura `src/`, servicios de GXK Core, adaptadores de envío, assets de Home |
| `sknnnnn/proyecto-raices` (rama `main`, `5bf33f9`) | Raíces | ✅ | Stack (HTML/CSS/JS vanilla, Supabase, i18n, Playwright), estructura de `assets/js`, CLAUDE.md, PROJECT-CONTEXT |
| Figma `PRANA STUDIOS` → página «GXK12.2 — Etapa 1 — Diseños aprobados» | GXK12:2 | ✅ (MCP) | 10 capturas de pantallas aprobadas + índice + sistema de superficies |
| Figma `PRANA STUDIOS` → página «Proyecto Raices» | Raíces | ✅ (MCP) | Visual DNA, biblioteca de referencias, 6 direcciones exploratorias de Home |
| Sitio `proyectoraices.com.ar` | Raíces | ❌ bloqueado por la política de red del entorno | Reemplazado por 4 capturas desktop aportadas por Ignacio |
| Supabase (datos de Raíces) | Raíces | ❌ bloqueado por la política de red | No necesario tras recibir las capturas |
| Ejecución local de GXK (Next.js) | GXK12:2 | ❌ instalación de dependencias denegada por permisos | No hay captura de la Home implementada de GXK; se usó el asset G & K del repo |
| Linear | Ambos | No consultado | La documentación de Obsidian ya enlaza y resume el estado de Linear |

## 2. Clasificación del material usado

| Recurso | Proyecto | Fuente | Categoría | Estado | Uso en el PDF |
|---|---|---|---|---|---|
| `fig-indice-etapa1` | GXK | Figma 764:8801 | Documentación y decisiones | Aprobado | Contexto (material visual) |
| `fig-superficies` | GXK | Figma 764:8872 | Componentes y sistemas visuales | Aprobado | Conceptualización |
| `fig-carrito-confirmacion` | GXK | Figma 764:753 | UX y flujos | Aprobado (diseño) | Decisiones UX |
| `fig-tienda-desktop` | GXK | Figma 764:380 | Diseño de interfaces | Aprobado (diseño) | Interfaces |
| `fig-pdp-desktop` / `fig-pdp-mobile` | GXK | Figma 764:573 / 764:643 | Diseño de interfaces | Aprobado (diseño) | Interfaces |
| `fig-checkout-pago` / `fig-checkout-mobile` | GXK | Figma 764:842 / 764:862 | Diseño de interfaces | Aprobado (diseño) | Interfaces |
| `fig-admin-inicio` | GXK | Figma 764:4007 | Diseño de interfaces | Aprobado (diseño) · datos de ejemplo | Interfaces |
| `gk-ilustracion` | GXK | Repo `public/home/` | Identidad visual | Implementado (asset de Home) | Apertura del caso |
| `fig-visual-dna` | Raíces | Figma 88:29 | Identidad visual / exploración | Exploratorio | Proceso de diseño |
| `fig-exploracion-periodico` | Raíces | Figma 85:12537 | Exploraciones y prototipos | Exploratorio, no aprobado | Proceso de diseño |
| `web-home-hero`, `web-home-experiencias`, `web-experiencias`, `web-ficha` | Raíces | Capturas de Ignacio del sitio público | Desarrollo e implementación | Implementado | Apertura, arquitectura, UX/UI |

Todas las capturas de GXK muestran fotos **marcadoras**: el sistema se diseñó antes de la producción fotográfica. Se aclara en los epígrafes.

## 3. Información confirmada vs. no disponible

**Confirmado y usado:** stacks y estructura de ambos repos; decisiones de arquitectura, UX/UI y datos documentadas; estado al 2026-11-03/05; formación, herramientas, idiomas y contacto (del brief).

**No disponible / no usado:** métricas, usuarios, ventas o resultados comerciales (ninguno de los dos productos tiene métricas publicables; GXK no está lanzado); fechas de inicio exactas de los proyectos; fechas y estado de finalización de la formación; institución de la formación en Branding; material de 3D, audiovisual o experimentos de IA propios (el Laboratorio deja espacios reservados, rotulados como tales).

## 4. Contradicciones registradas (no resueltas por suposición)

1. **Propiedad de los proyectos.** El brief los describe como «proyectos propios». La documentación indica que GXK tiene un dueño distinto («beta presentable al dueño de GxK») y que Raíces tiene un contacto de negocio propio con stakeholder «pendiente de definir». El PDF presenta tu **rol** (integral) sin afirmar propiedad de las marcas. **Conviene que confirmes cómo querés describir la relación** (cliente, socio, proyecto personal).
2. **Estado del diseño de GXK.** Obsidian (2026-11-03) dice que el diseño integral A–Z está pendiente; la página de Figma más reciente dice «Etapa 1 · cerrada». Se usó Figma como fuente para el diseño y se describe como «Etapa 1», no como diseño integral terminado.
3. **Paleta del portfolio.** `06 — ITS` registra `#9E1F32 / #FED3A8 / #1B5956` como dirección candidata no aprobada. El brief la propone ahora como punto de partida; se usó.
4. **Destinos de Raíces.** El conteo de 12 destinos provenía de un archivo eliminado al migrar a Supabase; no se citó ningún número.
5. **Home de GXK.** El índice de Figma la cita como «producción: master 30a1054», pero el brief indica que no hay web pública: no se incluyó ninguna URL.

## 5. Transparencia sobre el uso de IA

La documentación de MACARIO establece que Ignacio define y aprueba producto, alcance, arquitectura y diseño, y que el código se implementa con agentes de IA (Claude Code). El PDF lo dice explícitamente en el caso GXK y en el Laboratorio: es un dato verificable y, bien contado, una fortaleza del perfil.

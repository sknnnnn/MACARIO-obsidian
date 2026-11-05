# Portfolio Ignacio Sconza — Producción

Entregables:

- `Portfolio_Ignacio_Sconza_ES.pdf` — 23 páginas, A4 apaisado.
- `Portfolio_Ignacio_Sconza_EN.pdf` — misma estructura, adaptación editorial al inglés.
- `RELEVAMIENTO.md` — fuentes, clasificación del material, faltantes y contradicciones.

## Sistema de identidad

| Elemento | Definición |
|---|---|
| Paleta principal | Granate `#9E1F32` (firma, acento) · Petróleo `#1B5956` (sistema, tecnología) · Arena `#FFE7CE` (paneles) · Durazno `#FED3A8` (resaltados sobre oscuro) |
| Neutros | Papel `#FFF5EA` (fondo) · Tinta `#1B1517` · Texto secundario `#5B4B47` (≈8:1 sobre papel) |
| Tipografías | Familjen Grotesk (titulares y texto) · Instrument Serif itálica (acento editorial) · JetBrains Mono (etiquetas, datos, sistema) — todas OFL, Google Fonts |
| Retícula | 12 columnas, márgenes laterales de 14 mm, cabecera con firma · sección · folio |
| Recursos gráficos | Nodos y conexiones (cover, ecosistema, metodología), coordenadas mono, numerales en contorno, etiquetas de estado (aprobado · implementado · en rama · pendiente · exploración) |
| Iconografía | 7 glifos lineales propios (SVG, trazo 1,5) para las áreas de trabajo |
| Imágenes | Capturas en proporción natural, sin recortes ni deformación; cada una con epígrafe de fuente y estado |

## Regenerar

Requiere Python 3 y Node con Playwright (Chromium).

```bash
cd portfolio/source
python3 build.py      # genera portfolio_es.html y portfolio_en.html
node render.js        # exporta ambos PDF a portfolio/
node qa.js es         # control automático: desbordes, imágenes rotas, enlaces
node qa.js en
```

Todo el texto vive en `source/build.py` como `t("español", "english")`, así las dos versiones comparten estructura y diagramación. Estilos en `source/styles.css`; tipografías locales en `source/fonts/`; imágenes en `source/img/`.

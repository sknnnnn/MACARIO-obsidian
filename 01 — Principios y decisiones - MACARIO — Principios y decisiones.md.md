# MACARIO — Principios y decisiones

> Documento maestro de principios.  
> Registra las reglas que orientan las decisiones de MACARIO y evita volver a discutir desde cero decisiones ya tomadas.

---

## 1. Propósito

MACARIO debe permitir construir proyectos digitales de forma:

- profesional;
    
- consistente;
    
- reutilizable;
    
- eficiente;
    
- visualmente cuidada;
    
- técnicamente sólida;
    
- documentada;
    
- y sostenible a medida que aumenta la cantidad de proyectos.
    

Los principios de este documento funcionan como criterios de decisión cuando aparece una nueva herramienta, proyecto, feature, proceso o problema.

---

# 2. Principios fundamentales

## 2.1 Primero el resultado, después la herramienta

No se incorpora una herramienta porque sea nueva, popular o técnicamente interesante.

Primero se define:

> ¿Qué problema necesitamos resolver?

Después:

> ¿Qué herramienta lo resuelve mejor?

Una herramienta sin una necesidad clara agrega complejidad.

---

## 2.2 Cada herramienta tiene una responsabilidad

No debemos convertir una herramienta en una copia de otra.

> **Modelo vigente (2026-10-07).** Detalle en [[00 — Arquitectura - MACARIO — Arquitectura general.md|MACARIO — Arquitectura general]] §5.

### Obsidian — Memory / Context

**Conocimiento permanente:** contexto, decisiones, principios, metodología, arquitectura.

### Linear — Operations / Work

**Trabajo operativo:** tareas, bugs, mejoras, prioridades, estados, seguimiento.

### GitHub — Implementation / Code

**Código e historial técnico.**

### Figma — Visual Source

**Fuente de verdad visual:** referencias, assets, reglas visuales y diseños aprobados.

### Claude Design — Creative Engine

**Exploración, composición, prototipado e iteración visual** antes de la aprobación. No reemplaza a Figma: lo aprobado se consolida en Figma.

### Claude Code — Implementation Engine

**Implementación del diseño aprobado, desarrollo, integración, correcciones y mantenimiento.**

### Preview / QA

**Validación del producto real.**

### Cowork — Audit / Coordination / Cross-tool Operations

**Auditoría transversal, coordinación entre herramientas, detección de inconsistencias, informes y ejecución de tareas transversales delegadas.** No reemplaza ninguna herramienta.

### Herramientas auxiliares

ChatGPT, Gemini y Grok pueden usarse cuando corresponda, pero **no forman parte de las capas fundamentales** y no deben convertirse en dependencias estructurales del sistema.

### WEB-BASE (histórico)

> Web-Base está **congelado como referencia histórica / fundacional** (decisión 2026-10-07). Los principios de esta nota que lo nombran describen cómo se lo construyó; su aprendizaje útil quedó absorbido por MACARIO.

**Foundation — base técnica reutilizable para websites y web apps, dentro de Product Development.** No es la única Foundation posible: MACARIO puede tener otras (Mobile-Base a futuro, otras según necesidad).

### MACARIO OS

**Orquestación.**

Cuando dos herramientas empiezan a hacer exactamente lo mismo, primero se revisa la arquitectura antes de agregar más automatización.

---

## 2.3 Una fuente de verdad por tipo de información

Evitar que la misma información viva en cinco lugares diferentes.

Ejemplo:

```
Decisión
→ Obsidian

Tarea
→ Linear

Código
→ GitHub

Error de producción
→ Sentry

Métrica de producto
→ PostHog
```

Las otras herramientas pueden enlazar esa información, pero no deberían duplicarla innecesariamente.

---

# 3. Principio de no duplicación

La documentación permanente no debe convertirse en un espejo de Linear.

Linear puede contener:

- tareas;
    
- subtareas;
    
- estados;
    
- prioridades;
    
- comentarios operativos;
    
- seguimiento;
    
- trabajo pendiente.
    

Obsidian debe contener:

- contexto;
    
- decisiones;
    
- arquitectura;
    
- metodología;
    
- aprendizajes;
    
- documentación estable.
    

Cuando una tarea de Linear genera conocimiento reutilizable, ese conocimiento puede convertirse en documentación de Obsidian.

### Reglas confirmadas (2026-10-07)

- Decisiones permanentes, principios, metodología, arquitectura y conocimiento estable → **Obsidian**.
- Estado, tareas, bugs, mejoras, prioridades y seguimiento → **Linear**.
- Linear puede enlazar a Obsidian, pero no debe convertirse en una segunda wiki.
- **No se migra Linear entero a Obsidian:** solo el conocimiento durable, dejando enlaces a Linear o GitHub cuando sean la referencia operativa correcta.
- Los planes históricos y las issues cerradas no se convierten en decisiones vigentes al migrarlos.

```
Linear
  ↓
trabajo
  ↓
aprendizaje
  ↓
Obsidian
  ↓
si es reutilizable
  ↓
WEB-BASE
```

---

# 4. Los proyectos son independientes

Cada proyecto debe poder:

- tener su propio repositorio;
    
- tener su propia identidad;
    
- tener sus propios datos;
    
- tener sus propios clientes;
    
- tener sus propias decisiones;
    
- evolucionar independientemente.
    

WEB-BASE no debe almacenar proyectos reales dentro de su repositorio.

MACARIO OS no debe acoplar técnicamente todos los proyectos entre sí.

La conexión debe producirse mediante metodología, herramientas y referencias.

---

# 5. WEB-BASE debe ser reutilizable (principio histórico)

> Web-Base está congelado (2026-10-07). Este principio se conserva como criterio para cualquier base técnica futura y como registro de cómo se construyó Web-Base.

WEB-BASE es una Foundation dentro de Product Development, no MACARIO completo. No debe absorber responsabilidades de Research, Visual/Assets, UX/UI o gestión que pertenecen a MACARIO en general.

WEB-BASE no debe construirse alrededor de un único proyecto.

No debe asumir:

- Proyecto Raíces;
    
- GXK;
    
- CONCRETO;
    
- ITS;
    
- ni ningún futuro cliente.
    

Cuando una necesidad aparece en varios proyectos y se demuestra que es reutilizable, puede convertirse en:

- regla;
    
- template;
    
- checklist;
    
- skill;
    
- command;
    
- quality gate;
    
- documentación.
    

No se agrega metodología solamente porque una vez pareció útil.

---

# 6. No sobreingeniería

Una de las reglas principales de MACARIO:

> **La complejidad debe estar justificada por un problema real.**

Antes de agregar:

- una dependencia;
    
- un plugin;
    
- una automatización;
    
- una integración;
    
- un servicio externo;
    
- una abstracción;
    
- un command;
    
- un skill;
    

preguntar:

1. ¿Qué problema resuelve?
    
2. ¿Con qué frecuencia aparece?
    
3. ¿Cuánto trabajo ahorra?
    
4. ¿Qué complejidad introduce?
    
5. ¿Podemos resolverlo de forma más simple?
    
6. ¿La solución puede reutilizarse?
    

Si el beneficio no justifica la complejidad, no se agrega.

---

# 7. La metodología evoluciona desde proyectos reales

WEB-BASE no debe intentar anticipar todos los problemas posibles.

Los proyectos reales funcionan como laboratorio.

```
Proyecto real
      ↓
problema
      ↓
solución
      ↓
validación
      ↓
¿es reutilizable?
   ↙          ↘
 NO            SÍ
 ↓              ↓
proyecto       WEB-BASE
```

Esto evita convertir WEB-BASE en una metodología teórica y excesivamente grande.

---

# 8. Calidad antes de velocidad

La velocidad es importante, pero no debe conseguirse sacrificando:

- funcionalidad;
    
- accesibilidad;
    
- responsive;
    
- seguridad;
    
- mantenibilidad;
    
- claridad;
    
- experiencia del usuario.
    

Un proyecto rápido que necesita rehacerse no es realmente rápido.

---

# 9. Visual antes de cerrar

El criterio visual no debe evaluarse solamente mirando código.

Cuando una modificación afecta significativamente la interfaz:

1. implementar;
    
2. generar preview/Artifact cuando sea posible;
    
3. revisar visualmente;
    
4. corregir;
    
5. volver a revisar;
    
6. recién después cerrar la tarea.
    

La revisión visual humana de Ignacio tiene prioridad sobre cualquier validación automática.

---

# 10. No inventar contenido

Nunca inventar:

- información comercial;
    
- características de productos;
    
- precios;
    
- servicios;
    
- testimonios;
    
- destinos;
    
- actividades;
    
- datos de clientes;
    
- claims;
    
- información institucional.
    

Si falta información:

```
falta información
      ↓
documentar el faltante
      ↓
preguntar / solicitar
      ↓
continuar
```

Un placeholder explícito es preferible a información falsa.

---

# 11. Decisiones reversibles vs. irreversibles

No todas las decisiones necesitan el mismo nivel de aprobación.

### Decisiones reversibles

Ejemplos:

- estructura interna de un componente;
    
- naming local;
    
- pequeños ajustes visuales;
    
- refactors internos.
    

Pueden resolverse durante la implementación si respetan las decisiones existentes.

### Decisiones importantes

Ejemplos:

- arquitectura general;
    
- cambio de stack;
    
- nueva dependencia importante;
    
- identidad visual;
    
- alcance comercial;
    
- cambios destructivos;
    
- migraciones de datos;
    
- cambios de infraestructura.
    

Deben proponerse antes de ejecutarse cuando puedan cambiar significativamente el proyecto.

---

# 12. Aprobaciones

### Claude puede ejecutar

- investigación;
    
- análisis;
    
- auditorías;
    
- reportes;
    
- QA;
    
- implementación de cambios ya aprobados;
    
- refactors internos;
    
- correcciones técnicas acotadas.
    

### Claude propone y Ignacio aprueba

- cambios importantes de alcance;
    
- arquitectura relevante;
    
- identidad visual;
    
- nuevas dependencias importantes;
    
- cambios destructivos;
    
- decisiones comerciales.
    

### Siempre requiere aprobación de Ignacio

- commit final;
    
- push;
    
- merge;
    
- deploy;
    
- decisiones comerciales;
    
- publicación definitiva.
    

---

# 13. Git es parte de la calidad

Nunca asumir que el estado local es correcto.

Antes de modificar un repositorio:

1. verificar rama;
    
2. verificar estado;
    
3. verificar cambios existentes;
    
4. verificar estado remoto cuando corresponda;
    
5. identificar PRs relevantes;
    
6. evitar sobrescribir trabajo existente.
    

Durante desarrollo:

- los cambios esperados pueden permanecer sin commit;
    
- se debe distinguir trabajo esperado de cambios accidentales.
    

Al cerrar:

- no debe haber cambios accidentales;
    
- el estado debe ser explícito;
    
- el commit/push/merge se realiza siguiendo la autorización definida.
    

---

# 14. Seguridad primero

Nunca exponer:

- API keys;
    
- tokens;
    
- contraseñas;
    
- secretos;
    
- credenciales;
    
- información privada del cliente.
    

Nunca colocar secretos en:

- repositorios públicos;
    
- código frontend;
    
- commits;
    
- documentación pública;
    
- screenshots;
    
- logs.
    

Las variables sensibles deben manejarse mediante los mecanismos apropiados del servicio utilizado.

### Visibilidad de repositorios

> **Private by default. Public only by explicit decision.** (2026-10-07)

Todo repositorio de MACARIO es privado por defecto, aunque no contenga secretos: la documentación, el historial y la estrategia también son información sensible. La documentación interna de MACARIO no se mantiene publicada como si fuera contenido público. Un repositorio se abre solo por decisión explícita, después de revisar qué documentación, código, historial y estrategia quedan expuestos.

---

# 15. Integraciones opt-in

Las herramientas externas no deben agregarse automáticamente a todos los proyectos.

Ejemplos:

### Playwright

Se incorpora cuando el proyecto necesita QA/E2E automatizado.

### Sentry

Se incorpora cuando el proyecto necesita monitoreo de errores en producción.

### PostHog

Se incorpora cuando existe una necesidad real de analítica/product analytics.

### Resend

Se incorpora cuando existe una necesidad real de email transaccional.

### n8n

Se incorpora cuando existe una automatización suficientemente repetible.

### Supabase

Se incorpora cuando realmente se necesita backend, base de datos, autenticación, storage u otras capacidades.

### Cloudflare

Se utiliza como infraestructura/deploy cuando corresponde al proyecto.

La regla general es:

> **Opt-in, no default.**

**Figma** tiene un rol propio: es la fuente visual de verdad (Visual Source) **cuando un proyecto tiene una definición visual que deba preservarse, explorarse, aprobarse o implementarse de forma sistemática** (sistema visual, diseño aprobado, referencias, assets o dirección visual relevante). En ese caso, lo aprobado —incluido lo explorado en Claude Design— se consolida en Figma. Los proyectos y cambios simples no necesitan crearse ni pasar por Figma.

---

# 16. Claude Code y tokens

Claude Code debe trabajar eficientemente.

Las instrucciones generales son:

- minimizar el scope;
    
- evitar análisis innecesarios;
    
- evitar verificaciones redundantes;
    
- no hacer cambios no solicitados;
    
- reutilizar información existente;
    
- no crear archivos porque "podrían ser útiles";
    
- advertir antes de tareas especialmente costosas;
    
- priorizar la solución más simple que cumpla el objetivo.
    

No modificar:

- `CLAUDE.md`;
    
- documentación de contexto;
    
- reglas globales;
    
- metodología;
    

salvo que sea parte explícita de la tarea o resulte estrictamente necesario.

Cuando sea posible, entregar:

- Artifact;
    
- preview;
    
- render;
    
- o resultado navegable
    

para revisión visual.

---

# 17. Proyectos reales alimentan ITS y PRANA

ITS es la identidad personal de Ignacio: autoría, criterio, proceso, experimentación y portfolio. PRANA es una marca / proyecto / negocio separado que se está evaluando; no reemplaza a MACARIO ESTUDIO (ver [[00 — Arquitectura - MACARIO — Arquitectura general.md|Arquitectura general]] §2). ITS y PRANA son superficies separadas.

> ⚠️ **Decisión abierta:** la superficie pública de los casos de MACARIO ESTUDIO. Mientras tanto: no asumir que PRANA es el canal público definitivo del estudio, y no mantener documentación interna de MACARIO publicada como si fuera contenido público.

Por eso los proyectos reales pueden convertirse en:

- casos de estudio;
    
- evidencia de capacidad;
    
- referencias visuales;
    
- resultados;
    
- aprendizajes;
    
- piezas de captación.
    

Pero no todo proyecto tiene que aparecer en ITS ni en el portfolio público de PRANA. La documentación interna puede contener proyectos en distintos estados; el portfolio público de PRANA muestra solamente proyectos suficientemente preparados. Ver [[PRANA — Estrategia]].

La decisión depende de:

- calidad;
    
- relevancia;
    
- autorización;
    
- valor comercial;
    
- estado de finalización.
    

---

# 18. Decisiones registradas

Las decisiones importantes deben quedar documentadas.

Formato recomendado:

```
Decisión
Fecha
Contexto
Alternativas consideradas
Decisión tomada
Motivo
Consecuencias
Estado
```

Esto evita volver a discutir una decisión sin recordar por qué fue tomada.

---

# 19. Principio de cierre

Un proyecto no está terminado simplemente porque "funciona".

Debe cumplir:

- alcance acordado;
    
- QA;
    
- auditoría;
    
- revisión visual;
    
- responsive;
    
- ausencia de problemas críticos;
    
- documentación;
    
- estado de Git claro;
    
- deploy validado cuando corresponda;
    
- tareas importantes cerradas.
    

El cierre debe ser explícito.

---

# 20. Regla de oro

> **Construir menos cosas, pero mejor conectadas, documentadas y reutilizables.**

MACARIO debe crecer por calidad y aprendizaje, no por cantidad de herramientas, archivos o automatizaciones.

---

## Decisiones pendientes

Estas decisiones quedan abiertas hasta que exista una necesidad concreta:

- canal formal de aprobación con clientes;
    
- participación del cliente en cada etapa;
    
- Playwright como estándar u opcional;
    
- paquete estándar de Sentry / PostHog / Resend / n8n;
    
- convención definitiva de nombres de repositorios;
    
- alcance futuro de MACARIO OS.
    

- superficie pública del trabajo de MACARIO ESTUDIO (ver §17);
    
- si el concepto de *Foundation* se mantiene para bases técnicas futuras.
    

Estas decisiones deben resolverse cuando aporten valor real, no por adelantado.

### Decisiones resueltas

- **2026-10-07 — Figma obligatorio u opcional:** Figma es la fuente visual de verdad cuando existe una definición visual que preservar, explorar, aprobar o implementar sistemáticamente; los proyectos y cambios simples no necesitan pasar por Figma (§15).
- **2026-10-07 — Fuente de verdad Obsidian vs Linear:** ver §3, "Reglas confirmadas".
- **2026-10-07 — Jerarquía de identidad:** MACARIO ESTUDIO / PRANA / ITS, ver Arquitectura general §2.
- **2026-10-07 — Web-Base:** histórico / fundacional / congelado; MACARIO absorbió sus aprendizajes útiles. No se elimina el repositorio ni su documentación.
- **2026-10-07 — Repositorios:** *private by default, public only by explicit decision* (ver §14).


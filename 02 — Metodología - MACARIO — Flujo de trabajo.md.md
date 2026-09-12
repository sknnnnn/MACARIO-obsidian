# MACARIO — Flujo de trabajo

> Define cómo MACARIO transforma una necesidad inicial en un proyecto terminado, documentado y reutilizable.

---

## 1. Flujo general

```
IDEA / NECESIDAD
      ↓
01 — INTAKE
      ↓
02 — CONTEXTO
      ↓
03 — DISCOVERY
      ↓
04 — SCOPE
      ↓
05 — ARQUITECTURA
      ↓
06 — DIRECCIÓN VISUAL
      ↓
07 — IMPLEMENTACIÓN
      ↓
08 — QA
      ↓
09 — AUDITORÍA
      ↓
10 — DEPLOY
      ↓
11 — DOCUMENTACIÓN
      ↓
12 — CIERRE
```

Las etapas no siempre son estrictamente lineales.

Puede existir iteración:

```
Discovery ↔ Scope
Architecture ↔ Implementation
Implementation ↔ QA
Visual ↔ Implementation
```

Pero **Audit → Deploy → Documentation → Close** funciona como tramo final.

---

# 2. Sistema de herramientas

Cada etapa utiliza las herramientas necesarias, no todas por defecto.

|Etapa|Herramientas principales|
|---|---|
|Intake|Linear + Obsidian|
|Contexto|Obsidian + Linear|
|Discovery|Obsidian + GitHub + Figma cuando corresponda|
|Scope|Linear + Obsidian|
|Arquitectura|Obsidian + GitHub|
|Dirección visual|Figma + Obsidian + Artifact/preview|
|Implementación|Claude Code + GitHub|
|QA|Claude Code + Playwright cuando corresponda|
|Auditoría|Claude Code + revisión humana|
|Deploy|GitHub + Cloudflare u otra infraestructura|
|Documentación|Obsidian|
|Cierre|Linear + Obsidian + GitHub|

MACARIO OS coordina estas relaciones.

---

# 3. Linear vs Obsidian

## Linear

Linear representa el trabajo.

Ejemplo:

```
PRO-34
Definir contenido editorial de Destinos
```

Contiene:

- estado;
    
- prioridad;
    
- responsable;
    
- dependencias;
    
- subtareas;
    
- seguimiento;
    
- bloqueos.
    

## Obsidian

Obsidian representa el conocimiento.

Ejemplo:

```
Proyecto Raíces — Contexto
```

Contiene:

- contexto del negocio;
    
- decisiones;
    
- estructura;
    
- aprendizajes;
    
- referencias;
    
- criterios permanentes.
    

### Regla

> Si mañana necesitamos volver a entender algo, probablemente pertenece en Obsidian.

> Si necesitamos hacer algo, probablemente pertenece en Linear.

---

# 4. GitHub

GitHub representa la implementación real.

Cada proyecto debería tener:

- repositorio;
    
- rama principal;
    
- ramas de trabajo cuando corresponda;
    
- commits;
    
- Pull Requests;
    
- historial.
    

Antes de modificar un repositorio:

1. comprobar estado;
    
2. comprobar rama;
    
3. comprobar cambios locales;
    
4. comprobar estado remoto;
    
5. comprobar PRs relevantes;
    
6. identificar posibles conflictos.
    

Nunca asumir que el estado local está actualizado.

---

# 5. Intake

El objetivo es transformar una petición informal en una necesidad entendible.

### Entrada

Puede ser cualquier cosa:

- mensaje;
    
- reunión;
    
- idea;
    
- problema;
    
- referencia;
    
- pedido de cliente.
    

### Salida

Un Intake documentado con:

- qué se pidió;
    
- quién lo pidió;
    
- por qué;
    
- objetivo;
    
- urgencia;
    
- información faltante;
    
- preguntas abiertas.
    

No se debe convertir automáticamente una petición informal en alcance definitivo.

---

# 6. Contexto

Antes de construir hay que entender el contexto.

Preguntas principales:

- ¿Qué es el proyecto?
    
- ¿Quién lo necesita?
    
- ¿Para quién?
    
- ¿Qué problema resuelve?
    
- ¿Cuál es el objetivo?
    
- ¿Qué existe actualmente?
    
- ¿Qué restricciones existen?
    
- ¿Qué información está confirmada?
    
- ¿Qué información falta?
    

### Regla

> Nunca rellenar información faltante inventando.

---

# 7. Discovery

Discovery reúne información suficiente para tomar decisiones.

Puede incluir:

- referencias visuales;
    
- competidores;
    
- sitios similares;
    
- contenido existente;
    
- estructura actual;
    
- assets;
    
- tecnología existente;
    
- restricciones;
    
- necesidades del usuario;
    
- problemas detectados.
    

El objetivo no es investigar infinitamente.

El objetivo es llegar al punto donde las decisiones puedan tomarse con fundamento.

---

# 8. Scope

Scope define:

### Qué entra

Lo que efectivamente se construirá.

### Qué no entra

Lo que queda fuera del proyecto actual.

### Qué queda pendiente

Información o decisiones necesarias para avanzar.

Cada elemento importante debería poder verificarse posteriormente.

Ejemplo:

```
[ ] Hero
[ ] Navegación
[ ] Catálogo
[ ] Formulario
[ ] Responsive
[ ] SEO básico
```

---

# 9. Arquitectura

La arquitectura traduce el alcance en una solución técnica.

Debe definir, según corresponda:

- estructura de proyecto;
    
- páginas;
    
- componentes;
    
- datos;
    
- tecnologías;
    
- integraciones;
    
- backend;
    
- almacenamiento;
    
- despliegue.
    

No se debe agregar arquitectura por anticipación.

La arquitectura debe responder al alcance real.

---

# 10. Dirección visual

Antes de implementar una identidad visual importante debe quedar suficientemente clara.

Puede incluir:

- referencias;
    
- tono;
    
- paleta;
    
- tipografía;
    
- fotografía;
    
- composición;
    
- interacción;
    
- espaciado;
    
- tratamiento de contenido.
    

No hace falta Figma obligatoriamente.

Si un proyecto puede resolverse con una dirección visual clara y un Artifact/preview, eso puede ser suficiente.

### Regla

> La herramienta de diseño es secundaria; la claridad de la dirección visual es lo importante.

---

# 11. Implementación

La implementación transforma las decisiones aprobadas en código.

Principios:

- cambios acotados;
    
- reutilización;
    
- accesibilidad;
    
- responsive;
    
- código mantenible;
    
- no agregar dependencias innecesarias;
    
- no modificar archivos fuera del scope.
    

Claude Code puede implementar cambios aprobados.

Si aparece una decisión importante no contemplada:

```
problema
   ↓
detener decisión
   ↓
proponer alternativas
   ↓
aprobar
   ↓
continuar
```

No improvisar arquitectura importante durante la implementación.

---

# 12. QA

QA verifica que el proyecto funciona como fue definido.

### Funcional

- navegación;
    
- botones;
    
- formularios;
    
- filtros;
    
- estados;
    
- enlaces;
    
- interacciones.
    

### Responsive

- desktop;
    
- tablet;
    
- mobile.
    

### Accesibilidad

- contraste;
    
- foco;
    
- navegación por teclado;
    
- labels;
    
- semántica;
    
- estados interactivos.
    

### Técnico

- consola;
    
- errores;
    
- assets;
    
- rutas;
    
- performance obvia;
    
- integraciones.
    

### Automatización

Playwright puede utilizarse cuando el proyecto justifique E2E o regresión automatizada.

No es obligatorio para todos los proyectos.

---

# 13. Auditoría

La auditoría es una revisión independiente de la implementación.

Debe comprobar:

- alcance;
    
- UX;
    
- UI;
    
- responsive;
    
- accesibilidad;
    
- contenido;
    
- SEO;
    
- performance;
    
- seguridad;
    
- código;
    
- Git;
    
- deploy.
    

La auditoría debe distinguir:

### Bloqueante

Debe resolverse antes del cierre.

### Importante

Debe resolverse o quedar explícitamente aceptado.

### Mejora

Puede quedar como trabajo futuro.

---

# 14. Deploy

Deploy significa publicar una versión que pasó los gates anteriores.

Antes del deploy:

- QA aprobado;
    
- auditoría aprobada;
    
- revisión visual aprobada;
    
- errores críticos resueltos.
    

Después:

- comprobar producción;
    
- comprobar rutas;
    
- comprobar assets;
    
- comprobar formularios;
    
- comprobar comportamiento principal.
    

La versión publicada debe representar la versión revisada.

---

# 15. Documentación

Una vez terminado el proyecto, se registra el conocimiento permanente.

No se copia el historial completo de Linear.

Se documenta:

- qué se construyó;
    
- por qué;
    
- decisiones importantes;
    
- arquitectura final;
    
- herramientas;
    
- integraciones;
    
- problemas relevantes;
    
- aprendizajes;
    
- enlaces;
    
- estado final.
    

La documentación vive principalmente en Obsidian.

---

# 16. Cierre

Un proyecto está cerrado cuando:

- el alcance fue completado;
    
- QA está aprobado;
    
- auditoría está aprobada;
    
- revisión visual está aprobada;
    
- deploy está validado cuando corresponde;
    
- documentación está actualizada;
    
- Git está en estado conocido;
    
- no existen tareas críticas abiertas.
    

Linear puede utilizarse para registrar el cierre operativo.

Obsidian conserva el conocimiento.

GitHub conserva la implementación.

---

# 17. Quality gates

Cada etapa debe producir una condición verificable.

```
INTAKE
↓
¿Entendemos el pedido?

CONTEXTO
↓
¿Entendemos el negocio/problema?

DISCOVERY
↓
¿Tenemos suficiente información?

SCOPE
↓
¿Sabemos qué entra y qué no?

ARQUITECTURA
↓
¿Sabemos cómo construirlo?

VISUAL
↓
¿Sabemos cómo debe verse?

IMPLEMENTACIÓN
↓
¿Existe una versión funcional?

QA
↓
¿Funciona correctamente?

AUDITORÍA
↓
¿Está listo para publicar?

DEPLOY
↓
¿La producción funciona?

DOCUMENTACIÓN
↓
¿El conocimiento quedó guardado?

CIERRE
↓
¿El proyecto está realmente terminado?
```

---

# 18. Flujo de aprobación

### Claude puede avanzar solo

Cuando la decisión ya está tomada y documentada.

Ejemplos:

- implementar un componente aprobado;
    
- corregir un bug;
    
- ejecutar una auditoría;
    
- generar un reporte;
    
- ejecutar QA;
    
- hacer refactors internos.
    

### Claude debe consultar

Cuando aparece:

- cambio importante de scope;
    
- nueva arquitectura;
    
- nueva dependencia significativa;
    
- cambio de identidad;
    
- migración destructiva;
    
- decisión comercial.
    

### Ignacio aprueba siempre

- commit final;
    
- push;
    
- merge;
    
- deploy;
    
- decisiones comerciales;
    
- publicación definitiva.
    

---

# 19. Flujo de revisión visual

Cuando el trabajo tiene impacto visual:

```
IMPLEMENTAR
    ↓
ARTIFACT / PREVIEW
    ↓
REVISIÓN HUMANA
    ↓
¿APROBADO?
   ↙       ↘
 NO         SÍ
 ↓           ↓
CORREGIR   CONTINUAR
             ↓
             QA
```

La revisión visual humana tiene prioridad sobre la percepción del agente.

---

# 20. Aprendizaje posterior al proyecto

Después de cerrar un proyecto:

1. identificar problemas repetidos;
    
2. identificar soluciones reutilizables;
    
3. documentarlas en Obsidian;
    
4. decidir si alguna debe entrar en WEB-BASE;
    
5. actualizar la metodología solamente si existe evidencia suficiente.
    

No toda experiencia se convierte en una nueva regla.

---

# 21. Evolución de MACARIO

El sistema debe evolucionar así:

```
PROYECTOS REALES
       ↓
experiencia
       ↓
aprendizaje
       ↓
Obsidian
       ↓
patrones repetibles
       ↓
WEB-BASE
       ↓
mejor ejecución
       ↓
mejores proyectos
```

MACARIO OS aparece por encima de este ciclo para coordinarlo.

---

# 22. Regla de eficiencia

Antes de comenzar una tarea:

1. verificar qué ya existe;
    
2. reutilizar lo existente;
    
3. trabajar solamente sobre el scope necesario;
    
4. evitar cambios colaterales;
    
5. evitar documentación duplicada;
    
6. evitar nuevas herramientas sin necesidad.
    

El objetivo no es hacer más.

El objetivo es **resolver mejor con menos fricción**.

---

# 23. Estado del flujo

Este documento describe el flujo general de MACARIO.

WEB-BASE contiene la implementación concreta de la metodología.

Cuando WEB-BASE cambie, este documento debe revisarse para mantener alineados:

- principios;
    
- metodología;
    
- herramientas;
    
- proyectos;
    
- MACARIO OS.
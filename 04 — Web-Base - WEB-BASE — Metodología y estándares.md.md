# WEB-BASE — Metodología y estándares

> WEB-BASE es una Foundation de MACARIO, dentro de Product Development: la base técnica reutilizable desde la que nace cada proyecto de website o web app, e implementa el ciclo general de MACARIO para diseñarlo, construirlo, validarlo y cerrarlo.

---

# 1. Qué es WEB-BASE

**WEB-BASE es una Foundation de MACARIO: la base técnica reutilizable para websites y web apps, dentro del área de Product Development.**

Su función es convertir una necesidad o idea en un proyecto digital terminado mediante un proceso repetible, verificable y adaptable. El ciclo general (las etapas y sus criterios) se define a nivel MACARIO en [[MACARIO — Flujo de trabajo]]; WEB-BASE es el punto de partida técnico reutilizable que lo implementa, con mayor granularidad, para websites y web apps.

WEB-BASE no es:

- una agencia;
    
- un framework;
    
- un stack tecnológico;
    
- un CMS;
    
- un repositorio de proyectos;
    
- una aplicación independiente;
    
- ni MACARIO completo.
    

Es la **Foundation: la base técnica reutilizable de MACARIO para websites y web apps** — una entre varias posibles (Mobile-Base a futuro, otras según necesidad). WEB-BASE no reemplaza ni absorbe las áreas de Research, Visual/Assets o UX/UI de MACARIO: sus etapas de Context, Discovery y Visual Direction son la aplicación técnica y acotada de esas áreas dentro de un proyecto de Web-Base, no la definición general de esas áreas a nivel MACARIO.

## 1.1 Cuándo se usa

WEB-BASE entra en juego en el momento en que una idea ya pasó (o está pasando, si el proyecto es simple) por Research general de MACARIO y se decide que el producto a construir es un website o una web app. A partir de ahí, WEB-BASE es el punto de partida técnico: no se usa para research puro, para decisiones de negocio, ni para gestionar el proyecto una vez cerrado (eso pertenece a Analytics/Operations, fuera de su alcance actual).

## 1.2 Qué recibe y qué entrega

|WEB-BASE|Detalle|
|---|---|
|**Recibe**|una necesidad o idea con contexto suficiente para iniciar Intake (ver [[MACARIO — Flujo de trabajo]] §3), y la decisión de que se materializa como website o web app|
|**Entrega**|un proyecto propio (repositorio independiente, base técnica implementada, documentación de cierre) que atravesó las doce etapas hasta Close, listo para pasar a Analytics/Operations|

## 1.3 Relación con un proyecto concreto

WEB-BASE no es el proyecto: es el punto de partida que el proyecto usa una sola vez, al nacer. Una vez creado el repositorio del proyecto (ver §18, modelo de distribución), ese proyecto sigue su propia vida — su propio contexto, decisiones e identidad — sin quedar acoplado técnicamente a WEB-BASE. Mejoras futuras a WEB-BASE no se propagan automáticamente a proyectos ya creados.

---

# 2. Objetivo

WEB-BASE busca que cada proyecto:

- empiece con contexto suficiente;
    
- tenga un alcance claro;
    
- tome decisiones conscientes;
    
- mantenga una estructura técnica razonable;
    
- tenga una dirección visual definida;
    
- pase por QA;
    
- sea auditado;
    
- sea revisado visualmente;
    
- se documente;
    
- y pueda cerrarse formalmente.
    

El objetivo no es agregar pasos por burocracia.

El objetivo es reducir:

- retrabajo;
    
- decisiones improvisadas;
    
- pérdida de contexto;
    
- errores repetidos;
    
- cambios de alcance no controlados;
    
- dependencia excesiva de conversaciones;
    
- y proyectos difíciles de mantener.
    

---

# 3. Las 12 etapas

WEB-BASE traduce el ciclo general de MACARIO ([[MACARIO — Flujo de trabajo]]) en doce etapas específicas para websites y web apps:

|Ciclo general MACARIO|Etapas WEB-BASE|
|---|---|
|Idea|—|
|Research|Intake, Context, Discovery|
|Product Definition|Scope|
|Visual|Visual Direction|
|UX / UI|(parte de Visual Direction y Architecture)|
|Technical Architecture|Architecture|
|Development|Implementation|
|QA|QA, Audit|
|Release|Deploy|
|Analytics / Operations|(fuera del alcance actual de WEB-BASE; ver [[MACARIO OS — Arquitectura y roadmap]])|
|Iteration|Documentation, Close alimentan la siguiente Idea|

Las doce etapas:

```
01 Intake
02 Context
03 Discovery
04 Scope
05 Architecture
06 Visual Direction
07 Implementation
08 QA
09 Audit
10 Deploy
11 Documentation
12 Close
```

---

## 01 — Intake

### Objetivo

Capturar la necesidad inicial sin convertirla todavía en una solución.

### Entrada

Puede ser:

- mensaje;
    
- reunión;
    
- idea;
    
- pedido de cliente;
    
- problema detectado;
    
- mejora propuesta.
    

### Salida

Un pedido suficientemente claro para comenzar Context.

Debe identificar:

- qué se pide;
    
- quién lo pide;
    
- objetivo;
    
- urgencia;
    
- información faltante;
    
- preguntas abiertas.
    

### Gate

> ¿Entendemos qué se está pidiendo?

---

# 4. 02 — Context

### Objetivo

Entender el contexto del proyecto.

Debe documentar, cuando corresponda:

- negocio;
    
- usuario;
    
- objetivo;
    
- problema;
    
- situación actual;
    
- restricciones;
    
- contenido disponible;
    
- información faltante.
    

### Regla

**No inventar información faltante.**

Si algo no está confirmado:

```
NO CONFIRMADO
```

y se registra como pendiente.

### Gate

> ¿Entendemos suficientemente el contexto para investigar y tomar decisiones?

---

# 5. 03 — Discovery

### Objetivo

Investigar y reunir información relevante.

Puede incluir:

- referencias;
    
- competidores;
    
- productos similares;
    
- contenido existente;
    
- assets;
    
- repositorio actual;
    
- tecnologías;
    
- restricciones;
    
- necesidades de usuario;
    
- problemas existentes.
    

Discovery debe ser suficiente, no infinito.

### Gate

> ¿Tenemos información suficiente para definir una solución?

---

# 6. 04 — Scope

### Objetivo

Definir exactamente qué se construye.

Debe establecer:

### Incluido

Qué forma parte del proyecto.

### Excluido

Qué explícitamente no forma parte.

### Pendiente

Qué requiere información o decisión adicional.

Cada elemento importante debe ser verificable posteriormente.

### Gate

> ¿Podemos describir el resultado esperado sin ambigüedad importante?

---

# 7. 05 — Architecture

### Objetivo

Traducir el scope a una solución técnica.

Puede definir:

- estructura de archivos;
    
- páginas;
    
- componentes;
    
- datos;
    
- frontend;
    
- backend;
    
- APIs;
    
- integraciones;
    
- almacenamiento;
    
- infraestructura;
    
- deploy.
    

La arquitectura debe ser proporcional al proyecto.

### Principio

> No construir infraestructura para problemas que todavía no existen.

### Gate

> ¿Sabemos cómo implementar el alcance sin introducir complejidad injustificada?

---

# 8. 06 — Visual Direction

### Objetivo

Definir cómo debe verse y sentirse el proyecto.

Puede incluir:

- referencias;
    
- identidad;
    
- color;
    
- tipografía;
    
- fotografía;
    
- composición;
    
- layout;
    
- espaciado;
    
- interacción;
    
- tono.
    

Puede utilizar:

- Figma;
    
- referencias externas;
    
- prototipos;
    
- Artifact;
    
- previews;
    
- exploraciones directas en código.
    

Figma no es obligatorio.

### Gate

> ¿La dirección visual está suficientemente clara para implementar y revisar?

---

# 9. 07 — Implementation

### Objetivo

Construir el proyecto según las decisiones aprobadas.

Principios:

- scope controlado;
    
- cambios pequeños;
    
- reutilización;
    
- accesibilidad;
    
- responsive;
    
- mantenibilidad;
    
- no introducir dependencias innecesarias.
    

Claude Code puede participar en esta etapa.

Debe respetar:

- el contexto;
    
- el scope;
    
- la arquitectura;
    
- la dirección visual;
    
- las reglas del proyecto;
    
- y los principios MACARIO.
    

### Regla

Si durante implementación aparece una decisión arquitectónica importante:

```
problema
↓
detener
↓
proponer alternativas
↓
aprobar
↓
continuar
```

No improvisar decisiones importantes.

---

# 10. 08 — QA

### Objetivo

Verificar que la implementación funciona.

QA cubre:

## Funcional

- navegación;
    
- botones;
    
- formularios;
    
- filtros;
    
- interacciones;
    
- estados;
    
- enlaces.
    

## Responsive

- desktop;
    
- tablet;
    
- mobile.
    

## Accesibilidad

- contraste;
    
- foco;
    
- teclado;
    
- labels;
    
- semántica;
    
- estados interactivos.
    

## Técnico

- consola;
    
- errores;
    
- assets;
    
- rutas;
    
- integraciones;
    
- performance obvia.
    

## Automatización

Playwright puede utilizarse cuando el proyecto lo justifique.

### Gate

> ¿El producto funciona correctamente dentro del scope definido?

---

# 11. 09 — Audit

### Objetivo

Realizar una revisión integral antes del cierre.

La auditoría debe revisar:

- producto;
    
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
    

Los hallazgos se clasifican:

### BLOCKER

Impide cerrar o publicar.

### IMPORTANT

Debe resolverse o aceptarse explícitamente.

### IMPROVEMENT

Puede quedar como evolución futura.

### Gate

> ¿Existe algún problema que impida considerar el proyecto terminado?

---

# 12. 10 — Deploy

### Objetivo

Publicar una versión validada.

Antes del deploy:

- QA aprobado;
    
- audit aprobado;
    
- revisión visual aprobada;
    
- blockers resueltos.
    

Después:

- comprobar producción;
    
- rutas;
    
- assets;
    
- formularios;
    
- comportamiento principal;
    
- errores evidentes.
    

### Principio

> La versión publicada debe corresponder a la versión revisada.

---

# 13. 11 — Documentation

### Objetivo

Convertir el conocimiento generado por el proyecto en información permanente.

La documentación debe registrar:

- qué se construyó;
    
- decisiones importantes;
    
- arquitectura final;
    
- herramientas utilizadas;
    
- integraciones;
    
- problemas relevantes;
    
- soluciones;
    
- aprendizajes;
    
- enlaces importantes.
    

La documentación permanente vive principalmente en **Obsidian**.

No se copia el historial completo de Linear.

---

# 14. 12 — Close

### Objetivo

Cerrar formalmente el proyecto.

Un proyecto puede cerrarse cuando:

- scope completado;
    
- QA aprobado;
    
- audit aprobado;
    
- revisión visual aprobada;
    
- deploy validado cuando corresponde;
    
- documentación actualizada;
    
- Git en estado conocido;
    
- no existen tareas críticas abiertas.
    

### Resultado

El proyecto pasa de:

```
ACTIVE
```

a:

```
CLOSED
```

El conocimiento importante permanece en Obsidian.

El código permanece en GitHub.

El historial operativo permanece en Linear.

---

# 15. Quality Gates

Los gates son condiciones de avance.

```
INTAKE
↓
entendimiento suficiente

CONTEXT
↓
contexto suficiente

DISCOVERY
↓
información suficiente

SCOPE
↓
alcance definido

ARCHITECTURE
↓
solución técnica definida

VISUAL
↓
dirección visual definida

IMPLEMENTATION
↓
versión funcional

QA
↓
funciona correctamente

AUDIT
↓
sin blockers

DEPLOY
↓
producción validada

DOCUMENTATION
↓
conocimiento registrado

CLOSE
↓
proyecto terminado
```

Un FAIL bloqueante impide avanzar.

---

# 16. Sistema de aprobación

## Claude puede decidir

Cuando la decisión:

- ya está definida;
    
- es reversible;
    
- está dentro del scope;
    
- no cambia arquitectura importante.
    

## Claude propone

Cuando aparece:

- cambio de scope;
    
- arquitectura nueva;
    
- dependencia significativa;
    
- cambio visual importante;
    
- migración;
    
- cambio destructivo.
    

## Ignacio aprueba

Siempre:

- commit final;
    
- push;
    
- merge;
    
- deploy;
    
- decisiones comerciales;
    
- publicación definitiva.
    

---

# 17. Git dentro de WEB-BASE

Git forma parte de la calidad del proyecto.

Durante desarrollo se permiten cambios esperados sin commit.

El quality gate debe detectar:

- archivos inesperados;
    
- cambios accidentales;
    
- modificaciones fuera del scope;
    
- conflictos;
    
- estado remoto inesperado.
    

El requisito de working tree limpio pertenece al **cierre**, no a cada etapa de desarrollo.

Antes de cerrar:

- no deben quedar cambios accidentales;
    
- el estado debe ser conocido;
    
- el historial debe ser coherente.
    

---

# 18. Distribución y `/nuevo-proyecto`

## 18.1 Modelo de distribución

WEB-BASE se distribuye como **GitHub Template repository**. Un proyecto nuevo nace copiando esa plantilla a un repositorio propio, no clonando ni referenciando el repositorio de WEB-BASE:

```
MACARIO
   ↓
GitHub Web-Base Template
   ↓
nuevo repositorio independiente
   ↓
/nuevo-proyecto
   ↓
Proyecto
```

La creación del repositorio (vía "Use this template" de GitHub) es un paso previo y separado de `/nuevo-proyecto`. `/nuevo-proyecto` actúa **después**, ya dentro del repositorio nuevo, y solo prepara técnicamente lo que ya existe — no crea el repositorio.

## 18.2 `/nuevo-proyecto`

WEB-BASE incluye un flujo para preparar técnicamente un proyecto nuevo una vez que su repositorio ya existe.

Su objetivo es:

> **scaffoldear un proyecto nuevo a partir de la Foundation WEB-BASE, dentro de un repositorio ya creado.**

`/nuevo-proyecto` **no**:

- crea repositorios (el repositorio se crea con GitHub Template, ver 18.1);
    
- copia manualmente HTML/CSS/JS/assets (eso ya viene incluido por el Template);
    
- decide identidad del proyecto;
    
- decide alcance del proyecto;
    
- hace commit ni push.
    

Estas decisiones (identidad, alcance, y toda acción de Git que confirme el estado) pertenecen a Intake/Context/Scope (etapas 01-04) y a la autorización de Ignacio, no al scaffolding técnico.

No debe, además:

- convertir Web-Base en contenedor de proyectos;
    
- copiar proyectos reales dentro de Web-Base;
    
- acoplar Web-Base a Raíces;
    
- acoplar Web-Base a Onda;
    
- acoplar Web-Base a GXK;
    
- acoplar Web-Base a ITS.
    

El nuevo proyecto debe existir como repositorio independiente.

WEB-BASE proporciona el método y los recursos reutilizables; la identidad, el alcance y las decisiones de negocio son siempre del proyecto.

---

# 19. Estructura reutilizable

WEB-BASE actualmente contiene conceptualmente:

```
metodologia/
├── README
├── etapas y aprobaciones
├── flujo de nuevo proyecto
├── quality gates
├── integración del ecosistema
├── documentación permanente
└── pendientes

templates/
├── intake
├── contexto
├── discovery
├── alcance
├── arquitectura
├── dirección visual
├── QA
├── auditoría
└── cierre

.claude/
├── skills/metodologia/
└── commands/nuevo-proyecto
```

La implementación real vive en el repositorio **Web-Base**.

Este documento solamente conserva el modelo permanente.

---

# 20. Qué NO debe convertirse en WEB-BASE

No todo aprendizaje debe transformarse en metodología.

No incorporar automáticamente:

- decisiones específicas de clientes;
    
- estilos particulares;
    
- contenido;
    
- hacks de un único proyecto;
    
- integraciones que solo sirvieron una vez;
    
- preferencias personales no generalizables;
    
- soluciones temporales.
    

Antes de incorporar algo:

> ¿Esto resuelve un patrón que probablemente vuelva a aparecer?

Si la respuesta es no, permanece en el proyecto.

---

# 21. Evolución de WEB-BASE

El ciclo de evolución es:

```
PROYECTO REAL
      ↓
problema repetido
      ↓
solución comprobada
      ↓
documentación
      ↓
evaluación
      ↓
¿reutilizable?
   ↙          ↘
 NO            SÍ
 ↓              ↓
proyecto       WEB-BASE
```

Esto mantiene la metodología pequeña y basada en evidencia.

---

# 22. Relación con MACARIO

```
MACARIO
   │
   ├── Principios
   │
   ├── Metodología (ciclo general)
   │      └── cómo trabajamos (ver "MACARIO — Flujo de trabajo")
   │
   ├── Product Development (una de las 6 áreas)
   │      └── WEB-BASE
   │             └── Foundation: base técnica reutilizable para websites/web apps
   │      └── (futuras foundations: Mobile-Base, otras)
   │
   ├── MACARIO OS
   │      └── cómo coordinamos
   │
   └── Proyectos
          └── dónde aplicamos el sistema
```

La presentación externa del trabajo (PRANA, e ITS como expresión personal dentro de PRANA) es una capa distinta, fuera de esta estructura interna.

WEB-BASE no es MACARIO completo.

Es la **Foundation técnica** dentro del área de Product Development de MACARIO: el punto de partida reutilizable para cada proyecto de website o web app. No es la única Foundation posible.

---

# 23. Estado actual

WEB-BASE v1 se encuentra implementado en su repositorio principal.

La versión actual incluye:

- metodología de 12 etapas;
    
- sistema de aprobaciones;
    
- quality gates;
    
- flujo de nuevo proyecto;
    
- templates;
    
- skill metodológica;
    
- command de nuevo proyecto;
    
- documentación base.
    

La implementación fue revisada y fusionada a `main`.

---

# 24. Próxima evolución

La evolución de WEB-BASE queda deliberadamente abierta.

Las próximas mejoras deberían surgir de:

- proyectos reales;
    
- auditorías;
    
- errores repetidos;
    
- necesidades recurrentes;
    
- aprendizajes de clientes;
    
- evolución de MACARIO OS.
    

No agregar funcionalidades solamente para hacer crecer el repositorio.

---

# 25. Regla principal

> **WEB-BASE debe hacer que empezar un proyecto nuevo sea más fácil sin hacer que el sistema sea más pesado.**

La mejor versión de WEB-BASE no es la que tiene más archivos.

Es la que permite producir proyectos mejores con menos fricción.
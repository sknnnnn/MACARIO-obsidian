# WEB-BASE — Metodología y estándares

> WEB-BASE es la metodología reutilizable de MACARIO para diseñar, construir, validar y cerrar proyectos digitales.

---

# 1. Qué es WEB-BASE

**WEB-BASE es el sistema metodológico de MACARIO.**

Su función es convertir una necesidad o idea en un proyecto digital terminado mediante un proceso repetible, verificable y adaptable.

WEB-BASE no es:

- una agencia;
    
- un framework;
    
- un stack tecnológico;
    
- un CMS;
    
- un repositorio de proyectos;
    
- una aplicación independiente.
    

Es una **metodología reutilizable**.

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

WEB-BASE utiliza doce etapas principales:

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

# 18. `/nuevo-proyecto`

WEB-BASE incluye un flujo para preparar nuevos proyectos.

Su objetivo es:

> **scaffoldear un proyecto nuevo utilizando la metodología WEB-BASE.**

No debe:

- convertir Web-Base en contenedor de proyectos;
    
- copiar proyectos reales dentro de Web-Base;
    
- acoplar Web-Base a Raíces;
    
- acoplar Web-Base a Onda;
    
- acoplar Web-Base a GXK;
    
- acoplar Web-Base a ITS.
    

El nuevo proyecto debe existir como repositorio independiente.

WEB-BASE proporciona el método y los recursos reutilizables.

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
   ├── WEB-BASE
   │      └── cómo trabajamos
   │
   ├── MACARIO OS
   │      └── cómo coordinamos
   │
   ├── ITS
   │      └── cómo mostramos el trabajo
   │
   └── Proyectos
          └── dónde aplicamos el sistema
```

WEB-BASE no es MACARIO completo.

Es el **motor metodológico** dentro de MACARIO.

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
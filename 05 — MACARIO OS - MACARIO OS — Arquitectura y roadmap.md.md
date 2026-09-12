# MACARIO OS — Arquitectura y roadmap

> MACARIO OS es la capa de orquestación del ecosistema MACARIO.  
> Coordina herramientas, proyectos, contexto, tareas, aprobaciones y resultados sin reemplazar las herramientas especializadas.

---

# 1. Qué es MACARIO OS

**MACARIO OS es el sistema de coordinación de MACARIO.**

Su función es conectar:

- conocimiento;
    
- tareas;
    
- código;
    
- agentes;
    
- QA;
    
- infraestructura;
    
- documentación;
    
- proyectos;
    
- y decisiones.
    

No es necesario que sea una aplicación desde el primer día.

Inicialmente puede existir como:

- arquitectura;
    
- convenciones;
    
- Integration Registry;
    
- flujos;
    
- documentación;
    
- automatizaciones pequeñas;
    
- conexiones entre herramientas.
    

Con el tiempo puede convertirse en una capa técnica más profunda.

---

# 2. Qué problema resuelve

Cuando el ecosistema crece aparecen problemas:

- demasiadas herramientas;
    
- contexto fragmentado;
    
- información duplicada;
    
- tareas desconectadas del código;
    
- documentación desconectada de los proyectos;
    
- decisiones perdidas en conversaciones;
    
- agentes trabajando con contexto incorrecto;
    
- QA separado de implementación;
    
- dificultad para saber el estado general de varios proyectos.
    

MACARIO OS existe para reducir esa fricción.

---

# 3. Principio fundamental

> **MACARIO OS centraliza la coordinación, no el trabajo.**

No debe convertirse en una aplicación que intente reemplazar:

- Linear;
    
- GitHub;
    
- Obsidian;
    
- Claude Code;
    
- ChatGPT;
    
- Sentry;
    
- PostHog;
    
- Figma;
    
- Supabase;
    
- Cloudflare;
    
- n8n.
    

Cada sistema continúa siendo responsable de su propia información.

MACARIO OS conoce cómo conectarlos.

---

# 4. Arquitectura conceptual

```
                         MACARIO OS
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
      CONTEXTO             EJECUCIÓN          CONTROL
          │                   │                   │
          ▼                   ▼                   ▼
      Obsidian             Claude Code        Linear
                              │                 │
                              ▼                 ▼
                           GitHub          prioridades /
                              │             estados
                              ▼
                           Proyecto
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
         Playwright         Sentry          PostHog
             │                │                │
             └────────────────┼────────────────┘
                              ▼
                         PRODUCCIÓN
                              │
                          Cloudflare
```

---

# 5. Capas de MACARIO OS

## 5.1 Context Layer

Responsabilidad:

- saber qué proyecto está activo;
    
- recuperar contexto relevante;
    
- identificar decisiones existentes;
    
- localizar documentación;
    
- evitar contaminación entre proyectos.
    

Fuente principal:

**Obsidian**

---

## 5.2 Task Layer

Responsabilidad:

- identificar trabajo pendiente;
    
- consultar prioridades;
    
- conocer bloqueos;
    
- relacionar tareas con proyectos.
    

Fuente principal:

**Linear**

---

## 5.3 Code Layer

Responsabilidad:

- localizar repositorios;
    
- conocer ramas;
    
- identificar PRs;
    
- consultar commits;
    
- relacionar tareas con código.
    

Fuente principal:

**GitHub**

---

## 5.4 Agent Layer

Responsabilidad:

- coordinar Claude Code;
    
- utilizar ChatGPT para análisis;
    
- eventualmente coordinar otros agentes/modelos;
    
- asignar el tipo correcto de trabajo al sistema adecuado.
    

Principio:

> Un agente debe recibir solamente el contexto que necesita.

---

## 5.5 Verification Layer

Responsabilidad:

- QA;
    
- auditoría;
    
- screenshots;
    
- tests;
    
- errores;
    
- validaciones.
    

Herramientas posibles:

- Playwright;
    
- Sentry;
    
- checks de GitHub;
    
- validaciones de Claude Code;
    
- revisión humana.
    

---

## 5.6 Infrastructure Layer

Responsabilidad:

- deploy;
    
- infraestructura;
    
- servicios;
    
- dominios;
    
- producción.
    

Herramientas posibles:

- Cloudflare;
    
- Supabase;
    
- otros servicios según proyecto.
    

---

## 5.7 Documentation Layer

Responsabilidad:

- registrar resultados;
    
- conservar decisiones;
    
- documentar aprendizajes;
    
- alimentar WEB-BASE.
    

Fuente principal:

**Obsidian**

---

# 6. Integration Registry

MACARIO OS debe mantener conceptualmente un registro de integraciones.

Ejemplo:

|Sistema|Rol|Entrada|Salida|
|---|---|---|---|
|Obsidian|conocimiento|contexto/documentación|contexto|
|Linear|tareas|necesidades/trabajo|estado/prioridad|
|GitHub|código|cambios|commits/PRs|
|Claude Code|implementación|contexto + tareas|código/reportes|
|ChatGPT|análisis|información|decisiones/análisis|
|Playwright|QA|aplicación|resultados|
|Sentry|errores|producción|eventos|
|PostHog|analítica|usuarios|métricas|
|Resend|email|eventos|emails|
|n8n|automatización|eventos|acciones|
|Supabase|datos|operaciones|datos/API|
|Cloudflare|infraestructura|deploy|producción|
|Figma|diseño|referencias|dirección visual|

El Integration Registry debe convertirse posteriormente en una referencia central para entender el ecosistema.

---

# 7. Flujo principal

El flujo ideal de MACARIO OS:

```
INTENCIÓN HUMANA
       ↓
IDENTIFICAR PROYECTO
       ↓
RECUPERAR CONTEXTO
       ↓
IDENTIFICAR TAREA
       ↓
DETERMINAR ACCIÓN
       ↓
EJECUTAR EN HERRAMIENTA CORRECTA
       ↓
VERIFICAR RESULTADO
       ↓
REGISTRAR RESULTADO
       ↓
ACTUALIZAR CONOCIMIENTO
```

Ejemplo:

```
"Hay que arreglar el formulario de Raíces"
             ↓
Proyecto = Raíces
             ↓
Obsidian → contexto del formulario
             ↓
Linear → buscar tarea correspondiente
             ↓
GitHub → localizar implementación
             ↓
Claude Code → corregir
             ↓
Playwright / QA → verificar
             ↓
Linear → actualizar tarea
             ↓
Obsidian → documentar aprendizaje si es reutilizable
```

---

# 8. Selección de proyecto

Una de las funciones más importantes de MACARIO OS es evitar mezclar contextos.

Ejemplo:

```
Proyecto Raíces
    ↓
solo contexto Raíces

Proyecto Onda
    ↓
solo contexto Onda

Proyecto GXK
    ↓
solo contexto GXK

Web-Base
    ↓
solo metodología

ITS
    ↓
solo portfolio
```

La información global de MACARIO puede compartirse.

La información específica de cada proyecto no debe mezclarse accidentalmente.

---

# 9. Context Hygiene

Antes de ejecutar una tarea, MACARIO OS debería poder identificar:

- proyecto;
    
- objetivo;
    
- tarea;
    
- contexto relevante;
    
- archivos relevantes;
    
- decisiones relevantes;
    
- restricciones;
    
- herramientas necesarias.
    

No cargar todo el universo MACARIO en cada tarea.

### Principio

> **Contexto suficiente, no contexto máximo.**

Esto reduce:

- errores;
    
- contradicciones;
    
- ruido;
    
- consumo de tokens;
    
- decisiones incorrectas.
    

---

# 10. Approval Gates

MACARIO OS debe respetar la autoridad humana.

### Acciones de bajo riesgo

Pueden ejecutarse automáticamente cuando estén dentro del scope.

Ejemplos:

- análisis;
    
- lectura;
    
- búsqueda;
    
- QA;
    
- reportes;
    
- preparación de cambios.
    

### Acciones sensibles

Requieren aprobación de Ignacio.

Ejemplos:

- deploy;
    
- merge;
    
- acciones destructivas;
    
- cambios de infraestructura;
    
- envío de comunicaciones externas;
    
- decisiones comerciales;
    
- cambios importantes de arquitectura.
    

```
ACCIÓN
  ↓
¿RIESGO?
  ↓
NO ─────────────→ EJECUTAR
  │
 SÍ
  ↓
SOLICITAR APROBACIÓN
  ↓
APROBADO?
 ↙       ↘
NO        SÍ
↓          ↓
DETENER   EJECUTAR
```

---

# 11. Verification before completion

MACARIO OS no debería considerar una tarea terminada simplemente porque un agente dice:

> "Listo."

Debe existir evidencia suficiente.

Dependiendo de la tarea:

- tests;
    
- screenshot;
    
- Artifact;
    
- preview;
    
- logs;
    
- auditoría;
    
- Git diff;
    
- producción validada.
    

### Regla

> **Resultado declarado ≠ resultado verificado.**

---

# 12. Execution Record

Para tareas importantes, el sistema debería poder reconstruir:

```
qué se pidió
↓
qué proyecto fue identificado
↓
qué contexto se utilizó
↓
qué herramienta ejecutó el trabajo
↓
qué cambios se realizaron
↓
qué validaciones se hicieron
↓
qué resultado se obtuvo
↓
qué decisión humana existió
```

No necesariamente hay que construir esto como una base de datos inmediatamente.

Primero se define el modelo.

---

# 13. Estado de proyecto

MACARIO OS debería poder obtener una visión resumida de cada proyecto:

```
Proyecto
├── estado
├── objetivo
├── tareas activas
├── bloqueos
├── PRs
├── última actividad
├── QA
├── deploy
└── próximos pasos
```

La información debe venir de las fuentes reales.

MACARIO OS no debería mantener copias paralelas de todos estos datos.

---

# 14. Relación con Linear

Linear sigue siendo el sistema de ejecución.

MACARIO OS puede:

- consultar tareas;
    
- identificar prioridades;
    
- relacionar tareas con proyectos;
    
- actualizar estados;
    
- crear microtareas cuando corresponda;
    
- detectar bloqueos.
    

Pero no debería crear tareas innecesariamente.

### Regla

> Si no existe trabajo accionable, no crear una issue solamente para registrar información.

---

# 15. Relación con GitHub

GitHub sigue siendo la fuente del código.

MACARIO OS puede:

- consultar repositorios;
    
- identificar ramas;
    
- revisar PRs;
    
- consultar commits;
    
- asociar trabajo con código;
    
- consultar CI;
    
- detectar estado de implementación.
    

Nunca debe asumir que un PR o commit existe sin verificar GitHub.

---

# 16. Relación con Obsidian

Obsidian conserva el conocimiento.

MACARIO OS puede:

- localizar documentos;
    
- recuperar contexto;
    
- enlazar decisiones;
    
- crear referencias;
    
- actualizar documentación cuando una tarea genera conocimiento permanente.
    

No debería convertir cada acción operativa en una nueva nota.

---

# 17. Relación con Claude Code

Claude Code es uno de los principales ejecutores técnicos.

MACARIO OS puede preparar para Claude:

```
PROYECTO
+
TAREA
+
CONTEXTO
+
RESTRICCIONES
+
ARCHIVOS RELEVANTES
+
CRITERIOS DE ÉXITO
```

Esto permite que Claude reciba un contexto acotado y útil.

---

# 18. Relación con ChatGPT

ChatGPT funciona principalmente como:

- analista;
    
- estratega;
    
- arquitecto;
    
- revisor;
    
- coordinador.
    

Puede ayudar a:

- decidir qué hacer;
    
- interpretar auditorías;
    
- evaluar alternativas;
    
- convertir resultados en decisiones;
    
- diseñar procesos.
    

---

# 19. Automatizaciones

n8n puede utilizarse para automatizaciones entre sistemas.

Ejemplos futuros:

```
GitHub PR merged
      ↓
n8n
      ↓
Linear update
      ↓
Obsidian documentation reminder
```

Otro ejemplo:

```
Formulario de contacto
      ↓
Resend
      ↓
notificación
      ↓
Linear lead/task
```

Estas automatizaciones deben incorporarse solamente cuando el flujo manual esté suficientemente probado.

---

# 20. MACARIO OS no es un agente gigante

No queremos crear un único agente con acceso irrestricto a todo.

El modelo preferido es:

```
MACARIO OS
     │
     ├── Proyecto Raíces
     ├── Proyecto Onda
     ├── Proyecto GXK
     ├── Web-Base
     └── ITS
```

Cada dominio mantiene su contexto.

MACARIO OS coordina entre dominios cuando corresponde.

---

# 21. Seguridad

MACARIO OS debe seguir el principio de mínimo acceso.

Una herramienta o agente debe recibir solamente:

- las credenciales necesarias;
    
- el proyecto necesario;
    
- los archivos necesarios;
    
- los permisos necesarios.
    

Nunca exponer secretos en:

- prompts;
    
- documentos;
    
- repositorios;
    
- logs;
    
- screenshots.
    

---

# 22. Coste y eficiencia

La orquestación también debe controlar consumo.

Principios:

- contexto mínimo;
    
- no repetir verificaciones;
    
- evitar loops innecesarios;
    
- usar modelos apropiados al problema;
    
- automatizar solamente tareas repetitivas;
    
- evitar agentes ejecutándose sin necesidad;
    
- detener procesos cuando ya existe evidencia suficiente.
    

### Regla

> **Más automatización no significa necesariamente mejor sistema.**

---

# 23. Roadmap

## Fase 1 — Arquitectura

Definir:

- componentes;
    
- responsabilidades;
    
- Integration Registry;
    
- permisos;
    
- flujo de contexto;
    
- approval gates.
    

**Estado:** en progreso.

---

## Fase 2 — Integración básica

Conectar:

```
Linear
GitHub
Obsidian
```

Objetivo:

- relacionar proyecto ↔ tarea ↔ código ↔ documentación.
    

---

## Fase 3 — Contexto unificado

Permitir recuperar:

- proyecto;
    
- tarea;
    
- documentación;
    
- repositorio;
    
- PR;
    
- decisiones.
    

Sin cargar información innecesaria.

---

## Fase 4 — Ejecución asistida

Integrar Claude Code en el flujo:

```
tarea
↓
contexto
↓
prompt controlado
↓
implementación
↓
QA
↓
resultado
```

---

## Fase 5 — QA y observabilidad

Incorporar cuando corresponda:

- Playwright;
    
- Sentry;
    
- PostHog.
    

Objetivo:

- verificar;
    
- observar;
    
- medir.
    

---

## Fase 6 — Automatizaciones

Incorporar:

- n8n;
    
- Resend;
    
- otros conectores.
    

Solo para procesos suficientemente estables.

---

## Fase 7 — Operator Layer

Construir eventualmente una interfaz única para visualizar:

- proyectos;
    
- tareas;
    
- PRs;
    
- bloqueos;
    
- QA;
    
- deploys;
    
- actividad;
    
- documentación relevante.
    

Esta fase no debe comenzar hasta que el flujo subyacente esté suficientemente probado.

---

# 24. Roadmap actual de Linear

Las iniciativas relacionadas son:

### PRO-61

**Definir arquitectura e Integration Registry de MACARIO OS**

Primera pieza formal de MACARIO OS.

### PRO-71

**Integrar Linear + GitHub + Obsidian**

Primera integración operativa.

### PRO-72

**Implementar relaciones cross-tool y contexto unificado**

Segunda etapa de integración.

Estas tareas deben ejecutarse después de consolidar la documentación base de MACARIO.

---

# 25. Qué no construir todavía

No construir todavía:

- dashboard complejo;
    
- agente autónomo general;
    
- sistema multiagente masivo;
    
- base de datos paralela de todos los proyectos;
    
- sistema propio de analytics;
    
- sistema propio de Git;
    
- sistema propio de tareas;
    
- automatizaciones para cada pequeña acción.
    

Primero validar el flujo manual y semiautomático.

---

# 26. Criterio para avanzar

Cada nueva fase debe demostrar una mejora real.

Antes de construir una nueva capa preguntar:

1. ¿Qué fricción actual resuelve?
    
2. ¿Cuántas veces ocurre?
    
3. ¿Qué tiempo ahorra?
    
4. ¿Qué errores evita?
    
5. ¿Qué mantenimiento introduce?
    
6. ¿Puede resolverse con las herramientas actuales?
    
7. ¿Tenemos evidencia suficiente para automatizarlo?
    

---

# 27. Estado actual

### Completado

- arquitectura conceptual;
    
- responsabilidades de herramientas;
    
- relación MACARIO / WEB-BASE / ITS / proyectos;
    
- metodología WEB-BASE v1;
    
- Linear como sistema operativo;
    
- GitHub como fuente de código;
    
- Obsidian como documentación permanente.
    

### En progreso

- bóveda MACARIO;
    
- documentación maestra;
    
- integración Linear + GitHub + Obsidian;
    
- definición del Integration Registry.
    

### Futuro

- contexto unificado;
    
- ejecución asistida;
    
- QA integrado;
    
- observabilidad;
    
- automatizaciones;
    
- operator layer.
    

---

# 28. Regla principal

> **MACARIO OS debe hacer que coordinar MACARIO sea más fácil, no convertirse en otra herramienta que haya que administrar.**

Si una integración agrega más trabajo del que elimina, todavía no está justificada.
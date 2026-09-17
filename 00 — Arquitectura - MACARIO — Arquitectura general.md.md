# MACARIO — Arquitectura general

> Documento maestro de arquitectura.  
> Define qué es MACARIO, cómo se relacionan sus partes y cuál es la responsabilidad de cada sistema.

---

## 1. Qué es MACARIO

**MACARIO** es el sistema general desde el cual se diseñan, construyen, documentan, gestionan y evolucionan proyectos digitales.

No es una marca ni una herramienta: es el **System** operativo interno.

Es la combinación de:

- una metodología de trabajo;
    
- un sistema de documentación;
    
- un sistema de ejecución;
    
- una capa de orquestación (MACARIO OS);
    
- una base técnica reutilizable (Web-Base, Foundation);
    
- y una colección de proyectos reales que validan y mejoran el sistema.
    

La identidad externa con la que ese trabajo se presenta hacia afuera es **PRANA**. MACARIO organiza; PRANA muestra; Web-Base inicia.

La arquitectura busca que cada herramienta tenga una responsabilidad clara y que la información no se duplique innecesariamente.

---

## 2. Arquitectura general

**Capa externa — lo que se ve:**

```
                     PRANA
              Marca / identidad externa
                       │
           ┌───────────┴───────────┐
           │                       │
           ▼                       ▼
          ITS              PROYECTOS REALES
  expresión personal        (casos que PRANA
  de Ignacio, dentro         presenta hacia
  de PRANA                   afuera)
```

**Capa interna — cómo se organiza:**

```
                        MACARIO
                         System
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
         WEB-BASE      MACARIO OS    gestión de
         Foundation    Orquestación   proyectos
```

**Relación entre capas:**

```
MACARIO (organiza) → PROYECTOS REALES → PRANA (muestra)
```

Los proyectos reales concretos actuales:

```
Raíces
GXK
Onda
futuros proyectos
```

Los proyectos reales alimentan el sistema:

```
PROYECTOS
    ↓
aprendizajes
    ↓
MACARIO (metodología) + WEB-BASE (base técnica)
    ↓
mejores proyectos
    ↓
mejores casos para PRANA / ITS
```

---

## 3. Componentes principales

### 3.1 MACARIO

Es el System operativo interno.

Responsabilidades:

- definir la dirección general;
    
- establecer principios;
    
- decidir cómo se trabaja;
    
- definir el ecosistema de herramientas;
    
- conectar metodología, proyectos y portfolio;
    
- mantener una visión unificada del sistema.
    

MACARIO no reemplaza a las herramientas que utiliza.

MACARIO no es una marca: la identidad externa con la que el trabajo se presenta es **PRANA**.

---

### 3.2 ITS

**ITS es la firma personal y el portfolio de Ignacio.**

Vive **dentro de PRANA**, como expresión personal de la marca — no como una marca independiente ni como un producto separado de MACARIO.

Su función principal es:

- presentar el trabajo;
    
- mostrar proyectos;
    
- comunicar capacidades;
    
- transmitir el criterio visual y técnico;
    
- generar confianza;
    
- facilitar la captación de clientes.
    

ITS funciona como la **capa personal** dentro de PRANA, la marca pública y comercial del trabajo realizado dentro del ecosistema MACARIO.

Los proyectos reales pueden convertirse en casos, referencias o evidencia para PRANA / ITS.

```
MACARIO
   ↓
proyectos reales
   ↓
trabajo validado
   ↓
PRANA (marca externa)
   ↓
ITS (expresión personal de Ignacio, dentro de PRANA)
   ↓
presentación / captación
```

---

### 3.3 WEB-BASE

**WEB-BASE es la Foundation: la base técnica reutilizable de MACARIO.**

Es el punto de partida técnico desde el que nace cada proyecto, e implementa la metodología definida a nivel MACARIO.

Incluye:

- etapas;
    
- criterios;
    
- quality gates;
    
- estándares;
    
- templates;
    
- skills;
    
- comandos;
    
- documentación metodológica;
    
- criterios de QA;
    
- reglas para nuevos proyectos.
    

WEB-BASE no contiene los proyectos reales.

Los proyectos utilizan WEB-BASE como sistema de trabajo.

```
WEB-BASE
    ↓
base técnica
    ↓
proyecto
    ↓
implementación
```

---

### 3.4 MACARIO OS

**MACARIO OS es la capa de orquestación.**

Su función es conectar y coordinar los distintos sistemas utilizados durante el trabajo.

No reemplaza a:

- Linear;
    
- GitHub;
    
- Obsidian;
    
- Claude Code;
    
- ChatGPT;
    
- ni otras herramientas especializadas.
    

MACARIO OS define cómo se relacionan.

Ejemplo:

```
Obsidian
   │
   │ conocimiento
   ▼
MACARIO OS
   │
   ├── Linear → tareas
   ├── GitHub → código
   ├── Claude Code → implementación
   ├── ChatGPT → análisis / estrategia
   ├── Playwright → QA
   ├── Sentry → errores
   ├── PostHog → analítica
   ├── Resend → email
   ├── n8n → automatizaciones
   ├── Figma → referencias visuales
   ├── Supabase → backend / datos
   └── Cloudflare → infraestructura / deploy
```

MACARIO OS es principalmente una **capa conceptual y operativa de coordinación**.

---

## 4. Proyectos reales

Los proyectos reales son donde se aplica y valida todo el sistema.

Ejemplos actuales:

- Proyecto Raíces
    
- GXK
    
- Onda
    
- CONCRETO
    
- futuros proyectos y clientes
    

Cada proyecto debe mantener su propia identidad, contenido, repositorio y decisiones.

No debe quedar acoplado estructuralmente a WEB-BASE.

WEB-BASE proporciona la base técnica.

MACARIO OS coordina las herramientas.

PRANA presenta el trabajo hacia afuera; ITS es el canal personal de Ignacio dentro de PRANA cuando corresponde.

---

## 5. Responsabilidad de cada herramienta

### Obsidian — Conocimiento

Obsidian es la documentación permanente.

Debe contener:

- arquitectura;
    
- contexto;
    
- decisiones;
    
- aprendizajes;
    
- metodología;
    
- documentación de proyectos;
    
- criterios;
    
- referencias;
    
- conocimiento reutilizable.
    

Obsidian no debe convertirse en una copia de Linear.

---

### Linear — Ejecución

Linear representa el trabajo operativo.

Debe contener:

- tareas;
    
- microtareas;
    
- prioridades;
    
- estados;
    
- ciclos;
    
- dependencias;
    
- bugs;
    
- trabajo pendiente;
    
- seguimiento de proyectos.
    

Linear responde:

> **¿Qué tenemos que hacer?**

---

### GitHub — Implementación

GitHub representa el código real.

Contiene:

- repositorios;
    
- ramas;
    
- commits;
    
- Pull Requests;
    
- código;
    
- historial de implementación.
    

GitHub responde:

> **¿Qué construimos realmente?**

---

### Claude Code — Implementación asistida

Claude Code se utiliza principalmente para:

- implementar;
    
- modificar;
    
- refactorizar;
    
- auditar;
    
- ejecutar QA técnico;
    
- trabajar sobre repositorios.
    

Debe respetar la metodología de MACARIO, la base técnica de WEB-BASE y las decisiones registradas.

---

### ChatGPT — Análisis y estrategia

ChatGPT se utiliza principalmente para:

- analizar;
    
- investigar;
    
- pensar arquitectura;
    
- comparar alternativas;
    
- definir estrategia;
    
- revisar resultados;
    
- ayudar a tomar decisiones.
    

---

## 6. Flujo general de información

```
IDEA / CLIENTE
      ↓
   WEB-BASE
      ↓
  DISCOVERY
      ↓
    SCOPE
      ↓
 ARCHITECTURE
      ↓
 VISUAL DIRECTION
      ↓
 IMPLEMENTATION
      ↓
      QA
      ↓
    AUDIT
      ↓
    DEPLOY
      ↓
 DOCUMENTATION
      ↓
    CIERRE
```

Durante ese proceso:

```
Obsidian ← conocimiento permanente
Linear   ← tareas y seguimiento
GitHub   ← implementación
Claude   ← ejecución técnica
ChatGPT  ← análisis y estrategia
MACARIO OS ← coordinación
```

---

## 7. Principio de no duplicación

Cada información debe tener un lugar principal.

### Ejemplo

Una decisión arquitectónica:

**Obsidian**

Una tarea para implementar esa decisión:

**Linear**

El código que implementa la decisión:

**GitHub**

El proceso utilizado para llegar a esa implementación:

**WEB-BASE**

La coordinación entre todas esas partes:

**MACARIO OS**

---

## 8. Fuente de verdad

La fuente de verdad depende del tipo de información.

|Información|Fuente principal|
|---|---|
|Arquitectura / decisiones|Obsidian|
|Metodología|WEB-BASE + Obsidian|
|Tareas|Linear|
|Estado del trabajo|Linear|
|Código|GitHub|
|Historial de cambios|GitHub|
|Implementación|GitHub + Claude Code|
|Análisis / estrategia|ChatGPT + Obsidian|
|Errores de producción|Sentry|
|Analítica|PostHog|
|Deploy / infraestructura|Cloudflare|
|Datos / backend|Supabase|
|Automatizaciones|n8n|

---

## 9. Principios de arquitectura

### 9.1 Separación de responsabilidades

Cada herramienta debe resolver el problema para el que fue elegida.

No convertir una herramienta en sustituto innecesario de otra.

### 9.2 Una fuente por tipo de información

Evitar duplicaciones que puedan generar contradicciones.

### 9.3 Los proyectos son independientes

Raíces, GXK, Onda y futuros proyectos deben poder existir y evolucionar independientemente.

### 9.4 WEB-BASE es reutilizable

Las mejoras descubiertas durante proyectos reales deben poder transformarse en metodología reutilizable.

### 9.5 MACARIO OS coordina, no reemplaza

MACARIO OS debe conectar sistemas, no reconstruir innecesariamente las funcionalidades que ya ofrecen.

### 9.6 Documentar decisiones importantes

Las decisiones que afectan arquitectura, metodología, identidad o estrategia deben quedar documentadas.

### 9.7 El trabajo real valida el sistema

La metodología no debe crecer por teoría.

Debe evolucionar a partir de problemas reales, aprendizajes y resultados.

---

## 10. Ciclo de aprendizaje

Cada proyecto puede producir conocimiento reutilizable.

```
PROYECTO
   ↓
problema / aprendizaje
   ↓
documentación en Obsidian
   ↓
evaluación
   ↓
si es reutilizable:
   ↓
WEB-BASE
   ↓
mejora del sistema
```

No todo aprendizaje debe convertirse en metodología.

Solo aquello que sea:

- repetible;
    
- útil;
    
- comprobado;
    
- y aplicable a otros proyectos.
    

---

## 11. Estado actual

### Consolidado

- MACARIO como sistema general (System).
    
- PRANA como marca / identidad externa.
    
- ITS como portfolio personal/profesional de Ignacio, dentro de PRANA.
    
- WEB-BASE como base técnica reutilizable (Foundation).
    
- MACARIO OS como capa de orquestación.
    
- Linear como sistema operativo de tareas.
    
- GitHub como sistema de código.
    
- Obsidian como documentación permanente.
    

### En construcción

- bóveda MACARIO;
    
- documentación maestra;
    
- migración desde Linear;
    
- integración Obsidian ↔ herramientas;
    
- MACARIO OS.
    

### Proyectos actuales

- Proyecto Raíces
    
- GXK
    
- Onda
    
- CONCRETO
    
- futuros proyectos
    

---

## 12. Documentos relacionados

- [[MACARIO — Principios y decisiones]]
    
- [[MACARIO — Flujo de trabajo]]
    
- [[MACARIO — Herramientas y ecosistema]]
    
- [[WEB-BASE — Metodología y estándares]]
    
- [[MACARIO OS — Arquitectura y roadmap]]
    
- [[ITS — Portfolio y posicionamiento]]
    

---

## 13. Regla final

**MACARIO no es una herramienta.**

Es el sistema que permite que la marca (PRANA), la metodología, el conocimiento, la ejecución y los proyectos funcionen como una sola estructura sin perder la independencia de cada componente.

[[01 — Principios y decisiones - MACARIO — Principios y decisiones.md]]

[[02 — Metodología - MACARIO — Flujo de trabajo.md]]

[[03 — Herramientas - MACARIO — Herramientas y ecosistema.md]]

[[04 — Web-Base - WEB-BASE — Metodología y estándares.md]]

[[05 — MACARIO OS - MACARIO OS — Arquitectura y roadmap.md]]

[[06 — ITS - ITS — Portfolio y posicionamiento.md]]

[[07 — Proyectos - Proyecto Raíces - Proyecto Raíces — Contexto.md]]




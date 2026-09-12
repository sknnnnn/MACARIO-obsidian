# Proyecto Raíces — Contexto

> Documento base del proyecto Proyecto Raíces dentro de MACARIO.  
> Contiene el contexto estable del proyecto, su propósito, estructura actual y decisiones relevantes.
> 
> Las tareas operativas y su estado viven en Linear.  
> El código real vive en GitHub.  
> Esta nota conserva el conocimiento permanente.

---

# 1. Identidad

**Proyecto:** Proyecto Raíces

**Tipo:** Proyecto de turismo de aventura y experiencias.

**Marca:** Proyecto Raíces

**Sitio:** proyectoraices.com.ar

**Contacto:** [proyectoraicestravel@gmail.com](mailto:proyectoraicestravel@gmail.com)

**WhatsApp:** +54 9 280 497-1939

---

# 2. Qué es Proyecto Raíces

Proyecto Raíces busca ofrecer experiencias de viaje alejadas del modelo tradicional de agencia.

La propuesta combina:

- naturaleza;
    
- aventura;
    
- cultura;
    
- encuentros;
    
- exploración;
    
- experiencias compartidas.
    

Las experiencias pueden desarrollarse como:

- Tours;
    
- Travesías;
    
- Paquetes integrales.
    

---

# 3. Tipos de experiencias

## Tours

Experiencias organizadas, generalmente de menor duración y con una propuesta concreta.

## Travesías

Experiencias de aventura y exploración que pueden incluir:

- trekking;
    
- senderismo;
    
- MTB;
    
- buceo;
    
- y otras actividades.
    

Pueden ser:

- de un día;
    
- de varios días.
    

Pueden ofrecerse como:

- experiencia;
    
- experiencia con servicios incluidos;
    
- propuesta integral.
    

## Paquetes

Propuestas integrales que combinan distintos componentes de una experiencia.

La categoría debe utilizarse cuando exista realmente una propuesta de paquete.

---

# 4. Arquitectura actual del sitio

La arquitectura actual diferencia claramente:

```
EXPERIENCIAS
    ↓
catálogo principal de experiencias
    ↓
Tours / Travesías / Paquetes
    ↓
filtros por destino
```

y:

```
DESTINOS
    ↓
contenido editorial e informativo
    ↓
información del lugar
    ↓
accesos a experiencias relacionadas
```

Esta separación es deliberada.

---

# 5. Experiencias

**Experiencias es el catálogo principal.**

Es la vía principal para descubrir y encontrar experiencias concretas.

Debe permitir explorar:

- todos;
    
- Tours;
    
- Travesías;
    
- Paquetes;
    
- destinos.
    

El usuario puede llegar a una experiencia desde el catálogo y desde filtros.

### Regla

No crear un segundo catálogo de experiencias dentro de Destinos.

---

# 6. Destinos

**Destinos pasa a ser principalmente editorial e informativo.**

Su objetivo es presentar los lugares desde una perspectiva más narrativa y contextual.

Puede incluir:

- información del destino;
    
- características;
    
- naturaleza;
    
- cultura;
    
- atractivos;
    
- contexto;
    
- contenido editorial;
    
- referencias visuales;
    
- experiencias relacionadas.
    

Puede incluir accesos a fichas de experiencias.

Pero:

> **Destinos no es la principal vía de descubrimiento del catálogo.**

La principal vía de descubrimiento es Experiencias.

---

# 7. Relación Destinos → Experiencias

La relación conceptual es:

```
DESTINO
   │
   ├── información
   ├── contexto
   ├── contenido editorial
   └── experiencias relacionadas
             │
             ▼
        ficha de experiencia
```

Esto permite que Destinos funcione como una puerta editorial hacia determinadas experiencias sin duplicar el catálogo.

---

# 8. Jerarquía geográfica

La estructura conceptual de experiencias mantiene:

```
País
  ↓
Destino
  ↓
Experiencias
```

**Patagonia no debe funcionar como un destino navegable independiente.**

Puede utilizarse como:

- referencia geográfica;
    
- categoría;
    
- contexto;
    
- agrupación conceptual.
    

Pero la navegación debe llevar a destinos concretos.

Ejemplos:

- Bariloche;
    
- El Chaltén;
    
- Ushuaia;
    
- otros destinos concretos.
    

---

# 9. Contenido

El proyecto debe utilizar contenido real.

No inventar:

- experiencias;
    
- destinos;
    
- precios;
    
- fechas;
    
- servicios;
    
- testimonios;
    
- datos comerciales;
    
- información geográfica específica.
    

Cuando falte información:

```
dato faltante
    ↓
registrar pendiente
    ↓
obtener información real
    ↓
incorporar
```

Los placeholders deben eliminarse antes del cierre del proyecto.

---

# 10. Dirección de producto

El sitio debe sentirse como una propuesta de experiencias y aventura, no como una agencia de turismo tradicional genérica.

La experiencia debe priorizar:

- descubrimiento;
    
- inspiración;
    
- claridad;
    
- fotografía;
    
- narrativa;
    
- confianza;
    
- acceso sencillo a las experiencias.
    

El contenido y las imágenes deben trabajar juntos.

---

# 11. Dirección visual

La referencia general busca una estética de turismo de aventura con personalidad.

Referencias utilizadas durante el proceso incluyen sitios como Wamani y otras propuestas de viajes/aventura que priorizan:

- fotografía;
    
- experiencias;
    
- composición;
    
- narrativa;
    
- identidad.
    

Debe evitarse una estética genérica de template.

La interfaz debe permitir que:

- las fotografías tengan protagonismo;
    
- el contenido respire;
    
- la navegación sea clara;
    
- las experiencias se sientan concretas.
    

---

# 12. Estado actual del proyecto

### Consolidado

- Experiencias funciona como catálogo principal.
    
- Se eliminó la duplicación de catálogo entre Experiencias y Destinos.
    
- Destinos queda orientado hacia contenido editorial/informativo.
    
- Las experiencias pueden enlazarse desde Destinos.
    
- Patagonia no funciona como destino navegable principal.
    

### En curso

El trabajo actual pendiente se concentra en:

1. establecer el contenido definitivo de Destinos;
    
2. realizar una revisión integral del sitio;
    
3. cerrar el proyecto cuando el contenido y la experiencia estén validados.
    

---

# 13. Próximo objetivo

## Destinos

Definir y completar el contenido editorial e informativo de cada destino.

Debe revisarse:

- estructura;
    
- contenido;
    
- imágenes;
    
- narrativa;
    
- información útil;
    
- relación con experiencias;
    
- navegación.
    

El resultado esperado es que Destinos pueda funcionar como sección editorial independiente sin competir con Experiencias.

---

# 14. Revisión final

Una vez completado Destinos, realizar una revisión integral.

### Contenido

- no hay información inventada;
    
- no quedan placeholders;
    
- textos coherentes;
    
- información consistente.
    

### UX

- navegación;
    
- jerarquía;
    
- filtros;
    
- enlaces;
    
- CTA;
    
- descubrimiento de experiencias.
    

### Visual

- desktop;
    
- tablet;
    
- mobile;
    
- composición;
    
- imágenes;
    
- espaciado;
    
- consistencia.
    

### Técnico

- consola;
    
- enlaces;
    
- formularios;
    
- responsive;
    
- assets;
    
- SEO básico;
    
- performance obvia.
    

### Resultado

Si no quedan problemas importantes:

> **Proyecto Raíces puede considerarse finalizado.**

---

# 15. Herramientas

### Linear

Seguimiento de tareas y microtareas.

### GitHub

Código e historial del proyecto.

### Claude Code

Implementación, QA y auditoría asistida.

### Obsidian

Documentación permanente y decisiones.

### MACARIO / WEB-BASE

Metodología utilizada para organizar el trabajo.

---

# 16. Enlaces

**Sitio:**  
[https://proyectoraices.com.ar](https://proyectoraices.com.ar/)

**Repositorio:**  
Agregar enlace al repositorio oficial de Proyecto Raíces cuando corresponda.

**Linear:**  
Las tareas operativas del proyecto se mantienen en Linear.

---

# 17. Aprendizajes para MACARIO

Proyecto Raíces funciona también como proyecto de validación de WEB-BASE.

Al finalizar, registrar:

- qué funcionó;
    
- qué generó fricción;
    
- qué decisiones se repitieron;
    
- qué problemas podrían prevenirse;
    
- qué procesos deberían convertirse en templates;
    
- qué aprendizajes podrían incorporarse a WEB-BASE.
    

No convertir automáticamente cada aprendizaje en metodología.

Solo incorporar patrones que hayan demostrado ser reutilizables.

---

# 18. Regla del proyecto

> **Experiencias vende y permite descubrir experiencias. Destinos informa, inspira y contextualiza.**

No volver a duplicar ambas funciones.

---

# 19. Estado de cierre

Proyecto Raíces se considera listo para cierre cuando:

- Destinos esté completo;
    
- el contenido haya sido validado;
    
- Experiencias funcione correctamente;
    
- no existan duplicaciones importantes;
    
- la navegación esté clara;
    
- la revisión visual esté aprobada;
    
- QA esté aprobado;
    
- la auditoría esté aprobada;
    
- el deploy esté validado;
    
- y la documentación permanente esté actualizada.
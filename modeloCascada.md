# Modelo de Desarrollo en Cascada - Actividad de Lectura de Productos

## Resumen de la Experiencia

Durante la implementación de la funcionalidad de lectura de productos utilizando la metodología de desarrollo en cascada, se identificaron varias dificultades y aprendizajes importantes.

## Dificultades Identificadas

### 1. **Dependencias entre Roles**
- **Problema**: El frontend developer no pudo comenzar su trabajo hasta que el backend developer completara su parte.
- **Impacto**: Esto generó tiempos de espera y una secuencia muy rígida de desarrollo.
- **Lección**: En proyectos reales, esta dependencia puede causar retrasos significativos si un miembro del equipo se atrasa.

### 2. **Falta de Comunicación Temprana**
- **Problema**: Las interfaces entre backend y frontend no se definieron claramente desde el inicio.
- **Impacto**: Hubo que hacer ajustes en la estructura de datos y métodos durante la integración.
- **Lección**: Es crucial definir contratos de interfaz desde las primeras etapas.

### 3. **Dificultad para Realizar Pruebas Tempranas**
- **Problema**: No se pudieron realizar pruebas integrales hasta que ambas partes estuvieran completamente desarrolladas.
- **Impacto**: Los errores se descubrieron tarde en el proceso, requiriendo más tiempo para corregirlos.
- **Lección**: La metodología en cascada retrasa la detección de errores de integración.

### 4. **Gestión de Archivos y Versionado**
- **Problema**: Trabajar en ramas separadas sin integración continua causó conflictos al momento de unir el trabajo.
- **Impacto**: Tiempo adicional invertido en resolver conflictos de merge.
- **Lección**: Incluso en cascada, es importante tener estrategias de integración claras.

## Ventajas Observadas

### 1. **Claridad en Responsabilidades**
- Cada rol tenía responsabilidades muy bien definidas.
- No hubo confusión sobre quién debía hacer qué tarea.

### 2. **Facilidad de Planificación**
- Los tiempos fueron más fáciles de estimar al tener fases bien definidas.

## Conclusiones

La metodología en cascada funcionó para este proyecto pequeño y con requisitos bien definidos, pero evidenció limitaciones importantes:

1. **Falta de flexibilidad**: Dificulta la adaptación a cambios.
2. **Detección tardía de problemas**: Los errores de integración se descubren al final.
3. **Dependencias bloqueantes**: Un retraso en una fase afecta todas las siguientes.
4. **Poca colaboración**: Los roles trabajan de forma muy aislada.

## Recomendaciones

1. **Definir interfaces claras** desde el inicio del proyecto.
2. **Establecer puntos de sincronización** regulares entre los roles.
3. **Crear prototipos tempranos** para validar la integración.


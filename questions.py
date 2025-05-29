# Sample questions - you can expand this list or load from a database
questions = [
    # Cuestionario sobre Metodologías de Desarrollo de Software
    {
        "question": "¿Qué modelo de desarrollo se caracteriza por tener fases bien definidas y no permitir retrocesos?",
        "options": ["Modelo en V", "Modelo Espiral", "Modelo en Cascada", "Modelo Iterativo"],
        "correct": 2  # Modelo en Cascada (index 2)
    },
    {
        "question": "En el modelo en V, ¿qué fase acompaña cada etapa de desarrollo?",
        "options": ["Implementación", "Pruebas", "Análisis de requisitos", "Mantenimiento"],
        "correct": 1  # Pruebas (index 1)
    },
    {
        "question": "¿Cuál es una característica fundamental de las metodologías ágiles?",
        "options": ["Documentación extensa", "Desarrollo incremental e iterativo", "Planificación rígida y detallada", "Uso exclusivo de diagramas UML"],
        "correct": 1  # Desarrollo incremental e iterativo (index 1)
    },
    {
        "question": "¿Cuál de las siguientes NO es una metodología ágil?",
        "options": ["Scrum", "XP (Extreme Programming)", "Modelo en Cascada", "Kanban"],
        "correct": 2  # Modelo en Cascada (index 2)
    },
    {
        "question": "¿Cuál de los siguientes es un principio clave de Scrum?",
        "options": ["Sprints iterativos", "Entregas solo al final del proyecto", "Desarrollo sin reuniones", "Se exige una práctica de desarrollo específica"],
        "correct": 0  # Sprints iterativos (index 0)
    },
    {
        "question": "¿Qué rol en Scrum es responsable de eliminar obstáculos y facilitar el proceso?",
        "options": ["Product Owner", "Scrum Master", "Jefe de Proyecto", "Desarrollador"],
        "correct": 1  # Scrum Master (index 1)
    },
    {
        "question": "¿Qué metodología ágil promueve la programación en pareja y pruebas automatizadas?",
        "options": ["Kanban", "Scrum", "XP (Extreme Programming)", "Modelo en V"],
        "correct": 2  # XP (index 2)
    },
    {
        "question": "¿Cuál es una característica clave de los métodos híbridos como Scrumban?",
        "options": ["No permiten iteraciones", "Mezclan elementos de metodologías tradicionales y ágiles", "Solo se usan en proyectos pequeños", "No requieren planificación"],
        "correct": 1  # Mezclan elementos (index 1)
    },
    {
        "question": "¿Qué marco de trabajo ágil es más utilizado en grandes organizaciones para escalar Agile?",
        "options": ["XP", "Scrum", "SAFe (Scaled Agile Framework)", "Kanban"],
        "correct": 2  # SAFe (index 2)
    },
    {
        "question": "En el ciclo de vida del software, ¿qué fase implica la verificación y validación del código?",
        "options": ["Diseño", "Implementación", "Pruebas", "Análisis de requisitos"],
        "correct": 2  # Pruebas (index 2)
    },
    {
        "question": "¿Cuál es la principal ventaja de utilizar metodologías ágiles?",
        "options": ["Reduce la necesidad de planificación", "Flexibilidad y adaptación a cambios", "Menos interacción con el cliente", "Desarrollo más lento pero más seguro"],
        "correct": 1  # Flexibilidad y adaptación a cambios (index 1)
    },
    {
        "question": "¿Qué enfoque de desarrollo mejora el producto en ciclos incrementales, adaptando el alcance en cada iteración?",
        "options": ["Predictivo", "Adaptativo", "Modelo en V", "Modelo en Cascada"],
        "correct": 1  # Adaptativo (index 1)
    },
    {
        "question": "¿Cuál de los siguientes es un objetivo clave de las metodologías de desarrollo de software?",
        "options": ["Reducir la necesidad de pruebas", "Estandarizar el proceso de desarrollo y reducir errores", "Eliminar la fase de mantenimiento", "Desarrollar software sin documentación"],
        "correct": 1  # Estandarizar el proceso (index 1)
    },
    {
        "question": "¿Qué tipo de ciclo de vida se caracteriza por dividir el desarrollo en pequeñas partes funcionales entregables?",
        "options": ["Predictivo", "Cascada", "Incremental", "Modelo en V"],
        "correct": 2  # Incremental (index 2)
    },
    {
        "question": "¿Qué ventaja tiene el modelo en espiral respecto al modelo en cascada?",
        "options": ["Permite evaluar riesgos en cada iteración", "Es más rápido", "No necesita planificación", "No requiere pruebas"],
        "correct": 0  # Permite evaluar riesgos (index 0)
    },
    {
        "question": "¿Cuál es una de las funciones principales del Product Owner en Scrum?",
        "options": ["Escribir código", "Priorizar los requisitos del producto", "Gestionar el equipo de desarrollo", "Diseñar la interfaz de usuario"],
        "correct": 1  # Priorizar los requisitos (index 1)
    },
    {
        "question": "¿Cómo se denomina la reunión diaria en Scrum donde el equipo sincroniza el trabajo?",
        "options": ["Daily Scrum", "Sprint Planning", "Sprint Retrospective", "Revisión del Sprint"],
        "correct": 0  # Daily Scrum (index 0)
    },
    {
        "question": "¿Qué ventaja tiene Kanban sobre Scrum?",
        "options": ["Utiliza reuniones diarias obligatorias", "No permite cambios en el flujo de trabajo", "No usa iteraciones fijas y permite flujo continuo", "Depende de la documentación extensa"],
        "correct": 2  # No usa iteraciones fijas (index 2)
    },
    {
        "question": "¿Qué significa la retrospectiva en Scrum?",
        "options": ["Reunión para evaluar y mejorar el proceso", "Presentación del software al cliente", "Revisión del código fuente", "Análisis de riesgos"],
        "correct": 0  # Reunión para evaluar (index 0)
    },
    {
        "question": "¿En qué metodología se utilizan tarjetas visuales para gestionar tareas y su progreso?",
        "options": ["Scrum", "XP", "Kanban", "Modelo en V"],
        "correct": 2  # Kanban (index 2)
    },
    # Cuestionario sobre Calidad del Software
    {
        "question": "¿Cuál de los siguientes NO es un factor clave en la calidad del software?",
        "options": ["Correctitud", "Mantenibilidad", "Inseguridad", "Eficiencia"],
        "correct": 2  # Inseguridad (index 2)
    },
    {
        "question": "Los estándares ...",
        "options": ["Sólo se enfocan en aspectos técnicos.", "Se enfocan en aspectos técnicos y en ética profesional y responsabilidad social.", "Se enfocan en ética profesional y responsabilidad social pero no en aspectos técnicos.", "Se enfocan en aspectos técnicos y en ética profesional solamente."],
        "correct": 1  # Se enfocan en aspectos técnicos y en ética profesional y responsabilidad social (index 1)
    },
    {
        "question": "Documentar errores y fallos de manera honesta es un principio de la ética en el software:",
        "options": ["Verdadero", "Falso"],
        "correct": 0  # Verdadero (index 0)
    },
    {
        "question": "El ISO 9000 ...",
        "options": ["Establece los principios fundamentales para la gestión de la calidad en las organizaciones.", "Establece un marco para gestionar y controlar la calidad en el ciclo de vida del desarrollo.", "Es una norma diseñada para ayudar a las organizaciones a mejorar su eficiencia y sostenibilidad a largo plazo.", "Estándar internacional para la evaluación de la calidad del software."],
        "correct": 0  # Establece los principios fundamentales (index 0)
    },
    {
        "question": "Las características de la ISO 25000 son ...",
        "options": ["Funcionalidad, usabilidad, fiabilidad, eficiencia, mantenibilidad, seguridad, portabilidad y compatibilidad.", "Funcionalidad, fiabilidad, seguridad y mantenibilidad.", "Funcionalidad, usabilidad, fiabilidad, eficiencia, mantenibilidad, seguridad, portabilidad, compatibilidad y liderazgo.", "Enfoque del cliente, liderazgo, compromiso del personal, enfoque por procesos, mejora continua y toma de decisiones basada en evidencias."],
        "correct": 0  # Funcionalidad, usabilidad, etc. (index 0)
    },
    {
        "question": "¿Qué es un estándar de calidad de software?",
        "options": ["Un conjunto de reglas para evaluar y mejorar la calidad del software.", "Un tipo de software de código abierto.", "Un modelo de negocio para la industria del software.", "Un programa de seguridad informática."],
        "correct": 0  # Un conjunto de reglas (index 0)
    },
    {
        "question": "¿Qué tipo de prueba se realiza sin ejecutar el código?",
        "options": ["Pruebas estáticas", "Pruebas dinámicas", "Pruebas de carga", "Pruebas de estrés"],
        "correct": 0  # Pruebas estáticas (index 0)
    },
    {
        "question": "¿Cuál es el propósito principal de un SQA (Software Quality Assurance)?",
        "options": ["Crear bases de datos seguras.", "Escribir código sin errores.", "Garantizar el cumplimiento de metodologías de calidad.", "Reemplazar a los testers manuales."],
        "correct": 2  # Garantizar el cumplimiento (index 2)
    },
    {
        "question": "¿Cuáles son los fundamentos de SQC (Software Quality Control)?",
        "options": ["Detecta problemas en los productos de trabajo.", "Verifica que los productos de trabajo cumplan con los estándares de calidad especificados.", "Revisa el contenido del producto.", "Todas las anteriores son correctas."],
        "correct": 3  # Todas las anteriores (index 3)
    },
    {
        "question": "Sobre la mejora continua de la calidad, señala la afirmación INCORRECTA.",
        "options": ["Estrategia iterativa para optimizar procesos y productos.", "Se basa en el ciclo PDCA (Plan-Do-Check-Act) y la gestión de calidad total (TQM).", "La retroalimentación constante de usuarios y desarrolladores ayuda a perfeccionar el software.", "Reduce el tiempo y los costos de mantenimiento"],
        "correct": 3  # Reduce el tiempo y los costos (index 3)
    },
    {
        "question": "¿Qué es un proceso de auditoría en el desarrollo de software?",
        "options": ["Evaluación para verificar el cumplimiento de estándares.", "Escribir código más rápido.", "Reducir costos de desarrollo.", "Desarrollar software sin documentación."],
        "correct": 0  # Evaluación para verificar (index 0)
    },
    {
        "question": "La evaluación y verificación de la calidad del software garantizan que el producto cumple con los estándares establecidos y satisface las necesidades del usuario.",
        "options": ["Verdadero", "Falso"],
        "correct": 0  # Verdadero (index 0)
    },
    {
        "question": "Sobre la seguridad en software crítico, señala la afirmación CORRECTA.",
        "options": ["Se aplican pruebas de estrés y carga", "Un software seguro protege la integridad de los datos y la privacidad del usuario.", "El análisis de fallos permite mitigar errores y prevenir problemas futuros.", "Ninguna es correcta."],
        "correct": 1  # Un software seguro protege (index 1)
    },
    {
        "question": "¿Cuál es la principal diferencia entre los métodos de evaluación de calidad estáticos y dinámicos?",
        "options": ["Los métodos estáticos requieren la ejecución del software, mientras que los dinámicos no.", "Los métodos dinámicos se aplican antes del desarrollo del software y los estáticos después.", "Los métodos estáticos no requieren la ejecución del software, mientras que los dinámicos sí.", "Ambos métodos requieren la ejecución del software, pero en diferentes entornos."],
        "correct": 2  # Los métodos estáticos no requieren (index 2)
    },
    {
        "question": "¿Cuál de estas métricas NO se utiliza en estándares de calidad?",
        "options": ["Densidad de defectos", "Tiempo entre fallos", "Complejidad ciclomática", "Densidad ciclomática"],
        "correct": 3  # Densidad ciclomática (index 3)
    },
    {
        "question": "El análisis estático ...",
        "options": ["Es fundamental para detectar errores en etapas tardías.", "Es fundamental para detectar errores en etapas tempranas.", "No permite identificar código ejecutable o redundante.", "Evalúa el comportamiento real del sistema bajo diferentes condiciones."],
        "correct": 1  # Es fundamental para detectar errores en etapas tempranas (index 1)
    },
    {
        "question": "¿Cual de estas herramientas pertenece al análisis dinámico?",
        "options": ["Sonarqube", "ESLint", "Selenium", "Infer"],
        "correct": 2  # Selenium (index 2)
    },
    {
        "question": "¿Cual de estas no es una técnica de reducción de riesgos?",
        "options": ["Evitación de fallos.", "Análisis de rendimiento.", "Uso de modelos de aseguramiento.", "Limitación del daño causado por fallos."],
        "correct": 1  # Análisis de rendimiento (index 1)
    },
    {
        "question": "La ISO 9001 permite a las empresas que desarrollan software conocer la calidad de sus productos.",
        "options": ["Verdadero", "Falso"],
        "correct": 1  # Falso (index 1)
    },
    {
        "question": "¿Cual de estas afirmaciones es correcta?",
        "options": ["La verificacion garantiza que el software cumple con los requisitos del usuario.", "Las verificación previene problemas de usabilidad y funcionalidad", "La verificación confirma que el desarrollo sigue las especificaciones técnicas.", "La verificación no detecta problemas antes de la entrega del producto."],
        "correct": 2  # La verificación confirma (index 2)
    },
    # Cuestionario del tema: Métricas de calidad de proyectos software
    {
        "question": "¿Para qué sirven las métricas de calidad a lo largo del desarrollo de un proyecto?",
        "options": ["Únicamente para la fase final de pruebas.", "Solo para la comunicación con los usuarios finales.", "Para identificar áreas de mejora, establecer objetivos realistas y tomar decisiones informadas.", "Principalmente para la gestión de la infraestructura del servidor."],
        "correct": 2  # Para identificar áreas de mejora (index 2)
    },
    {
        "question": "¿Qué se busca conseguir al analizar el problema antes de iniciar un proyecto de software?",
        "options": ["Definir el lenguaje de programación a utilizar.", "Entender qué se quiere hacer y qué se quiere conseguir para no afectar la calidad.", "Establecer el cronograma detallado de tareas.", "Asignar los roles y responsabilidades del equipo."],
        "correct": 1  # Entender qué se quiere hacer (index 1)
    },
    {
        "question": "¿Desde qué perspectiva principal miden el software las métricas de función?",
        "options": ["La cantidad de líneas de código.", "La eficiencia del algoritmo.", "El rendimiento del servidor.", "La del usuario, en términos de tamaño, complejidad y funcionalidad."],
        "correct": 3  # La del usuario (index 3)
    },
    {
        "question": "¿Cuál es el propósito del factor de ajuste de complejidad en el cálculo de Puntos de Función?",
        "options": ["Simplificar el proceso de conteo de elementos funcionales.", "Reflejar mejor las características técnicas y operativas del software en el cálculo final.", "Asegurar que todos los proyectos tengan el mismo número de Puntos de Función.", "Eliminar la necesidad de contar los elementos funcionales individualmente."],
        "correct": 1  # Reflejar mejor las características técnicas (index 1)
    },
    {
        "question": "¿Cuál de los siguientes es un tipo de elemento funcional que se considera al calcular los Puntos de Función?",
        "options": ["Entradas Externas (EI).", "Líneas de código comentadas.", "Número de pruebas unitarias.", "Cantidad de diagramas UML."],
        "correct": 0  # Entradas Externas (index 0)
    },
    {
        "question": "¿Qué representan los Archivos Lógicos Internos (ILF) en el modelo de Puntos de Función?",
        "options": ["Datos que ingresan al sistema desde el exterior.", "Datos generados por el sistema y enviados al usuario.", "Conjuntos de datos almacenados dentro de la aplicación y mantenidos por el sistema.", "Archivos referenciados por la aplicación pero no mantenidos por ella."],
        "correct": 2  # Conjuntos de datos almacenados (index 2)
    },
    {
        "question": "¿Qué indica un valor alto en la métrica \"Falta de Cohesión en Métodos (LCOM)\"?",
        "options": ["Que los métodos de la clase están bien relacionados.", "Que la clase realiza demasiadas tareas no relacionadas.", "Que la clase tiene una interfaz bien definida.", "Que la clase es altamente reutilizable."],
        "correct": 1  # Que la clase realiza demasiadas tareas (index 1)
    },
    {
        "question": "¿A qué se refiere el concepto de \"acoplamiento\" en el diseño de clases?",
        "options": ["Qué tan bien los elementos dentro de una clase trabajan juntos.", "La cantidad de elementos y relaciones dentro del sistema.", "El contexto donde una clase puede operar.", "El grado de interdependencia entre dos sistemas o clases."],
        "correct": 3  # El grado de interdependencia (index 3)
    },
    {
        "question": "¿Qué evalúan las métricas de diseño de clases en el desarrollo de software orientado a objetos?",
        "options": ["La calidad de la estructura y las relaciones de las clases dentro de un sistema.", "El rendimiento de los métodos de las clases.", "La cantidad de documentación generada para cada clase.", "El número de pruebas unitarias escritas para cada clase."],
        "correct": 0  # La calidad de la estructura (index 0)
    },
    {
        "question": "¿Qué mide la \"Complejidad Ciclomática del Caso de Uso (CC)\"?",
        "options": ["La cantidad total de actores involucrados en el caso de uso.", "La cantidad de caminos alternativos dentro del caso de uso.", "El porcentaje de acciones realizadas por el sistema.", "El número de casos de uso incluidos en el caso de uso principal."],
        "correct": 1  # La cantidad de caminos alternativos (index 1)
    },
    {
        "question": "¿Qué evalúan las métricas de casos de uso?",
        "options": ["La eficiencia del código generado a partir de los casos de uso.", "La calidad de la especificación de requisitos en un sistema orientado a objetos, centrada en la interacción usuario-sistema.", "El número de diagramas de secuencia creados para cada caso de uso.", "La complejidad técnica de la implementación de cada caso de uso."],
        "correct": 1  # La calidad de la especificación (index 1)
    },
    {
        "question": "¿Qué mide la métrica de \"trazabilidad\" en los requisitos de software?",
        "options": ["La longitud promedio de las frases en los requisitos.", "La frecuencia con la que se actualizan los requisitos.", "La capacidad de seguir un requisito a lo largo del ciclo de vida del software.", "El nivel de detalle técnico incluido en cada requisito."],
        "correct": 2  # La capacidad de seguir un requisito (index 2)
    },
    {
        "question": "¿Cuál es un beneficio esperado de mantener un bajo acoplamiento entre las clases en un sistema orientado a objetos?",
        "options": ["Mejora la modularidad y facilita la reutilización del código.", "Mayor dificultad para realizar cambios en el código.", "Menor modularidad y dificultad para la reutilización del código.", "Aumento de la complejidad en las pruebas unitarias"],
        "correct": 0  # Mejora la modularidad (index 0)
    },
    {
        "question": "¿Qué mide la métrica de diseño de clases \"Weighted Methods per Class (WMC)\"?",
        "options": ["La profundidad de la jerarquía de herencia.", "El número de subclases de una clase.", "El número de clases con las que una clase está acoplada.", "La complejidad de una clase sumando la complejidad de cada uno de sus métodos."],
        "correct": 3  # La complejidad de una clase (index 3)
    },
    {
        "question": "¿Qué distingue a una Salida Externa (EO) de una Consulta Externa (EQ) en el contexto de los Puntos de Función?",
        "options": ["La EO no involucra datos almacenados, mientras que la EQ sí.", "La EQ siempre modifica archivos internos, mientras que la EO no.", "La EO incluye cálculos, transformaciones o datos derivados, a diferencia de la EQ que solo muestra información sin procesamiento adicional.", "La EO es iniciada por un sistema externo, mientras que la EQ por el usuario."],
        "correct": 2  # La EO incluye cálculos (index 2)
    },
    {
        "question": "¿Qué métrica de requisitos se centra en asegurar que cada requisito tenga una única interpretación técnica?",
        "options": ["Completitud.", "Consistencia.", "Corrección.", "Trazabilidad."],
        "correct": 2  # Corrección (index 2)
    },
    {
        "question": "¿Qué indica un valor alto en la métrica de diseño de clases \"Coupling Between Object Classes (CBO)\"?",
        "options": ["Una alta dependencia entre clases, lo que dificulta la modificación y reutilización del código.", "Una alta cohesión entre los métodos de la clase.", "Una baja dependencia de la jerarquía de herencia.", "Una buena encapsulación de los atributos de la clase."],
        "correct": 0  # Una alta dependencia entre clases (index 0)
    },
    {
        "question": "¿Qué herramienta basada en PLN se menciona en el texto para medir la calidad de los requisitos, basándose en problemas comunes de redacción?",
        "options": ["ARM Tool de la NASA.", "Visure Quality Analyzer.", "IBM DOORS.", "Enterprise Architect."],
        "correct": 1  # Visure Quality Analyzer (index 1)
    },
    {
        "question": "¿Cuál es el objetivo principal de las métricas de requisitos?",
        "options": ["Medir la velocidad de codificación de los programadores.", "Evaluar el rendimiento del software una vez implementado.", "Asegurar que los requisitos sean claros, completos, consistentes y trazables.", "Gestionar el presupuesto y el cronograma del proyecto"],
        "correct": 2  # Asegurar que los requisitos sean claros (index 2)
    },
    {
        "question": "¿Cuál de los siguientes factores se considera para ajustar la complejidad en el cálculo de Puntos de Función?",
        "options": ["La experiencia del analista de requisitos.", "El lenguaje de programación utilizado.", "Comunicación de Datos.", "El tamaño del equipo de pruebas."],
        "correct": 2  # Comunicación de Datos (index 2)
    },
    # Cuestionario sobre Refactorización de Código
    {
        "question": "La refactorización consiste en modificar el código fuente para mejorar su estructura interna sin alterar su comportamiento externo.",
        "options": ["Verdadero", "Falso"],
        "correct": 0  # Verdadero (index 0)
    },
    {
        "question": "El objetivo principal de la refactorización es corregir errores de funcionalidad en el código.",
        "options": ["Verdadero", "Falso"],
        "correct": 1  # Falso (index 1)
    },
    {
        "question": "La refactorización es una práctica recomendada solo para proyectos grandes.",
        "options": ["Verdadero", "Falso"],
        "correct": 1  # Falso (index 1)
    },
    {
        "question": "La refactorización mejora el rendimiento del código en todos los casos.",
        "options": ["Verdadero", "Falso"],
        "correct": 1  # Falso (index 1)
    },
    {
        "question": "\"Feature Envy\" es un code smell qué ocurre cuando un método de una clase accede con demasiada frecuencia a los datos de otra clase.",
        "options": ["Verdadero", "Falso"],
        "correct": 0  # Verdadero (index 0)
    },
    {
        "question": "¿Cuándo se debe realizar la refactorización en el desarrollo de software?",
        "options": ["Solo al final del ciclo de desarrollo.", "Únicamente cuando aparecen errores en producción", "De manera continua durante el desarrollo para mejorar la calidad del código.", "Solo cuando el equipo decida reescribir todo el código desde cero."],
        "correct": 2  # De manera continua... (index 2)
    },
    {
        "question": "¿Qué son los bloaters en el contexto de la refactorización de código?",
        "options": ["Patrones de diseño que mejoran la eficiencia del código.", "Secciones de código que han crecido demasiado y afectan la mantenibilidad.", "Técnicas para aumentar el rendimiento de un programa.", "Herramientas automatizadas para detectar errores en el código."],
        "correct": 1  # Secciones de código... (index 1)
    },
    {
        "question": "¿Por qué es importante acompañar la refactorización con pruebas?",
        "options": ["Porque ayuda a garantizar que la funcionalidad no se vea afectada.", "Porque reduce el tiempo de desarrollo sin importar los errores.", "Porque la refactorización siempre introduce nuevos errores.", "Porque evita la necesidad de documentar los cambios."],
        "correct": 0  # Porque ayuda a garantizar... (index 0)
    },
    {
        "question": "¿Qué es un \"Code smell\" en el contexto de la refactorización?",
        "options": ["Un error de sintaxis en el código que puede resolverse con una técnica de refactorización.", "Una indicación de que el código puede tener problemas de diseño que requieren refactorización.", "Una característica nueva añadida al código que resulta contradictoria con los principios de la refactorización.", "Una herramienta para depurar el código en busca de casos para la aplicación de refactorización."],
        "correct": 1  # Una indicación de que el código... (index 1)
    },
    {
        "question": "¿Qué técnica de refactorización se utiliza para mover una funcionalidad de una clase a otra más apropiada?",
        "options": ["Extract Class", "Move Method", "Inline Method", "Pull Up Method"],
        "correct": 1  # Move Method (index 1)
    },
    {
        "question": "¿Qué problema aborda la técnica \"Replace Magic Number with Symbolic Constant\"?",
        "options": ["El uso de números literales en el código que carecen de significado claro.", "La presencia de números complejos en el código.", "La utilización de constantes simbólicas en lugar de variables.", "El uso de números en comentarios del código."],
        "correct": 0  # El uso de números literales... (index 0)
    },
    {
        "question": "¿Cuál de los siguientes no es un code smell?",
        "options": ["Long Method", "Magic Numbers", "Single Parameter", "Feature Envy"],
        "correct": 2  # Single Parameter (index 2)
    },
    {
        "question": "¿Cuál es una ventaja de \"Inline Class\"?",
        "options": ["Simplifica el código al eliminar clases innecesarias.", "Hace que el código sea más modular.", "Duplica la lógica del programa en diferentes clases.", "Aumenta la dependencia entre clases."],
        "correct": 0  # Simplifica el código... (index 0)
    },
    {
        "question": "¿Cuál de las siguientes afirmaciones sobre la refactorización es falsa?",
        "options": ["Mejora la legibilidad del código.", "Siempre aumenta el rendimiento del software.", "Puede hacer que el código sea más difícil de mantener.", "Facilita el mantenimiento del código."],
        "correct": 1  # Siempre aumenta el rendimiento... (index 1)
    },
    {
        "question": "¿Cuál es un beneficio clave de la técnica \"Separate Query from Modifier\"?",
        "options": ["Evita efectos secundarios en consultas de datos.", "Permite cambiar el estado de los objetos más rápidamente.", "Reduce el número de clases en el código.", "Convierte todos los métodos en estáticos."],
        "correct": 0  # Evita efectos secundarios... (index 0)
    },
    {
        "question": "¿Cuál de los siguientes NO es un motivo para refactorizar código?",
        "options": ["Mejorar la mantenibilidad del código.", "Facilitar la incorporación de nuevas funcionalidades.", "Asegurar que el código compile sin errores.", "Reducir la complejidad del código."],
        "correct": 2  # Asegurar que el código compile... (index 2)
    },
    {
        "question": "¿Qué técnica ayuda a eliminar código repetitivo en múltiples clases?",
        "options": ["Extract Interface", "Push Down Method", "Pull Up Method", "Replace Conditional with Polymorphism"],
        "correct": 2  # Pull Up Method (index 2)
    },
    {
        "question": "¿Cuál es el riesgo de \"Cambiar Valor a Referencia\" si no se maneja bien?",
        "options": ["Puede provocar efectos colaterales si los objetos referenciados se modifican inesperadamente.", "Genera más copias de datos en memoria, lo que puede hacer que el programa sea más lento.", "Hace que cada objeto sea completamente independiente, lo que puede causar redundancia de datos.", "Obliga a usar estructuras de datos ineficientes para representar objetos."],
        "correct": 0  # Puede provocar efectos colaterales... (index 0)
    },
    # Cuestionario sobre Patrones de Diseño
    {
        "question": "¿Qué es un patrón de diseño en software?",
        "options": ["Un lenguaje de programación", "Un conjunto de reglas de sintaxis", "Una herramienta de depuración", "Una solución estandarizada a problemas comunes en desarrollo de software"],
        "correct": 3  # Una solución estandarizada... (index 3)
    },
    {
        "question": "¿Cuál de los siguientes NO es un beneficio de los patrones de diseño?",
        "options": ["Reutilización de soluciones", "Establecimiento de un vocabulario común", "Dependencia estricta de una tecnología específica", "Código más mantenible"],
        "correct": 2  # Dependencia estricta de una tecnología específica (index 2)
    },
    {
        "question": "¿Quiénes popularizaron los patrones de diseño en informática con el libro *Design Patterns*?",
        "options": ["Alan Turing", "Linus Torvalds", "Gang of Four (GoF)", "Donald Knuth"],
        "correct": 2  # Gang of Four (GoF) (index 2)
    },
    {
        "question": "¿Qué patrón de diseño se usa para garantizar que solo haya una única instancia de una clase?",
        "options": ["Factory Method", "Singleton", "Builder", "Prototype"],
        "correct": 1  # Singleton (index 1)
    },
    {
        "question": "¿Cuál de los siguientes patrones se usa para construir objetos paso a paso?",
        "options": ["Singleton", "Factory Method", "Prototype", "Builder"],
        "correct": 3  # Builder (index 3)
    },
    {
        "question": "¿El patrón *Abstract Factory* permite...?",
        "options": ["Crear una única instancia de una clase", "Construir objetos paso a paso", "Producir familias de objetos relacionados sin especificar clases concretas", "Clonar objetos existentes"],
        "correct": 2  # Producir familias de objetos... (index 2)
    },
    {
        "question": "¿Qué patrón permite a objetos con interfaces incompatibles trabajar juntos?",
        "options": ["Composite", "Adapter", "Proxy", "Facade"],
        "correct": 1  # Adapter (index 1)
    },
    {
        "question": "¿Cuál es la principal ventaja del patrón *Facade*?",
        "options": ["Proporciona una interfaz simplificada a un sistema complejo", "Minimiza el uso de memoria compartiendo objetos", "Controla el acceso a un objeto", "Desacopla una abstracción de su implementación"],
        "correct": 0  # Proporciona una interfaz simplificada... (index 0)
    },
    {
        "question": "¿Cuál es el propósito principal del patrón *Decorator*?",
        "options": ["Separar el comportamiento de la lógica de negocio", "Mejorar la estructura de clases en jerarquías", "Añadir responsabilidades a un objeto en tiempo de ejecución sin modificar su código fuente", "Evitar la creación de instancias innecesarias"],
        "correct": 2  # Añadir responsabilidades... (index 2)
    },
    {
        "question": "¿Qué patrón se usa para estructurar objetos en jerarquías tipo árbol?",
        "options": ["Composite", "Proxy", "Decorator", "Flyweight"],
        "correct": 0  # Composite (index 0)
    },
    {
        "question": "¿Cuál de los siguientes patrones se usa para encapsular una solicitud como un objeto?",
        "options": ["Command", "Observer", "State", "Mediator"],
        "correct": 0  # Command (index 0)
    },
    {
        "question": "¿Qué patrón define una dependencia uno-a-muchos entre objetos, notificando cambios automáticamente?",
        "options": ["Strategy", "Memento", "Observer", "Chain of Responsibility"],
        "correct": 2  # Observer (index 2)
    },
    {
        "question": "¿Cuál es el propósito del patrón *State*?",
        "options": ["Controlar el acceso a un objeto", "Permitir que un objeto cambie su comportamiento cuando cambia su estado interno", "Separar la creación de objetos en pasos", "Coordinar la comunicación entre múltiples objetos"],
        "correct": 1  # Permitir que un objeto cambie... (index 1)
    },
    {
        "question": "¿Cuál es la principal función del patrón *Strategy*?",
        "options": ["Controlar el ciclo de vida de un objeto", "Crear objetos a partir de prototipos", "Definir una familia de algoritmos intercambiables", "Administrar la memoria en objetos reutilizados"],
        "correct": 2  # Definir una familia de algoritmos... (index 2)
    },
    {
        "question": "¿Cuál de los siguientes patrones se usa para permitir que varios objetos manejen una solicitud sin que el emisor conozca cuál la procesará?",
        "options": ["Chain of Responsibility", "Mediator", "Command", "Memento"],
        "correct": 0  # Chain of Responsibility (index 0)
    },
    {
        "question": "¿Qué patrón permite guardar y restaurar el estado de un objeto sin afectar su encapsulación?",
        "options": ["Proxy", "Observer", "Strategy", "Memento"],
        "correct": 3  # Memento (index 3)
    },
    {
        "question": "¿Cuál es una buena práctica al aplicar patrones de diseño?",
        "options": ["Usarlos en cualquier parte del código sin análisis previo", "Reemplazar todas las estructuras existentes con patrones", "Comprender el problema antes de aplicar un patrón", "Evitar la reutilización de patrones en proyectos distintos"],
        "correct": 2  # Comprender el problema antes... (index 2)
    },
    {
        "question": "¿Cuál es un error común al usar patrones de diseño?",
        "options": ["No seguir el principio de abierto/cerrado", "Usar patrones innecesarios que aumentan la complejidad del código", "No encapsular objetos correctamente", "No aplicar la herencia en todos los casos"],
        "correct": 1  # Usar patrones innecesarios... (index 1)
    },
    {
        "question": "¿En qué situaciones es ideal aplicar el patrón *Visitor*?",
        "options": ["Cuando se necesita una única instancia de una clase", "Cuando se quiere añadir nuevas operaciones a una jerarquía sin modificar sus clases", "Cuando se requiere recorrer una colección sin exponer su estructura interna", "Cuando se quiere crear un objeto de manera eficiente"],
        "correct": 1  # Cuando se quiere añadir nuevas operaciones... (index 1)
    },
    {
        "question": "¿Cuál de los siguientes es un patrón de diseño creacional?",
        "options": ["Observer", "Prototype", "Decorator", "Chain of Responsibility"],
        "correct": 1  # Prototype (index 1)
    },
    # Cuestionario sobre Desarrollo Basado en Pruebas (TDD)
    {
        "question": "¿Cuál es el enfoque principal del Desarrollo Basado en Pruebas (TDD)?",
        "options": ["Escribir el código primero y luego las pruebas.", "Escribir las pruebas automatizadas antes del código.", "Escribir pruebas manuales después de la implementación.", "No escribir pruebas hasta la fase de integración."],
        "correct": 1  # Escribir las pruebas automatizadas antes del código (index 1)
    },
    {
        "question": "¿Cuál es el primer paso del ciclo de TDD?",
        "options": ["Escribir la prueba (Red).", "Escribir el código mínimo (Green).", "Refactorización (Refactor).", "Ejecutar todas las pruebas."],
        "correct": 0  # Escribir la prueba (Red) (index 0)
    },
    {
        "question": "¿Qué se espera que suceda inicialmente al ejecutar una prueba en el ciclo de TDD?",
        "options": ["La prueba debe pasar inmediatamente.", "La prueba debe fallar, confirmando que la funcionalidad aún no está implementada.", "La prueba debe generar un error de compilación.", "La prueba debe quedar en un estado pendiente."],
        "correct": 1  # La prueba debe fallar... (index 1)
    },
    {
        "question": "¿Cuál es el objetivo principal del paso (\"Green\") del ciclo de TDD?",
        "options": ["Escribir código completo y optimizado.", "Documentar exhaustivamente la funcionalidad.", "Escribir el código justo y solamente lo necesario para que la prueba pase.", "Realizar pruebas de integración con otros módulos."],
        "correct": 2  # Escribir el código justo... (index 2)
    },
    {
        "question": "En el contexto de TDD, ¿cuál es la distinción fundamental entre un \"mock\" y un \"stub\" al trabajar con dependencias de un componente bajo prueba?",
        "options": ["Un \"stub\" se utiliza para simular el comportamiento de un objeto devolviendo salidas predefinidas, mientras que un \"mock\" se centra en verificar que se hayan producido interacciones específicas con ese objeto.", "Un \"mock\" es una implementación simplificada de una dependencia con cierta lógica, mientras que un \"stub\" es un objeto que solo se utiliza para cumplir con la firma de un método sin funcionalidad real.", "Tanto los \"mocks\" como los \"stubs\" se utilizan para aislar el código bajo prueba, pero los \"mocks\" son más adecuados para probar unidades pequeñas y los \"stubs\" para probar integraciones entre componentes.", "Los \"stubs\" son más complejos de implementar ya que requieren definir un comportamiento específico, mientras que los \"mocks\" son objetos genéricos que registran interacciones."],
        "correct": 0  # Un "stub" se utiliza para simular... (index 0)
    },
    {
        "question": "¿Cuál de las siguientes es una ventaja principal de utilizar TDD?",
        "options": ["Aumenta el tiempo inicial de desarrollo significativamente.", "Genera una documentación extensa que siempre está desactualizada.", "Dificulta la refactorización del código existente.", "Detección Temprana de Errores."],
        "correct": 3  # Detección Temprana de Errores (index 3)
    },
    {
        "question": "¿Cómo actúan las pruebas automatizadas creadas con TDD?",
        "options": ["Como una guía para los testers manuales.", "Como una documentación preliminar del sistema.", "Como una documentación viva que describe el comportamiento esperado del sistema.", "Como un registro de los errores encontrados en el pasado."],
        "correct": 2  # Como una documentación viva... (index 2)
    },
    {
        "question": "¿Cómo fomenta TDD la creación de código?",
        "options": ["Con clases grandes y altamente acopladas.", "Más limpio y modular, con componentes pequeños y bien definidos.", "Con una gran cantidad de lógica compleja desde el inicio.", "Con un diseño rígido y difícil de modificar."],
        "correct": 1  # Más limpio y modular... (index 1)
    },
    {
        "question": "¿Qué se requiere para adoptar TDD de manera efectiva?",
        "options": ["Formar al equipo en buenas prácticas de escritura de pruebas y aceptar que el tiempo invertido en la fase inicial se traduce en menos tiempo dedicado a la depuración en el futuro.", "Escribir la mayor cantidad de pruebas posible sin importar su calidad.", "Enfocarse en probar solo las funcionalidades más críticas al final del desarrollo.", "No modificar las pruebas una vez que han sido escritas."],
        "correct": 0  # Formar al equipo en buenas prácticas... (index 0)
    },
    {
        "question": "¿Con qué metodologías ágiles encaja perfectamente TDD?",
        "options": ["TDD no se relaciona directamente con metodologías ágiles.", "Metodologías con una planificación exhaustiva a largo plazo.", "Metodologías que priorizan la documentación detallada antes de la codificación.", "Aquellas basadas en iteraciones rápidas y entregas continuas de software funcional."],
        "correct": 3  # Aquellas basadas en iteraciones rápidas... (index 3)
    },
    {
        "question": "¿Qué impacto tiene TDD en la calidad del software?",
        "options": ["Mejora la calidad al detectar errores de forma temprana y reducir el tiempo dedicado a depurar.", "Disminuye la calidad al enfocar el esfuerzo en las pruebas en lugar del código funcional.", "No tiene un impacto significativo en la calidad del software.", "La calidad depende completamente de la experiencia del desarrollador, independientemente de la metodología."],
        "correct": 0  # Mejora la calidad al detectar errores... (index 0)
    },
    {
        "question": "¿Qué diferencia principal existe entre TDD y las Pruebas Tradicionales?",
        "options": ["En TDD las pruebas son manuales y en las tradicionales son automatizadas.", "En las pruebas tradicionales se escriben pruebas unitarias y en TDD no.", "Primero las pruebas, luego el código en TDD, mientras que en las tradicionales es primero el código, luego las pruebas.", "Primero las pruebas, luego el código según las pruebas tradicionales, mientras que en TDD es primero el código, luego las pruebas."],
        "correct": 2  # Primero las pruebas, luego el código en TDD... (index 2)
    },
    {
        "question": "¿Cómo se alinea TDD con el proceso de diseño de software en un contexto ágil?",
        "options": ["Traduciendo criterios de aceptación simples en pruebas unitarias y repitiendo el ciclo hasta completar la aplicación.", "Definiendo toda la arquitectura del sistema antes de escribir cualquier prueba.", "Centrándose en la implementación del código y dejando las pruebas para el final de cada iteración.", "No existe una alineación específica entre TDD y el diseño ágil de software."],
        "correct": 0  # Traduciendo criterios de aceptación simples... (index 0)
    },
    {
        "question": "Dentro de los patrones de implementación de TDD se encuentra 'Fake it 'til you make it'. ¿En qué consiste este patrón de implementación?",
        "options": ["Este patrón se refiere a la idea de comenzar con una implementación mínima y luego ir mejorándola poco a poco, usando sustitutos temporales para partes del código que aún no están listas.", "Este patrón implica realizar una implementación completamente funcional desde el principio, sin importar que algunas partes del sistema aún no estén definidas.", "Este patrón se refiere a la creación de pruebas que se basan solo en datos estáticos sin necesidad de implementar el código real, y se evita escribir pruebas hasta tener la implementación completa.", "Este patrón sugiere que las pruebas deben escribir un código completamente detallado, sin necesidad de crear implementaciones mínimas para las pruebas."],
        "correct": 0  # Este patrón se refiere a la idea de comenzar... (index 0)
    },
    {
        "question": "¿Cuál es un principio de diseño de software relacionado con TDD?",
        "options": ["Alto acoplamiento entre componentes.", "Código complejo para abarcar todas las posibles funcionalidades futuras.", "El código debe funcionar, ser fácil de entender, tener mínima duplicación y ser lo más simple posible.", "Clases con múltiples responsabilidades para evitar la fragmentación del código."],
        "correct": 2  # El código debe funcionar, ser fácil de entender... (index 2)
    },
    {
        "question": "¿Cuál es una buena práctica en TDD relacionada con el número de pruebas por regla de negocio?",
        "options": ["Escribir la menor cantidad de pruebas posible para ahorrar tiempo.", "Una prueba por cada regla de negocio.", "Escribir una prueba que cubra múltiples reglas de negocio para mayor eficiencia.", "No existe una recomendación específica sobre el número de pruebas por regla de negocio."],
        "correct": 1  # Una prueba por cada regla de negocio (index 1)
    },
    {
        "question": "¿Cuál es el propósito principal de utilizar \"dobles de prueba\" en TDD?",
        "options": ["Aumentar la complejidad de las pruebas para simular escenarios más realistas.", "Probar la comunicación entre diferentes módulos del sistema en un entorno controlado.", "Simular colaboraciones entre objetos y facilitar el aislamiento del código a probar.", "Generar automáticamente una gran cantidad de casos de prueba para aumentar la cobertura."],
        "correct": 2  # Simular colaboraciones entre objetos... (index 2)
    },
    {
        "question": "¿Cómo contribuye TDD a la Integración Continua (CI) y la Entrega Continua (CD)?",
        "options": ["Al contar con un amplio conjunto de pruebas automatizadas que permiten detectar errores de integración de forma temprana y asegurar que el sistema sigue funcionando tras cada cambio.", "Al eliminar la necesidad de realizar pruebas de integración manuales en un entorno de CI/CD.", "Al simplificar el proceso de despliegue al garantizar que solo se entrega código probado manualmente.", "TDD no tiene una relación directa con las prácticas de Integración y Entrega Continua."],
        "correct": 0  # Al contar con un amplio conjunto... (index 0)
    },
    {
        "question": "¿Qué se sugiere como una estrategia para trabajar con código legado sin pruebas al adoptar TDD?",
        "options": ["Reemplazar todo el código existente con una nueva implementación basada en pruebas desde el inicio.", "Ignorar el código legado y enfocarse únicamente en aplicar TDD al nuevo código que se desarrolle.", "Identificar el punto de cambio, localizar puntos de inflexión y añadir cualquier tipo de prueba para empezar a tener cierta cobertura.", "Documentar exhaustivamente todo el código legado antes de intentar escribir cualquier prueba."],
        "correct": 2  # Identificar el punto de cambio... (index 2)
    },
    {
        "question": "¿Qué se recomienda para adoptar TDD con éxito?",
        "options": ["Enfocarse en lograr una cobertura de pruebas del 100% desde las primeras etapas del proyecto.", "Escribir la mayor cantidad de código funcional posible antes de comenzar a escribir las pruebas.", "Delegar la responsabilidad de escribir las pruebas a un equipo de QA independiente.", "Practicar continuamente, hacer de TDD el comportamiento por defecto y no escribir código sin una prueba que lo necesite."],
        "correct": 3  # Practicar continuamente... (index 3)
    },
    # Cuestionario sobre Documentación de Software
    {
        "question": "¿Por qué es importante escribir documentación en un proyecto software?",
        "options": ["Para reemplazar la necesidad de escribir buen código", "Para facilitar la incorporación de nuevos miembros al equipo", "Para llevar un control del trabajo del equipo de desarrollo", "Para evitar el uso de control de versiones"],
        "correct": 1  # Para facilitar la incorporación de nuevos miembros al equipo (index 1)
    },
    {
        "question": "¿Qué documento recoge los requisitos funcionales y no funcionales de un sistema?",
        "options": ["BRD", "ERS", "Manual de usuario", "Guía de estilos"],
        "correct": 1  # ERS (index 1)
    },
    {
        "question": "¿Cuál es el estándar principal para documentar pruebas de software?",
        "options": ["ISO/IEC 15289", "IEEE 829", "UML", "Guía de documentación de Google"],
        "correct": 1  # IEEE 829 (index 1)
    },
    {
        "question": "¿Qué herramienta permite generar automáticamente documentación de la estructura de una API?",
        "options": ["Swagger", "Doxygen", "UML", "AsciiDoc"],
        "correct": 0  # Swagger (index 0)
    },
    {
        "question": "¿Qué ocurre si la documentación se queda desactualizada?",
        "options": ["Mejora la calidad del código", "Incrementa la velocidad del desarrollo", "Genera confusión y errores", "No pasa nada"],
        "correct": 2  # Genera confusión y errores (index 2)
    },
    {
        "question": "¿Qué estándar define todos los documentos necesarios a lo largo del ciclo de vida del software?",
        "options": ["IEEE 830", "ISO/IEC 15289", "IEEE 831", "IEEE 829"],
        "correct": 1  # ISO/IEC 15289 (index 1)
    },
    {
        "question": "¿Qué herramienta es más comúnmente usada en proyectos Python para documentar?",
        "options": ["JavaDoc", "Docusaurus", "Sphinx", "MkDocs"],
        "correct": 2  # Sphinx (index 2)
    },
    {
        "question": "¿Qué representa un wireframe?",
        "options": ["El diseño gráfico final", "La estructura base de la interfaz de usuario", "El comportamiento backend", "El flujo de las pruebas unitarias"],
        "correct": 1  # La estructura base de la interfaz de usuario (index 1)
    },
    {
        "question": "¿Qué característica deben tener los comentarios en el código?",
        "options": ["Ser largos y explicativos", "Ser breves, claros y precisos", "Específicos para clases abstractas", "Solo necesarios en código de prueba"],
        "correct": 1  # Ser breves, claros y precisos (index 1)
    },
    {
        "question": "¿Qué debe incluir un plan de pruebas?",
        "options": ["Capturas de pantalla", "Estrategia, herramientas y criterios de aceptación", "Listado de bugs", "Listado de riesgos"],
        "correct": 1  # Estrategia, herramientas y criterios de aceptación (index 1)
    },
    {
        "question": "¿Qué contiene una historia de usuario?",
        "options": ["Solo requisitos técnicos", "Rol, acción, motivo y criterio de aceptación", "Código fuente", "Requisitos funcionales y no funcionales"],
        "correct": 1  # Rol, acción, motivo y criterio de aceptación (index 1)
    },
    {
        "question": "¿Cuál de los siguientes no es un lenguaje de marcado?",
        "options": ["AsciiDoc", "Markdown", "reStructuredText", "UML"],
        "correct": 3  # UML (index 3)
    },
    {
        "question": "¿Cuál de las siguientes es una guía de estilo reconocida?",
        "options": ["PostgreSQL Style Guide", "Microsoft Writing Style Guide", "Manual de Selenium", "PyDoc Manual"],
        "correct": 1  # Microsoft Writing Style Guide (index 1)
    },
    {
        "question": "¿Cuál es el objetivo principal de un manual de usuario?",
        "options": ["Describir la arquitectura interna", "Enseñar al usuario cómo utilizar el software", "Listar los bugs del sistema", "Mostrar la implementación de la API"],
        "correct": 1  # Enseñar al usuario cómo utilizar el software (index 1)
    },
    {
        "question": "¿Qué herramienta permite documentar, probar y compartir APIs en entornos colaborativos?",
        "options": ["Swagger", "JavaDoc", "Postman", "Selenium"],
        "correct": 2  # Postman (index 2)
    },
    {
        "question": "¿Cuál de los siguientes no es un diagrama UML?",
        "options": ["Diagrama de Clases", "Diagrama de Secuencia", "Diagrama de Requisitos", "Diagrama de Casos de Uso"],
        "correct": 2  # Diagrama de Requisitos (index 2)
    },
    {
        "question": "¿Para qué sirve un registro de errores?",
        "options": ["Desarrollar wireframes", "Documentar decisiones de diseño", "Registrar incidencias detectadas y soluciones aplicadas", "Mostrar el historial de versiones"],
        "correct": 2  # Registrar incidencias detectadas y soluciones aplicadas (index 2)
    },
    {
        "question": "¿Qué propone el modelo C4?",
        "options": ["Estandarizar casos de prueba", "Documentar arquitectura en distintos niveles de abstracción", "Medir rendimiento de aplicaciones", "Gestionar APIs externas"],
        "correct": 1  # Documentar arquitectura en distintos niveles de abstracción (index 1)
    },
    {
        "question": "¿Qué debe contener un caso de prueba?",
        "options": ["Solo el resultado esperado", "Diagrama de flujo de la prueba", "ID, descripción, precondiciones, entradas, pasos y resultados esperados", "Lista de errores históricos"],
        "correct": 2  # ID, descripción, precondiciones, entradas, pasos y resultados esperados (index 2)
    },
    {
        "question": "¿Cuál es un problema habitual en la documentación de software?",
        "options": ["Usar herramientas modernas", "Tener documentación desincronizada con el código fuente", "Generar documentación automática", "Demasiada documentación"],
        "correct": 1  # Tener documentación desincronizada con el código fuente (index 1)
    },
    # Cuestionario sobre Contenerización de Aplicaciones
    {
        "question": "¿Qué es la contenerización de aplicaciones?",
        "options": ["Proceso de ejecutar software en la nube", "Virtualización completa de hardware", "Empaquetar aplicaciones y dependencias en contenedores", "Ejecutar múltiples sistemas operativos a la vez"],
        "correct": 2  # Empaquetar aplicaciones y dependencias en contenedores (index 2)
    },
    {
        "question": "¿Qué elemento es fundamental en un contenedor?",
        "options": ["Máquina virtual", "BIOS", "Imagen", "Kernel externo"],
        "correct": 2  # Imagen (index 2)
    },
    {
        "question": "¿Cuál es una ventaja clave de los contenedores?",
        "options": ["Uso eficiente de recursos", "Mayor peso que las máquinas virtuales", "Menor portabilidad", "Requieren más sistema operativo"],
        "correct": 0  # Uso eficiente de recursos (index 0)
    },
    {
        "question": "¿Qué diferencia a un contenedor de una VM?",
        "options": ["Los contenedores incluyen su propio kernel", "Las VMs no requieren hipervisor", "Los contenedores comparten el kernel del host", "Las VMs son más ligeras"],
        "correct": 2  # Los contenedores comparten el kernel del host (index 2)
    },
    {
        "question": "¿Qué herramienta es la más usada para contenerización?",
        "options": ["Docker", "VMware", "VirtualBox", "Git"],
        "correct": 0  # Docker (index 0)
    },
    {
        "question": "¿Qué es una imagen en Docker?",
        "options": ["Una foto del contenedor", "Una plantilla inmutable con todo lo necesario para correr una app", "Una copia del sistema operativo", "Un archivo de logs"],
        "correct": 1  # Una plantilla inmutable con todo lo necesario para correr una app (index 1)
    },
    {
        "question": "¿Qué comando lanza un contenedor desde una imagen en Docker?",
        "options": ["docker build", "docker ps", "docker run", "docker pull"],
        "correct": 2  # docker run (index 2)
    },
    {
        "question": "¿Qué son los namespaces en Linux?",
        "options": ["Aíslan recursos como procesos y redes en contenedores", "Sistemas de archivos", "Tipos de usuarios", "Conjuntos de puertos"],
        "correct": 0  # Aíslan recursos como procesos y redes en contenedores (index 0)
    },
    {
        "question": "¿Qué gestionan los cgroups?",
        "options": ["Usuarios y permisos", "Recursos como CPU, memoria y disco", "Versiones de kernel", "Redes"],
        "correct": 1  # Recursos como CPU, memoria y disco (index 1)
    },
    {
        "question": "¿Qué tipo de almacenamiento persiste tras eliminar un contenedor?",
        "options": ["Memoria RAM", "Volumen", "Bind Mount", "Cache"],
        "correct": 1  # Volumen (index 1)
    },
    {
        "question": "¿Qué tipo de red Docker aísla completamente al contenedor?",
        "options": ["None", "Host", "Overlay", "Bridge"],
        "correct": 0  # None (index 0)
    },
    {
        "question": "¿Qué permite Docker Compose?",
        "options": ["Definir múltiples servicios en un solo archivo", "Crear interfaces gráficas", "Compilar imágenes", "Acceder a la nube"],
        "correct": 0  # Definir múltiples servicios en un solo archivo (index 0)
    },
    {
        "question": "¿Qué ventaja tiene contenerizar microservicios?",
        "options": ["Monitoreo más complejo", "Escalabilidad y despliegue independiente", "Más dependencias", "Menor portabilidad"],
        "correct": 1  # Escalabilidad y despliegue independiente (index 1)
    },
    {
        "question": "¿Cuál es la diferencia entre imagen y contenedor?",
        "options": ["Ninguna, son sinónimos", "Imagen es la plantilla; contenedor es la instancia en ejecución", "Imagen contiene datos; contenedor no", "Contenedor es más grande que la imagen"],
        "correct": 1  # Imagen es la plantilla; contenedor es la instancia en ejecución (index 1)
    },
    {
        "question": "¿Qué comando se usa para ver contenedores en ejecución?",
        "options": ["docker run", "docker ps", "docker build", "docker exec"],
        "correct": 1  # docker ps (index 1)
    },
    {
        "question": "¿Qué gestor de contenedores no requiere daemon y es rootless?",
        "options": ["Docker", "Podman", "LXC", "VirtualBox"],
        "correct": 1  # Podman (index 1)
    },
    {
        "question": "¿Qué permite almacenar imágenes?",
        "options": ["Dockerfile", "Registro (registry)", "Volumen", "Kernel"],
        "correct": 1  # Registro (registry) (index 1)
    },
    {
        "question": "¿Qué es Containerd?",
        "options": ["Es una imágen de Docker", "Herramienta para debug", "Runtime ligero para ejecutar contenedores", "Interfaz gráfica de Docker"],
        "correct": 2  # Runtime ligero para ejecutar contenedores (index 2)
    },
    {
        "question": "¿Qué contiene un Dockerfile?",
        "options": ["Instrucciones para construir una imagen", "Datos de ejecución del contenedor", "Logs del sistema", "Información del sistema host"],
        "correct": 0  # Instrucciones para construir una imagen (index 0)
    },
    {
        "question": "¿Qué hace el comando docker pull?",
        "options": ["Inicia un contenedor", "Detiene una imagen", "Descarga una imagen del registro", "Ejecuta una red"],
        "correct": 2  # Descarga una imagen del registro (index 2)
    },
    # Cuestionario sobre Integración Continua y Despliegue Continuo (CI/CD)
    {
        "question": "El despliegue continuo es ...",
        "options": ["una estrategia de desarrollo en la que los cambios de código de la aplicación se publican automáticamente al entorno de producción tras pasar una serie de pruebas predefinidas.", "una técnica de diseño gráfico que permite optimizar la resolución de las imágenes antes del despliegue del sitio web.", "un proceso manual en el que los desarrolladores publican actualizaciones solo después de completar todo el ciclo de desarrollo y aprobación por parte del equipo de marketing.", "una metodología de respaldo que almacena copias del código fuente cada vez que un desarrollador guarda un archivo."],
        "correct": 0  # una estrategia de desarrollo... (index 0)
    },
    {
        "question": "¿Cuál de las siguientes herramientas se utiliza comúnmente para la integración continua y despliegue continuo (CI/CD)?",
        "options": ["MySQL.", "GitHub Actions.", "Bootstrap.", "Nginx."],
        "correct": 1  # GitHub Actions (index 1)
    },
    {
        "question": "Señala la opción incorrecta:",
        "options": ["En la etapa de seguridad, en la etapa de compilación y pruebas, el código se convierte en ejecutable y se validan sus funcionalidades.", "DAST (Dynamic Application Security Testing) analiza la aplicación mientras está en ejecución.", "SAST (Static Application Security Testing) analiza el código sin ejecutarlo.", "Se deben usar credenciales en archivos de configuración."],
        "correct": 3  # Se deben usar credenciales en archivos de configuración (index 3)
    },
    {
        "question": "¿Cuál de las siguientes afirmaciones es una buena práctica del despliegue del continuo de aplicaciones?",
        "options": ["Uso de credenciales en archivos de configuración.", "No verificar cambios en código de terceros.", "Uso de repositorios privados con control de acceso."],
        "correct": 2  # Uso de repositorios privados con control de acceso (index 2)
    },
    {
        "question": "El archivo de configuración de GitHub Actions suele tener extensión _.exe_.",
        "options": ["Verdadero.", "Falso (Se usa YAML, por ejemplo: .yml)."],
        "correct": 1  # Falso (Se usa YAML, por ejemplo: .yml) (index 1)
    },
    {
        "question": "¿Cuál de las siguientes opciones es un beneficio de CI/CD seguro?",
        "options": ["Incrementa la cantidad de pruebas visuales que se deben realizar manualmente antes del lanzamiento.", "Aumenta el número de líneas de código escritas por el equipo cada día.", "Reducción de riesgos de ataques y fugas de datos.", "Mejora la calidad del diseño gráfico en la interfaz de usuario."],
        "correct": 2  # Reducción de riesgos de ataques y fugas de datos (index 2)
    },
    {
        "question": "Un rollback es ...",
        "options": ["el proceso de realizar pruebas de seguridad adicionales en una nueva versión antes de lanzarla.", "el proceso de volver a una versión anterior de la aplicación cuando una actualización presenta problemas.", "la acción de compilar el código fuente para crear una nueva versión de la aplicación.", "el proceso de agregar nuevas funcionalidades a una aplicación sin necesidad de realizar pruebas"],
        "correct": 1  # el proceso de volver a una versión anterior... (index 1)
    },
    {
        "question": "Con un Feature branching:",
        "options": ["Cada funcionalidad se desarrolla en una rama separada.", "Se trabaja directamente en la rama main para una implementación directa.", "Se crean pull request sin revisión previa.", "Se hace un commit and push en la rama main cada vez que se realiza un cambio."],
        "correct": 0  # Cada funcionalidad se desarrolla en una rama separada (index 0)
    },
    {
        "question": "¿Qué significa CI en desarrollo de software?",
        "options": ["Código Interactivo.", "Comunicación Inmediata.", "Integración Continua.", "Instalación Controlada."],
        "correct": 2  # Integración Continua (index 2)
    },
    {
        "question": "Github actions se utiliza para …",
        "options": ["la creación de bases de datos en la nube sin necesidad de configuración.", "el despliegue de páginas estáticas.", "la automatización de la integración de diseño gráfico en la aplicación.", "gestionar la documentación en producción."],
        "correct": 1  # el despliegue de páginas estáticas (index 1)
    },
    {
        "question": "¿Qué es una pipeline?",
        "options": ["Un servidor.", "Una app móvil.", "Una serie de pasos automatizados.", "Un lenguaje de programación."],
        "correct": 2  # Una serie de pasos automatizados (index 2)
    },
    {
        "question": "¿Cuál no es un beneficio del CI/CD seguro?",
        "options": ["Reducción de ataques y fugas de datos.", "Codigo más bonito.", "Mayor confianza en la estabilidad del código.", "Cumplimientos de normativas y estándares de calidad."],
        "correct": 1  # Codigo más bonito (index 1)
    },
    {
        "question": "¿Por qué no se sube un archivo _node_modules_ a un repositorio común?",
        "options": ["Porque contiene archivos sensibles como contraseñas y claves de API.", "Es un archivo muy pesado.", "Porque no se puede acceder a él desde sistemas operativos diferentes a Linux.", "Porque se genera automáticamente."],
        "correct": 1  # Es un archivo muy pesado (index 1)
    },
    {
        "question": "En un sistema centralizado …",
        "options": ["Cada persona guarda sus cambios.", "Todos los cambios se guardan en un único lugar, obligando a una conexión constante.", "Los cambios se almacenan en múltiples servidores dispersos para mayor seguridad y disponibilidad.", "Los cambios nunca están visibles para los usuarios."],
        "correct": 1  # Todos los cambios se guardan en un único lugar... (index 1)
    },
    {
        "question": "¿Qué hace el comando _npm install_?",
        "options": ["Eliminar todas las dependencias de la aplicación.", "Limpiar el directorio.", "Instalar las dependencias indicadas en el package.json.", "Inicializar todas las variables de la aplicación."],
        "correct": 2  # Instalar las dependencias indicadas en el package.json (index 2)
    },
    {
        "question": "Los pipelines en CI se ejecutan automáticamente tras detectar cambios.",
        "options": ["Verdadero.", "Falso."],
        "correct": 0  # Verdadero (index 0)
    },
    {
        "question": "El Despliegue continuo y la entrega continua:",
        "options": ["son lo mismo.", "el despliegue continuo necesita interacción manual para publicar los cambios a producción y la entrega continua no.", "La entrega continua necesita interacción manual para publicar los cambios a producción y el despliegue continuo no.", "El despliegue continuo despliega los cambios a producción si se pasan unas pruebas, y la entrega continua verifica los cambios para poder integrarlos a la rama principal de un repositorio compartido."],
        "correct": 2  # La entrega continua necesita interacción manual... (index 2)
    },
    {
        "question": "¿Cuál es un área crítica de seguridad?",
        "options": ["La interfaz gráfica.", "El código fuente, compilación, pruebas y despliegue.", "La estructura de la aplicación.", "Los estilos visuales de la aplicación."],
        "correct": 1  # El código fuente, compilación, pruebas y despliegue (index 1)
    },
    {
        "question": "¿Github se utiliza para el control de versiones?",
        "options": ["Verdadero.", "Falso."],
        "correct": 0  # Verdadero (index 0)
    },
    {
        "question": "¿Cuál no es una herramienta de CI/CD completa?",
        "options": ["Gitlab.", "Jenkins.", "Cloudfare.", "Travis CI."],
        "correct": 2  # Cloudfare (index 2)
    },
    # Cuestionario sobre Aspectos Legales y Éticos en el Desarrollo de Software
    {
        "question": "¿Cuál es el objetivo principal de los aspectos legales y éticos en el desarrollo de software?",
        "options": ["Aumentar los beneficios de las empresas de software.", "Proteger a los usuarios, la sociedad y la integridad profesional.", "Agilizar el proceso de desarrollo de software.", "Reducir los costes de producción del software."],
        "correct": 1  # Proteger a los usuarios, la sociedad y la integridad profesional (index 1)
    },
    {
        "question": "¿Qué tipo de obligaciones imponen los aspectos legales en el desarrollo de software?",
        "options": ["Valores y principios morales.", "Obligaciones que impone la ley (como protección de datos).", "Decisiones responsables sin base legal.", "Normas establecidas por las empresas."],
        "correct": 1  # Obligaciones que impone la ley (como protección de datos) (index 1)
    },
    {
        "question": "¿Qué orientan los aspectos éticos en el desarrollo de software?",
        "options": ["El cumplimiento estricto de las leyes.", "Valores y principios que orientan las decisiones responsables.", "La maximización de la eficiencia técnica.", "Los requisitos del cliente sin considerar las consecuencias."],
        "correct": 1  # Valores y principios que orientan las decisiones responsables (index 1)
    },
    {
        "question": "¿En qué áreas críticas interviene el software que requieren estándares éticos?",
        "options": ["Redes sociales y videojuegos.", "Salud, seguridad aérea, educación o finanzas.", "Diseño gráfico y marketing online.", "Comunicación personal y entretenimiento."],
        "correct": 1  # Salud, seguridad aérea, educación o finanzas (index 1)
    },
    {
        "question": "¿Qué organizaciones se dieron cuenta de la urgencia de definir estándares éticos en los años noventa?",
        "options": ["Microsoft y Apple.", "IEEE Computer Society y la ACM.", "Google y Facebook.", "Amazon y Netflix."],
        "correct": 1  # IEEE Computer Society y la ACM (index 1)
    },
    {
        "question": "¿Cómo se llama el código de ética resultado del trabajo conjunto de ACM e IEEE?",
        "options": ["Código de Buenas Prácticas de Software.", "Software Engineering Code of Ethics and Professional Practice.", "Estándares Legales del Desarrollo de Software.", "Guía Ética para Ingenieros Informáticos."],
        "correct": 1  # Software Engineering Code of Ethics and Professional Practice (index 1)
    },
    {
        "question": "¿Qué organización adoptó y tradujo el código de la ACM/IEEE al contexto hispanohablante?",
        "options": ["IEEE España.", "ACM Latinoamérica.", "SISTEDES.", "ISO Software."],
        "correct": 2  # SISTEDES (index 2)
    },
    {
        "question": "¿Qué tipo de retos éticos plantea la aparición de la inteligencia artificial?",
        "options": ["Retos relacionados únicamente con la velocidad de procesamiento.", "Retos puramente técnicos sin implicaciones sociales.", "Preguntas sobre la responsabilidad en errores y la garantía de no reproducción de sesgos.", "Desafíos centrados en la interfaz de usuario."],
        "correct": 2  # Preguntas sobre la responsabilidad en errores... (index 2)
    },
    {
        "question": "¿En cuántos principios éticos fundamentales está dividido el Código de Ética y Conducta Profesional de ACM (v5.2)?",
        "options": ["Seis.", "Siete.", "Ocho.", "Nueve."],
        "correct": 2  # Ocho (index 2)
    },
    {
        "question": "¿Cuál es el eje principal del Código de Ética y Conducta Profesional de ACM?",
        "options": ["La eficiencia en el desarrollo de software.", "La satisfacción del cliente.", "El interés público.", "El beneficio económico de la empresa."],
        "correct": 2  # El interés público (index 2)
    },
    {
        "question": "¿Qué enfatiza el código ético de SISTEDES además de los principios generales?",
        "options": ["La rapidez en la entrega de proyectos.", "El uso exclusivo de tecnologías patentadas.", "La educación ética y el uso de ejemplos reales.", "La minimización de la documentación técnica."],
        "correct": 2  # La educación ética y el uso de ejemplos reales (index 2)
    },
    {
        "question": "¿Cuál es uno de los principales propósitos de un código de ética como el de ACM/IEEE o SISTEDES?",
        "options": ["Facilitar la competencia desleal entre empresas.", "Proteger al público y al usuario frente a posibles daños.", "Limitar la innovación en el desarrollo de software.", "Favorecer los intereses empresariales por encima de todo."],
        "correct": 1  # Proteger al público y al usuario frente a posibles daños (index 1)
    },
    {
        "question": "¿Qué principio ético universal destaca la importancia de proteger la seguridad, la salud y el bienestar social?",
        "options": ["Honestidad y veracidad.", "Interés público.", "Minimización de riesgos.", "Protección de derechos fundamentales."],
        "correct": 1  # Interés público (index 1)
    },
    {
        "question": "¿Qué exige el principio de no maleficencia en el desarrollo de software?",
        "options": ["Maximizar los beneficios económicos a toda costa.", "Diseñar y mantener software seguro y libre de fallos graves.", "Ignorar las posibles consecuencias negativas del software.", "Entregar el software lo más rápido posible sin pruebas exhaustivas."],
        "correct": 1  # Diseñar y mantener software seguro y libre de fallos graves (index 1)
    },
    {
        "question": "¿Qué implica la responsabilidad profesional en el ejercicio de la profesión del software?",
        "options": ["Actuar únicamente según las directrices de la empresa.", "Ignorar las normas éticas y legales si dificultan el trabajo.", "Actuar conforme a normas éticas y legales, y reconocer limitaciones personales.", "Ocultar los fallos de seguridad para evitar problemas."],
        "correct": 2  # Actuar conforme a normas éticas y legales... (index 2)
    },
    {
        "question": "En el caso de Occidental Engineering, ¿qué problema técnico crítico se descubrió en el prototipo Safe Skies?",
        "options": ["Problemas de interfaz de usuario.", "Un fallo donde un avión podía desaparecer del sistema cuando había demasiados.", "Lentitud en el procesamiento de datos.", "Incompatibilidad con sistemas operativos."],
        "correct": 1  # Un fallo donde un avión podía desaparecer... (index 1)
    },
    {
        "question": "En el caso de subcontratación en Lesak, ¿qué parentesco tenía la vicepresidenta de MBE Design Group con el dueño de Lesak?",
        "options": ["Era su esposa.", "Era su hermana.", "Era su hija.", "Era su prima."],
        "correct": 2  # Era su hija (index 2)
    },
    {
        "question": "¿Qué tecnología permitía el sistema TTWI (Through-the-Wall Imaging) en el Caso 3?",
        "options": ["Escuchar conversaciones a través de paredes.", "Ver a través de paredes usando radar de impulsos.", "Desactivar sistemas electrónicos a distancia.", "Camuflar objetos haciéndolos invisibles."],
        "correct": 1  # Ver a través de paredes usando radar de impulsos (index 1)
    },
    {
        "question": "Según el Principio 1.3 del Código ACM, ¿qué se debe proporcionar sobre las capacidades, limitaciones y riesgos del software?",
        "options": ["Información técnica detallada solo para expertos.", "Información completa de manera honesta y confiable.", "Información mínima para no alarmar a los usuarios.", "Información optimista exagerando las funcionalidades."],
        "correct": 1  # Información completa de manera honesta y confiable (index 1)
    },
    {
        "question": "¿Qué busca el enfoque \"ethical by design\" en el desarrollo de software?",
        "options": ["Añadir consideraciones éticas al final del proyecto.", "Integrar principios éticos en cada etapa del desarrollo desde el diseño.", "Externalizar la responsabilidad ética a un equipo especializado.", "Cumplir con los requisitos funcionales sin considerar la ética."],
        "correct": 1  # Integrar principios éticos en cada etapa... (index 1)
    },
    # Cuestionario sobre Securización de aplicaciones web
    {
        "question": "¿Cuál de los siguientes es un pilar del modelo CIA en seguridad?",
        "options": ["Compatibilidad", "Integridad", "Accesibilidad", "Escalabilidad"],
        "correct": 1  # Integridad (index 1)
    },
    {
        "question": "¿Cuál de los siguientes es un ejemplo de autenticación multifactor?",
        "options": ["Contraseña compleja", "SMS con código", "Nombre de usuario", "Captcha"],
        "correct": 1  # SMS con código (index 1)
    },
    {
        "question": "Verdadero o falso: \"Las cookies HttpOnly pueden ser accedidas mediante JavaScript en el navegador.\"",
        "options": ["Verdadero", "Falso"],
        "correct": 1  # Falso (index 1)
    },
    {
        "question": "Verdadero o falso: \"El uso de eval() en JavaScript es una buena práctica de seguridad.\"",
        "options": ["Verdadero", "Falso"],
        "correct": 1  # Falso (index 1)
    },
    {
        "question": "¿Qué herramienta permite la autenticación sin contraseña usando biometría?",
        "options": ["OAuth", "WebAuthn", "LDAP", "JWT"],
        "correct": 1  # WebAuthn (index 1)
    },
    {
        "question": "¿Qué cabecera permite controlar los orígenes permitidos en CORS?",
        "options": ["Access-Control-Allow-Origin", "Referrer-Policy", "Content-Type", "X-CORS-Token"],
        "correct": 0  # Access-Control-Allow-Origin (index 0)
    },
    {
        "question": "¿Qué opción describe mejor el concepto de \"Confianza cero\"?",
        "options": ["Permitir acceso local", "Validar solo usuarios externos", "Verificar siempre, sin asumir confianza", "Depender del firewall"],
        "correct": 2  # Verificar siempre, sin asumir confianza (index 2)
    },
    {
        "question": "¿Cuál de estos no es parte de un JSON Web Token (JWT)?",
        "options": ["Header", "Payload", "Footer", "Signature"],
        "correct": 2  # Footer (index 2)
    },
    {
        "question": "¿Qué herramienta analiza código sin ejecutarlo (SAST)?",
        "options": ["Burp Suite", "ZAP", "SonarQube", "Nmap"],
        "correct": 2  # SonarQube (index 2)
    },
    {
        "question": "¿Qué mecanismo evita el almacenamiento de secretos en código?",
        "options": ["SAST", "Vault", "HSTS", "CSRF"],
        "correct": 1  # Vault (index 1)
    },
    {
        "question": "¿Cuál es el objetivo del principio de mínimo privilegio?",
        "options": ["Proporcionar máximo acceso", "Compartir credenciales", "Restringir el acceso solo a lo necesario", "Mantener sesiones activas"],
        "correct": 2  # Restringir el acceso solo a lo necesario (index 2)
    },
    {
        "question": "¿Qué vulnerabilidad se caracteriza por inyectar scripts maliciosos en el navegador?",
        "options": ["CSRF", "XSS", "Broken Access Control", "SSRF"],
        "correct": 1  # XSS (index 1)
    },
    {
        "question": "¿Cuál es una práctica recomendada para manejar tokens de acceso?",
        "options": ["Almacenarlos en localStorage", "No cifrarlos", "Usar HTTPS y expiración corta", "Compartir por URL"],
        "correct": 2  # Usar HTTPS y expiración corta (index 2)
    },
    {
        "question": "¿Qué protocolo proporciona autenticación y autorización federada?",
        "options": ["JWT", "OAuth + OpenID Connect", "API Key", "TLS"],
        "correct": 1  # OAuth + OpenID Connect (index 1)
    },
    {
        "question": "¿Qué opción representa una medida de seguridad para el frontend?",
        "options": ["Uso de innerHTML", "Cookies sin restricciones", "Uso de CSP y headers de seguridad", "Permitir scripts externos sin control"],
        "correct": 2  # Uso de CSP y headers de seguridad (index 2)
    },
    {
        "question": "¿Qué es un ataque de relleno de credenciales?",
        "options": ["Inyección de SQL", "Uso de contraseñas robadas en múltiples sitios", "Suplantación de IP", "Sobrecarga del servidor"],
        "correct": 1  # Uso de contraseñas robadas en múltiples sitios (index 1)
    },
    {
        "question": "¿Qué tipo de prueba permite descubrir rutas y parámetros ocultos?",
        "options": ["SAST", "Pentesting manual", "Linter", "Firewall"],
        "correct": 1  # Pentesting manual (index 1)
    },
    {
        "question": "Verdadero o falso: \"WebAuthn permite autenticación sin contraseña.\"",
        "options": ["Verdadero", "Falso"],
        "correct": 1  # Falso (index 1)
    },
    {
        "question": "¿Qué estándar regula la seguridad en pagos con tarjeta?",
        "options": ["GDPR", "PCI-DSS", "HIPAA", "ISO 27001"],
        "correct": 1  # PCI-DSS (index 1)
    },
    # Cuestionario sobre Ingeniería Inversa
    {
        "question": "¿En qué consiste el desensamblado de un código?",
        "options": ["Programa escrito en un lenguaje de alto nivel se traduce a un lenguaje de bajo nivel", "Convierte el binario en instrucciones de lenguaje ensamblador", "Traduce el código en lenguaje de alto nivel a lenguaje binario", "Herramienta que traduce un archivo de código binario a un lenguaje de alto nivel, intentando reconstruir el código fuente original"],
        "correct": 1  # Convierte el binario en instrucciones de lenguaje ensamblador (index 1)
    },
    {
        "question": "¿En qué consiste la descompilación de un código?",
        "options": ["Traduce el código en lenguaje de alto nivel a lenguaje binario", "Convierte el binario en instrucciones de lenguaje ensamblador", "Herramienta que traduce un archivo de código binario a un lenguaje de alto nivel, intentando reconstruir el código fuente original", "Programa escrito en un lenguaje de alto nivel se traduce a un lenguaje de bajo nivel"],
        "correct": 2  # Herramienta que traduce un archivo de código binario a un lenguaje de alto nivel... (index 2)
    },
    {
        "question": "¿En qué consiste la compilación de un código?",
        "options": ["Programa escrito en un lenguaje de alto nivel se traduce a un lenguaje de bajo nivel", "Herramienta que traduce un archivo de código binario a un lenguaje de alto nivel, intentando reconstruir el código fuente original", "Convierte el binario en instrucciones de lenguaje de ensamblador", "Traduce el código en lenguaje de alto nivel a lenguaje binario"],
        "correct": 0  # Programa escrito en un lenguaje de alto nivel se traduce a un lenguaje de bajo nivel (index 0)
    },
    {
        "question": "¿En qué consiste el ensamblado de un código?",
        "options": ["Herramienta que traduce un archivo de código binario a un lenguaje de alto nivel, intentando reconstruir el código fuente original", "Traduce el código en lenguaje de alto nivel a lenguaje binario", "Programa escrito en un lenguaje de alto nivel se traduce a un lenguaje de bajo nivel", "Convierte el binario en instrucciones de lenguaje ensamblador"],
        "correct": 3  # Convierte el binario en instrucciones de lenguaje ensamblador (index 3)
    },
    {
        "question": "¿Qué es la EULA?",
        "options": ["Contrato legal que el usuario acepta antes de utilizar un software", "Protocolo de seguridad utilizado en redes privadas", "Lenguaje de programación orientado a objetos", "Tipo de licencia libre para distribuir contenido multimedia"],
        "correct": 0  # Contrato legal que el usuario acepta antes de utilizar un software (index 0)
    },
    {
        "question": "¿Qué protegen los derechos de autor en el contexto del software?",
        "options": ["La estructura lógica y los métodos subyacentes del software, como los algoritmos y las rutinas de procesamiento de datos.", "La expresión concreta del programa, en su forma de código fuente y ejecutable, pero no los métodos o ideas que subyacen en él.", "Los diseños arquitectónicos del hardware utilizado para ejecutar el software, incluyendo la disposición de sus componentes físicos.", "La especificación y los protocolos de comunicación utilizados por el software para la interacción en redes y la transmisión de datos."],
        "correct": 1  # La expresión concreta del programa... (index 1)
    },
    {
        "question": "¿Qué es la propiedad intelectual?",
        "options": ["Es un conjunto de normas que regulan la propiedad física de los bienes muebles e inmuebles.", "Es el derecho exclusivo que tiene el Estado para explotar comercialmente las ideas desarrolladas dentro de sus fronteras.", "Es el conjunto de requisitos que se deben cumplir para poder trabajar en algunos proyectos.", "Conjunto de derechos que protegen las creaciones del intelecto, como invenciones, marcas y secretos industriales."],
        "correct": 3  # Conjunto de derechos que protegen las creaciones del intelecto... (index 3)
    },
    {
        "question": "¿Qué es la ingeniería inversa en el contexto del software?",
        "options": ["Un proceso que implica la creación de una versión funcional de un software a partir de su código fuente disponible, sin modificar su estructura interna.", "El análisis y descomposición de un producto de software para extraer sus componentes y entender su funcionamiento, con el fin de crear un software compatible o mejorar el original.", "La reimplementación de un software a partir de su especificación funcional, sin tener acceso a su código fuente o componentes internos.", "Un enfoque que busca mejorar el rendimiento de un software mediante la manipulación de su código ejecutable para optimizar su eficiencia sin alterar su funcionalidad."],
        "correct": 1  # El análisis y descomposición de un producto de software... (index 1)
    },
    {
        "question": "¿En cuál de los siguientes casos podría contradecirse legalmente una cláusula de una licencia de software?",
        "options": ["Aunque el usuario no haya leído la licencia, la instalación del software implica aceptación tácita, por lo que debe cumplirla en su totalidad.", "Si el software se utiliza únicamente con fines educativos, cualquier cláusula puede ignorarse por motivos pedagógicos.", "Cuando una cláusula vulnera derechos reconocidos por la legislación vigente, como el derecho a realizar ingeniería inversa para lograr interoperabilidad.", "Bajo ninguna circunstancia puede desobedecer una cláusula contractual si el usuario ha aceptado la licencia, independientemente de su contenido."],
        "correct": 2  # Cuando una cláusula vulnera derechos reconocidos... (index 2)
    },
    {
        "question": "¿Cuál no es el fin ético de la ingeniería inversa?",
        "options": ["Garantizar la interoperabilidad de sistemas.", "Vulnerar protecciones para obtener ventajas económicas.", "Reparar o mejorar software/hardware sin soporte oficial.", "Detectar vulnerabilidades en productos para mejorar la seguridad."],
        "correct": 1  # Vulnerar protecciones para obtener ventajas económicas (index 1)
    },
    {
        "question": "¿Cuáles son las principales fases de la ingeniería inversa?",
        "options": ["Diseño, compilación, validación y distribución, centradas en reproducir el software original con mejoras funcionales.", "Captura, edición, reconstrucción y despliegue, orientadas a modificar el comportamiento del software sin analizar su estructura.", "Análisis estático, desensamblado, documentación y modelado, enfocadas en entender el funcionamiento interno sin acceso al código fuente.", "Desarrollo, prueba, refactorización y liberación, aplicadas durante el ciclo de vida convencional del desarrollo de software."],
        "correct": 2  # Análisis estático, desensamblado, documentación y modelado... (index 2)
    },
    {
        "question": "¿Cuál de las siguientes afirmaciones describe mejor el papel emergente de la inteligencia artificial (IA) en la ingeniería inversa según el texto?",
        "options": ["La IA se utiliza principalmente para reemplazar completamente a los ingenieros de software en el análisis de código.", "La IA está demostrando ser una herramienta poderosa para automatizar y acelerar tareas complejas de análisis manual en la ingeniería inversa.", "La IA se limita a la generación de pseudocódigo sin capacidad para ofrecer resúmenes funcionales.", "La IA ha disminuido la importancia de la reconstrucción de código fuente a partir de ejecutables en la ingeniería inversa."],
        "correct": 1  # La IA está demostrando ser una herramienta poderosa... (index 1)
    },
    {
        "question": "¿Cuál de los siguientes enunciados describe con mayor precisión los objetivos principales de la ingeniería inversa en el ámbito del software?",
        "options": ["Reproducir funcionalidades de un sistema sin necesidad de comprender su estructura ni su comportamiento interno.", "Analizar y comprender el diseño y funcionamiento de un software existente, a menudo sin acceso al código fuente, con fines como la interoperabilidad, la auditoría de seguridad o la recuperación de información.", "Optimizar el rendimiento del software original modificando directamente sus componentes binarios sin ningún tipo de análisis previo.", "Proteger sistemas contra vulnerabilidades mediante técnicas de ofuscación y criptografía aplicadas a sus ejecutables."],
        "correct": 1  # Analizar y comprender el diseño y funcionamiento... (index 1)
    },
    {
        "question": "¿Cuál de los siguientes mecanismos representa una técnica común utilizada para dificultar la ingeniería inversa del software mediante la alteración deliberada de su legibilidad o comprensión?",
        "options": ["Ofuscación de código, que transforma el código para hacerlo intencionadamente difícil de analizar sin alterar su funcionalidad.", "Criptografía y empaquetado, que ocultan el contenido ejecutable mediante cifrado o compresión.", "AntiDebugging y detección de entornos virtuales, que impiden el análisis dinámico en entornos controlados.", "Hardware seguro, que impide el acceso directo al sistema mediante protección física o chips especializados."],
        "correct": 0  # Ofuscación de código... (index 0)
    },
    {
        "question": "¿Cuál no es una técnica de la ofuscación?",
        "options": ["Transformar nombres de variables y funciones en identificadores sin sentido.", "Eliminar comentarios y documentación del código fuente.", "Reordenar instrucciones sin alterar el resultado final.", "Insertar código basura o condicionar la ejecución con múltiples saltos lógicos."],
        "correct": 1  # Eliminar comentarios y documentación del código fuente (index 1)
    },
    {
        "question": "¿Cuál es el objetivo principal de la ingeniería inversa?",
        "options": ["Crear un producto desde cero sin referencias", "Analizar un producto para entender su funcionamiento", "Diseñar un nuevo sistema completamente innovador", "Eliminar fallos en una fase de producción inicial"],
        "correct": 1  # Analizar un producto para entender su funcionamiento (index 1)
    },
    {
        "question": "¿Cómo puede afectar el uso de hardware seguro al proceso de ingeniería de requisitos en el desarrollo de un sistema?",
        "options": ["Impone requisitos no funcionales adicionales, como restricciones de acceso físico o cifrado en hardware, que deben ser considerados desde las etapas iniciales del análisis.", "Elimina la necesidad de definir requisitos de seguridad, ya que el hardware seguro proporciona protección completa de manera automática.", "Simplifica la validación de requisitos funcionales, al garantizar que todas las operaciones del sistema se ejecuten en un entorno confiable por defecto.", "Sustituye los requisitos de interoperabilidad, dado que los dispositivos seguros actúan como estándares universales en cualquier entorno de ejecución."],
        "correct": 0  # Impone requisitos no funcionales adicionales... (index 0)
    },
    {
        "question": "¿En qué conflicto histórico se popularizó el uso del término \"ingeniería inversa\"?",
        "options": ["Primera Guerra Mundial", "Guerra Fría", "Segunda Guerra Mundial", "Guerra de Vietnam"],
        "correct": 1  # Guerra Fría (index 1)
    },
    {
        "question": "¿Qué herramienta se utiliza comúnmente para ingeniería inversa de software?",
        "options": ["AutoCAD", "Adobe Illustrator", "Ghidra", "Arduino IDE"],
        "correct": 2  # Ghidra (index 2)
    },
    {
        "question": "¿Qué fase implica la verificación del comportamiento del modelo reconstruido?",
        "options": ["Recolección de información", "Análisis estructural", "Validación", "Modelado y documentación"],
        "correct": 2  # Validación (index 2)
    },
    # Cuestionario sobre Vibe Coding y programación asistida por la IA
    {
        "question": "¿Qué distingue principalmente al \"vibe coding\" de otros enfoques asistidos por IA?",
        "options": ["Que solo utiliza lenguaje natural.", "Que acepta las sugerencias de la IA sin revisar en detalle.", "Que se basa en compilar constantemente.", "Que se ejecuta exclusivamente en navegadores."],
        "correct": 1  # Que acepta las sugerencias de la IA sin revisar en detalle (index 1)
    },
    {
        "question": "¿Qué herramienta mencionada funciona como un IDE completo?",
        "options": ["GitHub Copilot", "Cursor", "Tabnine", "Ponicode"],
        "correct": 1  # Cursor (index 1)
    },
    {
        "question": "¿Cuál es un riesgo legal clave del uso de código generado por IA?",
        "options": ["Incluir sin saberlo fragmentos con derechos de autor.", "Que los lenguajes usados sean obsoletos.", "Que se rompan las reglas del compilador.", "Que el código sea demasiado eficiente."],
        "correct": 0  # Incluir sin saberlo fragmentos con derechos de autor (index 0)
    },
    {
        "question": "¿Qué característica tiene Lovable que lo diferencia de herramientas como Copilot?",
        "options": ["Ofrece refactorización en tiempo real.", "Genera código basado en voz.", "Permite crear apps completas sin escribir código.", "Detecta errores lógicos automáticamente."],
        "correct": 2  # Permite crear apps completas sin escribir código (index 2)
    },
    {
        "question": "¿Cuál es un riesgo ético destacado relacionado con la responsabilidad del código generado por IA?",
        "options": ["Que los usuarios finales no puedan modificarlo.", "No está claro quién es responsable si el código falla.", "Las empresas lo reclaman como código libre.", "No se puede compilar sin licencia."],
        "correct": 1  # No está claro quién es responsable si el código falla (index 1)
    },
    {
        "question": "¿Cuál es un problema frecuente al aceptar código sugerido sin comprensión profunda?",
        "options": ["Reduce el tamaño del proyecto.", "Mejora demasiado el rendimiento.", "Dificulta el mantenimiento y depuración.", "Limita la capacidad de escalar horizontalmente."],
        "correct": 2  # Dificulta el mantenimiento y depuración (index 2)
    },
    {
        "question": "¿Qué afirmación refleja una limitación contextual de las IAs actuales?",
        "options": ["Entienden todos los contextos empresariales.", "No comprenden bien los objetivos globales de un proyecto.", "Solo funcionan con proyectos en Python.", "No pueden generar HTML o CSS."],
        "correct": 1  # No comprenden bien los objetivos globales de un proyecto (index 1)
    },
    {
        "question": "¿Quién introdujo el término \"vibe coding\"?",
        "options": ["Los desarrolladores de GitHub Copilot.", "Andrej Karpathy.", "Los creadores de Cursor.", "Un grupo de investigación en procesamiento del lenguaje natural."],
        "correct": 1  # Andrej Karpathy (index 1)
    },
    {
        "question": "¿Por qué es problemático el uso de IA en entornos con datos sensibles?",
        "options": ["La información puede enviarse a servidores externos.", "El código generado siempre es público.", "Las IAs no soportan cifrado.", "Se pierde el control del teclado."],
        "correct": 0  # La información puede enviarse a servidores externos (index 0)
    },
    {
        "question": "¿Qué impacto ambiental tiene el uso masivo de IAs generativas en desarrollo?",
        "options": ["Reducción total del uso energético.", "Ninguno, ya que se usa en la nube.", "Aumento del consumo eléctrico y emisiones de CO₂.", "Solo afecta a usuarios sin conexión."],
        "correct": 2  # Aumento del consumo eléctrico y emisiones de CO₂ (index 2)
    },
    {
        "question": "¿Qué rol mantiene el desarrollador en el enfoque de vibe coding?",
        "options": ["Ninguno, todo lo hace la IA.", "Define la intención y supervisa la calidad del código.", "Se limita a validar compilaciones.", "Corrige manualmente cada sugerencia."],
        "correct": 1  # Define la intención y supervisa la calidad del código (index 1)
    },
    {
        "question": "¿Qué hace Amazon CodeGuru que lo diferencia de otras herramientas?",
        "options": ["Genera código desde cero.", "Solo se integra con GitHub.", "Analiza rendimiento y detecta malas prácticas.", "Crea dashboards en tiempo real."],
        "correct": 2  # Analiza rendimiento y detecta malas prácticas (index 2)
    },
    {
        "question": "¿Qué puede hacer la IA al detectar errores en código?",
        "options": ["Detener automáticamente la ejecución.", "Cambiar el lenguaje del proyecto.", "Proponer correcciones y explicarlas.", "Reiniciar el entorno de desarrollo."],
        "correct": 2  # Proponer correcciones y explicarlas (index 2)
    },
    {
        "question": "¿Qué función NO cubre típicamente Lovable?",
        "options": ["Generar backend.", "Crear documentación técnica.", "Construir login y dashboards.", "Desplegar en la nube."],
        "correct": 1  # Crear documentación técnica (index 1)
    },
    {
        "question": "¿Qué desafío ético plantea el entrenamiento de modelos con código público?",
        "options": ["El código deja de funcionar.", "No se pidió consentimiento a los autores originales.", "El código se hace obsoleto al ser usado por IA.", "Se dificulta el aprendizaje automático."],
        "correct": 1  # No se pidió consentimiento a los autores originales (index 1)
    },
    {
        "question": "¿Qué práctica fomenta la erosión de habilidades básicas del desarrollador?",
        "options": ["Uso de algoritmos clásicos.", "Aceptar sugerencias de IA sin reflexión crítica.", "Trabajar con código open source.", "Programar en C++."],
        "correct": 1  # Aceptar sugerencias de IA sin reflexión crítica (index 1)
    },
    {
        "question": "¿A qué se refiere Andrej Karpathy con \"vibe coding\"?",
        "options": ["Un método que requiere una revisión manual intensiva de cada línea de código.", "Un enfoque donde el desarrollador se deja llevar por las sugerencias de la IA, permitiendo que el código evolucione orgánicamente.", "Una técnica centrada únicamente en la optimización del rendimiento del código.", "Un proceso que minimiza el uso de herramientas asistidas por IA."],
        "correct": 1  # Un enfoque donde el desarrollador se deja llevar... (index 1)
    },
    {
        "question": "¿Qué hacen los benchmarks como WebDev Arena?",
        "options": ["Evalúan la seguridad de código Java.", "Comparan modelos LLMs resolviendo desafíos de desarrollo.", "Miden el uso de CPU por lenguaje.", "Optimizan el despliegue continuo."],
        "correct": 1  # Comparan modelos LLMs resolviendo desafíos de desarrollo (index 1)
    },
    {
        "question": "¿Cuál es una ventaja del uso de lenguaje natural en programación asistida?",
        "options": ["Requiere permisos root.", "Solo es útil en HTML.", "Hace el flujo de trabajo más intuitivo.", "Solo funciona con IA locales."],
        "correct": 2  # Hace el flujo de trabajo más intuitivo (index 2)
    },
    {
        "question": "¿Qué podría pasar si se integra código de IA sin revisión en un entorno comercial?",
        "options": ["Aumenta la velocidad sin consecuencias.", "Se puede incurrir en demandas por violación de licencias.", "Se compila más rápido siempre.", "Mejora automáticamente la seguridad."],
        "correct": 1  # Se puede incurrir en demandas por violación de licencias (index 1)
    },
    # Cuestionario sobre Legacy Code
    {
        "question": "¿Qué es el \"legacy code\"?",
        "options": ["Código muy antiguo.", "Código heredado difícil de manejar.", "Código mal documentado."],
        "correct": 1  # Código heredado difícil de manejar (index 1)
    },
    {
        "question": "¿Cuál es uno de los principales riesgos al modificar legacy code?",
        "options": ["Complicar la documentación.", "Hacer el código demasiado eficiente.", "Introducir nuevos bugs."],
        "correct": 2  # Introducir nuevos bugs (index 2)
    },
    {
        "question": "¿Qué técnica ayuda a entender el comportamiento de legacy code?",
        "options": ["Añadir pruebas automatizadas.", "Solamente leer comentarios.", "Usar variables globales."],
        "correct": 0  # Añadir pruebas automatizadas (index 0)
    },
    {
        "question": "¿Por qué es importante refactorizar legacy code?",
        "options": ["Para aumentar la complejidad.", "Para reducir la deuda técnica.", "Para mejorar la mantenibilidad."],
        "correct": 2  # Para mejorar la mantenibilidad (index 2)
    },
    {
        "question": "¿Qué patrón es útil para aislar dependencias en legacy code?",
        "options": ["Singleton.", "Dependency Injection.", "Observer."],
        "correct": 1  # Dependency Injection (index 1)
    },
    {
        "question": "¿Cuál es el primer paso recomendado antes de modificar legacy code?",
        "options": ["Cambiar el nombre de las funciones.", "Eliminar código muerto.", "Cubrir el código con pruebas."],
        "correct": 2  # Cubrir el código con pruebas (index 2)
    },
    {
        "question": "¿Qué herramienta ayuda a identificar áreas problemáticas en legacy code?",
        "options": ["Javadoc.", "Análisis estático de código.", "Swagger."],
        "correct": 1  # Análisis estático de código (index 1)
    },
    {
        "question": "¿Qué significa \"characterization test\" en el contexto de legacy code?",
        "options": ["Prueba que documenta el comportamiento actual del código.", "Prueba de rendimiento.", "Prueba de integración continua."],
        "correct": 0  # Prueba que documenta el comportamiento actual del código (index 0)
    },
    {
        "question": "¿Cuál es una buena práctica al trabajar con legacy code?",
        "options": ["Hacer grandes cambios de una vez.", "Realizar cambios pequeños y controlados.", "Ignorar los errores de compilación."],
        "correct": 1  # Realizar cambios pequeños y controlados (index 1)
    },
    {
        "question": "¿Qué es la \"deuda técnica\" en legacy code?",
        "options": ["Dinero que se debe al equipo de desarrollo.", "Acumulación de decisiones de diseño subóptimas.", "Falta de comentarios en el código."],
        "correct": 1  # Acumulación de decisiones de diseño subóptimas (index 1)
    },
    {
        "question": "¿Qué facilita la refactorización de legacy code?",
        "options": ["Variables globales.", "Código duplicado.", "Pruebas automatizadas."],
        "correct": 2  # Pruebas automatizadas (index 2)
    },
    {
        "question": "¿Qué patrón ayuda a introducir pruebas en legacy code?",
        "options": ["Factory.", "Single Responsibility.", "Test Harness."],
        "correct": 2  # Test Harness (index 2)
    },
    {
        "question": "¿Qué es el \"code coverage\" y por qué es útil en legacy code?",
        "options": ["Un indicador del porcentaje de código cubierto por pruebas.", "Una métrica de rendimiento.", "Un tipo de refactorización."],
        "correct": 0  # Un indicador del porcentaje de código cubierto por pruebas (index 0)
    },
    {
        "question": "¿Qué es recomendable hacer si no se entiende una parte del legacy code?",
        "options": ["Eliminarla.", "Añadir pruebas para documentar su comportamiento.", "Pedirle a la IA que lo cambie."],
        "correct": 1  # Añadir pruebas para documentar su comportamiento (index 1)
    },
    {
        "question": "¿Qué técnica ayuda a reducir el acoplamiento en legacy code?",
        "options": ["Uso de variables globales.", "Uso de métodos estáticos.", "Introducir interfaces."],
        "correct": 2  # Introducir interfaces (index 2)
    },
    {
        "question": "¿Por qué es peligroso reescribir todo el legacy code de una vez?",
        "options": ["Porque no reduce la deuda técnica.", "Porque se pueden perder funcionalidades y aumentar los errores.", "Porque no todo el código puede estar mal."],
        "correct": 1  # Porque se pueden perder funcionalidades y aumentar los errores (index 1)
    },
    {
        "question": "¿Qué es el \"Refactoring\" en el contexto de legacy code?",
        "options": ["El proceso de mejorar la estructura interna del código sin cambiar su comportamiento externo.", "El proceso de eliminar código muerto.", "El proceso de documentar el código existente."],
        "correct": 0  # El proceso de mejorar la estructura interna del código sin cambiar su comportamiento externo (index 0)
    },
    {
        "question": "¿Qué ayuda a reducir el miedo a modificar legacy code?",
        "options": ["Tener una buena suite de pruebas y buena documentación.", "Estar familiarizado con el lenguaje de programación.", "Tener comentarios."],
        "correct": 0  # Tener una buena suite de pruebas y buena documentación (index 0)
    },
    {
        "question": "¿Qué es una \"prueba de humo\" en el contexto de legacy code?",
        "options": ["Prueba que verifica el comportamiento.", "Prueba básica para comprobar que el sistema funciona tras un cambio.", "Prueba de rendimiento."],
        "correct": 1  # Prueba básica para comprobar que el sistema funciona tras un cambio (index 1)
    },
    {
        "question": "¿Qué actitud es recomendable al enfrentarse a legacy code?",
        "options": ["Cambiar todo de una vez.", "Anteponer tu criterio a la documentación.", "Ser cauteloso y validar cada cambio."],
        "correct": 2  # Ser cauteloso y validar cada cambio (index 2)
    },
    # Cuestionario sobre Protocolo Modelo-Contexto (MCP)
    {
        "question": "¿Cuál es el objetivo principal del Protocolo Modelo-Contexto (MCP)?",
        "options": ["Desarrollar un nuevo modelo de IA", "Establecer un protocolo estandarizado para conectar modelos de IA con fuentes de datos externas", "Crear un sistema operativo para dispositivos inteligentes", "Mejorar la velocidad de conexión entre servidores físicos"],
        "correct": 1  # Establecer un protocolo estandarizado para conectar modelos de IA con fuentes de datos externas (index 1)
    },
    {
        "question": "¿Qué problema común de integración resuelve el MCP?",
        "options": ["La falta de potencia de cómputo en los dispositivos móviles", "El sobreajuste de los modelos de IA durante el entrenamiento", "La necesidad de crear conectores independientes para cada combinación de modelo y fuente de datos", "La latencia entre modelos entrenados y su uso en dispositivos"],
        "correct": 2  # La necesidad de crear conectores independientes para cada combinación de modelo y fuente de datos (index 2)
    },
    {
        "question": "¿Cómo se describe mejor la arquitectura fundamental del MCP?",
        "options": ["Una arquitectura blockchain donde los datos se validan en un registro público", "Una red peer-to-peer descentralizada donde todos comparten datos sin servidores", "Un diseño cliente-servidor donde la aplicación de IA actúa como cliente que se conecta a servidores de datos", "Un modelo federado de entrenamiento distribuido"],
        "correct": 2  # Un diseño cliente-servidor donde la aplicación de IA actúa como cliente que se conecta a servidores de datos (index 2)
    },
    {
        "question": "Dentro de MCP, ¿qué función tiene un servidor MCP?",
        "options": ["Entrenar y actualizar el modelo de IA con nuevos datos", "Proporcionar acceso a datos y funcionalidades externas al modelo de IA", "Aumentar la velocidad de procesamiento del modelo", "Coordinar múltiples agentes de IA en paralelo"],
        "correct": 1  # Proporcionar acceso a datos y funcionalidades externas al modelo de IA (index 1)
    },
    {
        "question": "Dentro de MCP, ¿qué función tiene un cliente MCP?",
        "options": ["Almacenar copias de los datos del servidor", "Ejecutar el modelo de IA localmente en una máquina cliente", "Facilitar la comunicación entre la aplicación de IA y los servidores MCP", "Traducir instrucciones del modelo a comandos de máquina"],
        "correct": 2  # Facilitar la comunicación entre la aplicación de IA y los servidores MCP (index 2)
    },
    {
        "question": "En un flujo típico de comunicación MCP, ¿qué ocurre primero?",
        "options": ["El servidor MCP envía datos al modelo sin solicitud", "El cliente MCP consulta al servidor sobre sus capacidades", "El modelo de IA se actualiza automáticamente con nuevos parámetros", "El servidor solicita acceso a la API del modelo"],
        "correct": 1  # El cliente MCP consulta al servidor sobre sus capacidades (index 1)
    },
    {
        "question": "¿Qué significa que las conexiones en MCP sean \"bidireccionales\"?",
        "options": ["El modelo de IA puede tanto solicitar información al servidor como invocar acciones en él", "Toda la comunicación se limita a una sola dirección (del servidor a la IA)", "Los datos fluyen solo del modelo al servidor sin respuestas", "Solo se pueden usar con redes privadas"],
        "correct": 0  # El modelo de IA puede tanto solicitar información al servidor como invocar acciones en él (index 0)
    },
    {
        "question": "¿Cuál es una ventaja clave de usar el MCP?",
        "options": ["Aumenta automáticamente la capacidad de memoria de los modelos de IA", "Evita el acceso a datos externos para mejorar la privacidad", "Permite usar un único protocolo estándar en lugar de múltiples integraciones personalizadas", "Crea modelos completamente nuevos desde cero"],
        "correct": 2  # Permite usar un único protocolo estándar en lugar de múltiples integraciones personalizadas (index 2)
    },
    {
        "question": "MCP ayuda a mantener el contexto en los sistemas de IA cuando…",
        "options": ["El modelo de IA se reinicia en cada nueva sesión", "Se entrena el modelo con datos desordenados", "El asistente de IA cambia entre diferentes herramientas y conjuntos de datos durante una tarea", "El servidor realiza pruebas automáticas sobre la IA"],
        "correct": 2  # El asistente de IA cambia entre diferentes herramientas y conjuntos de datos durante una tarea (index 2)
    },
    {
        "question": "¿Cuál es un ejemplo de caso de uso real de MCP?",
        "options": ["Un modelo de IA que mejora automáticamente la calidad de las fotos", "Un sistema que entrena varios modelos sin supervisión", "Un asistente de codificación que lee el código en un repositorio para dar sugerencias basadas en el contexto", "Un motor de búsqueda que indexa páginas web aleatorias"],
        "correct": 2  # Un asistente de codificación que lee el código en un repositorio para dar sugerencias basadas en el contexto (index 2)
    },
    {
        "question": "¿Qué significa que MCP sea \"independiente del modelo\" (model-agnostic)?",
        "options": ["Solo funciona con un modelo de IA particular", "Puede trabajar con cualquier asistente de IA o modelo de lenguaje, sin importar el proveedor", "Selecciona automáticamente el mejor modelo de IA para cada tarea", "Funciona únicamente con modelos entrenados en la nube"],
        "correct": 1  # Puede trabajar con cualquier asistente de IA o modelo de lenguaje, sin importar el proveedor (index 1)
    },
    {
        "question": "¿Cuál de los siguientes no es un componente principal del MCP?",
        "options": ["La especificación del protocolo y sus SDK", "Servidores MCP locales y en la nube", "Un repositorio interno de datos no relacionado", "Conectores estandarizados para APIs abiertas"],
        "correct": 2  # Un repositorio interno de datos no relacionado (index 2)
    },
    {
        "question": "¿Cómo puede usarse MCP en un entorno empresarial?",
        "options": ["Conectando todos los sistemas de la empresa a la nube sin control", "Reemplazando al departamento de TI en la toma de decisiones", "Un asistente interno recupera información de sistemas CRM y bases de conocimiento de forma segura", "Usando asistentes virtuales para marketing automático sin permisos"],
        "correct": 2  # Un asistente interno recupera información de sistemas CRM y bases de conocimiento de forma segura (index 2)
    },
    {
        "question": "¿Cuál podría ser una limitación práctica de MCP?",
        "options": ["Requiere configurar y mantener servidores MCP, lo que puede agregar complejidad inicial", "Asegura datos a nivel militar automáticamente", "Impide que los modelos de IA accedan a datos externos por diseño", "Solo es compatible con Linux"],
        "correct": 0  # Requiere configurar y mantener servidores MCP, lo que puede agregar complejidad inicial (index 0)
    },
    {
        "question": "¿Cómo se intercambian mensajes entre clientes y servidores en MCP?",
        "options": ["Conversando por chat en tiempo real", "Usando mensajes en formato JSON (JSON-RPC 2.0) a través de HTTP", "Intercambiando archivos de texto manualmente", "A través de mensajes binarios encriptados con QR"],
        "correct": 1  # Usando mensajes en formato JSON (JSON-RPC 2.0) a través de HTTP (index 1)
    },
    {
        "question": "¿Qué operaciones típicas puede realizar un modelo de IA mediante un servidor MCP?",
        "options": ["Reentrenar otros modelos directamente en el servidor", "Realizar procesamiento de imágenes localmente sin ayuda", "Leer archivos de datos y ejecutar funciones o consultas en el servidor", "Modificar el hardware del servidor de forma remota"],
        "correct": 2  # Leer archivos de datos y ejecutar funciones o consultas en el servidor (index 2)
    },
    {
        "question": "Al usar MCP con múltiples herramientas, ¿qué permite esto a un agente de IA?",
        "options": ["Solo elegir una herramienta al azar para cada tarea", "Entrar automáticamente en un modo de aprendizaje no supervisado", "Acceder simultáneamente a varias fuentes de información y combinarlas en su razonamiento", "Ejecutar múltiples instancias del mismo servidor MCP"],
        "correct": 2  # Acceder simultáneamente a varias fuentes de información y combinarlas en su razonamiento (index 2)
    },
    {
        "question": "¿Por qué es importante que MCP sea un estándar abierto?",
        "options": ["Obliga a todos los usuarios a pagar una licencia costosa", "Cambia continuamente sin una versión estable", "Facilita que varios proveedores y herramientas sean compatibles sin licencias cerradas", "Impide el uso de servidores privados"],
        "correct": 2  # Facilita que varios proveedores y herramientas sean compatibles sin licencias cerradas (index 2)
    },
    {
        "question": "¿Qué permite un servidor MCP personalizado?",
        "options": ["Convertir el servidor en un modelo de IA", "Crear nuevos idiomas de programación automáticamente", "Conectar sistemas internos o bases de datos privadas de la organización con los modelos de IA", "Generar modelos de IA basados en ADN"],
        "correct": 2  # Conectar sistemas internos o bases de datos privadas de la organización con los modelos de IA (index 2)
    },
    {
        "question": "¿Cuál de estas NO es una función del MCP?",
        "options": ["Proporcionar contexto adicional a un asistente de IA durante una conversación", "Entrenar un nuevo modelo de lenguaje por sí mismo", "Ejecutar funciones externas (como consultas o comandos) en respuesta a solicitudes del modelo de IA", "Gestionar el acceso a fuentes de datos remotas"],
        "correct": 1  # Entrenar un nuevo modelo de lenguaje por sí mismo (index 1)
    }
]
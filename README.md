# PRIS2-Test

## Descripción
PRIS2-Test es una aplicación web desarrollada con Flask que permite a los estudiantes practicar preguntas tipo test para la asignatura de PRIS 2. La aplicación ofrece dos modos de estudio para adaptarse a diferentes necesidades de preparación.

## Características principales
### Dos modos de estudio:
- **Simulacro de Examen**: 40 preguntas seleccionadas aleatoriamente
- **Responde a Todas las Preguntas**: Practica con el pool completo de preguntas

### Funcionalidades avanzadas:
- Preguntas y opciones presentadas en orden aleatorio en cada intento
- Feedback visual inmediato al responder (colores para respuestas correctas/incorrectas)
- Contador de respuestas correctas e incorrectas
- Barra de progreso visual
- Sistema de puntuación con nota final (escala 0-10)
- Las respuestas incorrectas restan 0.5 puntos de una correcta

## Temas cubiertos
El banco de preguntas incluye temas como:
- Metodologías de Desarrollo de Software
- Calidad del Software
- Métricas de calidad
- Refactorización de Código
- Patrones de Diseño
- Desarrollo Basado en Pruebas (TDD)
- Documentación de Software
- Contenerización de Aplicaciones
- Integración Continua y Despliegue Continuo
- Aspectos Legales y Éticos
- Securización de aplicaciones web
- Ingeniería Inversa
- Vibe Coding y programación asistida por IA
- Legacy Code
- Protocolo Modelo-Contexto (MCP)

## Instalación
1. Clona este repositorio:
   ```
   git clone https://github.com/yourusername/PRIS2-Test.git
   cd PRIS2-Test
   ```
2. Crea un entorno virtual e instala las dependencias:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```
   python app.py
   ```
4. Abre tu navegador y visita: http://127.0.0.1:5000/

## Uso
1. En la página principal, selecciona el modo de estudio que prefieras:
   - **Simulacro de Examen**: 40 preguntas aleatorias
   - **Responde a Todas las Preguntas**: Todas las preguntas disponibles
2. Responde a las preguntas seleccionando una opción.
3. Recibirás feedback inmediato sobre tu respuesta, mostrando la opción correcta si has fallado.
4. Al final del cuestionario, verás tu puntuación total calculada según la fórmula:
   - Puntuación = (Aciertos - (Fallos * 0.5)) / Total Preguntas * 10

## Estructura del proyecto
```
PRIS2-Test/
├── app.py               # Aplicación Flask principal
├── questions.py         # Base de datos de preguntas
├── requirements.txt     # Dependencias del proyecto
├── static/
│   ├── script.js        # Lógica del cliente
│   └── style.css        # Estilos CSS
└── templates/
    ├── index.html       # Página de inicio/selección de modo
    └── quiz.html        # Interfaz del cuestionario
```

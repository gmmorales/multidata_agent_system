# 🤖 Protocolo Operativo: MultiData Agent System (MDAS)
**Consultora:** Prado & Morales  
**Ecosistema:** Agentes Especializados de Google (Gems)  
**Proyecto:** MultiData Agent System (MDAS)  
**Descripción:** Un ecosistema multi-agente modular para la automatización, gobernanza y estandarización del ciclo de vida del dato.  
**Propósito:** Estandarización, trazabilidad y automatización en proyectos de Consultoría y Ciencia de Datos  

---

## 1. Introducción
El presente documento establece el marco metodológico y operativo para el desarrollo de proyectos de analítica y ciencia de datos mediante **MultiData Agent System (MDAS)**, un ecosistema multi-agente modular. Utilizando los **Gems de Google**, se asigna una responsabilidad única y delimitada a cada agente de IA dentro de la cadena de valor del dato.

Esta arquitectura garantiza:
* **Estandarización:** Estructura física y entornos uniformes en cada proyecto.
* **Trazabilidad:** Seguimiento auditable de cada etapa mediante registros operacionales (`log.md`).
* **Calidad y Gobernanza:** Validación rigurosa de los datos desde la ingesta cruda hasta el modelado predictivo.
* **Eficiencia:** Eliminación de tareas repetitivas de configuración mediante scripts automatizados.

---

## 2. Esquema del Flujo Operativo

El flujo de trabajo sigue una secuencia lineal y dependiente, donde la salida de cada agente constituye el insumo obligatorio del siguiente:

<pre>
  [ ENTRADA: Solicitud de Proyecto / Cliente ]
                        │
                        ▼
           ┌────────────────────────┐
           │ data-scaffolder-agent  │ ──► Genera directorio físico y entorno (.venv)
           └────────────────────────┘
                        │
                        ▼  (Colocación de dataset crudo en data/raw/)
           ┌────────────────────────┐
           │  data-inspector-agent  │ ──► Audita sanidad, tipos y anomalías
           └────────────────────────┘
                        │
                        ▼  (Informe de sanidad aprobado)
           ┌────────────────────────┐
           │   data-wrangler-agent  │ ──► Limpia, transforma y guarda en data/processed/
           └────────────────────────┘
                        │
                        ▼
           ┌────────────────────────┐
           │  data-explorer-agent   │ ──► Análisis exploratorio (EDA) e insights clave
           └────────────────────────┘
                        │
                        ▼
           ┌────────────────────────┐
           │   data-modeler-agent   │ ──► Entrenamiento, evaluación y algoritmos
           └────────────────────────┘
                        │
                        ▼
  [ SALIDA: Entregables Analíticos y Modelos en Producción ]
</pre>

---

## 3. Catálogo y Descripción de Agentes

### 3.1. `data-scaffolder-agent`
* **Fase:** Inicialización e Infraestructura.
* **Función Principal:** Automatizar la creación del andamiaje físico del proyecto, la configuración de entornos virtuales aislados y la generación de documentación base.
* **Inputs:** Parámetros del proyecto (Nombre del Customer, S.O. objetivo, CLI, Manejador de entorno, Lenguaje).
* **Outputs:** 
  1. `instrucciones_inicio.md` (con gráfico de árbol preformateado mediante `<pre>` y guía paso a paso).
  2. `log.md` (registro de operaciones inicial).
  3. Script ejecutable de consola (`PowerShell` o `Bash`) para crear el entorno, instalar librerías (`requirements.txt`) y registrar el kernel en Jupyter Lab.
* **Ubicación de Trabajo:** Raíz del proyecto.

---

### 3.2. `data-inspector-agent`
* **Fase:** Control de Calidad y Auditoría del Dato.
* **Función Principal:** Realizar un diagnóstico exhaustivo sobre los datasets crudos recién ingresados antes de que sufran cualquier tipo de manipulación.
* **Inputs:** Datasets alojados en `data/raw/`.
* **Outputs:** Informe técnico de salud de los datos (identificación de valores nulos, registros duplicados, inconsistencias de tipos, desviaciones y posibles atípicos).
* **Ubicación de Trabajo:** `data/raw/` y `notebooks/`.

---

### 3.3. `data-wrangler-agent`
* **Fase:** Limpieza y Preparación (Data Wrangling).
* **Función Principal:** Aplicar reglas de negocio y correcciones técnicas para transformar los datos crudos en un conjunto de datos limpio, curado y optimizado.
* **Inputs:** Dataset de `data/raw/` + Informe del `data-inspector-agent`.
* **Outputs:** Datasets curados en formato óptimo (ej. Parquet/CSV) depositados en `data/processed/`, acompañados de scripts de limpieza documentados en `src/`.
* **Ubicación de Trabajo:** `data/processed/` y `src/`.

---

### 3.4. `data-explorer-agent`
* **Fase:** Análisis Exploratorio de Datos (EDA).
* **Función Principal:** Desentrañar patrones, distribuciones, métricas de negocio y correlaciones mediante el uso de librerías analíticas y de visualización (Pandas, Matplotlib, Seaborn).
* **Inputs:** Datasets curados ubicados en `data/processed/`.
* **Outputs:** Visualizaciones avanzadas, dashboards analíticos, gráficos de distribución/correlación y síntesis de hallazgos para la toma de decisiones.
* **Ubicación de Trabajo:** `notebooks/` y `docs/`.

---

### 3.5. `data-modeler-agent`
* **Fase:** Aprendizaje Automático y Modelado Predictivo.
* **Función Principal:** Seleccionar, entrenar y evaluar algoritmos de Machine Learning (desde modelos lineales/regresiones hasta *Ensemble Learning*) en función de los objetivos de la consultoría.
* **Inputs:** Datasets procesados de `data/processed/` + Variables de interés identificadas por el `data-explorer-agent`.
* **Outputs:** Modelos entrenados, métricas de rendimiento (RMSE, $R^2$, Accuracy, F1-Score) y artefactos de código para inferencia en producción.
* **Ubicación de Trabajo:** `notebooks/` y `src/`.

---

## 4. Gobernanza y Protocolo de Ejecución

1. **Modos de Operación:**
   * **Modo Instructivo (Ayuda):** Si la interacción no contiene la orden explícita, el agente responderá con asistencia técnica sobre sus parámetros de uso.
   * **Modo Ejecución:** Activado únicamente con la sintaxis explícita (ej. `"Iniciar proceso..."`), desencadenando la generación estricta de sus artefactos.
2. **Registro Obligatorio (`log.md`):** Cada agente tiene la responsabilidad de anexar la traza de sus acciones en el log común del proyecto al finalizar su tarea, indicando timestamp, operador y estado del proceso.
3. **Puntos de Control (Quality Gates):** Ningún agente puede operar sobre un directorio si el agente previo no ha validado y cerrado su respectiva etapa.
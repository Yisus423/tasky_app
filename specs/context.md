# 📂 Contexto del Proyecto y Estructura de Directorios

Este documento detalla la distribución de carpetas del proyecto **Tasky App** y explica la responsabilidad y propósito de cada una de ellas, basándose en la arquitectura modular (adaptación del patrón MVC/MVVM para Kivy).

## Estructura Principal

```text
tasky_app/
│
├── .venv/                 # Entorno virtual de Python
├── models/                # Capa de Datos (Modelo)
├── specs/                 # Documentación y Especificaciones
├── views/                 # Capa de Presentación (Vistas y Componentes)
│   ├── components/        # Widgets Reutilizables
│   ├── menu/              # Módulo de Menú
│   └── tasks/             # Módulo de Tareas
│
├── main.py                # Punto de entrada de la aplicación
├── pyproject.toml         # Configuración y dependencias del proyecto
└── README.md              # Documentación general del repositorio
```

---

## Detalle de Carpetas

### 📁 `models/` (Capa de Datos)
Contiene la lógica de negocio y el manejo de estado de la aplicación.
- **Responsabilidad:** Gestionar los datos (leer, escribir, actualizar, eliminar). Puede incluir la conexión a bases de datos (locales como SQLite o en memoria), peticiones a APIs externas o archivos de configuración.
- **Regla de oro:** No debe tener dependencias de la interfaz de usuario (Kivy). Funciona de forma totalmente independiente a las pantallas.

### 📁 `specs/` (Especificaciones)
Carpeta destinada a la documentación técnica y hojas de ruta.
- **Responsabilidad:** Almacenar documentos Markdown (`.md`) que definen cómo está construido el proyecto, requisitos del MVP, flujos de trabajo, y convenciones de equipo.
- **Archivos comunes:** `mvp_dev.md`, `context.md`.

### 📁 `views/` (Capa de Presentación)
Es el núcleo de la interfaz de usuario. Organiza las diferentes pantallas y los elementos visuales de la aplicación separándolos por "Features" o módulos.
Dentro de `views/`, la estructura se divide en submódulos:

#### ↳ 📁 `views/components/`
- **Responsabilidad:** Almacenar widgets pequeños y modulares que se utilizan en múltiples partes de la app (ej: botones personalizados, tarjetas de información como `task_card`, barras de navegación).
- **Contenido:** Suelen constar de pares de archivos (`.py` para la lógica del widget y `.kv` para su diseño visual).

#### ↳ 📁 `views/tasks/`
- **Responsabilidad:** Contener la pantalla principal de gestión de tareas.
- **Contenido:** Lógica del controlador de esta vista (`tasks_view.py`) donde se comunica con el `TaskModel` para actualizar su estado y su representación visual (`tasks.kv`).

#### ↳ 📁 `views/menu/`
- **Responsabilidad:** Manejar la vista relacionada con el menú principal de la aplicación, configuración o navegación secundaria.
- **Contenido:** Código Python (`menu_view.py` u otros) y diseño (`menu.kv`) dedicados exclusivamente a este módulo.

### 📁 `.venv/`
- **Responsabilidad:** Contiene todas las dependencias y librerías de Python instaladas localmente para el proyecto (como `kivy`). **No** se debe modificar manualmente ni subir al control de versiones de Git.

---

## Archivos Raíz

- **`main.py`:** Es el punto de arranque de la aplicación. Su única tarea es inicializar la app de Kivy, configurar los ajustes base de la ventana y montar la vista inicial.
- **`pyproject.toml`:** Archivo estándar moderno de Python para definir metadatos del proyecto y gestionar sus dependencias.

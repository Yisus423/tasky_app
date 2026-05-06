# 🚀 Documentación del MVP: Aplicación de Tareas Kivy (Arquitectura Modular)

Este documento define la estructura y el código base para el Producto Mínimo Viable (MVP) de nuestra aplicación de tareas, utilizando el patrón arquitectónico de separación por "Features" (Módulos) y el patrón MVC/MVVM adaptado para Kivy.

---

## 📂 1. Estructura de Directorios del Proyecto


```text
tasky_app/
│
├── main.py
├── models/
│   └── task_model.py
└── views/
    ├── components/
    │   ├── task_card.py
    │   └── task_card.kv
    └── tasks/
        ├── tasks_view.py
        └── tasks.kv
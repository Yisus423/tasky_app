class TaskModel:
    def __init__(self):
        # Base de datos simulada en memoria
        self.tasks = [
            {"id": 1, "text": "Configurar arquitectura Kivy"},
            {"id": 2, "text": "Crear el componente TaskCard"}
        ]
        self.next_id = 3

    def get_all_tasks(self):
        return self.tasks

    def add_task(self, text):
        if text.strip():
            self.tasks.append({"id": self.next_id, "text": text})
            self.next_id += 1

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]

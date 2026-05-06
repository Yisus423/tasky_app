from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from models.task_model import TaskModel
from views.components.task_card import TaskCard

# Cargamos el archivo .kv principal de la vista
Builder.load_file('views/tasks/tasks.kv')

class TasksScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = TaskModel()
        self.refresh_ui()

    def refresh_ui(self):
        """Limpia el contenedor visual y lo vuelve a llenar leyendo el Modelo."""
        container = self.ids.tasks_container
        container.clear_widgets()
        
        for task in self.model.get_all_tasks():
            # Creamos el componente y le pasamos el texto y la función de borrar
            card = TaskCard(
                task_text=task["text"],
                delete_action=lambda t_id=task["id"]: self.delete_task(t_id)
            )
            container.add_widget(card)

    def add_task_from_ui(self):
        """Lee el input, lo guarda en el modelo y actualiza la vista."""
        text_input = self.ids.new_task_input
        if text_input.text:
            self.model.add_task(text_input.text)
            text_input.text = ""
            self.refresh_ui()

    def delete_task(self, task_id):
        """Elimina una tarea del modelo y actualiza la vista."""
        self.model.remove_task(task_id)
        self.refresh_ui()

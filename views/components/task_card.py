from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.lang import Builder

# Cargamos su diseño visual correspondiente
Builder.load_file('views/components/task_card.kv')

class TaskCard(BoxLayout):
    task_text = StringProperty("")
    delete_action = ObjectProperty(None) # Función callback para cuando se presione 'X'

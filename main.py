from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from views.tasks.tasks_view import TasksScreen
from views.menu.menu_view import MenuScreen

class MVPApp(App):
    def build(self):
        self.title = "MVP Tareas Kivy"
        
        sm = ScreenManager(transition=SlideTransition())
        
        menu_screen = MenuScreen(name='menu')
        tasks_screen = TasksScreen(name='tasks')
        
        sm.add_widget(menu_screen)
        sm.add_widget(tasks_screen)
        
        return sm

if __name__ == '__main__':
    MVPApp().run()

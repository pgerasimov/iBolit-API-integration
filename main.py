from random import randint

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

Window.size = (250, 200)
Window.clearcolor = (255 / 255, 186 / 255, 3 / 255, 1)
Window.title = 'Название окна'


class MyApp(App):

    def __init__(self):
        super().__init__()
        self.input_data = TextInput(hint_text='Введите Имя врача:')
        self.label = Label(text='Поиск врача')

    def button_pressed(self, *args):
        self.label.color = (randint(0, 255) / 255, randint(0, 255) / 255, randint(0, 255) / 255, 1)

    def build(self):
        button = Button(text='Найти врача')
        button.bind(on_press=self.button_pressed)
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(button)

        return box


if __name__ == '__main__':
    MyApp().run()

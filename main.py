# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class SimpleApp(App):
    def build(self):
        # Creamos un layout (contenedor) vertical
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Etiqueta de texto
        self.label = Label(text='¡Hola, Kivy y Python!', 
                           font_size='30sp',
                           color=(1, 0, 0, 1)
                          )
        
        # Botón
        self.button = Button(text='Presióname', 
                             font_size='20sp',
                             size_hint=(None, None), # Permite cambiar el tamaño manualmente
                             size=(200, 80),
                             pos_hint={'center_x': 0.5} # Centra el botón horizontalmente
                            )
        
        # Asignamos una acción al botón
        self.button.bind(on_press=self.on_button_press)
        
        # Añadimos los widgets al layout
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        
        return self.layout

    def on_button_press(self, instance):
        # Función que se ejecuta al presionar el botón
        self.label.text = '¡El botón ha sido presionado!'

if __name__ == '__main__':
    SimpleApp().run()
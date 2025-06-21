# - Convert the temperature converter CLI tool into a GUI tool kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
class TemperatureConverterApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input_label = Label(text='Enter temperature:')
        self.layout.add_widget(self.input_label)

        self.input_text = TextInput(multiline=False)
        self.layout.add_widget(self.input_text)

        self.convert_button = Button(text='Convert to Fahrenheit')
        self.convert_button.bind(on_press=self.convert_temperature)
        self.layout.add_widget(self.convert_button)

        return self.layout

    def convert_temperature(self, instance):
        try:
            celsius = float(self.input_text.text)
            fahrenheit = Temperature.celsius_to_fahrenheit(celsius)
            popup = Popup(title='Conversion Result',
                          content=Label(text=f'{celsius}°C is {fahrenheit}°F'),
                          size_hint=(0.6, 0.4))
            popup.open()
        except ValueError:
            popup = Popup(title='Error',
                          content=Label(text='Please enter a valid number.'),
                          size_hint=(0.6, 0.4))
            popup.open()
if __name__ == '__main__':
    TemperatureConverterApp().run()
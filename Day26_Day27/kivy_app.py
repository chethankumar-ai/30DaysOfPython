import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

API_URL = "http://127.0.0.1:8000/books"

class BookApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.title_input = TextInput(hint_text="Title")
        self.author_input = TextInput(hint_text="Author")
        self.description_input = TextInput(hint_text="Description")

        self.add_widget(self.title_input)
        self.add_widget(self.author_input)
        self.add_widget(self.description_input)

        self.submit_button = Button(text="Add Book")
        self.submit_button.bind(on_press=self.add_book)
        self.add_widget(self.submit_button)

        self.show_button = Button(text="Show All Books")
        self.show_button.bind(on_press=self.show_books)
        self.add_widget(self.show_button)

        self.output = Label(text="Results will show here", halign="left", valign="top")
        self.add_widget(self.output)

    def add_book(self, instance):
        book = {
            "title": self.title_input.text,
            "author": self.author_input.text,
            "description": self.description_input.text,
        }
        response = requests.post(API_URL, json=book)
        if response.status_code == 200:
            self.output.text = "Book added successfully!"
        else:
            self.output.text = "Failed to add book"

    def show_books(self, instance):
        response = requests.get(API_URL)
        if response.status_code == 200:
            books = response.json()
            book_list = "\n".join([f"{b['id']}. {b['title']} by {b['author']}" for b in books])
            self.output.text = f"Books:\n{book_list}"
        else:
            self.output.text = "Failed to fetch books"

class MyBookApp(App):
    def build(self):
        return BookApp()

if __name__ == "__main__":
    MyBookApp().run()

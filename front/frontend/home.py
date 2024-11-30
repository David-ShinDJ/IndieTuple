import reflex as rx
from .styles.style import banner_style, style



class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

def index():
    return rx.vstack(rx.hstack(style=banner_style))

app = rx.App(style=style)
app.add_page(index) 
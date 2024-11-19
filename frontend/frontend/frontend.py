# frontend/app.py (Reflex)

import reflex as rx
import httpx

class State(rx.State):
  todos: list[dict[str, str]] = []

  async def get_todos(self):
    async with httpx.AsyncClient() as client:
      response = await client.get("http://127.0.0.1:5000/api/todos")
      self.todos = response.json()

def index():
  return rx.center(
    rx.button("할 일 목록 가져오기", on_click=State.get_todos),
    rx.foreach(State.todos, lambda todo: rx.text(todo.text)),
  )

app = rx.App()
app.add_page(index)
import reflex as rx
import httpx
from typing import Any


class TodoState(rx.State):
  todos: list[dict[str, Any]] = []
  async def get_todos(self):
      async with httpx.AsyncClient() as client:
          response = await client.get("http://127.0.0.1:5000/api/todos")
          self.todos = response.json()
          print(response.json())
      
  async def add_todo(self, form_data: dict):
      text = form_data.get("todo")
      if text:
              async with httpx.AsyncClient() as client:
                response = await client.post("http://127.0.0.1:5000/api/todos/add", json={"text": text})
                print(response.json())
  async def update_todo(self, text: str):
      if text:
        async with httpx.AsyncClient() as client:
            response = await client.put("http://127.0.0.1:5000/api/todos/update", json={"text": text})
            if response.status_code == 200:
               await self.get_todos()

  async def delete_todo(self, text: str):
      if text:
        async with httpx.AsyncClient() as client:
          response = await client.delete(f"http://127.0.0.1:5000/api/todos/delete/{text}")
          print(response.json())
      
  

def todo_item(item: dict[str, Any]) -> rx.Component:
  return rx.list_item(
    rx.hstack(
       rx.checkbox(
          on_change=lambda: TodoState.update_todo(item["text"]),
          is_checked=item["completed"],
       ),
       rx.text(
          item["text"],
          text_decoration=rx.cond(
              item["completed"],
              "line-through",
              "none"
          ),
       ),
       rx.button("삭제", on_click=lambda: TodoState.delete_todo(item["text"])),
       align="center",
    ),
    class_name="list-one",
  )

def todo_list() -> rx.Component:

  return rx.ordered_list(
    rx.foreach(TodoState.todos, lambda todo: todo_item(todo)),
  )

def add_todo() -> rx.Component:

  return rx.form(
    rx.hstack(
      rx.input(
        id="todo",
        placeholder="할 일 추가",
        bg=rx.color("gray", 2),
        width="100%",
      ),
      rx.button("추가")
    ),
    on_submit=TodoState.add_todo,
    reset_on_submit=True,
    width="100%",
  )
def index() -> rx.Component:

  return rx.center(
    rx.vstack(
      rx.hstack(rx.heading("할 일 목록", size="lg"),
      rx.button("todo 불러오기", on_click=TodoState.get_todos),),
      add_todo(),
      rx.divider(),
      todo_list(),
      rx.divider(),
      bg=rx.color("gray", 7),
      margin_top="5em",
      margin_x="25vw",
      padding="1em",
      border_radius="0.5em",
      spacing="3",
    ),

  )
# Reflex (frontend)
app = rx.App()
app.add_page(index, title="할 일 목록")
# class State(rx.State):
#   todos: list[dict[str, str]] = []

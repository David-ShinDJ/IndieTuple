# class State(rx.State):
#   todos: list[dict[str, str]] = []

#   async def get_todos(self):
#     async with httpx.AsyncClient() as client:
#       response = await client.get("http://127.0.0.1:5000/api/todos")
#       self.todos = response.json()


  

# class FormState(rx.State):
  
#   @rx.event
#   def submit(self, form_data):
#     return rx.toast(form_data)


# def form() -> rx.Component:
#     return rx.center(rx.card(
#         rx.form(
#             rx.hstack(
#                 rx.image(src="/icon.png", width="3em", height="3em"),
#                  rx.vstack(rx.heading("할 일 추가"), rx.text("할 일을 입력하고 추가하세요."), spacing="4", align_items="stretch")
#                 ),
#             rx.vstack(
#                 rx.text(
#                     "Todo ",
#                     rx.text.span("*", color="indigo"),
#                 ),
#                 rx.input(
#                     name="todo",
#                     required=True,
#                 ),
#                 rx.button("Plus", type="submit"),
#             ),
#             on_submit=FormState.submit,
#         )
#     )
#     )


# def index():
#   return rx.vstack(
#     rx.button("할 일 목록 가져오기", on_click=State.get_todos),
#     rx.foreach(State.todos, lambda todo: rx.text(todo.text)),
    
#     # 폼 추가
#     form() # 컴포넌트들을 동일한 너비로
#   )

# app = rx.App()
# app.add_page(index)
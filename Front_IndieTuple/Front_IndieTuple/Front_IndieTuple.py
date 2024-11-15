"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


import reflex as rx
import httpx

class State(rx.State):
  message: str = ""

  async def get_message(self):
    async with httpx.AsyncClient() as client:
      response = await client.get("http://127.0.0.1:5000/api/hello")
      self.message = response.json()["message"]

def index():
  return rx.center(
    rx.button("Get Message", on_click=State.get_message),
    rx.text(State.message),
  )

app = rx.App()
app.add_page(index)

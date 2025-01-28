import reflex as rx
import styles.style as style
from .components.chat import chat_room, send_button
from .components.user import user_form
from .state import Message, MessageState
import random
from .pages.redirect import redirect
from .pages.test import test
## FrontEnd Logic

def index() -> rx.Component:
    # 쿠키 체크를 통한 접근 제어 
    if True :
        return rx.fragment(
            rx.script("window.location.href = '/test'")
        )

    return rx.vstack(
             rx.hstack(
            rx.text("Welcome to Indie Tuple", style=style.text_style),
            style=style.stack_style,
        ),
        rx.hstack(
            style= {
                "background_image": "url('/background.png')",
                "background_size": "cover",
                "background_position": "center",
                "border_radius": "15px 50px",
                "border": "5px solid #555",
                "width": "100%",
                "height": "25vh",
            }
        ),
        rx.flex(
            chat_room(),
            user_form(),
            width="100%",
            justify_content="center",
            align_items="center",
        ),
    )

## TODO: 
app = rx.App()
app.add_page(index)
app.add_page(redirect, route="/redirect")
app.add_page(test, route="/test")
import reflex as rx

from ..components.user import user_form

def test() -> rx.Component:
    return rx.vstack(
        rx.center(
            user_form()
        )
    )
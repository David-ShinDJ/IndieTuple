import reflex as rx


from ..components.user import user_form
from ..components.login import login_form
def test() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
                login_form(),
                user_form(),
                width="100%",
                justify_content="center",
                align_items="center",
            ),
            width="100%",
            justify_content="center",
            align_items="center",
        )
    )


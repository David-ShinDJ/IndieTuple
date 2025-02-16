import reflex as rx
from .components.game import game_component, GameState

def main() -> rx.Component:
    return rx.cond(
        GameState.token != "",
        rx.center(
            rx.vstack(
                rx.heading("인디튜플", size="lg"),
                rx.text("인디튜플 페이지입니다.", size="md"), 
            )
        ),
        rx.center(
            rx.script("window.location.href = '/game'")
        )
    )

def game() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("타겟 클릭 게임", size="lg"),
            rx.text("100점을 달성하면 인디튜플 페이지로 이동합니다!", size="sm", color="gray"),
            game_component(),
            bg=rx.color("gray", 7),
            margin_top="5em",
            margin_x="25vw",
            padding="1em",
            border_radius="0.5em",
            spacing="3",
        ),
    )

def index() -> rx.Component:
        return rx.center(
        rx.script("window.location.href = '/game'")
    )

# Reflex (frontend)
app = rx.App()
app.add_page(index)
app.add_page(game, route="/game", title="게임")
app.add_page(main, route="/main", title="인디튜플")

import reflex as rx
import jwt

from .components.create import create_post_component
from .components.chat import chat_room
from .components.post import post_component
from .components.user import user_form
from .components.game import game_component, GameState
import httpx

## TODO : game.py 저장한 닉네임이 저장이안대고 다르게보이는 이슈존재함
## 게임시작을 위해 닉네임을 받고
## 게임 종료시 닉네임과 게임점수와 jwt로 변환하자
## 처음설정한 nickname 로컬스토리지에 저장하자
## 포스트작성시 닉네임과 user 프로필정보를 DB에 저장하자, sesseion id발급및 저장
## 포스트 참가시 닉네임과 포스트 정보를 DB에 저장하자
class MainState(rx.State):
    is_authenticated: bool = False
    nickname: str = rx.LocalStorage("nickname")
    score: int = 0

    @rx.event
    async def check_auth(self):
        await self.verify_token()
        if not self.is_authenticated:
            return rx.redirect("/game")

    @rx.event
    async def verify_token(self):
        try:
            token = self.get_local_storage("game_token")
            if not token:
                self.is_authenticated = False
                return
                
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "http://127.0.0.1:5000/api/verify-token",
                    headers={"Authorization": f"Bearer {token}"}
                )
                if response.status_code == 200:
                    data = response.json()
                    self.score = data["score"]
                    self.is_authenticated = True
                else:
                    self.is_authenticated = False
        except:
            self.is_authenticated = False

def main() -> rx.Component:
    return rx.center(
            rx.vstack(
                rx.heading("인디튜플", size="lg"),
                rx.text(f"환영합니다, {MainState.nickname}님!", size="md"),
                rx.button(
                    "게임 다시하기",
                    on_click=rx.redirect("/game"),
                    color_scheme="blue",
                ),
                padding="2em",
                bg="white",
                border_radius="1em",
                box_shadow="lg",
            )
        ),

def game() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("타겟 클릭 게임", size="lg"),
            rx.text("10점을 달성하면 인디튜플 페이지로 이동합니다!", size="sm", color="gray"),
            game_component(),
            bg=rx.color("gray", 7),
            margin_top="5em",
            margin_x="25vw",
            padding="1em",
            border_radius="0.5em",
            spacing="3",
        ),
    )


def create() -> rx.Component:
    return rx.center(
        create_post_component()
    )

def test() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            user_form(),
            chat_room(),
        ),
        post_component(),
        rx.button(
            "Create",
            on_click=rx.redirect("/create"),
        )
    )
# @rx.page(on_load=MainState.check_auth)
def index() -> rx.Component:
    return test()

# Reflex (frontend)
app = rx.App()
app.add_page(index)
app.add_page(game, route="/game", title="게임")
app.add_page(main, route="/main", title="인디튜플")
app.add_page(test, route="/test", title="테스트")
app.add_page(create, route="/create", title="테스트")
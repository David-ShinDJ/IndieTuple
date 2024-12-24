import reflex as rx
import styles.style as style
from .components.chat import chat_room, send_button
from .state import Message, MessageState
import dataclasses, datetime, json
import random
from .pages.redirect import redirect
## Database Login
@dataclasses.dataclass
class User:
    id: int
    nickname: str
    email: str | None
    profile_image: str | None
    created_at: datetime.datetime

## TODO: Onboaring 페이지추가하기 닉네임, 이메일, 프로필사진설정 완류 후 메인페이지로 이동시키자 쿠키방식사용
## Cookie True

database = [
    User(id=0, nickname="David",email="dnrur124@gmail.com",profile_image="profile0.jpg",created_at=datetime.datetime.now()),
    User(id=1, nickname="Smith",email="smith124@naver.com",profile_image="profile0.jpg",created_at=datetime.datetime.now()),
    User(id=2, nickname="Anderson",email=None, profile_image="profile0.jpg",created_at=datetime.datetime.now()),
    User(id=3, nickname="Movius",email=None, profile_image=None, created_at=datetime.datetime.now()),
]

def cookie(cookie: bool, user_id: int = 0) -> dict:
    if cookie:
        data = {
            "exists": True,
            "message": f"{user_id} 데이터를 가져왔습니다",
            "user": {
                "id": user_id,
                "nickname": database[user_id].nickname,
                "email": database[user_id].email,
                "profile_image": database[user_id].profile_image,
                "created_at": str(database[user_id].created_at)
            }
        }
    else:
        data = {
            "exists": False,
            "message": "쿠키의 데이터가 없습니다",
            "user": None
        }
    return data




## FrontEnd Logic

class UserState(rx.State):
    nickname: str | None = f"user{random.randint(0, 1000000)}"
    email: str | None = "None"
    profile_image: str | None = "/user.png"
    edit_profile_mode: bool = True


    def set_nickname(self, nickname: str):
        self.nickname = nickname
    
    def set_email(self, email: str):
        self.email = email
    
    def set_profile_image(self):
        self.profile_image = FileState.profile_image[0]

    def edit_profile(self, form_data: dict[str, str]):
        self.edit_profile_mode = False
        self.set_nickname(form_data["nickname_input"])
        self.set_email(form_data["email_input"])

    def save_profile(self):
        self.edit_profile_mode = True

    def set_user_data(self, cookie_data: dict):
        """쿠키 데이터를 상태에 저장"""
        self.user_data = cookie_data
        if cookie_data.get("exists") and cookie_data.get("user"):
            self.nickname = cookie_data["user"]["nickname"]
            self.email = cookie_data["user"]["email"]
            self.profile_image = cookie_data["user"]["profile_image"]

class FileState(rx.State):
    profile_image: list[str]
    async def handle_upload(
    self, files: list[rx.UploadFile]):

        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)

color = "rgb(107,99,246)"

def user_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.cond(
                UserState.edit_profile_mode,
                profile_component(),
                edit_profile_component(),
            )
        ),
        on_submit=UserState.edit_profile,
    )

def profile_component() -> rx.Component:
    return rx.flex(
    rx.avatar(src=UserState.profile_image, fallback="RU", size="9"),
    rx.text(f"Nickname: {UserState.nickname}", weight="bold", size="4"),
    rx.text(f"Email: {UserState.email}", color_scheme="gray"),
    rx.button(
        "프로필수정",
        on_click=UserState.save_profile,
        color_scheme="indigo",
            variant="solid",
        ),
        direction="column",
        spacing="1",
    )

def edit_profile_component() -> rx.Component:
    return rx.flex(
            rx.upload(
            rx.vstack(
                rx.button(
                    "이미지 업로드",
                    color=color,
                    bg="white",
                    border=f"1px solid {color}",
                ),
                rx.text(
                    "사진을 업로드해주세요"
                ),
            ),
            id="profile_upload",
            border=f"1px dotted {color}",
            padding="5em",
        ),
    rx.input(name="input", placeholder="닉네임을 입력해주세요", type_="text", id="nickname_input",required=True),
    rx.input(name="input", placeholder="이메일을 입력해주세요(선택)", type_="email", id="email_input", required=False),
    rx.button(
        "저장하기",
        on_click=UserState.save_profile,
        color_scheme="green",
            variant="solid",
        ),
        direction="column",
        spacing="1",
    )

def check_cookie(have_cookie:bool):
    # 예시: user_id 0으로 테스트
    if have_cookie:
        cookie_data = cookie(True, 0)
        UserState.set_user_data(cookie_data)
        return True
    else:
        cookie_data = cookie(False)
        return False



def index() -> rx.Component:
    # 쿠키 체크를 통한 접근 제어 
    if not check_cookie(False):
        return rx.fragment(
            rx.script("window.location.href = '/redirect'")
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
            rx.container(
                style={
                    "background_color": "red",
                    "height": "40vh",
                }
            ),
            rx.vstack(
                rx.scroll_area(
                chat_room(),
                type="auto",
                scrollbars="vertical",
            ),
            rx.hstack(
                send_button(),
                style={
                    "width": "100%",
                }
            ),
                style={
                    "width": "40%",
                    "height": "40vh",
                    "margin": "0 auto",
                }
            ),
            rx.vstack(
                user_form(),
            ),
            width="100%",
            justify_content="center",
            align_items="center",
        ),
    )




app = rx.App()
app.add_page(index)
app.add_page(redirect, route="/redirect")
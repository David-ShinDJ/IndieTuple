import reflex as rx
import styles.style as style
from .components.chat import chat_room, send_button
from .state import Message, MessageState
import dataclasses, datetime
import random

## BackEnd Logic
def back_check_cookie(cookie: bool) -> dict[str, str | None]:
    if cookie:
        return {"id": 0, "nickname": "test", "email": "test@test.com", "profile_image": "test.com"}
    else:
        return {"id": 1, "nickname": None, "email": None, "profile_image": None}

def back_load_chat_room():
    return [
        Message(text="안녕하세요", is_my_message=True, index=0),
        Message(text="환영합니다", is_my_message=False, index=1),
        Message(text="반갑습니다", is_my_message=False, index=2),
        Message(text="다들 뭐하세요?", is_my_message=True, index=3),
        Message(text="어 아무것도 안해요..", is_my_message=False, index=4),
        Message(text="그렇군요", is_my_message=True, index=5),
    ]

## Database Login
@dataclasses.dataclass
class User:
    id: int
    nickname: str
    email: str | None
    profile_image: str | None
    created_at: datetime.datetime
## FrontEnd Logic
class UserState(rx.State):
    nickname: str | None = f"user{random.randint(0, 1000000)}"
    email: str | None = "None"
    profile_image: str | None = "/user.png"
    edit_profile_mode: bool = True
    
    def set_nickname(self, nickname: str):
        self.nickname = nickname
        print(self.nickname)
    
    def set_email(self, email: str):
        self.email = email
    
    ## TODO: Profile Image 업로드 처리
    
    def set_profile_image(self, profile_image: str):
        self.profile_image = profile_image
    def edit_profile(self, form_data: dict[str, str]):
        State.handle_upload(rx.upload_files(upload_id="upload1"))
        self.profile_image = rx.get_upload_url(State.img[0])
        self.set_nickname(form_data["nickname_input"])
        self.set_email(form_data["email_input"])
        print(self.profile_image)
        
        print(self.nickname, self.email)

    def toggle_edit_profile(self):
        self.edit_profile_mode = not self.edit_profile_mode


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
        on_click=UserState.toggle_edit_profile,
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
                    "업로드",
                    color=color,
                    bg="white",
                    border=f"1px solid {color}",
                ),
                rx.text(
                    "사진을 업로드해주세요"
                ),
            ),
            id="upload1",
            border=f"1px dotted {color}",
            padding="5em",
        ),
    rx.input(name="input", placeholder="닉네임을 입력해주세요", type_="text", id="nickname_input",required=True),
    rx.input(name="input", placeholder="이메일을 입력해주세요(선택)", type_="email", id="email_input", required=False),
    rx.button(
        "저장하기",
        on_click=UserState.toggle_edit_profile,
        color_scheme="green",
            variant="solid",
        ),
        direction="column",
        spacing="1",
    )
class State(rx.State):
    """The app state."""

    # The images to show.
    img: list[str]

    @rx.event
    async def handle_upload(
        self, files: list[rx.UploadFile]
    ):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)


color = "rgb(107,99,246)"
def index() -> rx.Component:
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

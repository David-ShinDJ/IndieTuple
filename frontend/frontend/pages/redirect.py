import reflex as rx
import styles.style as style
import random
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

def redirect_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(name="input", placeholder="닉네임을 입력해주세요", type_="text", id="nickname_input",required=True),
            rx.input(name="input", placeholder="이메일을 입력해주세요", type_="email", id="email_input", required=True),
            rx.button(
                "완료",
                on_click=UserState.save_profile,
                color_scheme="green",
                    variant="solid",
            ),
        ),
        on_submit=UserState.save_profile,
    )

def redirect() -> rx.Component:
    return rx.vstack(
        rx.heading("Welcome to Indie Tuple!", size="lg"),
        rx.container(
            rx.text("필요한 정보를 입력해주세요"),
            redirect_form()
        ),
    )
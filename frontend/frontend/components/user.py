import reflex as rx


def user_form() -> rx.Component:
    return rx.vstack(
        rx.cond(
            UserState.editing,
            edit_profile_component(),
            profile_component()
        ),

    )

def profile_component() -> rx.Component:
    return rx.flex(
    rx.avatar(src=UserState.profile_image, fallback="RU", size="9"),
    rx.text(f"Nickname: {UserState.nickname}", weight="bold", size="4"),
    rx.text(f"Email: {UserState.email}", color_scheme="gray"),
    rx.button("편집", on_click=UserState.toggle_edit),
        direction="column",
        spacing="1",
    )

def edit_profile_component() -> rx.Component:
    return rx.form(
            rx.flex(
            rx.upload(
            rx.vstack(
                rx.button(
                    "이미지 업로드",
                ),
                rx.text(
                    "사진을 업로드해주세요"
                ),
            ),
            id="profile_upload",
        ),
    rx.input(name="nickname", default_value=UserState.nickname,placeholder="닉네임을 입력해주세요", type_="text", required=True),
    rx.input(name="email", default_value=UserState.email, placeholder="이메일을 입력해주세요(선택)", type_="email", required=False),
    rx.button("저장",),
    direction="column",
    spacing="1",
    ),
    on_submit=UserState.save_profile,
    )
class UserState(rx.State):
    nickname: str | None = "None"
    email: str | None = "None"
    profile_image: str = "/user.png"
    editing: bool = False

    def get_nickname(self):
        return self.nickname
    
    def get_email(self):
        return self.email
    
    def get_profile_image(self):
        return self.profile_image
    
    def set_nickname(self, nickname: str):
        self.nickname = nickname
    
    def set_email(self, email: str):
        self.email = email
    
    def set_profile_image(self, profile_image: str):
        self.profile_image = profile_image
    
    def toggle_edit(self):
        self.editing = not self.editing
    
    def form_data(self, form_data: dict[str, str]):
        self.set_nickname(form_data["nickname"])
        self.set_email(form_data["email"])

    def save_profile(self, form_data: dict[str, str]):
        self.set_nickname(form_data["nickname"])
        self.set_email(form_data["email"])
        ## TODO: 프로필 이미지 편집하기
        self.toggle_edit()

    def cancel_edit(self):
        self.toggle_edit()
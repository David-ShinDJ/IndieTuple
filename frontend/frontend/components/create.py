import reflex as rx
from .post import PostState, Post

class MyPost(rx.State):
    title: str = ""
    content: str = ""
    location: str = ""
    max_participants: int = 0

    def set_title(self, title: str):    
        self.title = title
    
    def set_content(self, content: str):
        self.content = content
    
    def set_location(self, location: str):
        self.location = location
    
    def create_post(self):
        pass
def create_post_component() -> rx.Component:
    return rx.vstack(
        rx.heading("새 모임 만들기", size="lg", mb=4),
        rx.input(
            placeholder="제목을 입력하세요",
            value=MyPost.title,
            on_change=MyPost.set_title,
            mb=2
        ),
        rx.text_area(
            placeholder="내용을 입력하세요",
            value=MyPost.content,
            on_change=MyPost.set_content,
            mb=2
        ),
        rx.input(
            placeholder="장소를 입력하세요",
            value=MyPost.location,
            on_change=MyPost.set_location,
            mb=2
        ),
        rx.input(
            placeholder="참가 인원을 입력하세요",
            value=MyPost.max_participants,
            on_change=MyPost.set_max_participants,
            mb=4
        ),
        rx.button(
            "모임 만들기",
            on_click=MyPost.create_post,
            color_scheme="blue",
            width="100%"
        ),
        spacing="4",
        width="100%",
        max_width="600px",
        padding="4",
    )
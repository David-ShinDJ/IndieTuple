import reflex as rx
import styles.style as style
from rxconfig import config
import dataclasses, datetime
from typing import List
def back_load_chat_room():
    return [
        Message(text="안녕하세요", is_my_message=True, index=0),
        Message(text="환영합니다", is_my_message=False, index=1),
        Message(text="반갑습니다", is_my_message=False, index=2),
        Message(text="다들 뭐하세요?", is_my_message=True, index=3),
        Message(text="어 아무것도 안해요..", is_my_message=False, index=4),
        Message(text="그렇군요", is_my_message=True, index=5),
    ]

@dataclasses.dataclass
class Message:
    text: str
    is_my_message: bool 
    index: int

class MessageState(rx.State):
    messages: List[Message] = back_load_chat_room()
    message: str = ""
    message_processing: bool = True
    checkbox_value: bool = False

    def on_mount(self) -> None:
        """컴포넌트가 마운트될 때 자동으로 실행됩니다."""
        self.load_chat_room()

    def load_chat_room(self):
        self.messages = back_load_chat_room()
    
    def set_message(self, message: str):
        self.message = message

    def send_message(self, form_data: dict[str, str]):
        self.message_processing = False
        self.message = form_data["message_input"]
        if self.checkbox_value:
            self.messages.append(Message(text=self.message, is_my_message=False, index=len(self.messages)))
        else:
            self.messages.append(Message(text=self.message, is_my_message=True, index=len(self.messages)))
    
    def checkbox_change(self, value: bool):
        self.checkbox_value = value


# 메시지 스타일 수정
message_style = dict(
    display="inline-block",
    padding="1em",
    border_radius="8px",
    max_width="60%",  # 최대 너비를 화면의 60%로 제한
    word_wrap="break-word",  # 긴 텍스트 자동 줄바꿈
    margin="0.5em",  # 메시지 간 여백
)

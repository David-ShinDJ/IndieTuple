import reflex as rx
from ..state import Message, MessageState

message_style = dict(
    display="inline-block",
    padding="1em",
    border_radius="8px",
    max_width="60%",  # 최대 너비를 화면의 60%로 제한
    word_wrap="break-word",  # 긴 텍스트 자동 줄바꿈
    margin="0.5em",  # 메시지 간 여백
)

def chat_room() -> rx.Component:
    return rx.vstack(
          rx.scroll_area(
                rx.box(
            rx.foreach(
                MessageState.messages,
                lambda m: message_box(m.text, m.is_my_message, m.index)
            ),
            width="100%",  # 채팅방 전체 너비
            padding="1em",  # 내부 여백
        ),
        width="100%",
        spacing="2",
        ),
                    rx.hstack(
                send_button(),
                style={
                    "width": "100%",
                }
            ),
            # 0-9 사이의 숫자만 사용 가능
    )

def message_box(text: str, is_my_message: bool, index: int):
    return rx.box(
        rx.cond(
            is_my_message,
            rx.box(
                rx.text(f"{index}"),
                rx.markdown(
                    text,
                    background_color=rx.color("mauve", 4),
                    color=rx.color("mauve", 12),
                    **message_style,
                ),
                text_align="right",
                margin_top="1em",
                width="100%",  # 컨테이너 전체 너비
                padding_right="1",  # 오른쪽 여백
            ),
            rx.box(
                rx.text(f"{index}"),
                rx.markdown(
                    text,
                    background_color=rx.color("accent", 4),
                    color=rx.color("accent", 12),
                    **message_style,
                ),
                text_align="left",
                padding_top="1em",
                width="100%",  # 컨테이너 전체 너비
                padding_left="1em",  # 왼쪽 여백
            ),
        ),
    )

def send_button() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.form(
                rx.hstack(
                    rx.checkbox(on_change=MessageState.checkbox_change),
                    rx.input(
                        rx.input.slot(
                            rx.tooltip(
                                rx.icon("info", size=15),
                                content="메시지입력하세요...",
                            ),
                        ),
                        placeholder="메시지를 입력해주세요",
                        id="message_input",
                        width="100%",
                    ),
                    rx.button(
                        rx.cond(
                            MessageState.message_processing,
                            rx.spinner(size="1em"),
                            rx.text("전송"),
                        ),
                        type_="submit",
                    ),
                    align_items="center",
                ),
                on_submit=MessageState.send_message,
                reset_on_submit=True,
            )
        )
    )
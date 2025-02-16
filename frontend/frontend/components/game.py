import reflex as rx
import random
import httpx

class GameState(rx.State):
    score: int = 0
    game_active: bool = False
    target_position: tuple = (0, 0)
    token: str = ""
    
    def start_game(self):
        self.game_active = True
        self.score = 0
        self.token = ""  # 게임 시작시 토큰 초기화
        self.move_target()
    
    def move_target(self):
        self.target_position = (
            random.randint(0, 280),  # x position
            random.randint(0, 180)   # y position
        )
    
    async def handle_click(self, x: int, y: int):
        if not self.game_active:
            return
            
        # 클릭 위치와 타겟 위치의 거리 계산
        distance = ((x - self.target_position[0])**2 + 
                   (y - self.target_position[1])**2)**0.5
                   
        if distance < 30:  # 타겟 히트 범위
            self.score += 10
            self.move_target()
            
            # 점수가 100점 이상이고 토큰이 없을 때만 토큰 발급 요청
            if self.score >= 10 and not self.token:
                async with httpx.AsyncClient() as client:
                    response = await client.post(
                        "http://127.0.0.1:5000/api/token",
                        json={"score": self.score}
                    )
                    if response.status_code == 200:
                        self.token = response.json()["token"]
                        self.game_active = False
                        return rx.redirect("/main")  # 메인 페이지로 리다이렉트

def game_component():
    return rx.vstack(
        rx.heading(f"점수: {GameState.score}"),
        rx.box(
            rx.box(
                position="absolute",
                left=f"{GameState.target_position[0]}px",
                top=f"{GameState.target_position[1]}px",
                width="20px",
                height="20px",
                border_radius="50%",
                bg="red",
                cursor="pointer",
                on_click=lambda: GameState.handle_click(
                    GameState.target_position[0],
                    GameState.target_position[1]
                )
            ),
            width="300px",
            height="200px",
            bg="white",
            position="relative",
            border="1px solid black",
        ),
        rx.button(
            "게임 시작",
            on_click=GameState.start_game,
            is_disabled=GameState.game_active,
            color_scheme="blue",
        ),
    )

import reflex as rx
import dataclasses, datetime
from typing import List

def back_load_post():
    return [
        Post(title="타겟 클릭 게임", content="타겟 클릭 게임을 즐겨보세요!", author="admin", created_at=datetime.datetime.now(), location="서울특별시 강남구 테헤란로 14길 6 남도빌딩 4층", attend_limit=10, attend_count=0, attend_list=[]),
        Post(title="타겟 클릭 게임", content="타겟 클릭 게임을 즐겨보세요!", author="admin", created_at=datetime.datetime.now(), location="서울특별시 강남구 테헤란로 14길 6 남도빌딩 4층", attend_limit=10, attend_count=0, attend_list=[]),
        Post(title="타겟 클릭 게임", content="타겟 클릭 게임을 즐겨보세요!", author="admin", created_at=datetime.datetime.now(), location="서울특별시 강남구 테헤란로 14길 6 남도빌딩 4층", attend_limit=10, attend_count=0, attend_list=[]),
        Post(title="타겟 클릭 게임", content="타겟 클릭 게임을 즐겨보세요!", author="admin", created_at=datetime.datetime.now(), location="서울특별시 강남구 테헤란로 14길 6 남도빌딩 4층", attend_limit=10, attend_count=0, attend_list=[]),   
        Post(title="타겟 클릭 게임", content="타겟 클릭 게임을 즐겨보세요!", author="admin", created_at=datetime.datetime.now(), location="서울특별시 강남구 테헤란로 14길 6 남도빌딩 4층", attend_limit=10, attend_count=0, attend_list=[]),
    ]

@dataclasses.dataclass
class Post:
    title: str
    content: str
    author: str
    created_at: datetime.datetime
    location: str
    attend_limit: int
    attend_count: int
    attend_list: List[str]

class PostState(rx.State):
    posts: List[Post] = back_load_post()

    def on_mount(self) -> None:
        """컴포넌트가 마운트될 때 자동으로 실행됩니다."""
        self.load_posts()
    
    def create_post(self, title: str, content: str, author: str, location: str, attend_limit: int):
        self.posts.append(Post(title=title, content=content, author=author, created_at=datetime.datetime.now(), location=location, attend_limit=attend_limit, attend_count=0, attend_list=[]))

    def load_posts(self):
        self.posts = back_load_post()

    def add_post(self, post: Post):
        self.posts.append(post)
    
    def delete_post(self, index: int):
        self.posts.pop(index)
    
    def edit_post(self, index: int, post: Post):
        self.posts[index] = post
    
    def attend_post(self, index: int, nickname: str):
        self.posts[index].attend_count += 1
        if self.posts[index].attend_count >= self.posts[index].attend_limit:
            self.posts[index].attend_list.append(nickname)
            self.posts[index].attend_count = 0
            
def post_component() -> rx.Component:
    return rx.vstack(
        rx.foreach(
            PostState.posts,
            lambda post: post_card(post)
        )
    )

def post_card(post: Post) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(post.title),
            rx.text(post.content),
            rx.text(f"작성자: {post.author}"),
            rx.text(f"작성일: {post.created_at}"),
            rx.text(f"위치: {post.location}"),
            rx.text(f"참가 제한: {post.attend_limit}"),
            rx.text(f"참가 인원: {post.attend_count}"),
    )
    )
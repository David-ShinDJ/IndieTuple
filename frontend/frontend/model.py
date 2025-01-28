import dataclasses
import datetime
from typing import List
@dataclasses.dataclass
class User:
    id: int
    nickname: str
    email: str | None
    profile_image: str | None
    created_at: datetime.datetime

@dataclasses.dataclass
class Message:
    text: str
    is_my_message: bool 
    index: int

@dataclasses.dataclass
class Appointment:
    id: str
    users: List[User]
    date: str
    time: str
    location: str
    numbers: int
    description: str

database_users = [
    User(id=0, nickname="David",email="dnrur124@gmail.com",profile_image="profile0.jpg",created_at=datetime.datetime.now()),
    User(id=1, nickname="Smith",email="smith124@naver.com",profile_image="profile1.jpg",created_at=datetime.datetime.now()),
    User(id=2, nickname="Anderson",email=None, profile_image="profile2.jpg",created_at=datetime.datetime.now()),
    User(id=3, nickname="Movius",email=None, profile_image=None, created_at=datetime.datetime.now()),
]

database_messages = [        Message(text="안녕하세요", is_my_message=True, index=0),
        Message(text="환영합니다", is_my_message=False, index=1),
        Message(text="반갑습니다", is_my_message=False, index=2),
        Message(text="다들 뭐하세요?", is_my_message=True, index=3),
        Message(text="어 아무것도 안해요..", is_my_message=False, index=4),
        Message(text="그렇군요", is_my_message=True, index=5),]

database_appointments = [
    Appointment(id="1", users=[database_users[0], database_users[1]], date="2025-01-01", time="10:00", location="서울", numbers=2, description="모임"),
    Appointment(id="2", users=[database_users[0], database_users[2]], date="2025-01-02", time="11:00", location="부산", numbers=3, description="모임"),
    Appointment(id="3", users=[database_users[0], database_users[3]], date="2025-01-03", time="12:00", location="대구", numbers=4, description="모임"),
]
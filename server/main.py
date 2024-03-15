from fastapi import FastAPI
from fastapi import Depends

from dependencies import get_query_token, get_token_header
from routers import items, users
"""
https://daco2020.tistory.com/62 // https://velog.io/@anjaekk/python%EC%A0%88%EB%8C%80%EA%B2%BD%EB%A1%9C%EC%83%81%EB%8C%80%EA%B2%BD%EB%A1%9C-%EC%83%81%EB%8C%80%EA%B2%BD%EB%A1%9C-import-%EC%97%90%EB%9F%AC%EC%9D%B4%EC%9C%A0%EC%99%80-%ED%95%B4%EA%B2%B0
 로 관련 main 파일에서는  절대 경로를 써야햐한다.
"""
"""
from .routers.items import router
from .routers.users import router
routerfrom 이 usersfrom을 덮어쓰게 되어 items동시에 사용할 수 없게 됩니다.
따라서 동일한 파일에서 두 가지를 모두 사용할 수 있도록 하위 모듈을 직접 가져옵니다. 아니면 각 파일에서 items_router 이런식으로 바꿔서 이름 안 겹치게 만들어도 좋다.
"""
# from .router는 main/routers 와 같음
#from 패키지 import 모듈 or from 패키지.모듈 import 함수 or 클래스

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)

# app.include_router(users.router)
# app.include_router(items.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )

@app.get("/")
async def root():
    return {"message": "Hello Bigger Application"}




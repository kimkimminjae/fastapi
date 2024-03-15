from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from dependencies import get_token_header
from .users import var
from .test.test1 import var2
from .tag_enum import Tags

print(var)
print(var2)


router = APIRouter(
    prefix="/items",
    tags=[Tags.items],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
) #APIRouter의 init 초기화임! 앞에는 초기화 멤버변수이고

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():
    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["custom"], # 이렇게 태그를 add 할 수도 있다.
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@router.post(
    "/items/",
    response_model=Item,
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
)
async def create_item(item: Item):
    return item

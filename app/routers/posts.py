from fastapi import APIRouter

router = APIRouter()


@router.get("/posts")
async def list_posts():
    pass

@router.post("/posts")
async def create_post():
    pass

@router.put("/posts/{id}")
async def update_post():
    pass

@router.delete("/posts/{id}")
async def delete_post():
    pass
from fastapi import FastAPI, UploadFile, File
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from models import Post, Tag, Category, Author, ImageModel
from tortoise import Tortoise
import uvicorn


app = FastAPI()


async def init_db():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']},
    )

    await Tortoise.generate_schemas()


register_tortoise(
    app=app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['models']},
    generate_schemas=True
)


Authors = pydantic_model_creator(Author, name='Author')
Tags = pydantic_model_creator(Tag, name='Tag')
Cats = pydantic_model_creator(Category, name='Category')
Posts = pydantic_model_creator(Post, name='Post')



@app.on_event('startup')
async def startup():
    await init_db()


# @app.post('/author_create')
# async def author_create(author: Authors, image: UploadFile = File(...)):
#     img = await image.read()
#     authordb = author.dict()
#     authordb['img'] = img
#     user = await Author.create(**authordb)

#     return user


@app.post('/author_create')
async def author_create(name: str, desc: str, image: UploadFile = File(...)):
    img = await image.read()
    user = await Author.create(id=2, name=name, desc=desc, img=img)
    print(user)
    return user


@app.post('/post_create')
async def post_create(post: Posts, image: UploadFile = File(...)):
    img = image.read()
    post = post.dict()
    post['img'] = img
    article = await Author.create(**post.dict())
    print(article)

    return article


@app.post("/upload/")
async def upload_image(image: UploadFile = File(...)):
    image_bytes = await image.read()
    img = await ImageModel.create(image_data=image_bytes)
    return {"message": "Image uploaded successfully", "image_id": img.id}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
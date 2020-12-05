import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from apps import settings, routers


app = FastAPI(
    title='english_coach',
    description='Author - skapralov',
    version='0.1',
)

app.include_router(routers.api_router)

register_tortoise(
    app,
    db_url=settings.DATABASE_URI,
    modules=settings.APPS,
    generate_schemas=False,
    add_exception_handlers=True,
)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)

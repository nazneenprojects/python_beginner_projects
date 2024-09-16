from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from village_info_service.database.connection import Settings
from village_info_service.routes.users import user_router
from village_info_service.routes.events import event_router
import uvicorn

app = FastAPI(
    title="village_info_service",
    description="""
                This 'village info service' project is designed to implement the backend service REST api endpoints of village information. Basically it will have below features:
    1. signup , signin [Completed]
    2. get_village_info (like name, geolocation, histroy, population) [to plan]
    3. events : create , delete, get, get_all, update [completed]
    4. get village map [to plan]
    5. services : create , delete, get, get_all, update [to plan]
                """,
    version="V0.1.0a"
)

settings = Settings()

# register origins

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.on_event("startup")
async def init_db():
    await settings.initialize_database()


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

# if __name__ == '__main__':
#     uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)

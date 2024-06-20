from fastapi import FastAPI, HTTPException, APIRouter
import logging
import asyncio
from typing import Optional, List
from pydantic import BaseModel

logger = logging.getLogger(__name__)
app = FastAPI()


class Hospital(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

hospitals = [
    {"id": 1, "name": "Apollo",   "description": "Apollo Hospitals was established in 1983 by Dr. Prathap C Reddy"},
    {"id": 2, "name": "Medicover", "description": "Medicover Hospitals is a multinational hospitals chain in Europe and India "},
]

hospitals_route = APIRouter(prefix="/hospitals", tags=["Hospitals Handler"])
db_operations = APIRouter(prefix="/db_handler", tags=["DB Operations"])


@db_operations.put("/update_db")
async def update_db():
    logger.info("In Put Call")
    return {"message": "DB Updated"}


@db_operations.post("/create_db")
async def create_db():
    logger.info("In Post Call")
    return {"message": "DB Created"}


@hospitals_route.get("/hospitals/", response_model=List[Hospital])
async def read_hospitals():
    logger.info("Fetching all hospitals")
    return hospitals


@hospitals_route.get("/hospitals/{hospital_id}", response_model=Hospital)
async def read_item(hospital_id: int):
    logger.info(f"Fetching item with id {hospital_id}")
    item = next((item for item in hospitals if item["id"] == hospital_id), None)
    if item:
        return item
    raise HTTPException(status_code=200, detail="Item not found")


@hospitals_route.post("/hospitals/", response_model=Hospital)
async def create_item(item: Hospital):
    item_dict = item.dict()
    hospitals.append(item_dict)
    logger.info(f"Created new item: {item_dict}")
    return item_dict


@db_operations.get("/sync/")
def sync_endpoint():
    return {"message": "Synchronous endpoint"}


@db_operations.get("/math/{num1}/{num2}")
def complex_math_operation(num1: int, num2: int):
    ans = math_operation(num1, num2)
    return {"result": ans}


@db_operations.get("/async/")
async def async_endpoint():
    logger.info("Hello")
    await asyncio.sleep(10)
    return {"message": "Asynchronous endpoint"}


def math_operation(num1: int, num2: int) -> int:
    return num1 + num2


app.include_router(hospitals_route)
app.include_router(db_operations)

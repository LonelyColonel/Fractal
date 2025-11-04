from fastapi import APIRouter
from app.clients.rabbit_client import publish_task
import uuid

router = APIRouter()

@router.post("/compress/")
async def compress_file(file_path: str):
    task_id = str(uuid.uuid4())
    task = {"task_id": task_id, "file_path": file_path}
    await publish_task(task)
    return {"task_id": task_id, "status": "queued"}

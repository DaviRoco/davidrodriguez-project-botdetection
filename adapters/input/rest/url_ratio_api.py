from fastapi import APIRouter, UploadFile, Depends
from core.ports.input.ingest_url_ratio import IngestUrlRatio
from dependencies import get_ingest_url_ratio
from adapters.input.rest.ingest_helpers import parse_csv_file
url_ratio_router = APIRouter()


@url_ratio_router.post("/url_ratio/ingest")
async def ingest_activity(file: UploadFile, ingest_url_ratio_service: IngestUrlRatio = Depends(get_ingest_url_ratio)):
    data = await parse_csv_file(file)
    ingest_url_ratio_service.ingest(data)
    return {"detail": "URL ratio data ingested successfully"}

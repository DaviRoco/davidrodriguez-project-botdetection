from fastapi import APIRouter, UploadFile, Depends
from core.ports.input.ingest_ip_usage import IngestIpUsage
from dependencies import get_ingest_ip_usage
from adapters.input.rest.ingest_helpers import parse_csv_file
ip_usage_router = APIRouter()


@ip_usage_router.post("/ip_usage/ingest")
async def ingest_activity(file: UploadFile, ingest_ip_usage_service: IngestIpUsage = Depends(get_ingest_ip_usage)):
    data = await parse_csv_file(file)
    ingest_ip_usage_service.ingest(data)
    return {"detail": "IP usage data ingested successfully"}

import pandas as pd
from io import StringIO
from fastapi import UploadFile, HTTPException


async def parse_csv_file(file: UploadFile) -> pd.DataFrame:
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")

    content = await file.read()
    try:
        data = pd.read_csv(StringIO(content.decode("utf-8")))
        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing CSV file: {str(e)}")
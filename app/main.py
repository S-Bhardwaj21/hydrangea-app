from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions import HydrangeaError

app = FastAPI()

@app.exception_handler(HydrangeaError)
async def hydrangea_exception_handler(request: Request, exc: HydrangeaError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.message},
    )
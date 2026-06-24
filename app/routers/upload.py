from fastapi import APIRouter, HTTPException
from app.schemas.upload import UploadBaseMaterial
from app.services.ai_service import generate_design_from_prompt

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/ai-prompt")
async def create_with_gemini(data: UploadBaseMaterial):
    try:
        design_result = await generate_design_from_prompt(data.content)
        return {"status": "success", "design": design_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
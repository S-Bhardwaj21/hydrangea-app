from pydantic import BaseModel

class UploadBaseMaterial(BaseModel):
    source_type: str  # 'ai_prompt', 'sketch', 'image', or 'link'
    content: str      # The actual prompt, image URL, or base64 data
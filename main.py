from fastapi import FastAPI, UploadFile, File
from watermark_embed import embed_watermark
from watermark_verify import verify_watermark
from certificate import generate_certificate

app = FastAPI()

@app.get("/")
def root():
    return {"message": "CreatorShield Watermark API Running"}

@app.post("/embed")
async def embed(file: UploadFile = File(...), creator_id: str = "unknown"):
    result = await embed_watermark(file, creator_id)
    return result

@app.post("/verify")
async def verify(file: UploadFile = File(...)):
    result = await verify_watermark(file)
    return result

@app.get("/certificate/{asset_id}")
async def certificate(asset_id: str):
    return generate_certificate(asset_id)
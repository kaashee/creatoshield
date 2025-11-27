from invisible_watermark import WatermarkDecoder
from PIL import Image
import io

async def verify_watermark(file):
    img = Image.open(io.BytesIO(await file.read()))
    decoder = WatermarkDecoder()
    watermark = decoder.decode(img, 'dwtDct')

    if watermark:
        creator_id = watermark.decode()
        return {
            "authentic": True,
            "creator_id": creator_id,
            "message": "Watermark detected successfully"
        }
    else:
        return {
            "authentic": False,
            "message": "No watermark found"
        }
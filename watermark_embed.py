from invisible_watermark import WatermarkEncoder
from PIL import Image
import io, base64

async def embed_watermark(file, creator_id):
    img = Image.open(io.BytesIO(await file.read()))
    encoder = WatermarkEncoder()
    encoder.set_watermark("bytes", creator_id.encode())
    watermarked = encoder.encode(img, 'dwtDct')

    img_byte_arr = io.BytesIO()
    watermarked.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    base64_image = base64.b64encode(img_byte_arr).decode("utf-8")

    return {
        "status": "success",
        "creator_id": creator_id,
        "watermarked_image": base64_image
    }
def generate_certificate(asset_id):
    return {
        "asset_id": asset_id,
        "certificate_url": f"https://your-domain.com/certificate/{asset_id}",
        "status": "verified",
        "message": "Verification certificate placeholder"
    }
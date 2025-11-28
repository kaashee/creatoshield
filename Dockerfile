FROM python:3.10-slim

WORKDIR /app

# Install system dependencies needed for OpenCV + invisible-watermark
RUN apt update && apt install -y libgl1 libglib2.0-0 ffmpeg

# Install build tools for some Python wheels
RUN apt install -y build-essential

# Copy and install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

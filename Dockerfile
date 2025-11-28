FROM python:3.10

WORKDIR /app

# System dependencies needed for invisible-watermark + OpenCV
RUN apt update && apt install -y libgl1 libglib2.0-0 ffmpeg

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your backend files
COPY . .

# Expose port for FastAPI
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

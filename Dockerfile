FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/VoxelHorizons/VoxelPluginBot"
LABEL org.opencontainers.image.description="Voxel Horizons Discord quick-reply support bot"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DATABASE_PATH=/data/replies.sqlite3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py storage.py ./

# The database must live on an EasyPanel persistent volume mounted at /data.
RUN mkdir -p /data && chown 10001:10001 /data
USER 10001:10001

CMD ["python", "bot.py"]

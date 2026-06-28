import os
from pathlib import Path

from configs.env import BASE_DIR


DJANGO_ENV = os.getenv("DJANGO_ENV").lower()

LOG_DIR_PATH = os.getenv("LOG_DIR_PATH")

if DJANGO_ENV == "production":
    LOGS_DIR = Path(os.getenv("LOGS_DIR", LOG_DIR_PATH))
elif DJANGO_ENV == "staging":
    LOGS_DIR = Path(os.getenv("LOGS_DIR", LOG_DIR_PATH))
else:
    LOGS_DIR = Path(os.getenv("LOGS_DIR", BASE_DIR / "logs"))
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

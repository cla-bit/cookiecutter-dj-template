import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent


def load_environment() -> None:
    env_file = BASE_DIR / ".env"

    if env_file.exists():
        load_dotenv(dotenv_path=env_file)


# Load environment immediately
load_environment()


DJANGO_ENV = os.environ.get("DJANGO_ENV", "development")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"configs.settings.{DJANGO_ENV}")

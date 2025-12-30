from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL", "")

# 3.1 Read env vars with defaults (plus a tiny config helper)
import os
from typing import Optional

def get_env(name: str, default: Optional[str] = None) -> str:
    val = os.getenv(name)
    return val if val is not None else default

def load_config() -> dict:
    return {
        "BASE_URL": get_env("BASE_URL", "https://api.example.com"),
        "API_KEY": get_env("API_KEY", ""),
        "TIMEOUT": float(get_env("TIMEOUT", "10")),
        "ENV": get_env("ENV", "dev"),
    }

# cfg = load_config()

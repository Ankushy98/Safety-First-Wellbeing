import os

from fastapi import Header, HTTPException
from dotenv import load_dotenv


load_dotenv()


def verify_admin_key(
    x_admin_key: str | None = Header(default=None)
):
    admin_key = os.getenv("ADMIN_API_KEY")

    if not admin_key or x_admin_key != admin_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing admin API key"
        )

    return True
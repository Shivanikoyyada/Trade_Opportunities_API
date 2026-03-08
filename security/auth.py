from fastapi import Header, HTTPException


def verify_token(authorization: str = Header(default=None)):

   
    if authorization is None:
        return None

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")

    token = authorization.split(" ")[1]

    if token != "mysecrettoken":
        raise HTTPException(status_code=401, detail="Invalid token")

    return token
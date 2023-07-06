from app.core.config import authorization_base_url, client_id, redirect_uri

async def authenticate():
    auth_url = f"{authorization_base_url}?client_id={client_id}&redirect_uri={redirect_uri}&scope=no_expiry"
    return auth_url

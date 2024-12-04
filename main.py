import uvicorn
from src.api.server import app


@app.get("/")
def read_root():
    return {"message": "Hello, Vercel!"}

# This handler function will be used by Vercel for serverless execution
def handler(event, context):
    """Serverless function handler that runs uvicorn"""
    config = uvicorn.Config("main:app", port=3000, log_level="info", reload=True, env_file=".env")
    server = uvicorn.Server(config)
    server.run()
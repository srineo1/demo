import uvicorn
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    uvicorn.run("api_service.fast_api_demo:app", host="127.0.0.1", port=8000, reload=True)


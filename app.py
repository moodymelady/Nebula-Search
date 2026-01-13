from fastapi import FastAPI
import uvicorn
from brain import NebulaBrain

app = FastAPI()
brain = NebulaBrain()

@app.get("/search")
async def search(query: str):
    print(f"📩 Received search request for: {query}")
    return brain.search(query)

@app.post("/index-folder")
async def index_folder():
    print("🔄 Watchman triggered a re-index...")
    brain.index_documents()
    return {"status": "success", "message": "Folder re-indexed"}

if __name__ == "__main__":
    # Initial index on startup
    brain.index_documents()
    uvicorn.run(app, host="127.0.0.1", port=8000)

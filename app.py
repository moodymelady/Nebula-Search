from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/search')
def search(query: str):
    print(f'📩 Received search request for: {query}')
    return {'answer': f'Python Brain says: I found some info about {query}!'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
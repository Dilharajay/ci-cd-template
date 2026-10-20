from fastapi import FastAPI
app = FastAPI(title="FastAPI starter")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}

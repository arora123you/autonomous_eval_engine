from fastapi import FastAPI
from api.routers import market,legal, operational   
app = FastAPI(
    title="Autonomous Enterprise Evaluation Engine",
    description="Digitizing assets and estimating financial impact for SMMs.",
    version="1.0.0"
)

# Include the routers for the three main layers
app.include_router(operational.router, prefix="/api/v1/operational", tags=["Operational Core"])
app.include_router(market.router, prefix="/api/v1/market", tags=["Market Dynamics"])
app.include_router(legal.router, prefix="/api/v1/legal", tags=["Legal & Disclosure"])

@app.get("/")
def read_root():
    return {"status": "Engine is online."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
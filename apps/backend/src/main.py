from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize resources
    print("Starting up...")
    yield
    # Shutdown: Clean up resources
    print("Shutting down...")

app = FastAPI(
    title="RaceCraftAnalyzer API",
    description="Backend API for RaceCraftAnalyzer - Motorsport Analytics Platform",
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    lifespan=lifespan
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "RaceCraftAnalyzer API is running"}

# Import and include routers here
# from .api.v1.router import api_router
# app.include_router(api_router, prefix="/api/v1")

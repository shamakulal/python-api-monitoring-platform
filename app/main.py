import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.config import (
    APP_DESCRIPTION,
    APP_NAME,
    APP_VERSION,
)
from app.routes.api import router


# Configure application logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle application startup and shutdown."""

    logger.info("Starting %s", APP_NAME)

    yield

    logger.info("Shutting down %s", APP_NAME)


# Initialize the FastAPI application
app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    lifespan=lifespan,
)


# Register API routes
app.include_router(router)


@app.get("/", tags=["Application"])
def root():
    """Return basic application information."""

    logger.info("Root endpoint accessed")

    return {
        "application": APP_NAME,
        "version": APP_VERSION,
        "description": APP_DESCRIPTION,
        "status": "running",
    }


@app.exception_handler(Exception)
async def handle_unexpected_exception(
    request: Request,
    exc: Exception,
):
    """Log unexpected errors and return a safe response."""

    logger.exception(
        "Unexpected error while processing %s %s",
        request.method,
        request.url.path,
    )

    return JSONResponse(
        status_code=500,
        content={
            "detail": "An unexpected internal server error occurred"
        },
    )
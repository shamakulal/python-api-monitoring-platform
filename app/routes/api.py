from fastapi import APIRouter, HTTPException

router = APIRouter()

# Sample service data
SERVICES = [
    {
        "id": 1,
        "name": "user-service",
        "status": "healthy",
        "description": "Handles user-related operations",
    },
    {
        "id": 2,
        "name": "payment-service",
        "status": "healthy",
        "description": "Handles payment-related operations",
    },
    {
        "id": 3,
        "name": "order-service",
        "status": "unhealthy",
        "description": "Handles order-related operations",
    },
]


@router.get("/health", tags=["Health"])
def health_check():
    """Check whether the API is responding."""
    return {
        "status": "healthy",
        "message": "Application is running",
    }


@router.get("/api/services", tags=["Services"])
def get_services():
    """Return the list of monitored services."""
    return {
        "total_services": len(SERVICES),
        "services": SERVICES,
    }


@router.get("/api/services/{service_id}", tags=["Services"])
def get_service(service_id: int):
    """Return details for one service."""
    for service in SERVICES:
        if service["id"] == service_id:
            return service

    raise HTTPException(
        status_code=404,
        detail=f"Service with ID {service_id} was not found",
    )


@router.get("/api/summary", tags=["Services"])
def get_summary():
    """Return a summary of service health."""

    total_services = len(SERVICES)

    healthy_services = sum(
        1 for service in SERVICES
        if service["status"] == "healthy"
    )

    unhealthy_services = total_services - healthy_services

    return {
        "total_services": total_services,
        "healthy_services": healthy_services,
        "unhealthy_services": unhealthy_services,
    }
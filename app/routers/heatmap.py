
from fastapi import APIRouter

router = APIRouter(prefix="/drivers", tags=["heatmap"])

@router.get("/heatmap")
def driver_heatmap():
    # Simulate high-demand areas
    high_demand_areas = [{"lat": 37.7749, "lng": -122.4194, "demand": 80}]
    return high_demand_areas

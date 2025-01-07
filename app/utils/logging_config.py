
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("ride_share_app.log"),  # Log to file
        logging.StreamHandler()  # Log to console
    ]
)

logger = logging.getLogger(__name__)

import logging
from datetime import datetime, timezone
from urllib.error import URLError
from urllib.request import urlopen

API_URL = "http://host.docker.internal:8000/health"

logging.basicConfig(
    filename="health_check.log",
    level=logging.INFO,
    format="%(asctime)s UTC - %(levelname)s - %(message)s",
)

def check_api():
    try:
        with urlopen(API_URL, timeout=10) as response:
            if response.status == 200:
                message = f"API is healthy: HTTP {response.status}"
                logging.info(message)
                print(message)
                return

            message = f"Unexpected HTTP status: {response.status}"
            logging.error(message)
            print(message)

    except (URLError, TimeoutError, OSError) as error:
        message = f"API health check failed: {error}"
        logging.error(message)
        print(message)

if __name__ == "__main__":
    print("Health check started:", datetime.now(timezone.utc).isoformat())
    check_api()

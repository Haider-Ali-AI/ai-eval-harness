
import functools
import logging
from collections.abc import Callable

logger = logging.getLogger(__name__)

def log_execution(func: Callable[..., dict]):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("START: %s", func.__name__)

        try:
            final = func(*args, **kwargs)

        except Exception:
            logger.exception("FAILED: %s", func.__name__)
            raise

        logger.info("FINISH: %s", func.__name__)
        return final

    return wrapper

@log_execution
def aggregate_results(results: list[dict]) -> dict:
    stats = {}

    default = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "pass_rate": 0.0
    }

    valid_case = ["PASS", "FAIL"]
    stats["total"] = len(results)

    for case in results:
        if case["status"] not in valid_case:
            raise ValueError("Invalid Input")

    if not results:
        return default

    stats["passed"] = sum(
        1 for case in results if case["status"] == "PASS"
    )
    stats["failed"] = sum(
        1 for case in results if case["status"] == "FAIL"
    )
    stats["pass_rate"] = (stats["passed"] / stats["total"]) * 100

    return stats

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    results = [
        {"case_id": 1, "status": "PASS"},
        {"case_id": 2, "status": "FAIL"},
        {"case_id": 3, "status": "PASS"}
    ]

    output = aggregate_results(results)
    print(output)
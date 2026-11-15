
import functools
import logging
import time

from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

logger = logging.getLogger(__name__)


def log_execution(func: Callable[P, R]) -> Callable[P, R]:

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start_time = time.perf_counter()

        logger.info("Started execution: %s", func.__qualname__)

        try:
            result = func(*args, **kwargs)

        except Exception:
            elapsed = time.perf_counter() - start_time

            logger.exception(
                "Execution failed: %s | Duration: %.4f seconds",
                func.__qualname__,
                elapsed,
            )
            raise

        elapsed = time.perf_counter() - start_time

        logger.info(
            "Execution completed: %s | Duration: %.4f seconds",
            func.__qualname__,
            elapsed,
        )

        return result

    return wrapper


@log_execution
def evaluate(test_case: dict) -> str:
    time.sleep(0.2)
    return test_case['status']


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    print(evaluate({"case_id": 3}))


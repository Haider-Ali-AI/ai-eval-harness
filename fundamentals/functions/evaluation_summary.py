
def summarize_results(results: list) -> dict:
    """Summarize total, passed, failed, and pass rate."""
    if not results:
        return {
            "total": 0,
            "passed": 0,
            "failed": 0,
            "pass_rate": 0.0,
        }

    total = len(results)
    passed = sum(
        case["status"] == "PASS"
        for case in results
    )
    failed = sum(
        case["status"] == "FAIL"
        for case in results
    )

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": (passed / total) * 100,
    }


def detect_failed_results(results: list) -> list:
    """Return all evaluation cases with FAIL status."""
    if not results:
        return []

    failed_list = []

    for case in results:
        if case["status"] == "FAIL":
            failed_list.append(case)

    return failed_list


def results_status(results: dict) -> str | None:
    """Return a case's status, or None if unavailable."""
    if not isinstance(results, dict):
        return None

    try:
        return results["status"]
    except KeyError:
        return None


def validate_results(results: dict) -> bool:
    """Check whether a result contains the required keys."""
    if not isinstance(results, dict):
        return False

    if "case_id" not in results or "status" not in results:
        return False
    if results["status"] == "PASS" or results["status"] == "FAIL":
        return True
    return False
    


def validation_exceptions(results: dict) -> bool:
    if not isinstance(results, dict):
        raise TypeError("Results must be a dictionary.")

    elif 'case_id' not in results or 'status' not in results:
        raise ValueError("Results must contain 'case_id' and 'status' keys.")

    elif results['status'] not in ['PASS', 'FAIL']:
        raise ValueError("Status must be 'PASS' or 'FAIL'.")

    return True

def validate_results(results : dict) -> bool:
    if not isinstance(results, dict):
        return False
    elif 'case_id' not in results or 'status' not in results:
        return False
    return True
if __name__ == "__main__" :
    print(validate_results({'case' : 12, 'status' : "PASS"}))

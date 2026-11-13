def process_results(results):
    processed = []

    for result in results:
        if result.get("status") == "PASS":
            processed.append(result["case_id"])

    return processed


if __name__== "__main__":

    results = [
    {"case_id": 1, "status": "PASS"},
    {"case_id": 2, "status": "FAIL"},
    {"case_id": 3},
    {"status": "PASS"},
    ]

    output = process_results(results)
    print(output)
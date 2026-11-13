import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logging.debug("Detailed diagnostic information")
logging.info("Evaluation started")
logging.warning("A test case has missing data")
logging.error("A test case failed")

def calculate_pass_rate(results):
    passed = 0

    for case in results:
        if case["status"] == "PASS":
            passed += 1

    result = passed / len([case["status"] for case in results])
    print (result)

def clean_input(results)-> bool:
    valid_case = 0
    for case in results :
        if case["status"] not in results or case["case_id"] not in results :
            logging.warning("Test case has missing data")
        elif case["status"] in results and case["case_id"] in results :
            valid_case += 1
    if valid_case == 0:
        logging.warning("No valid case detected")
        return False
    else :
        logging.info("Evaluation started")
        return True

if __name__ =="__main__":

    results = [
        {"case_id": 1, "status": "PASS"},
        {"case_id": 2, "status": "FAIL"},
        {"case_id": 3, "status": "PASS"},
        {"case_id": 4},
    ]

    if clean_input() is True :
        print(calculate_pass_rate(results))
    else :
        return 0.0
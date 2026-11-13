import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logging.debug("Detailed diagnostic information")
logging.info("Evaluation started")
logging.warning("A test case has missing data")
logging.error("A test case failed")

def evaluate_case(results:list):
    for case in results :
        if case.get("status") == 'PASS':
            logging.info("Test case passed: %s", case)
        else:
            logging.error("Test case failed: %s", case)
        logging.debug("Case status: %s", case.get("status"))

    
if __name__ == "__main__":
    output  = [
                        {"case_id": 1, "status": "PASS"},
                        {"case_id": 2, "status": "FAIL"},
                        {"case_id": 3, "status": "PASS"},
                        {"case_id": 4, "status": "FAIL"},
                        ]
    evaluate_case(output)
def log_exe(func):
    def wrapper(*args):
        print("Function started")
        val = func(*args)
        print("Function finished")
        return val
    return wrapper


@log_exe
def evaluate(*test_case):
    print(f"Evaluating: {test_case}")
    return "PASS"


if __name__ == "__main__":
    print(evaluate({"case_id": 1, "status": "PASS"}))
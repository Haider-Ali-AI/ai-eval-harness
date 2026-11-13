def log_exe(func):
    def wrapper():
        print("Function started")
        val = func()
        print("Funtion Finished")
        return val
    return wrapper

@log_exe
def outer_func():
    print("Evaluating test case")
    return "PASS"



if __name__ == "__main__":
    print(outer_func())
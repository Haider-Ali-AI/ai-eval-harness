def retrieve(results : list):
        iterator = iter(results)
        new = next(iterator)
        new_2 = next(iterator)
        print(new, new_2)

def retrieve_all(results: list):
    iterator = iter(results)
    collected = []
    while True:
        try:
            val = next(iterator)
        except StopIteration:
            break
        collected.append(val)
    return collected

def generate_results():
    yield {'case_id':1, "status":'PASS'}
    yield {'case_id':2, 'status':'FAIL'}
    yield {"case_id":3, "status":"PASS"}

def generate_failed_cases(results:list):
        for case in results:
            if case.get('status') == 'FAIL':
                yield case
if __name__ == "__main__":
    output  = [
                        {"case_id": 1, "status": "PASS"},
                        {"case_id": 2, "status": "FAIL"},
                        {"case_id": 3, "status": "PASS"},
                        {"case_id": 4, "status": "FAIL"},
                        ]
    try :
        print("Generator Created")
        output = generate_failed_cases(output)
        n1 = next(output)
        n2 = next(output)
        print(n1, n2)
        
    except StopIteration:
        print("Stop")
        for output in generate_failed_cases(output):
                print(output)

   
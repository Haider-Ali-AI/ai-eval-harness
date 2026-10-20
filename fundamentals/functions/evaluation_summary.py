

def detect_failed_results(results:list) ->list:
    if not results:
        return []

    failed_list = []
    for case in results :
        if case['status'] == 'FAIL' :
            failed_list.append(case)

    return failed_list

if __name__ == "__main__":
    print (detect_failed_results([{'status': 'PASS'}]))
import pytest
from evaluation_summary import validate_results, results_status, detect_failed_results, summarize_results
from validation_exceptions import validation_exceptions
from aggregator import  aggregate_results

test_cases = [
    {"case_id": 1, "status": "PASS"},
    {"case_id": 2, "status": "PASS"},
    {"case_id": 3, "status": "PASS"},

    {"case_id": 1, "status": "FAIL"},
    {"case_id": 2, "status": "FAIL"},
    {"case_id": 3, "status": "FAIL"},

    {"case_id": 1, "status": ""},
    {"case_id": 2, "status": ""},
    {"case_id": 3, "status": ""},

    {"case_id": 1, "status": "PASS"},
    {"case_id": 2, "status": "FAIL"},
    {"case_id": 3, "status": "PASS"},

    {"case_id": 1, "status": "PASS"},
    {"case_id": 2, "status": "FAIL"},
    {"case_id": 3, "status": "P"}
]


@pytest.mark.parametrize("case", test_cases)
def test_unified_runner(case):
    function = case["function"]
    input_data = case["input"]
    expected = case["expected"]
    expected_exception = case["expected_exception"]

    if expected_exception is not None:
        with pytest.raises(expected_exception):
            function(input_data)
    else:
        actual = function(input_data)
        assert actual == expected

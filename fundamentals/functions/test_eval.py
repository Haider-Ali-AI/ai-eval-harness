
import pytest

from evaluation_summary import (
    validate_results,
    results_status,
    detect_failed_results,
    summarize_results,
)
from validation_exceptions import validation_exceptions
from aggregator import aggregate_results


test_cases = [
    # validate_results
    {
        "function": validate_results,
        "input": {"case_id": 1, "status": "PASS"},
        "expected": True,
        "expected_exception": None,
    },
    {
        "function": validate_results,
        "input": {"case_id": 1, "status": "INVALID"},
        "expected": False,
        "expected_exception": None,
    },

    # results_status
    {
        "function": results_status,
        "input": {"case_id": 1, "status": "PASS"},
        "expected": "PASS",
        "expected_exception": None,
    },
    {
        "function": results_status,
        "input": {"case_id": 1},
        "expected": None,
        "expected_exception": None,
    },

    # validation_exceptions
    {
        "function": validation_exceptions,
        "input": {"case_id": 1, "status": "PASS"},
        "expected": True,
        "expected_exception": None,
    },
    {
        "function": validation_exceptions,
        "input": {"case_id": 1, "status": "INVALID"},
        "expected": None,
        "expected_exception": ValueError,
    },

    # aggregate_results
    {
        "function": aggregate_results,
        "input": [
            {"case_id": 1, "status": "PASS"},
            {"case_id": 2, "status": "FAIL"},
            {"case_id": 3, "status": "PASS"},
        ],
        "expected": {
            "total": 3,
            "passed": 2,
            "failed": 1,
            "pass_rate": pytest.approx(66.6666666667),
        },
        "expected_exception": None,
    },
    {
        "function": aggregate_results,
        "input": [],
        "expected": {
            "total": 0,
            "passed": 0,
            "failed": 0,
            "pass_rate": 0.0,
        },
        "expected_exception": None,
    },
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

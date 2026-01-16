# test_prime.py
from prime import prime_details

def test_prime_details():
    expected_output = (
        "Number: 7\n"
        "Prime\n"
    )

    assert prime_details(7) == expected_output

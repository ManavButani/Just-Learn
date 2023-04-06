"""
Write unit tests for the Phishtank exercise form REST API session. 
Use mocking to mock any API calls that need to be made.
"""
from task6 import main
def test_mocking(mocker):
    mocker.patch("task6.phishing",return_value=200)
    assert main("https://www.google.com/")==200

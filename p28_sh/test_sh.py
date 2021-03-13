import sys
from unittest import TestCase
from unittest.mock import patch
import sh


#@patch("sh.run_cmd", return_value="Mock!")
#@patch("sh.run_cmd")
@patch('subprocess.check_output', return_value="Mock!")
def test_run_cmd(Mock_check_output):
    exec = "python sh.py < testin.txt"
    print( exec )

    output = sh.run_cmd(exec)
    print(output)
    expect_out = "Mock!"
    assert( output == expect_out )


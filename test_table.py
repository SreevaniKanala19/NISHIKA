import subprocess
output = subprocess.check_output('python table.py')
output2 = output.decode()
output3 = output2.split('\n')
def test_first_line():
    assert  output3[0] == '5X1 = 5'


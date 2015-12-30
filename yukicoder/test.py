import time
import subprocess
import sys
import os

argvs = sys.argv
current_directory = os.getcwd()

path = (current_directory + '/' +
        str(argvs[1]) + '-testcase/').replace('/', '\\')
testcases = os.listdir(path + '\\test_in\\')
if not os.path.exists(path + '\\my_out\\'):
    os.mkdir(path + '\\my_out\\')

count_testcase = len(testcases)
count_AC = 0
count_WA = 0
count_TLE = 0

for case in testcases:
    input_file = path + '\\test_in\\' + case
    expected_file = input_file.replace('test_in', 'test_out')
    output_file = input_file.replace('test_in', 'my_out')

    cmd = ['python', './' + argvs[1] + '.py', '<', input_file, '>', output_file]

    start_time = time.time()
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        cp = p.communicate(timeout=1)
        stdout_data = cp.stdout.decode('utf-8')
        stderr_data = cp.stderr.decode('utf-8')
    except subprocess.TimeoutExpired:
        p.kill()
        count_TLE += 1
        status = 'TLE'
    except Exception as e:
        raise
    else:
        cmd = ['diff', '-q', expected_file, output_file]
        cp = subprocess.run(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if 'differ' in cp.stdout.decode('utf-8'):
            status = 'WA'
            count_WA += 1
        else:
            status = 'AC'
            count_AC += 1
    elapsed_time = time.time() - start_time
    print(status, str(round(elapsed_time, 7)) + '[s]', end=' ')
    print(input_file.replace(path + '\\test_in\\', ''))

print('AC', count_AC, '/', count_testcase)
print('WA', count_WA, '/', count_testcase)
print('TLE', count_TLE, '/', count_testcase)

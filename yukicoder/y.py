import sys
import os


def download_testcase(problem_number):
    import urllib3
    import bs4
    http = urllib3.PoolManager()
    url = 'http://yukicoder.me/problems/no/' + str(problem_number)
    contents = http.urlopen('GET', url).data
    soup = bs4.BeautifulSoup(contents.decode('utf-8'), 'html.parser')

    problem_number = ('0000' + str(problem_number))[-4:]
    problem_id = soup.find('div', id='content').get('data-problem-id')
    url = 'http://yukicoder.me/problems/' + str(problem_id) + '/testcase.zip'

    filename = str(problem_number) + '-' + str(problem_id) + '-testcase.zip'

    data = http.urlopen('GET', url)
    if data.status == 200:
        f = open(filename, 'wb')
        f.write(data.data)
        f.close()
    return filename


def unzip(filename, place):
    import zipfile
    if not os.path.exists(place):
        os.mkdir(place)
    zf = zipfile.ZipFile(filename, 'r')
    for f in zf.namelist():
        fn = os.path.basename(place + f)
        dir_name = (place + f).replace(fn, '')
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

        uzf = open(place + f, 'wb')
        uzf.write(zf.read(f))
        uzf.close()
        print(place + f)
    zf.close()


def run_test(python_file, test_path):
    import time
    import subprocess

    testcases = os.listdir(test_path + 'test_in/')
    if not os.path.exists(test_path + 'my_out/'):
        os.mkdir(test_path + 'my_out/')

    count_testcase = len(testcases)
    count_AC = 0
    count_WA = 0
    count_TLE = 0

    for case in testcases:
        input_file = test_path + '/test_in/' + case
        expected_file = input_file.replace('test_in', 'test_out')
        output_file = input_file.replace('test_in', 'my_out')

        cmd = ['python', python_file, '<', input_file, '>', output_file]

        start_time = time.time()
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            stdout_data, stderr_data = p.communicate(timeout=5)
            stdout_data = stdout_data.decode('utf-8')
            stderr_data = stderr_data.decode('utf-8')
        except subprocess.TimeoutExpired:
            p.kill()
            count_TLE += 1
            status = 'TLE'
        except Exception as e:
            raise
        else:
            cmd = ['diff',  expected_file, output_file]
            cp = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if '' == cp.stdout.decode('utf-8'):
                status = 'AC'
                count_AC += 1
            else:
                status = 'WA'
                count_WA += 1
        elapsed_time = time.time() - start_time
        print(status, str(round(elapsed_time, 7)) + '[s]', end=' ')
        print(input_file.replace(test_path + '/test_in/', ''))

    print('AC', count_AC, '/', count_testcase)
    print('WA', count_WA, '/', count_testcase)
    print('TLE', count_TLE, '/', count_testcase)


if __name__ == '__main__':
    argvs = sys.argv
    problem_number = ('0000'+argvs[1])[-4:]
    current_directory = os.getcwd()
    python_file = '.\\' + problem_number + '.py'
    path = (current_directory + '\\' + problem_number + '_test\\')
    if not os.path.exists(path):
        zip_name = download_testcase(problem_number)
        unzip(zip_name, path)
    run_test(python_file, path)

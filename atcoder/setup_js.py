import os
import sys


def main():
    argvs = sys.argv
    argc = len(argvs)

    if argc < 1:
        print('Usege\nsetup_js.py contest_name')
        exit(0)

    contest_name = argvs[1]
    if os.path.exists(contest_name):
        print('folder:', contest_name, 'is exists.')
    else:
        os.mkdir(contest_name)
        print('folder:', contest_name, 'is created.')

    problem_number = 4
    if argc > 2:
        problem_number = int(argvs[2])
    for i in range(problem_number):
        path = contest_name + '\\' + chr(ord('a') + i) + '.js'
        if os.path.isfile(path):
            print(path, 'is exists')
        else:
            f = open(path, 'w')
            f.write('function main(input) {\n\n}\n')
            f.write('main(require("fs").readFileSync("/dev/stdin", "utf8"));')
            f.close()
            print(path, 'created')
    for s in ['in.txt', 'out.txt']:
        path = contest_name + '\\' + s
        if os.path.isfile(path):
            print(path, 'is exists')
        else:
            f = open(path, 'w')
            f.close()
            print(path, 'created')


if __name__ == '__main__':
    main()

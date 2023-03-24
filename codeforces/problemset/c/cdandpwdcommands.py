# https://codeforces.com/contest/158/problem/C
n = int(input())
path = []

for i in range(n):
    cmdline = input().split()

    if cmdline[0] == 'pwd':
        if path:
            print(f"/{'/'.join(path)}/")
        else:
            print('/')
    else:
        cd_path = cmdline[1]
        if cd_path[0] == '/':
            path.clear()
        for directory in cd_path.split('/'):
            if directory:
                if directory == '..':
                    path.pop()
                else:
                    path.append(directory)

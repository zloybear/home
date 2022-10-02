import os

def gen_files_path(some_deer):
    print(f'')
    for i in os.walk(some_deer):
        if len(i[2]) > 0:
            for k in i[2]:
                yield f'{i[0]}\\{k}'

deer = gen_files_path('G:\\')
for file in deer:
    print(file)
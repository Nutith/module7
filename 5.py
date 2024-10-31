import os
import time

KIB = 1000
MIB = KIB ** 2
GIB = KIB ** 3
TIB = KIB ** 4


for root, dirs, files in os.walk('.'):
    print(os.path.join(root))

    for file in files:
        if not os.access(os.path.join(root, file), os.R_OK):
            continue

        fullname = os.path.join(root, file)
        mtime = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(fullname)))
        os_size = os.path.getsize(fullname)

        if os_size < KIB:
            size_suffics = 'B'
            size = os_size
        elif os_size < MIB:
            size_suffics = 'KiB'
            size = os_size / KIB
        elif os_size < GIB:
            size_suffics = 'MiB'
            size = os_size / MIB
        elif os_size < TIB:
            size_suffics = 'GiB'
            size = os_size / GIB
        else:
            size_suffics = 'TiB'
            size = os_size / TIB

        print(f'\t{file[:46]:.<50} '
              f'{size:5.1f} {size_suffics:<5}'
              f'{mtime}')

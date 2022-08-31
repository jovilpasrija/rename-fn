import os,sys

def rename_files(path):

    for filename in os.listdir(path):
        if not filename.startswith('.') and filename.endswith('.mkv'):
            file_path = os.path.join(path, filename)
            # print(filename)

            new_name = filename.split(' - ',1)[1].split(' (1080')[0] + '.mkv'
            new_name = os.path.join(path, new_name)

            # print(new_name)
            os.rename(file_path, new_name)


if __name__ == "__main__":
    path=sys.argv[1:][0]
    print(f"Entered {path=}")

    rename_files(r'{}'.format(path))

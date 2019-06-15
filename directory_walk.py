import os

ROOT_PATH = os.path.dirname(__file__)


def ls(container):
    """ list the contents of the container and join the results of the list to the path of the container
    """
    contents = [os.path.join(container, p) for p in os.listdir(container)]
    for item in contents:
        if os.path.isfile(item):
            print(f'{item} is a file')
        if os.path.isdir(item):
            print(f'{item} is a directory and its contents are:')
            ls(item)


def get_new_path(container, original_container, new_root):
    """ list the contents of the container and join the path relative to the original container with the new_root
    """
    contents = [os.path.join(container, p) for p in os.listdir(container)]
    for item in contents:
        if os.path.isfile(item):
            new_path = os.path.join(new_root, os.path.relpath(item, original_container))
            print(f'destination path of file {item} will be {new_path}')
        if os.path.isdir(item):
            new_path = os.path.join(new_root, os.path.relpath(item, original_container))
            print(f'destination path of dir {item} will be {new_path}')
            get_new_path(item, original_container, new_root)


def traverse():
    get_new_path(os.path.abspath(ROOT_PATH), os.path.abspath(ROOT_PATH), "C:\\Temp")


if __name__ == '__main__':
    traverse()
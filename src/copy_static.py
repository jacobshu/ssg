import os
import shutil


def copy_files_recursive(source, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for filename in os.listdir(source):
        from_path = os.path.join(source, filename)
        target_path = os.path.join(dest, filename)
        print(f" * {from_path} -> {target_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, target_path)
        else:
            copy_files_recursive(from_path, target_path)


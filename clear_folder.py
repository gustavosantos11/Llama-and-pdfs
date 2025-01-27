import os
import shutil


def clear_folder(folder):
    if os.path.exists(folder):
        for archive in os.listdir(folder):
            path_archive = os.path.join(folder, archive)
            try:
                if os.path.isdir(path_archive):
                    shutil.rmtree(path_archive)
                else:
                    os.remove(path_archive)
            except Exception as e:
                print(f"Erro ao remover {path_archive}: {e}")
    else:
        print(f"A pasta {folder} não existe.")

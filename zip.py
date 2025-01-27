from shutil import make_archive, move
from pathlib import Path


def zipping():
    make_archive('tabelas', 'zip', 'tables')

    absolute_path = Path.cwd()
    new_path = Path("\\".join(str(absolute_path).split("\\")[:-1]))
    new_folder = new_path / "Tabelas extraidas"

    new_folder.mkdir(exist_ok=True)
    print(f'Pasta: {new_folder} criada na área de trabalho')

    dir_original = "tabelas.zip"
    dir_final = new_folder / dir_original

    move(dir_original, dir_final)

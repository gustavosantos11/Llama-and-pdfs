from tkinter import filedialog


def buttonfile():
    filepath = filedialog.askopenfilenames(title='Selecione o .PDF')
    filepath_modified = "".join(filepath)
    return filepath_modified

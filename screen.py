# type:ignore
from PySimpleGUI import PySimpleGUI as sg
from main import extract_tables
from clear_folder import clear_folder


folder = "tables"
folder2 = "my_pdf"

sg.theme('LightBlue')
layout = [
    [sg.Text('Selecione o arquivo .PDF')],
    [sg.Button('PDF')],
    [sg.Text("", key='wait')],
    [sg.Text("", key="finished"),]
]

window = sg.Window('.PDF para Excel', layout)
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == "PDF":
        window["wait"].update("Aguarde, estamos extraindo os dados")
        clear_folder(folder)
        clear_folder(folder2)
        extract_tables()
        window["finished"].update(
            "Operação finalizada, resultados na pasta 'Tabelas Extraidas' em sua área de Trabalho",
        )

window.close()

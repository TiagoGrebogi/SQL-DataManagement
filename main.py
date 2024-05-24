import PySimpleGUI as sg
from functions import *

def update_layout(window, message):
    window.extend_layout(window, [[sg.Text(message, key='-MESSAGE-', font=('Fira-Code', 10), text_color='black')]])

layout = [
    [sg.Text('Seja bem vindo(a) a Oficina Auto Tech!', font=('Fira-Code', 16), text_color='black')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('Selecione a opção desejada!', font=('Fira-Code', 10))],
    [sg.Combo(['Inventário', 'Movimento de Estoque', 'Em falta'], default_value='Inventário', size=(500), font='Fira-Code', key='option-input')],
    [sg.Button('Rodar')],
    [sg.Text('', key='-MESSAGE-', font=('Fira-Code', 10), text_color='black')]
]

window = sg.Window('Oficina Auto Tech', layout=layout, size=(800, 800))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Rodar':
        option = values['option-input']
        if option == 'Inventário':
            message = 'Você selecionou a opção Inventário'
            window['-MESSAGE-'].update(message)
        elif option == 'Movimento de Estoque':
            message = 'Você selecionou a opção Movimento de Estoque'
            window['-MESSAGE-'].update(message)
        elif option == 'Em falta':
            message = 'Você selecionou a opção Em falta'
            window['-MESSAGE-'].update(message)

window.close()

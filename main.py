import PySimpleGUI as sg
from functions import *

#Interface Layout
layout = [
  [sg.Text('Seja bem vindo(a) a Oficina Auto Tech!', font=('Fira-Code', 16))],
  [sg.HorizontalSeparator(color='black')],
  [sg.Combo(['Inventário', 'Movimento de Estoque', 'Em falta'], default_value='Inventário', size=(500), font='Fira-Code')]
]

window = sg.Window('Oficina Auto Tech', layout=layout, size=(800,800))

while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED:
    break
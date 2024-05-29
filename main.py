import PySimpleGUI as sg
import mysql.connector
import os

def Limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

host = "167.99.252.245"
user = "ESW2024_E7"
passwd = "123mudar"
database = "ESW2024_E7_AUTOTECH"
conector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
cursor = conector.cursor()

def InserirPeca(peca, marca, modelo, quantidade, preco):
    sql = "INSERT INTO InventarioPecas (peca, marca, modelo, quantidade, preco) VALUES (%s, %s, %s, %s, %s)"
    val = (peca, marca, modelo, quantidade, preco)
    cursor.execute(sql, val)
    conector.commit()
    print(cursor.rowcount, "registro(s) inserido(s).")

def ListarInventario():
    cursor.execute("SELECT * FROM InventarioPecas")
    myresult = cursor.fetchall()

    colunas = [i[0] for i in cursor.description]

    formatted_results = []
    for row in myresult:
        row = list(row)
        row[colunas.index('preco')] = f"R$ {row[colunas.index('preco')]:.2f}"
        formatted_results.append(row)

    return colunas, formatted_results

colunas, _ = ListarInventario()

layout = [
    [sg.Text('Seja bem vindo(a) a Oficina Auto Tech!', font=('Fira-Code', 16), text_color='black')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('Selecione a opção desejada!', font=('Fira-Code', 10))],
    [sg.Combo(['Inventário', 'Inserir Peças', 'Relatório','Em falta'], default_value='Inventário', size=(30), font='Fira-Code', key='option-input')],
    [sg.Button('Rodar')],
    [sg.Table(values=[], headings=colunas, col_widths=20, auto_size_columns=False, display_row_numbers=False, justification='center', num_rows=20, key='-TABLE-', row_height=25, font=('Fira-Code', 10), visible=False)],
    [sg.Text('', key='-MESSAGE-', font=('Fira-Code', 10), text_color='black')]
]

window = sg.Window('Oficina Auto Tech', layout=layout, size=(1000, 700))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Rodar':
        option = values['option-input']
        if option == 'Inventário':
            colunas, data = ListarInventario()
            window['-TABLE-'].update(values=data, visible=True)
            window['-MESSAGE-'].update('Você selecionou a opção Inventário')
        elif option == 'Inserir Peças':
            layout_inserir = [
                [sg.Text('Inserir Nova Peça', font=('Fira-Code', 14))],
                [sg.Text('Peça:'), sg.InputText(key='-PECA-')],
                [sg.Text('Marca:'), sg.InputText(key='-MARCA-')],
                [sg.Text('Modelo:'), sg.InputText(key='-MODELO-')],
                [sg.Text('Quantidade:'), sg.InputText(key='-QUANTIDADE-')],
                [sg.Text('Preço:'), sg.InputText(key='-PRECO-')],
                [sg.Button('Inserir')]
            ]
            window_inserir = sg.Window('Inserir Peça', layout=layout_inserir)
            while True:
                event_inserir, values_inserir = window_inserir.read()
                if event_inserir == sg.WIN_CLOSED:
                    break
                if event_inserir == 'Inserir':
                    peca = values_inserir['-PECA-']
                    marca = values_inserir['-MARCA-']
                    modelo = values_inserir['-MODELO-']
                    quantidade = values_inserir['-QUANTIDADE-']
                    preco = values_inserir['-PRECO-']
                    InserirPeca(peca, marca, modelo, quantidade, preco)
                    sg.popup('Peça inserida com sucesso!')
                    window_inserir.close()
        elif option == 'Movimento de Estoque':
            window['-MESSAGE-'].update('Você selecionou a opção Movimento de Estoque')
            window['-TABLE-'].update(visible=False)
        elif option == 'Em falta':
            window['-MESSAGE-'].update('Você selecionou a opção Em falta')
            window['-TABLE-'].update(visible=False)

window.close()
conector.close()

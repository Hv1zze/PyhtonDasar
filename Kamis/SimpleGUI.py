import PySimpleGUI as sg
layout = [[sg.Button('Klik Saya')]]
Window = sg.Window('Contoh Program PySimpleGUI', layout)

while True:
    event, values = Window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Klik Saya':
        print('Tombol DiKlik')

Window.close()
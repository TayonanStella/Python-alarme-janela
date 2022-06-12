from PySimpleGUI import PySimpleGUI as sg
from time import localtime
from time import sleep
from pygame import mixer
hora = minu = 0
sg.theme('dark')
layout = [
    [sg.Text('Hora'), sg.Input(key='Hora', size=(10, 1))],
    [sg.Text('Minutos'), sg.Input(key='Minutos', size=(10, 1))],
    [sg.Button('Definir alarme')]
]

janela = sg.Window('alarme', layout)

while True:
    eventos, valores = janela.Read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Definir alarme':
        hora = valores['Hora']
        minu = valores['Minutos']
        break

while True:
    if localtime().tm_hour == int(hora) and localtime().tm_min == int(minu):
        print("acorde")
        mixer.init()
        mixer.music.load("ani.mp3")
        mixer.music.play()
        sleep(200)
        break

import PySimpleGUI as sg
import serial
import serial.tools.list_ports
import time

ser = serial.Serial()
com_port = [comport.device for comport in serial.tools.list_ports.comports()] + ['']  # получаем список  COM портов

layout=[[sg.Text('COM порт:', size=(9, 1)), sg.Combo((com_port[:-1]), readonly=True, size=(6, 20),
    default_value=com_port[0], key='COM'), sg.Button('DFU', key='send', enable_events=True)]]

com_port = [comport.device for comport in serial.tools.list_ports.comports()]
window = sg.Window('DFU_mode', layout, finalize=True)

while True:
    event, values = window.read()
    if event == 'send':
        ser = serial.Serial(values['COM'], 115200, timeout=5)
        comand = 'cdfu\0'  # откл заряд и разряд
        ser.write(comand.encode('utf-8'))
        time.sleep(0.5)
        ser.close()
    if event in (sg.WIN_CLOSED, 'Выход'):
        ser.close()
        break

window.close()
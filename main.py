
# BY DOGAN ALP AKBAS
import PySimpleGUI as sg
layout = [
    [sg.Input(key = '-INPUT-', font = ('Arial', 16)),
    sg.Spin(['binary to decimal', 'decimal to binary'], key ='-UNITS-',  font = ('Arial', 16)),
    sg.Button('Convert', key='-CONVERT-', font = ('Arial', 16))
    ],
    [sg.Text('OUTPUT', key='-OUTPUT-')]
]
window =sg.Window('Binary <-> Decimal Converter', layout)
def binary_converter(binary_val):

    decimal_num = 0
    for n in range(len(binary_val)):
        revers_num = int(binary_val[::-1][n])
        decimal_num += revers_num * 2**n
    return decimal_num

def decimal_converter(decimal_val):
    binary_num =''
    decimal_val = int(decimal_val)
    if decimal_val == 0:
        binary_num = "0"

    while decimal_val > 0:
        binary_num = str(decimal_val % 2) + binary_num
        decimal_val = decimal_val // 2

    return binary_num


while True:
    event, values =window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-CONVERT-':
        input_value =values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'binary to decimal':
                    output = binary_converter(input_value)
                    output_string = 'Binary value = {} ===>> Decimal value = {}'.format(input_value, output)
                case 'decimal to binary':
                    output = decimal_converter(input_value)
                    output_string = 'Decimal value = {} ===>> Binary value = {}'.format(input_value, output)
            window['-OUTPUT-'].update(output_string, font = ('Arial', 16))
        else:
            window['-OUTPUT-'].update('Please enter a valid input',font = ('Arial', 16))
window.close()

# pip install pysimplegui
import PySimpleGUI as sg


def metric_converter(data, in_metric, out_metric):
    metrics = {
        'm': 1, 'mm': 1000, 'cm': 100, 'mi': 0.000621371192,
        'in': 39.3700787, 'km': 0.001, 'ft': 3.2808399, 'yd': 1.0936133
    }
    return data/metrics[in_metric]*metrics[out_metric]


sg.theme('BluePurple')

layout = [
    [sg.Text('Input:'),
     sg.InputText(key='-IN-'),
     sg.Combo(('m', 'mm', 'cm', 'mi', 'in', 'km', 'ft', 'yd'), 'm', readonly=True, key='-IN-M-')],
    [sg.Text('Output:'),
     sg.Text('0', key='-OUT-'),
     sg.Combo(('m', 'mm', 'cm', 'mi', 'in', 'km', 'ft', 'yd'),
              'm', readonly=True, key='-OUT-M-'),
     sg.Submit('Convert')]
]
window = sg.Window('Metric Converter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Convert' and values['-IN-'] != '':
        result = metric_converter(
            float(values['-IN-']), values['-IN-M-'], values['-OUT-M-'])
        window['-OUT-'].update(result)
window.close()

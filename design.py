import PySimpleGUI as sg
sg.theme('SandyBeach')
layout = [
    [sg.Text('Version 0.3'),
     ],
    [sg.Text('Developed by Jabka125'),
     ],
    [sg.Button('Start'),
     ],
    [sg.Output(size=(60, 15))],
    [sg.Cancel()]
]
window = sg.Window('Minada16', layout)
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
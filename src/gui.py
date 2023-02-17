import PySimpleGUI as sg
import os 

class popupgui:
    def __init__(self):
        self.file_path = None
        self.layout = [
            [sg.Text('Select a file:'), sg.Input(key='-FILE-', enable_events=True,
                                                 default_text="Do not write the file path here. Use the browse button"),
             sg.FileBrowse()],
            [sg.OK(), sg.Cancel()]
        ]
        self.window = sg.Window('File Selection', self.layout)

    def get_file_path(self):
        while True:
            event, values = self.window.read()
            if event in (sg.WINDOW_CLOSED, 'Cancel'):
                self.window.close()
                return None
            if event == 'OK' and self.file_path is not None:
                self.window.close()
                return self.file_path
            if event == '-FILE-':
                self.file_path = values['-FILE-']
                file_size = os.path.getsize(self.file_path) / 1024 / 1024
                file_size = round(file_size, 2)
                confirm_layout = [
                    [sg.Text(f'Filename: {self.file_path}')],
                    [sg.Text(f'Size: {file_size} MB')],
                    [sg.Button('Continue'), sg.Button('Cancel')]
                ]
                confirm_window = sg.Window('Confirm', confirm_layout)
                confirm_event, confirm_values = confirm_window.read()
                confirm_window.close()
                if confirm_event == 'Continue':
                    return self.file_path
                else:
                    self.file_path = None











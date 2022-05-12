import PySimpleGUI as sg
import pathlib

WIN_W = 90
WIN_H = 25
file = None

menu_layout = [['Plik', ['Nowy (Ctrl+N)', 'Otwórz (Ctrl+O)', 'Zapisz (Ctrl+S)', 'Zapisz jako', '---', 'WYJDŹ']],
               ['Info', ['Po co ten program?']]]

layout = [[sg.Menu(menu_layout)],
          [sg.Text('Nowa Notka', font=('Consolas', 10),
                   size=(WIN_W, 1), key='_INFO_')],
          [sg.Multiline(font=('Consolas', 12), size=(WIN_W, WIN_H), key='_BODY_')]]

window = sg.Window('Notatnik Plejka', layout=layout, margins=(
    0, 0), resizable=True, return_keyboard_events=True, finalize=True)
window.maximize()
window['_BODY_'].expand(expand_x=True, expand_y=True)


def new_file():
    window['_BODY_'].update(value='')
    window['_INFO_'].update(value='Nowa Notka')
    file = None
    return file


def open_file():
    filename = sg.popup_get_file('Otwórz', no_window=True)
    if filename:
        file = pathlib.Path(filename)
        window['_BODY_'].update(value=file.read_text())
        window['_INFO_'].update(value=file.absolute())
        return file


def save_file(file):
    if file:
        file.write_text(values.get('_BODY_'))
    else:
        save_file_as()


def save_file_as():
    filename = sg.popup_get_file('Zapisz jako', save_as=True, no_window=True)
    if filename:
        file = pathlib.Path(filename)
        file.write_text(values.get('_BODY_'))
        window['_INFO_'].update(value=file.absolute())
        return file


def about_me():
    sg.popup_no_wait(
        '"Więc stworzyłem to gówno by inni zadawali pytania i się dziwili" ~ Plejek Klejek 2k22')


while True:
    event, values = window.read()
    if event in ('WYJDŹ', None):
        break
    if event in ('Nowy (Ctrl+N)', 'n:78'):
        file = new_file()
    if event in ('Otwórz (Ctrl+O)', 'o:79'):
        file = open_file()
    if event in ('Zapisz (Ctrl+S)', 's:83'):
        save_file(file)
    if event in ('Zapisz jako',):
        file = save_file_as()
    if event in ('Po co ten program?',):
        about_me()
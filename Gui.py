import PySimpleGUI as sg
import asyncio
import aiohttp
import json

from main_async import coinbase, kucoin, myfin, myfin_btc


def load_json_data():
    asyncio.run(coinbase())
    with open('JSON/cryptoDictCOINBASE.json') as file:
        data = json.load(file)
    return data


def main():
    # Load the initial JSON data
    data = load_json_data()

    # Create the PySimpleGUI layout
    layout = [
        [sg.Text('Coinbase JSON Data', font=('Arial', 14))],
        [sg.Listbox(zvalues=list(data.keys()), size=(20, 10), key='-KEYS-', enable_events=True)],
        [sg.Text('Value:', size=(10, 1)), sg.Text('', size=(30, 1), key='-VALUE-')],
        [sg.Button('Update')],
    ]

    # Create the PySimpleGUI window
    window = sg.Window('Coinbase JSON Viewer', layout)

    # Event loop to process PySimpleGUI events
    while True:
        event, values = window.read()

        # Close the window if the 'Exit' button is clicked or the window is closed
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        # Update the JSON data if the 'Update' button is clicked
        if event == 'Update':
            data = load_json_data()

        # Get the selected key from the listbox
        selected_keys = values['-KEYS-']

        # Update the value text element with the selected key's value
        if selected_keys:
            selected_key = selected_keys[0]
            window['-VALUE-'].update(data.get(selected_key, ''))

    # Close the PySimpleGUI window
    window.close()


if __name__ == "__main__":
    main()

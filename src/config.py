from modules import os
get_dir = os.path.dirname(__file__)

interface = {
    'palette': {
        'cor1': '#017f74',
        'cor2': '#158ca2',
        'cor3': '#A3A5A5',
        'cor4': '#23395b',
        'cor5': '#ffffff',
    },

    'icon': {
        'login': f'{get_dir}\images\\personal.ico',
        'system': f'{get_dir}\images\\people.ico',
    },

    'font': {
        1: 'Helvetica',
        2: 'Arial'
    },
}

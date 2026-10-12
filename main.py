# Lester checker
from pyscript import document # type: ignore


def lester_finder(e):
    document.getElementById('conclusion').innerHTML = ''
    last_name = document.getElementById('lester').value.lower().strip()
    first_name = document.getElementById('firstname').value.lower().strip()

    full_name = first_name + " " + last_name
    missing_people = ['seb ucie', 'basti smith', 'les turr', 'lesty zaboy', 'tian parker', 'marclyndon becortiez', 'sebastian uclaray']
    people_checker = full_name in missing_people

    display_message = (f'no {full_name} found.', f'{full_name} is someone we know')
    display(display_message[people_checker], target='conclusion') # type: ignore

import json
import os


def load_existing_save(savefile):
    with open(os.path.join(savefile), 'r+') as file:
        variables = json.load(file)
    return variables


def write_save(data):
    with open(os.path.join(os.getcwd(), 'save.json'), 'w') as file:
        json.dump(data, file)


def load_save():
    try:
        save = load_existing_save('save.json')
    except:
        save = create_save()
        write_save(save)
    return save


def create_save():
    save = {'score': 0}  # Initialize save with a score of 0
    return save

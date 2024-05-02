import json
import pygame
if __name__ == '__main__':
    def get_word_list():
        with open('en_UK.json', 'r', encoding='utf-8') as data:
            return json.load(data)


    def get_ipa_list():
        with open("ipa_sounds.json", 'r', encoding='utf=8') as data:
            return json.load(data)

    pygame.init()
    pygame.mixer.init()
    remove_char = ['ˈ', '/', 'ˌ', "\u200d"]
    sounds = []
    ipa_sounds = get_ipa_list()
    word_dict = get_word_list()
    x = input("Input any word in the English language:")
    try:
        edited_ipa_key = word_dict[x]
    except KeyError:
        print(f"{x} isn't in the dictionary")
        exit()
    for char in remove_char:
        edited_ipa_key = edited_ipa_key.replace(char, '')
    i = 0
    while i < len(edited_ipa_key):
        char = edited_ipa_key[i]
        if i < len(edited_ipa_key) - 1 and char + edited_ipa_key[i + 1] in ipa_sounds:
            sounds.append(char + edited_ipa_key[i + 1])
            i += 2
        else:
            sounds.append(char)
            i += 1
    print(x, word_dict[x])
    print(edited_ipa_key)
    print(sounds)
    for i in sounds:
        print(ipa_sounds.get(i))
        current_sound = pygame.mixer.Sound(str(ipa_sounds.get(i)))
        current_sound.play()

import json
import pygame
import time

# TODO:
#    Do more testing, expend the dictionary: as, seashore
if __name__ == '__main__':
    def get_word_list():
        with open('en_UK.json', 'r', encoding='utf-8') as data:
            return json.load(data)


    def get_ipa_list():
        with open("ipa_sounds.json", 'r', encoding='utf=8') as data:
            return json.load(data)

    def process(word_, word_dict_, ipa_sounds_):
        remove_char = ['ˈ', '/', 'ˌ', "\u200d", ",", ".", "?", "...", "!", "'", ":", ";", "-", "(", ")", '"']
        sounds = []
        try:
            edited_ipa_key = word_dict_[word_]
        except KeyError:
            print(f"{word_} isn't in the dictionary")
            exit()
        for char in remove_char:
            edited_ipa_key = edited_ipa_key.replace(char, '')
        i = 0
        while i < len(edited_ipa_key):
            char = edited_ipa_key[i]
            if i < len(edited_ipa_key) - 1 and char + edited_ipa_key[i + 1] in ipa_sounds_:
                sounds.append(char + edited_ipa_key[i + 1])
                i += 2
            else:
                sounds.append(char)
                i += 1
        print(word_, word_dict_[word_])
        print(edited_ipa_key)
        print(sounds)
        for i in sounds:
            print(ipa_sounds_.get(i))
            current_sound = pygame.mixer.Sound(str(ipa_sounds_.get(i)))
            current_sound.play()
            time.sleep(1)

    pygame.init()
    pygame.mixer.init()
    ipa_sounds = get_ipa_list()
    word_dict = get_word_list()
    print("Without any special characters, number symbols, abbreviations etc,")
    sentence = input("Input any sentence in the English language :")
    sentence = sentence.lower()
    words = sentence.split()
    for word in words:
        if word == "i":
            word = "I"
        process(word, word_dict, ipa_sounds)

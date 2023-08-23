import configparser

config = configparser.ConfigParser()
config.read('config.ini')
language = config.get('Language', 'lang')
skip_checking = config.getboolean('Options', 'skip_checking')

texts = {}


def read_languages():
    if language == 'hu':
        with open('src/hu/hu_settings.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    key, value = line.split('=', 1)
                    texts[key] = value
    else:
        with open('src/en/en_settings.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    key, value = line.split('=', 1)
                    texts[key] = value


def show_language_chooser():
    print('=' * 25)
    print(texts['select_lang'])
    print('=' * 25)
    print('')

    print('[1] English')
    print('[2] Hungarian')

    choice = input(f'\n{texts["enter_lang_option"]} ')

    if choice == '1':
        return 'en'
    elif choice == '2':
        return 'hu'

    else:
        print(texts['invalid'])

    return show_language_chooser()


def show_skip_checking():
    read_languages()

    print('=' * 50)
    print(f"{texts['skip_account_check']} ({texts['y'].upper()}/{texts['n'].upper()})")
    print('=' * 50)
    print('')

    choice = input(': ').lower()
    if choice == texts['y']:
        return 'true'
    elif choice == texts['n']:
        return 'false'

    else:
        print(texts['invalid'])

    return show_skip_checking()


read_languages()

language = show_language_chooser()
config.set('Language', 'lang', language)

with open('config.ini', 'w') as file:
    config.write(file)

skip = show_skip_checking()
config.set('Options', 'skip_checking', skip)

with open('config.ini', 'w') as file:
    config.write(file)

print(texts['setup_done'])

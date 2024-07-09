import re
import string
from collections import Counter
from pathlib import Path
from typing import *

WORD_MINIMUM_LENGTH = 3
WORD_MAXIMUM_LENGTH = 50


def open_file(location) -> str:
    try:
        with open(location, 'r', encoding='charmap') as file:
            raps = file.read()
    except UnicodeDecodeError:
        print('Error')
    finally:
        print('File opened')
    return raps


def word_match(word, prepositions):

    if word.lower() == 'omitted':
        word = '$0000media00000$'
    if (
            WORD_MINIMUM_LENGTH <= len(word) <= WORD_MAXIMUM_LENGTH and
            word not in string.punctuation
    ):
        if not word.isdigit():
            if word.lower() not in prepositions:
                if word[0].isalnum():
                    return True
    return False


# reserve = [\s:.,*\d}\\!?+/><]

def list_of_matches(text):
    pattern = re.compile(r'[\s:.,*\d}\\!?+/><]')
    return re.split(pattern, text)


def filter_result(text: str, include_common_words=False) -> List:  # TODO COMMON WORDS
    if not include_common_words:
        prepositions = [

            'that', 'for', 'you', 'the', 'be', 'i', 'on', 'up', 'in',
            'they', 'to', 'my', 'me', 'or', 'of', 'is', 'then', 'and',
            'then', 'are', 'it', 'an', 'as', 'by', 'at', 'with', 'this',
            'can', 'do', 'media'
        ]
    else:
        prepositions = []
    return [word.lower() for word in list_of_matches(text) if word_match(word, prepositions)]


def word_counter(result) -> List:
    counter = Counter(result)
    counter = sorted(list(counter.items()), key=lambda x: x[1], reverse=True)
    print('words have been counted')
    return counter


def finalise() -> Tuple:
    location = Path(r'')  # TODO PUT LOCATION HERE

    result = open_file(location)
    result = filter_result(result, include_common_words=False)
    final_result = word_counter(result)

    name = location.name.replace('.txt', '')

    locator = location.parent
    file = locator / f'{name}__statistics.txt'

    print('finalising...')
    return final_result, file


def save_to_file() -> None:
    lines_man = 150
    final_result, file_location = finalise()
    total_number_of_words = 0
    with open(file_location, 'w', encoding='charmap') as file:
        for _, count in final_result:
            total_number_of_words += int(count)
        print('statistics'.upper().center(round(lines_man / 2), '_'), file=file)
        print(file=file)
        print(f'total number of words :     {len([word for word, _ in final_result])}'.upper(),
              file=file)
        print(f'Word with highest value:     {final_result[0][0]}'.upper(), file=file)
        print(f'Total word count :    {total_number_of_words}'.upper(), file=file)
        print(f'Location of file :    {file_location.as_posix()}'.upper(), file=file)
        print(file=file)
        print('information'.upper().center(round(lines_man / 2), '_'), file=file)

        print('_' * lines_man, file=file)
        print('| {:^50}  |  {:>20}'.format('WORD', 'COUNT'), file=file)
        print('_' * lines_man, file=file)

        for word, count in final_result:
            print('| {:^50}  |  {:^20}'.format(word.upper(), count), file=file)
            print('_' * lines_man, file=file)

    print('file saved')


def main() -> None:
    save_to_file()
    print('DONE!!!!!!!!! ')


if __name__ == '__main__':
    main()

import requests

base_url = "https://swapi.dev/api/"
list_characters = set()


def get_characters_from_film(film_url):
    """
    Функция получает айди фильм и возвращает данные по персонажам,
    что встречаются в этом фильме
    :param film_url:
    :return:
    """
    get_result = requests.get(film_url)
    assert get_result.status_code == 200, 'Invalid status code'
    characters = get_result.json().get("characters")
    return characters


def get_characters_info_for_Veider():
    """
        Функция получает список фильмов, где встречается Дарт Вейдер
        :param film_url:
        :return:
        """
    url = f"{base_url}people/4"
    get_result = requests.get(url)
    assert get_result.status_code == 200, 'Invalid status code'
    films = get_result.json().get("films")
    return films


def get_characters_info(character_url):
    """
        Функция получает информация о персонаже и возвращает его имя
        :param film_url:
        :return:
        """
    request = requests.get(character_url)
    assert request.status_code == 200, 'Invalid status code'
    character_name = request.json().get("name")
    return character_name


def write_characters_into_file():
    """
    Функция перебирает персонажей в characters и записывает в файле
    :return:
    """
    try:
        with open('characters.txt', 'a', encoding='utf-8') as f:
            for character in list_characters:
                f.write(character)
    except Exception as e:
        print(f"Error {e}")


def test_starwars_api():
    """
    Основная функция, которая вызывает другие функции внутри себя
    :return:
    """
    for film in get_characters_info_for_Veider():
        title_film = requests.get(film)
        print(f"Получаем информация о фильме {title_film.json().get('title')}")
        for character in get_characters_from_film(film):
            character_name = get_characters_info(character)
            print(f"Получаем информацию о персонаже {character_name}")
            list_characters.add(f'{character_name}\n')
            print(f"Информация о персонаже {character_name} добавлена в список")
    write_characters_into_file()


test_starwars_api()
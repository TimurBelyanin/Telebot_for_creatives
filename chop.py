from PIL import Image
import os
from random import choice, random


def remake_data(string: str):
    """Цель этой функции - выдать 4 фрагмента, из строки, данной пользователем:
    1) Путь до папки откуда будут рандомно браться фоны
    2) Путь до папки откуда будут рандомно браться рамки
    3) Путь до папки откуда будут рандомно браться текста
    4) Размер пака"""
    elements = string.split(", ")
    backgrounds_folder = f'{elements[0]}\\Фоны\\Фоны_{elements[-2].lower().replace(" ", "_") if "(" not in elements[-2] else "две_рамки"}\\Фоны\\{elements[1]}'
    frames_folder = f'{elements[0]}\\Фоны\\Фоны_{elements[-2].lower().replace(" ", "_") if "(" not in elements[-2] else "две_рамки"}\\Рамки'
    texts_folder = f'{elements[0]}\\Текста\\Текста_{elements[-2].lower().replace(" ", "_") if "(" not in elements[-2] else "две_рамки"}\\{elements[2]}'
    size_pack = elements[-1]
    return backgrounds_folder, frames_folder, texts_folder, size_pack


def blaming_elements(
    background: str, frame_1: str, text_1: str, frame_2: str = None, text_2: str = None
):
    """Функция для объединения переданных фрагментов. Фрагменты содержат полные пути до файлов, которые нужно будет загрузить."""
    with Image.open(background) as background:
        background.load()
        if choice([True, False]):
            background = background.transpose(Image.FLIP_LEFT_RIGHT)
    with Image.open(frame_1) as frame_1:
        background.paste(frame_1, (0, 0), mask=frame_1)
    with Image.open(text_1) as text_1:
        background.paste(text_1, (0, 0), mask=text_1)
    if frame_2 is not None:
        with Image.open(frame_2) as frame_2:
            background.paste(frame_2, (0, 0), mask=frame_2)
    if text_2 is not None:
        with Image.open(text_2) as text_2:
            background.paste(text_2, (0, 0), mask=text_2)
    return background


def generation_elements(
    path_to_backgrounds: str, path_to_frames: str, path_to_texts: str, size_pack: str
):
    """Функция для генерации элементов для создания изображения, таких как фоны, текста_1, текста_2: option,
    рамки_1, рамки_2: option. Возвращает 5 списков."""
    first_hash = {"S": 5, "M": 10, "L": 15}
    second_hash = {".DS_Store", None}
    background = None
    frame_1 = ".DS_Store"
    frame_2 = ".DS_Store"
    text_1 = ".DS_Store"
    text_2 = ".DS_Store"
    text_1_filename = None
    text_2_filename = None
    backgrounds = []
    frames_1 = []
    frames_2 = []
    texts_1 = []
    texts_2 = []
    chosen_kind_of_frames = None
    chosen_font_of_texts = None

    # Создание списка фонов
    # Выходит, список больше не нужен. Потому что Микса больше нет. Достаточно указать имя ГЕО
    for i in range(first_hash[size_pack]):
        while background in second_hash:
            path = (
                path_to_backgrounds
                if random() < 0.95
                else os.path.join(
                    "\\".join(path_to_backgrounds.split("\\")[:-1]), "Общие"
                )
            )
            background = os.path.join(
                path, choice(os.listdir(path))
            )  # Формирование фона. Тут сделаем всю СУЕТУ с 95/5. Отзеркаливание не здесь
        # Теперь фоны формируются с нужной вероятностью, осталось отзеркаливание
        backgrounds.append(background)
        second_hash.add(background)

    # Далее создание и рамок и текстов, но прежде условие на наличие выбранного Стандартного набора
    if path_to_frames.split("\\")[-2] == "Фоны_две_рамки":
        for i in range(first_hash[size_pack]):
            #############
            while (
                frame_1.split("\\")[-1] == ".DS_Store"
                or frame_2.split("\\")[-1] == ".DS_Store"
                or chosen_kind_of_frames == ".DS_Store"
            ):
                chosen_kind_of_frames = choice(os.listdir(path_to_frames))
                frame_1 = os.path.join(
                    path_to_frames,
                    chosen_kind_of_frames,
                    "Верх",
                    choice(
                        os.listdir(
                            os.path.join(path_to_frames, chosen_kind_of_frames, "Верх")
                        )
                    ),
                )
                frame_2 = os.path.join(
                    path_to_frames,
                    chosen_kind_of_frames,
                    "Низ",
                    choice(
                        os.listdir(
                            os.path.join(path_to_frames, chosen_kind_of_frames, "Низ")
                        )
                    ),
                )

            frames_1.append(frame_1)
            frames_2.append(frame_2)

            # В этом цикле нужно проверять именно равенство именов файлов текстов, а не сравнивать их пути, пути их и так всегда равны
            while (
                text_1_filename == text_2_filename
                or text_1.split("\\")[-1] == ".DS_Store"
                or text_2.split("\\")[-1] == ".DS_Store"
            ):
                chosen_font_of_texts = choice(os.listdir(path_to_texts))
                text_1 = os.path.join(
                    path_to_texts,
                    chosen_font_of_texts,
                    "Верх",
                    choice(
                        os.listdir(
                            os.path.join(path_to_texts, chosen_font_of_texts, "Верх")
                        )
                    ),
                )  # Тут мы задаем путь до файла
                text_2 = os.path.join(
                    path_to_texts,
                    chosen_font_of_texts,
                    "Низ",
                    choice(
                        os.listdir(
                            os.path.join(path_to_texts, chosen_font_of_texts, "Низ")
                        )
                    ),
                )

                text_1_filename = os.path.basename(text_1)
                text_2_filename = os.path.basename(text_2)

            texts_1.append(text_1)
            texts_2.append(text_2)
            text_1 = ".DS_Store"
            text_2 = ".DS_Store"
            text_1_filename = None
            text_2_filename = None
            frame_1 = ".DS_Store"
            frame_2 = ".DS_Store"
    # Название файлов в папке Рамки должны быть разными
    else:
        for i in range(first_hash[size_pack]):
            frame_1 = os.path.join(path_to_frames, choice(os.listdir(path_to_frames)))
            frames_1.append(frame_1)
            # Рамки, кажется, готовы. Теперь текста
            chosen_font_of_texts = choice(os.listdir(path_to_texts))
            text_1 = os.path.join(
                path_to_texts,
                chosen_font_of_texts,
                choice(os.listdir(os.path.join(path_to_texts, chosen_font_of_texts))),
            )
            texts_1.append(text_1)

    return backgrounds, frames_1, frames_2, texts_1, texts_2


def zip_function(string: str):
    """Функция для создания списка PIL-файлов, которая получает данные из функции generation_elements"""
    PIL_files = []
    backgrounds_folder, frames_folder, texts_folder, size_pack = remake_data(string)
    backgrounds, frames_1, frames_2, texts_1, texts_2 = generation_elements(
        backgrounds_folder, frames_folder, texts_folder, size_pack
    )
    # Получили нужные списки
    if frames_2 == []:
        texts_2 = frames_2 = [None] * len(backgrounds)
    images = zip(backgrounds, frames_1, texts_1, frames_2, texts_2)
    for i in images:
        # Хотим брать элементы изображений и на их основе создавать изображения
        PIL_files.append(blaming_elements(i[0], i[1], i[2], i[3], i[4]))
    return PIL_files

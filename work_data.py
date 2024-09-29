"""Модуль для работы с БД"""

import random

class StoryManager:
    """Класс отвечает за чтение файла (выводить по строчно).
     Выбирать рандом, менять под запрос юзера"""

    PATH = "DataBaseStory.txt"
    result_story = None

    @classmethod
    def read_db_story(cls):
        with open(cls.PATH, "r", encoding="utf-8") as file:
            cls.result_story = file.readlines()
            return cls.result_story

    def random_story(self):
        self.read_db_story()
        res = random.choice(self.result_story)
        print(res)
"""
Модуль Tasks предоставляет методы для работы со списками чисел.
"""


class Tasks:
    """
    Класс Tasks содержит методы для вычисления среднего значения списка
    и сравнения средних значений двух списков.
    """

    @staticmethod
    def find_average(numbers):
        """
        Вычисляет среднее значение списка чисел.

        :param numbers: Список чисел
        :return: Среднее значение
        """
        if not isinstance(numbers, list):
            raise TypeError("Input should be a list.")
        if not numbers:
            raise ValueError("List cannot be empty.")
        return sum(numbers) / len(numbers)

    @staticmethod
    def compare_averages(list1, list2):
        """
        Сравнивает средние значения двух списков.

        :param list1: Первый список чисел
        :param list2: Второй список чисел
        :return: Строка с результатом сравнения
        """
        avg1 = Tasks.find_average(list1)
        avg2 = Tasks.find_average(list2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        if avg1 < avg2:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"

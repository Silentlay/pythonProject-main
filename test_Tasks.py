from tasks import Tasks
import pytest

def test_find_average():
    # Тест корректных случаев
    assert Tasks.find_average([10, 20, 30, 40, 50]) == 30
    assert Tasks.find_average([5]) == 5
    # Пустой список
    with pytest.raises(ValueError, match="List cannot be empty."):
        Tasks.find_average([])
    # Неверный тип данных
    with pytest.raises(TypeError, match="Input should be a list."):
        Tasks.find_average("Not a list")
    # Проверка с отрицательными числами
    assert Tasks.find_average([-10, -20, -30]) == -20
    # Проверка с дробными числами
    assert Tasks.find_average([1.5, 2.5, 3.5]) == 2.5

def test_compare_averages_first_higher():
    # Первый список имеет большее среднее значение
    list1 = [5, 10, 15]
    list2 = [1, 2, 3]
    assert Tasks.compare_averages(list1, list2) == "Первый список имеет большее среднее значение"

def test_compare_averages_second_higher():
    # Второй список имеет большее среднее значение
    list1 = [1, 2, 3]
    list2 = [5, 10, 15]
    assert Tasks.compare_averages(list1, list2) == "Второй список имеет большее среднее значение"

def test_compare_averages_equal():
    # Средние значения равны
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    assert Tasks.compare_averages(list1, list2) == "Средние значения равны"

def test_compare_averages_empty_list():
    # Проверка ошибки при пустом списке
    with pytest.raises(ValueError, match="List cannot be empty."):
        Tasks.compare_averages([], [1, 2, 3])

def test_compare_averages_large_numbers():
    # Проверка больших чисел
    list1 = [1e9, 2e9, 3e9]
    list2 = [1e8, 2e8, 3e8]
    assert Tasks.compare_averages(list1, list2) == "Первый список имеет большее среднее значение"

def test_compare_averages_negative_numbers():
    # Проверка отрицательных чисел
    list1 = [-5, -10, -15]
    list2 = [-1, -2, -3]
    assert Tasks.compare_averages(list1, list2) == "Второй список имеет большее среднее значение"

def test_compare_averages_single_element():
    # Один элемент в списке
    list1 = [42]
    list2 = [1, 2, 3]
    assert Tasks.compare_averages(list1, list2) == "Первый список имеет большее среднее значение"

def test_compare_averages_both_empty():
    # Проверка ошибки, если оба списка пусты
    with pytest.raises(ValueError, match="List cannot be empty."):
        Tasks.compare_averages([], [])

def test_compare_averages_invalid_input():
    # Проверка TypeError для некорректного типа входных данных
    with pytest.raises(TypeError, match="Input should be a list."):
        Tasks.compare_averages("invalid", [1, 2, 3])

    with pytest.raises(TypeError, match="Input should be a list."):
        Tasks.compare_averages([1, 2, 3], "invalid")

def test_main():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert Tasks.compare_averages(list1, list2) == "Второй список имеет большее среднее значение"
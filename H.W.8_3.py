def find_unique_value(some_list):
    # проходимось по кожному числу зі списку
    for num in some_list:
        # перевіряємо чи число  входить у список тільки один раз
        if some_list.count(num) == 1:
            return num
    return None


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def return_text_1_func():
    return "qwerty"


@uppercase
def return_text_2_func():
    return "iuytrew"


print(return_text_1_func())
print(return_text_2_func())

# def decorator(func):
#     def wrapper():
#         print("Перед функцией")
#         func()
#         print("После функции")
#
#     return wrapper
#
#
# @decorator
# def text_func():
#     print("text")
#
#
# @decorator
# def number_func():
#     print(123456789)
#
#
# text_func()
#
# number_func()

import pytest


@pytest.mark.parametrize("wrong_name_data", ["1234", 'q', 'q' * 100, '@', ')', '.'])
def test_name_field_negative(wrong_name_data):
    pass
    # функция для ввода в поле имени данных(wrong_name_data)
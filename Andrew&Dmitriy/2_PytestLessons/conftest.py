import pytest
import allure


@pytest.fixture
def setup_and_teardown_fixture():
    with allure.step("Начало выполнение автотеста."):
        print("Начало выполнение автотеста.")
    yield
    with allure.step("Конец выполнение автотеста."):
        print("Конец выполнение автотеста.")


# @pytest.fixture
# def teardown_fixture():
#     yield
#     print("Конец выполнение автотеста3.")


@pytest.fixture
def returning_fixture():
    print("Начало выполнение автотеста.")
    print("Отправка объекта в автотест.")
    yield "Объект"
    print("Конец выполнение автотеста.")

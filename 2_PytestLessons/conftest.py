import pytest


@pytest.fixture
def setup_teardown_fixture1(teardown_fixture3):
    print("Начало выполнение автотеста1.")
    yield


@pytest.fixture
def setup_fixture2():
    print("Начало выполнение автотеста2.")


@pytest.fixture
def teardown_fixture3():
    yield
    print("Конец выполнение автотеста3.")


@pytest.fixture
def returning_fixture():
    print("Начало выполнение автотеста.")
    print("Отправка объекта в автотест.")
    yield "Объект"
    print("Конец выполнение автотеста.")

import pytest


@pytest.fixture
def setup_fixture():
    print("Начало выполнение автотеста.")


@pytest.fixture
def setup_and_teardown_fixture():
    print("Начало выполнение автотеста.")
    yield
    print("Конец выполнение автотеста.")


@pytest.fixture
def teardown_fixture():
    yield
    print("Конец выполнение автотеста.")


@pytest.fixture
def returning_fixture():
    print("Начало выполнение автотеста.")
    print("Отправка объекта в автотест.")
    yield "Объект"
    print("Конец выполнение автотеста.")

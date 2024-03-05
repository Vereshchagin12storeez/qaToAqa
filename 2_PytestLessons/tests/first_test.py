import allure
import pytest


@allure.epic("Тест-кейс")
class TestFirst:
    @allure.title("Title: Успешный автотест")
    @allure.description("Desc: Успешный автотест")
    def test_pass_autotest(self, setup_and_teardown_fixture):
        assert False

    @allure.title("Title: Успешный автотест с шагами")
    @allure.description("Desc: Успешный автотест с шагами")
    def test_pass_autotest_with_steps(self, setup_and_teardown_fixture):
        with allure.step("Происходит сложение."):
            a = 5 + 5
        with allure.step("Происходит вычитание."):
            a = 5 - 5
        assert True

    @allure.title("Title: Падающий автотест")
    @allure.description("Desc: Падающий автотест")
    def test_fail_autotest(self, setup_and_teardown_fixture):
        a = 5
        assert a != 5, "Переменная не равна 6."


# @pytest.mark.parametrize("test_number", [1, 2, 3])
# def test_parametrized_autotest(test_number):
#     assert test_number == 2

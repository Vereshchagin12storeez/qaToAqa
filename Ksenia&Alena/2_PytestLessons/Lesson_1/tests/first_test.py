import pytest

# def test_pass_autotest():
#     assert 1 == 1
#
# def test_fail_autotest():
#     a = 5
#     assert a == 6, "Переменная не равна 6."


class TestFirst:
    def test_pass_autotest(self, setup_and_teardown_fixture):
        print("test")
        assert True

    def test_fail_autotest(self):
        a = 5
        assert a == 6, "Переменная не равна 6."


@pytest.mark.parametrize("test_number", [1, 2, 3, 67, 234])
def test_parametrized_autotest(test_number):
    assert isinstance(test_number, int)

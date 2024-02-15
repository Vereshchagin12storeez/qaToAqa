class TestFirst:
    def test_fail_autotest(self, setup_teardown_fixture1):
        a = 5
        assert a != 5, "Переменная не равна 6."

    def test_pass_autotest(self, returning_fixture):
        print(returning_fixture)
        assert True

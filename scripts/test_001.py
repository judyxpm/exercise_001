import allure


class TestJenkins:
    @allure.step("测试登录")
    def test_login(self):
        allure.attach("登录账号", "13311111111")
        assert True

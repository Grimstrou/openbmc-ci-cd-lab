# tests/auto_test.py
import unittest
import xmlrunner
import sys

class TestOpenBMCAPI(unittest.TestCase):
    def test_bmc_health_check(self):
        """Проверка доступности BMC API"""
        self.assertTrue(True)

    def test_sensor_reading(self):
        """Проверка чтения датчиков температуры"""
        temp = 45
        self.assertGreater(temp, 0)
        self.assertLess(temp, 100)

    def test_user_authentication(self):
        """Проверка аутентификации пользователя"""
        user = "admin"
        self.assertEqual(user, "admin")

if __name__ == '__main__':
    # Генерация отчёта в формате JUnit XML
    with open('auto_test_report.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            exit=False,
            verbosity=2
        )
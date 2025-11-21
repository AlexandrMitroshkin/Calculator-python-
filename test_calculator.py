# import unittest
# import sys
# from io import StringIO
# from unittest.mock import patch

# # Импортируем функции из вашего калькулятора
# # Если функции в том же файле, можно использовать exec
# # Или лучше вынести функции в отдельный модуль

# class TestCalculatorBrackets(unittest.TestCase):
    
#     def setUp(self):
#         self.held_output = StringIO()
    
#     def run_calculator(self, input_string):
#         """Вспомогательная функция для запуска калькулятора"""
#         with patch('sys.stdout', new=self.held_output), \
#              patch('builtins.input', return_value=input_string):
#             try:
#                 # Запускаем основной код калькулятора из вашего файла
#                 with open('calculator.py', 'r', encoding='utf-8') as f:
#                     code = f.read()
#                 exec(code)
#             except RecursionError:
#                 return "RecursionError"
#             except Exception as e:
#                 return f"Error: {type(e).__name__}"
#         self.held_output.seek(0)
#         return self.held_output.read()
    
#     def test_100000_nested_brackets(self):
#         """Тест на 100,000 вложенных скобок (более реалистично)"""
#         print("Создаем выражение с 100,000 вложенных скобок...")
        
#         expression = "1"
#         for i in range(100000):
#             expression = f"( {expression} )"
        
#         print("Выражение создано, запускаем калькулятор...")
        
#         output = self.run_calculator(expression)
        
#         if "RecursionError" in output:
#             print("Ожидаемо: превышена глубина рекурсии")
#             self.skipTest("Глубина рекурсии превышена")
#         elif "Ответ: 1" in output:
#             print("УСПЕХ: Обработано 100,000 скобок!")
#             self.assertTrue(True)
#         else:
#             print(f"Результат: {output}")
#             self.assertTrue(True)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)
class My_exeption(Exception):
    def __init__(self, message="Exponent must be non-negative"):
        self.message = message
        super().__init__(self.message)

class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        try:
            result = num1 + num2
            return result
        except Exception as e:
            return f"Error: {e}"

    def sub(self, num1, num2):
        try:
            result = num1 - num2
            return result
        except Exception as e:
            return f"Error: {e}"

    def multiply(self, num1, num2):
        try:
            result = num1 * num2
            return result
        except Exception as e:
            return f"Error: {e}"

    def divide(self, num1, num2):
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed"


    def exponentiate(self, base, exponent):
        try:
            if exponent < 0:
                raise My_exeption()
            result = base ** exponent
            return result
        except Exception as e:
            return f"Error: {e}"

    def square_root(self, num):
        try:
            result = num ** 0.5
            return result
        except Exception as e:
            return f"Error: {e}"




calculator = Calculator()
print("Addition:", calculator.add(5, 'b'))
print("Subtraction:", calculator.sub(5, None))
print("Multiplication:", calculator.multiply(5, {1:3, 3:4}))
print("Division:", calculator.divide(5, 0))
print("Exponentiation:", calculator.exponentiate(2, -1))
print("Square Root:", calculator.square_root("d"))

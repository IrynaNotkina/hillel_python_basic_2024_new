# Створіть власний клас String на основі стандартного класу str.
# В ньому необхідно:
# • Розширити стандартний метод, відповідальний за додавання
# • Написати відсутній у класі str метод відповідальний за віднімання
# Принцип роботи в новому класі String: обєкти типу String можна додавати як між собою,
# так і з будь-яким іншим типом, який може бути приведений до типу рядка. "Під капотом",
# обидва операнди приводиться до типу рядків та потім відбувається конкаткатенація.
# Результатом додавання буде новий обєкт класу String. Приклади виконання:

# String('New') + String(890)    ->    'New890'
# String(1234) + 5678            ->    '12345678'
# String('New') + 'castle'       ->    'Newcastle'
# String('New') + 77             ->    'New77'
# String('New') + True           ->    'NewTrue'
# String('New') + ['s', ' ', 23] ->    "New['s', ' ', 23]"
# String('New') + None           ->    'NewNone'

# Принцип віднімання в новому класі String: з обєкту типу String ви можете відняти
# значення будь-якого іншого типу, яке можна привести до типу рядка.
# "Під капотом", обидва операнди приводяться до типу str, а потім з першого операнду
# видаляється перше входження значення другоо операнду, якщо такий має місце.
# Результатом віднімання стане новий обєкт класу String.
# Якщо в першому операнді немає значення другого операнду, то результатом віднімання
# стане перший операнд без змін. Приклади виконання:

# String('New bala7nce') - 7               ->    'New balance'
# String('New balance') - 'bal'            ->    'New ance'
# String('New balance') - 'Bal'            ->    'New balance'
# String('pineapple apple pine') - 'apple' ->    'pine apple pine'
# String('New balance') - 'apple'          ->    'New balance'
# String('NoneType') - None                ->    'Type'
# String(55678345672) - 7                  ->    '5568345672'

# *Важливо! Результатом додавання або віднімання завжди буде обєкт типу String.

class String(str):
    def __add__(self, other):
        return String(str(self) + str(other))
    def __sub__(self, other):
        other_str = str(other)
        return String(self.replace(other_str, '', 1))

print('---task2---')

b1 = String('New bala7nce')
b2 = 7
b3 = String('New balance')
b4 = 'bal'
b5 = 'Bal'
b6 = String('pineapple apple pine')
b7 = 'apple'
b8 = String('NoneType')
b9 = None
b10 = String(55678345672)
b11 = 7

res2 = (b1 - b2)
print(res2)
print(type(res2))
print(b3 - b4)
print(b3 - b5)
print(b6 - b7)
print(b3 - b7)
print(b8 - b9)
print(b10 - b11)

print()
print('---task1---')

a1 = String('New')
a2 = String(890)
a3 = String(1234)
a4 = 5678
a5 = 'castle'
a6 = 77
a7 = True
a8 = ['s', ' ', 23]
a9 = None

res1 = a1 + a2
print(res1)
print(type(res1))
print(a3 + a4)
print(a1 + a5)
print(a1 + a6)
print(a1 + a7)
print(a1 + a8)
print(a1 + a9)

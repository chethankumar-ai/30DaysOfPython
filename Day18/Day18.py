# Enforce a naming convention with a metaclass
class captial_names(type):
    def __new__(cls, name, bases, attrs):
        if not name[0].isupper():
            raise ValueError(f"Class name '{name}' must start with a capital letter.")
        return super().__new__(cls, name, bases, attrs)

# example : using meta class captial_name(type):

class anotherClass(metaclass=captial_names):
    def __init__(self, value):
        self.value = value
# example uing meta class captial_names(type):
class MyClass(metaclass=captial_names):
    def __init__(self, value):
        self.value = value

obj = MyClass(10)
print(f"Object created with value: {obj.value}")

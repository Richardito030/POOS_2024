def get_type_message(var):
    type_dict = {
        list: "La variable es una lista.",
        str: "La variable es una cadena.",
        int: "La variable es un entero.",
        bool: "La variable es un lógico."
    }
    return type_dict.get(type(var))

my_list = [1, 2, 3]
my_string = "Hola"
my_integer = 10
my_boolean = True

print(get_type_message(my_list))
print(get_type_message(my_string))
print(get_type_message(my_integer))
print(get_type_message(my_boolean))

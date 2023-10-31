random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

float_data = list(filter(lambda x: isinstance(x, float), random_list))
int_data = list(filter(lambda x: isinstance(x, int), random_list))
string_data = list(filter(lambda x: isinstance(x, str), random_list))

def map_int_to_units_tens_hundreds(x):
    if isinstance(x, int):
        units = x % 10
        tens = (x % 100) // 10
        hundreds = x // 100
        return {'ratusan': hundreds, 'puluhan': tens, 'satuan': units}
    return x

int_mapped = list(map(map_int_to_units_tens_hundreds, int_data))

print("Data Float:", float_data)
print("Data Integer:")

for item in int_mapped:
    print(item)

print("Data String:", string_data)

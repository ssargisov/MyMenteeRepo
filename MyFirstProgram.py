#1
def sum_or_triple(x, y, z):
    sum = x + y + z
    if x == y == z:
        return sum * 3
    else:
        return sum

#2
def replace_except_last_five_chars(string):
    last = string[-5:]

    first = (len(string)-5) * "*"
    result = first+last
    return result

#3
def get_country(countries, input_dict):
    result = []
    for elem in countries:
        if elem in input_dict:
            city = input_dict[elem]
            result.append(city)
    return result

#4
def sort_dict(input_dict):
    sorted_items = sorted(input_dict.items())
    result = dict(sorted_items)
    return result

# 5
def split_sentence(sentence):
    sentence = sentence.replace("n/a", "A")
    words = sentence.split()
    return words

# 6
def number_multiplication():
    num = input("enter a number: ")
    num = int(num)
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)


#7

def your_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    your_info = {"Name": name, "Age": age, "Gender": gender}
    print(your_info)


#8
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(6, 5)
area = rectangle.area()
print(area)
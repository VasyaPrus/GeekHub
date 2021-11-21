#11.Write a script to remove duplicates from Dictionary.

dict1 = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five"
}
dict2 = {
    1 : "one",
    6 : "six",
    5 : "five",
    2 : "second",
    3 : "third",
    4 : "four"
}
result = {}


for val in dict1:
    if dict1[val] == dict2[val]:
        result[val] = dict1[val]
print(result)

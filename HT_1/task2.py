my_st1 = input("Enter colors through ',':").lower()
my_st2 = input("Enter colors through ',' to check:").lower()

color_list_1 = set(my_st1.split(","))
color_list_2 = set(my_st2.split(","))
print(color_list_1)
print(color_list_2)
print(color_list_1.difference(color_list_2)) 


     
    
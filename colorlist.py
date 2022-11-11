#18. Print out all colors from color-list1 not contained in color-list2 
color_list_1 = input("Enter colors seperated by spaces: ")
color_list_2 = input("Enter colors seperated by spaces: ")

color_list_1 = color_list_1.split()
color_list_2 = color_list_2.split()

diff_list = [x for x in color_list_1 if x not in color_list_2]
print("Colors in list1 not in list2: ", diff_list)
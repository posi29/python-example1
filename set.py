#Creating a set
Sample_set = {1, 2, 3, 4, 5, 6, 7, 8, }
print(Sample_set)

#Converting list to set
List_of_numbers = (1, 2, 3, 4, 5, 8, 10)
print(len(List_of_numbers))
set_of_numbers = set(List_of_numbers)
print(set_of_numbers)
print(type(set_of_numbers))

#Check if element is in set
print(2 in set_of_numbers)
print(30 in set_of_numbers)

#Length of a set
print(len(set_of_numbers))


#Add items to a set
set_of_numbers.add(13)
print(len(set_of_numbers))
set_of_numbers.add(50)
print(set_of_numbers)
print(len(set_of_numbers))



#Remove items from a set
set_of_numbers.remove(50)
print(set_of_numbers)

Color_set = {"yellow", "blue", "pink", "purple", "green"} 
remaining_color = {"indigo", "violet", "yellow"}

all_colors = Color_set | remaining_color
print(all_colors)

intersection= Color_set & remaining_color
print(intersection)
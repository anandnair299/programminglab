#16.Create a list of colors from comma seprated color names entered by user. Display first and last colors
color_line = input("Enter colors seperated by ,: ")
colors = color_line.split(",")
print("First color is", colors[0])
print("Last color is", colors[-1])
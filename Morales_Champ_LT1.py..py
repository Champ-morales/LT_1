#Box calculator

#asks for the total of the notebooks and sets it as the value of the variable 
notebooks_total = int(input("How many notebooks total: "))
#asks for the total of the notebooks per box and sets it as the value of the variable
notebooks_per_box = int(input("How many notebooks per box: "))

#calculates how many full boxes there will be
boxes_total = notebooks_total // notebooks_per_box
#calculates the total of the notebooks that go to a loose pack
left_over = notebooks_total % notebooks_per_box


#Finds out if there will be a loose pack or not, then prints the result
if left_over == 0:
    print(f"There will be {boxes_total} boxes and 0 notebooks go to a loose pack")
else: 
    print(f"There will be {boxes_total} full boxes and {left_over} notebook/s go in a loose pack." )
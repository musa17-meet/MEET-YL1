from meet import * 
cells=[]
get_screen_width()
get_screen_height()
get_random_x()
get_random_y()
for x in range(15):
	
	x=random.randint(0,1)
	t=random.random()
		
	if x==1:

		t=-t
	cell1={"x":get_random_x(), "y":get_random_y(), "radius":random.randint(10,65), "dy":t, "dx":t, "color":"blue"}
	z=create_cell(cell1)
	cells.append(z)

	

while True:
	move_cells(cells)
	

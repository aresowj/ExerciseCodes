/*
	code author: aresowj
	
	ch02_Chess_Board.js
	Creates a string that represents an 8x8 grid, using newline characters to separate lines.
	Print the string in console will look like this:
	
	 # # # #
	# # # # 
	 # # # #
	# # # # 
	 # # # #
	# # # # 
	 # # # #
	# # # # 
	
	Modify the program to work for any size, outputting a grid of the given width and height.
	
	Solution from the book author:
	
	var size = 8;

	var board = "";

	for (var y = 0; y < size; y++) {
	  for (var x = 0; x < size; x++) {
		if ((x + y) % 2 == 0)
		  board += " ";
		else
		  board += "#";
	  }
	  board += "\n";
	}

	console.log(board);
*/

var width, height = 0
var grid = ""

width = prompt("Please input thhe width of Chess Board:");
height = prompt("Please input thhe height of Chess Board:");

for (var h = 1; h <= height; h++) {	//Odd lines starts with space, even lines starts with #.
	for (var w = 1; w <= width; w++) {
		if (h % 2 != 0)		//Odd lines
			if (w % 2 == 0) grid += "#";
			else grid += " ";
		else	//Even lines
			if (w % 2 == 0) grid += " ";
			else grid += "#";
	}
	grid += "\n"
}

console.log(grid)
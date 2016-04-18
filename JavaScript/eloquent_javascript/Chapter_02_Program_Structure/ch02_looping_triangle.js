/*
	code author: aresowj
	
	ch02_looping_triangle.js
	Looping a triangle
	#
	##
	###
	####
	...
	#######
	
	Solution from the book author:
	
	for (var line = "#"; line.length < 8; line += "#")
		console.log(line);
*/

var sharps = "#";
for(var i=0; i<7; i++){
	console.log(sharps);
	sharps += "#"
}
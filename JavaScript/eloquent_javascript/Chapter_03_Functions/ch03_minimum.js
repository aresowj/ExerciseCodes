/*
	code author: aresowj
	
	ch03_minimum.js
	Return the minimum argument. (Receiving two)
	
	Solution from the book author:
	
	function min(a, b) {
	  if (a < b)
		return a;
	  else
		return b;
	}

*/

function min(a, b) {
	if (a > b)
		return b;
	else
		return a
}

console.log(min(0, 10));
// → 0
console.log(min(0, -10));
// → -10
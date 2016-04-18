/*
	code author: aresowj
	
	ch05_flattening.js
	Flatten an array of arrays to a single array that has all the elements of the input arrays.
	
	Solution from the book author:
	
	console.log(arrays.reduce(function(flat, current) {
	  return flat.concat(current);
	}, []));
*/

var arrays = [[1, 2, 3], [4, 5], [6]];

result = arrays.reduce(function (pre, current) {
	return pre.concat(current);
});
console.log(result);
// → [1, 2, 3, 4, 5, 6]
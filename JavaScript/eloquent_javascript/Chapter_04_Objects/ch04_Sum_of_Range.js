/*
	code author: aresowj
	
	ch04_Sum_of_Range.js
	range(start, end): Returns an array of numbers from start (including) to end (excluding).
	sum(array): Returns the sum of all numbers in array.
	
	Solution from the book author:
	
	function range(start, end, step) {
	  if (step == null) step = 1;
	  var array = [];

	  if (step > 0) {
		for (var i = start; i <= end; i += step)
		  array.push(i);
	  } else {
		for (var i = start; i >= end; i += step)
		  array.push(i);
	  }
	  return array;
	}

	function sum(array) {
	  var total = 0;
	  for (var i = 0; i < array.length; i++)
		total += array[i];
	  return total;
	}
*/

function range(start, end, step) {
	result = [];
  	if (step == undefined || typeof step != "number")
      step = 1;
  	
  	var i = start;
  	dif = Math.abs(start - end);
  	
  	for (var n = 0; n <= dif; n++)
		result.push(start + step * n);
	return result;
}

function sum(array) {
	var result = 0;
	for (var n in array)
		result += array[n];
	return result;
}

if (-1) console.log('True');
console.log(sum(range(1, 10)));
// → 55
console.log(range(5, 2, -1));
// → [5, 4, 3, 2]
console.log(range(5, 2));
console.log(range(1, 10));
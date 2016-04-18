/*
	code author: aresowj
	
	ch04_Reverse_Array.js
	Write two functions.
	reverseArray(array): Produces a new array that has the same elements in the inverse order.
	reverseArrayInPlace(array): Modifies the array given in order to reverse its elements.
	
	Solution from the book author:
	
	function reverseArray(array) {
	  var output = [];
	  for (var i = array.length - 1; i >= 0; i--)
		output.push(array[i]);
	  return output;
	}

	function reverseArrayInPlace(array) {
	  for (var i = 0; i < Math.floor(array.length / 2); i++) {
		var old = array[i];
		array[i] = array[array.length - 1 - i];
		array[array.length - 1 - i] = old;
	  }
	  return array;
	}
*/

function reverseArray(array) {
	result = [];
	for (var i = array.length - 1; i >= 0; i--)
		result.push(array[i]);
	return result;
}

function reverseArrayInPlace(array) {
	var temp;
	for (var i = array.length - 1; i >= Math.floor(array.length/2); i--) {
		temp = array[i];
		array[i] = array[(array.length - 1) - i];
		array[(array.length - 1) - i] = temp;
	}
}

console.log(reverseArray(["A", "B", "C"]));
// → ["C", "B", "A"];
var arrayValue = [1, 2, 3, 4, 5];
reverseArrayInPlace(arrayValue);
console.log(arrayValue);
// → [5, 4, 3, 2, 1]
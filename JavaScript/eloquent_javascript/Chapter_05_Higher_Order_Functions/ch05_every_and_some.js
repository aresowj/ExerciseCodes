/*
	code author: aresowj
	
	ch05_every_and_some.js
	Try to write functions like array.every() and array.some().
	
	Solution from the book author:
	
	function every(array, predicate) {
	  for (var i = 0; i < array.length; i++) {
		if (!predicate(array[i]))
		  return false;
	  }
	  return true;
	}

	function some(array, predicate) {
	  for (var i = 0; i < array.length; i++) {
		if (predicate(array[i]))
		  return true;
	  }
	  return false;
	}

*/
function every(array, f) {
  for (var i = 0; i < array.length; i++) {
    if (f(array[i]) == false) return false;
  }
  return true;
}

function some(array, f) {
  for (var i = 0; i < array.length; i++) {
    if (f(array[i]) == true) return true;
  }
  return false;
}

console.log(every([NaN, NaN, NaN], isNaN));
// → true
console.log(every([NaN, NaN, 4], isNaN));
// → false
console.log(some([NaN, 3, 4], isNaN));
// → true
console.log(some([2, 3, 4], isNaN));
// → false
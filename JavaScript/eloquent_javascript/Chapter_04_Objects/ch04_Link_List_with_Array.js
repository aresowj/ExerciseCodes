/*
	code author: aresowj
	
	ch04_Link_List_with_Array.js
	Create lists (could be linked with different arrays) with arrays.
	Set the last element link to the next part of list if it is not the last part.
	List can share parts of their structure.
	
	Solution from the book author:
	

*/

function arrayToList(array) {
  var len = array.length;
  if (len == 1) return {value: array[0], rest: null};
  else return {value: array[0], rest: arrayToList(array.slice(1))};
}

function listToArray(list) {
  	var result = [];
  	do {
      if (list.rest == null) {
        result.push(list.value);;
        break;
      }
      else {
      result.push(list.value);
      list = list.rest;
      }
    } while (true);
  	return result;
}

function prepend (value, rest) {
    return {value: value, rest: rest};
}

function nth(list, n) {
  if (n == 0) return list.value;
  return nth(list.rest, n - 1);
}

console.log(arrayToList([10, 20]));
// → {value: 10, rest: {value: 20, rest: null}}
console.log(listToArray(arrayToList([10, 20, 30])));
// → [10, 20, 30]
console.log(prepend(10, prepend(20, null)));
// → {value: 10, rest: {value: 20, rest: null}}
console.log(nth(arrayToList([10, 20, 30]), 1));
// → 20
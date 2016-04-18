/*
	code author: aresowj
	
	ch03_Bean_Counts.js
	Write a function countBs that takes a string as its only argument and returns a number that 
	indicates how many uppercase "B" characters are in the string.	
	
	Then write a function countChar that acts like countBs, but with a second argumnet that indicates 
	the character to be counted.
	
	Solution from the book author:

	function countChar(string, ch) {
	  var counted = 0;
	  for (var i = 0; i < string.length; i++)
		if (string.charAt(i) == ch)
		  counted += 1;
	  return counted;
	}

	function countBs(string) {
	  return countChar(string, "B");
	}

*/

function countBs(s) {
	/* this function could be rewritten to a single line: return countChar(s, "B")*/
	
	var count = 0;
	
	for (var i = 0; i < s.length; i++) {
		if (s.charAt(i) == "B")
			count += 1;
	}
	
	return count;
}

function countChar(s, ch) {
	var count = 0;
	
	for (var i = 0; i < s.length; i++) {
		if (s.charAt(i) == ch)
			count += 1;
	}
	
	return count;
}

console.log(countBs("BBC"));
// → 2
console.log(countChar("kakkerlak", "k"));
// → 4
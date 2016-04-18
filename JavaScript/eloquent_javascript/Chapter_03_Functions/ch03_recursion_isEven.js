/*
	code author: aresowj
	
	ch03_recursion_isEven.js
	Write a function countBs that takes a string as its only argument and returns a number that 
	indicates how many uppercase "B" characters are in the string.	
	
	Then write a function countChar that acts like countBs, but with a second argumnet that indicates 
	the character to be counted.
	
	Solution from the book author:

	function isEven(n) {
	  if (n == 0)
		return true;
	  else if (n == 1)
		return false;
	  else if (n < 0)
		return isEven(-n);
	  else
		return isEven(n - 2);
	}

*/

function isEven(n) {
	n = Math.abs(n)
	
	if (n == 0)
		return true;
	else if (n == 1)
		return false;
	else
		return isEven(n-2);
}
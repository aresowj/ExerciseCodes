/*
	code author: aresowj
	
	ch02_FizzBuzz.js
	Print numbers from 1 to 100, with following rules:
	1. Replace numbers divisible by 3 to "Fizz"
	2. Replace numbers divisible by 5 (but not 3) to "Buzz"
	3. Replace numbers divisible by both 3 and 5 to "FizzBuzz"
	
	Solution from the book author:
	
	for (var n = 1; n <= 100; n++) {
	  var output = "";
	  if (n % 3 == 0)
		output += "Fizz";
	  if (n % 5 == 0)
		output += "Buzz";
	  console.log(output || n);
	}
*/

for (var i=1; i<=100; i++){
	if (i % 3 == 0 && i % 5 != 0)
		console.log("Fizz");
	else if (i % 5 ==0 && i % 3 != 0)
		console.log("Buzz");
	else if (i % 3 == 0 && i % 5 == 0)
		console.log("FizzBuzz");
	else
		console.log(i);
}
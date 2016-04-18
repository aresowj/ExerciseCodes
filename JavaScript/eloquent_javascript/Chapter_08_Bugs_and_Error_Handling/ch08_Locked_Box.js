/*
	code author: aresowj
	
	ch08_Locked_Box.js
	It is a box with a lock. Inside is an array, 
	but you can get at it only when the box is unlocked. 
	Directly accessing the _content property is not allowed.

	Write a function called withBoxUnlocked that takes a function value as argument, 
	unlocks the box, runs the function, and then ensures that the box is locked again 
	before returning, regardless of whether the argument function returned normally 
	or threw an exception.
	
	function withBoxUnlocked(body) {
	  var locked = box.locked;
	  if (!locked)
		return body();

	  box.unlock();
	  try {
		return body();
	  } finally {
		box.lock();
	  }
	}
*/
var box = {
  locked: true,
  unlock: function() { this.locked = false; },
  lock: function() { this.locked = true;  },
  _content: [],
  get content() {
    if (this.locked) throw new Error("Locked!");
    return this._content;
  }
};

function withBoxUnlocked(body) {
  // Your code here.
  try {
	  box.unlock();
	  body();
  } finally {
	  box.lock();
  }
}

withBoxUnlocked(function() {
  box.content.push("gold piece");
});

try {
  withBoxUnlocked(function() {
    throw new Error("Pirates on the horizon! Abort!");
  });
} catch (e) {
  console.log("Error raised:", e);
}
console.log(box.locked);
// → true
// 1. The signum of a number is 1 if the number is positive, –1 if it is negative, and 0 if it is zero. Write a function that computes this value.
def signum(n: Double): Int = {
  var sign = 0
  if (n > 0) sign = 1
  if (n < 0) sign = -1
  sign
}

signum(123)   // 1
signum(-12939)// -1
signum(0)     // 0

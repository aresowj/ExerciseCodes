package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	z := 1.0
	for {
		fmt.Println(z)
		z -= (z*z - x) / (2*z)
		if (z * z - x) < 0.001 {
			fmt.Println("math.Sqrt: %f", math.Sqrt(x))
			return z
		}
	}
}

func main() {
	fmt.Println(Sqrt(2))
	fmt.Println(Sqrt(4))
	fmt.Println(Sqrt(9))
	fmt.Println(Sqrt(889987865))
	fmt.Println(Sqrt(23452))
	fmt.Println(Sqrt(1213))
}

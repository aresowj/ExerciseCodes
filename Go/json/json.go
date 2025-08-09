package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type User struct {
	Firstname string `json:"firstname"`
	Lastname  string `json:"lastname"`
	Age       int    `json:"age"`
}


func decode(w http.ResponseWriter, r *http.Request) {
	var user User
	json.NewDecoder(r.Body).Decode(&user)
	fmt.Fprintf(w, "%s %s is %d years old!", user.Firstname, user.Lastname, user.Age)
}

func encode(w http.ResponseWriter, r *http.Request) {
	john := User{
		Firstname: "John",
		Lastname: "Doe",
		Age: 109,
	}
		json.NewEncoder(w).Encode(john)
}

func main() {
	http.HandleFunc("/decode", decode)
	http.HandleFunc("/encode", encode)
	http.ListenAndServe(":8080", nil)
}


/*
examples
$ curl -X POST http://localhost:8080/decode -H "Content-Typ
e: application/json" -d '{"firstname":"Weijie","lastname":"
Ou","age":999}'
> Weijie Ou is 999 years old!

$ curl http://localhost:8080/encode
> {"firstname":"John","lastname":"Doe","age":109}
/*
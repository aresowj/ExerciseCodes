package main

import (
	"fmt"
	"net/http"
    // "io"
    "os"
    // "bufio"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}


func main() {
	dat, err := os.ReadFile("templates/index.html")
	check(err)

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, string(dat), r.URL.Query().Get("token"))
	})
	fs := http.FileServer(http.Dir("static/"))
	http.Handle("/static/", http.StripPrefix("/static/", fs))
	http.ListenAndServe(":80", nil)
}

// main.go

package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os/exec"
)

type Location struct {
	IP      string `json:"ip"`
	City    string `json:"city"`
	Region  string `json:"region"`
	Country string `json:"country"`
	Loc     string `json:"loc"`
}

func getLocation() Location {
	cmd := exec.Command("python3", "location.py")
	output, err := cmd.Output()
	if err != nil {
		fmt.Println("Error running Python script:", err)
	}

	var loc Location
	err = json.Unmarshal(output, &loc)
	if err != nil {
		fmt.Println("Error parsing JSON:", err)
	}

	return loc
}

func handler(w http.ResponseWriter, r *http.Request) {
	loc := getLocation()
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(loc)
}

func main() {
	http.HandleFunc("/location", handler)
	fmt.Println("Server running on port 8080...")
	http.ListenAndServe(":8080", nil)
}

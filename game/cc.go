package main

func main() {
	var visited = make(map[string]bool)
	slice := []string{"cc"}
	slice = append(slice, "a", "v", "b")
	// slice1 :=[]string{"a","s","w"}
	visited["a"] = true
	for _, i := range slice {
		if !visited[i] {
			println(i)
		}
	}

}

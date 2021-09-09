package hello_injection

import (
	"fmt"
	"io"
)

// dependency injection: instead of depending on a concrete type like fmt.Printf,
// depend on an interface that imitates I/O writer.
func Greet(w io.Writer, name string) {
	fmt.Fprintf(w, "Hello, %s", name)
}

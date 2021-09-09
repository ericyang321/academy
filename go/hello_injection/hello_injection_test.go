package hello_injection

import (
	"bytes"
	"testing"
)

// test printing format by redirecting I/O write
// to a buffer. in order to do that the function needs to
// have its dependencies injected and not directly use fmt.Printf
func TestGreet(t *testing.T) {
	// a buffer implements Write interface
	// Greet needs a io.Writer interface and buffer fulfills that
	buf := bytes.Buffer{}
	Greet(&buf, "e")

	received := buf.String()
	expect := "Hello, e"

	if received != expect {
		t.Errorf("Received %q, expected %q", received, expect)
	}
}

package hello

import "testing"

func TestHello(t *testing.T) {
	assertMessage := func(t testing.TB, received, expected string) {
		t.Helper()
		if received != expected {
			t.Errorf("got %q, expected %q", received, expected)
		}
	}

	t.Run("should say hello to a human", func(t *testing.T) {
		name := "Eric"

		received := Hello(name)
		expected := prefix + name

		assertMessage(t, received, expected)
	})

	t.Run("should say hello to everyone", func(t *testing.T) {
		received := Hello("")
		expected := prefix + "World"

		assertMessage(t, received, expected)
	})
}

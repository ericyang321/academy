package iterate

import "testing"

func TestIterate(t *testing.T) {
	t.Run("should create a 5 character repeat", func(t *testing.T) {
		received := Repeat("a")
		expected := "aaaaa"

		if received != expected {
			t.Errorf("Received %q, expected %q", received, expected)
		}
	})
}

func BenchmarkRepeat(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Repeat("a")
	}
}

package sync

import (
	"sync"
	"testing"
)

func assertCounter(t testing.TB, got, want int) {
	t.Helper()
	if got != want {
		t.Errorf("got %d want %d", got, want)
	}
}

func TestCounter(t *testing.T) {
	t.Run("Should increase number to 3 when incremented 3 times", func(t *testing.T) {
		wantedCount := 3

		counter := Counter{}
		counter.Inc()
		counter.Inc()
		counter.Inc()

		assertCounter(t, counter.Value(), wantedCount)
	})

	t.Run("Should increase number correctly under concurrent conditions", func(t *testing.T) {
		wantedCount := 1000
		counter := Counter{}

		var wg sync.WaitGroup
		wg.Add(wantedCount)

		for i := 0; i < wantedCount; i++ {
			go func() {
				counter.Inc()
				wg.Done()
			}()
		}
		wg.Wait()

		assertCounter(t, counter.Value(), wantedCount)
	})
}

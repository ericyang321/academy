package web_racer_select

import (
	"net/http"
	"net/http/httptest"
	"testing"
	"time"
)

func TestRacer(t *testing.T) {
	t.Run("should return the faster URL", func(t *testing.T) {
		slowServer := createTestServer(20 * time.Millisecond)
		fastServer := createTestServer(0)
		defer slowServer.Close()
		defer fastServer.Close()

		slowUrl := slowServer.URL
		fastUrl := fastServer.URL

		received, _ := Race(fastUrl, slowUrl)

		if received != fastUrl {
			t.Errorf("Expected %q but got %q", fastUrl, received)
		}
	})

	t.Run("should return time out error when url req times out", func(t *testing.T) {
		slowServer := createTestServer(20 * time.Millisecond)
		slowerServer := createTestServer(21 * time.Millisecond)
		defer slowServer.Close()
		defer slowerServer.Close()

		slowUrl := slowerServer.URL
		fastUrl := slowServer.URL

		_, err := ConfigurableRace(fastUrl, slowUrl, 10*time.Millisecond)

		if err == nil {
			t.Errorf("Expected an error but did not get one: %v", err)
		}
	})
}

func createTestServer(responseDelay time.Duration) *httptest.Server {
	return httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if responseDelay > 0 {
			time.Sleep(responseDelay)
		}
		w.WriteHeader(http.StatusOK)
	}))
}

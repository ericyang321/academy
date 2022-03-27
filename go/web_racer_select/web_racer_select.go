package web_racer_select

import (
	"fmt"
	"net/http"
	"time"
)

func Race(url1, url2 string) (string, error) {
	return ConfigurableRace(url1, url2, 10*time.Second)
}

func ConfigurableRace(url1 string, url2 string, timeout time.Duration) (string, error) {
	select {
	case <-Ping(url1):
		return url1, nil
	case <-Ping(url2):
		return url2, nil
	case <-time.After(timeout):
		return "", fmt.Errorf("timed out after 10 seconds waiting for %q and %q", url1, url2)
	}
}

func Ping(url string) chan bool {
	ch := make(chan bool)
	go func(url string) {
		http.Get(url)
		close(ch)
	}(url)

	return ch
}

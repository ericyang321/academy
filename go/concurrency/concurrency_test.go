package concurrency

import (
	"reflect"
	"strconv"
	"testing"
	"time"
)

func mockWebsiteChecker(url string) bool {
	return url != "waat://furhurterwe.geds"
}

// purposefully slow website checker to test for concurrency
func slowWebsiteChecker(_ string) bool {
	time.Sleep(20 * time.Millisecond)
	return true
}

func TestCheckWebsite(t *testing.T) {
	websites := []string{
		"http://google.com",
		"http://blog.gypsydave5.com",
		"waat://furhurterwe.geds",
	}

	expected := map[string]bool{
		"http://google.com":          true,
		"http://blog.gypsydave5.com": true,
		"waat://furhurterwe.geds":    false,
	}

	received := CheckWebsite(mockWebsiteChecker, websites)

	if !reflect.DeepEqual(expected, received) {
		t.Errorf("expected %v but got %v", expected, received)
	}
}

func BenchmarkWebsiteChecker(b *testing.B) {
	testUrls := make([]string, 100)
	for i := 0; i < len(testUrls); i++ {
		testUrls[i] = "https://testurl" + strconv.Itoa(i) + ".com"
	}

	for i := 0; i < b.N; i++ {
		CheckWebsite(slowWebsiteChecker, testUrls)
	}
}

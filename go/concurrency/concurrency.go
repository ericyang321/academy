package concurrency

type WebsiteChecker func(string) bool
type Result struct {
	Url    string
	Status bool
}

func CheckWebsite(checker WebsiteChecker, urls []string) map[string]bool {
	results := make(map[string]bool)
	resultChan := make(chan Result)

	for _, url := range urls {
		go func(u string) {
			resultChan <- Result{Url: u, Status: checker(u)}
		}(url)
	}

	for i := 0; i < len(urls); i++ {
		r := <-resultChan
		results[r.Url] = r.Status
	}

	return results
}

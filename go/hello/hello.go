package hello

const prefix = "Hello "

func Hello(name string) string {
	if name == "" {
		return prefix + "World"
	}

	return prefix + name
}

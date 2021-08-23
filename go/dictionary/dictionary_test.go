package dictionary

import "testing"

func TestSearch(t *testing.T) {
	dict := Dictionary{"test": "value"}

	t.Run("should find searched word", func(t *testing.T) {
		received, _ := dict.Search("test")
		expect := "value"

		assertStrings(t, expect, received)
	})

	t.Run("should return an err if word not found", func(t *testing.T) {
		_, err := dict.Search("unknown")

		if err == nil {
			t.Fatal("Expected an error but didn't get one")
		}
	})
}

func TestAdd(t *testing.T) {
	testKey := "test"
	testVal := "this is test string"

	t.Run("should add a new word to dictionary", func(t *testing.T) {
		dict := Dictionary{}
		dict.Add(testKey, testVal)

		received, _ := dict.Search(testKey)
		expected := testVal

		assertStrings(t, received, expected)
	})

	t.Run("should error if word already exists", func(t *testing.T) {
		dict := Dictionary{testKey: testVal}
		err := dict.Add(testKey, testVal)

		assertErr(t, err, ErrWordExists)
	})
}

func TestUpdate(t *testing.T) {
	t.Run("should update existing word", func(t *testing.T) {
		key := "test"
		value := "test value"
		dict := Dictionary{key: value}
		newValue := "new value"

		err := dict.Update(key, newValue)

		assertErr(t, err, nil)
		assertStrings(t, dict[key], newValue)
	})

	t.Run("should error when updating nonexistent word", func(t *testing.T) {
		key := "test"
		newValue := "test value"
		dict := Dictionary{}

		err := dict.Update(key, newValue)

		assertErr(t, err, ErrWordDoesNotExist)
	})
}

func TestDelete(t *testing.T) {

}

func assertStrings(t testing.TB, got, want string) {
	t.Helper()

	if got != want {
		t.Errorf("got %q want %q", got, want)
	}
}

func assertErr(tb testing.TB, received, expected error) {
	tb.Helper()
	if received != expected {
		tb.Errorf("got %q want %q", received, expected)
	}
}

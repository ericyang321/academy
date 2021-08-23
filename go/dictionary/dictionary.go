package dictionary

type Dictionary map[string]string

// dictionary specific error
type DictionaryErr string

func (de DictionaryErr) Error() string {
	return string(de)
}

const (
	ErrWordNotFound     = DictionaryErr("word not found")
	ErrWordExists       = DictionaryErr("word already exist")
	ErrWordDoesNotExist = DictionaryErr("cannot update word because it does not exist")
)

func (d Dictionary) Search(key string) (string, error) {
	word, ok := d[key]

	if !ok {
		return "", ErrWordNotFound
	}

	return word, nil
}

func (d Dictionary) Add(key, value string) error {
	_, err := d.Search(key)
	switch err {
	case ErrWordNotFound:
		d[key] = value
		return nil
	case nil:
		return ErrWordExists
	default:
		return err
	}
}

func (d Dictionary) Update(key, value string) error {
	_, err := d.Search(key)

	switch err {
	case ErrWordNotFound:
		return ErrWordDoesNotExist
	case nil:
		d[key] = value
		return nil
	default:
		return err
	}
}

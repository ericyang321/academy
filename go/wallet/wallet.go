package wallet

import (
	"errors"
	"fmt"
)

type Coin int

// this type function def lets you define how your type is printed when used with the %s format string in prints.
// this is the interface for fmt.Sprintf %s printing
// type Stringer interface {
//     String() string
// }
func (c Coin) String() string {
	return fmt.Sprintf("%d coins", c)
}

var ErrInsufficientFund = errors.New("insufficient funds")

type Wallet struct {
	balance Coin
}

func (w *Wallet) Balance() Coin {
	return w.balance
}

func (w *Wallet) Deposit(amount Coin) {
	w.balance += amount
}

func (w *Wallet) Withdraw(amount Coin) error {
	if amount > w.balance {
		return ErrInsufficientFund
	}

	w.balance -= amount

	return nil
}

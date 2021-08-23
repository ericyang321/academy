package wallet

import (
	"testing"
)

func TestWallet(t *testing.T) {

	t.Run("Deposit", func(t *testing.T) {
		wallet := Wallet{}
		wallet.Deposit(Coin(10))

		received := wallet.Balance()
		expected := Coin(10)

		assertWalletAmount(t, received, expected)
	})

	t.Run("Withdraw", func(t *testing.T) {
		wallet := Wallet{balance: Coin(30)}

		err := wallet.Withdraw(Coin(30))

		received := wallet.Balance()
		expected := Coin(0)

		assertNoError(t, err)
		assertWalletAmount(t, received, expected)
	})

	t.Run("Withdraw beyond what you have", func(t *testing.T) {
		startingBalance := Coin(30)
		wallet := Wallet{balance: startingBalance}

		err := wallet.Withdraw(Coin(80))

		assertError(t, err, ErrInsufficientFund.Error())
		assertWalletAmount(t, startingBalance, wallet.Balance())
	})
}

func assertWalletAmount(tb testing.TB, received, expected Coin) {
	tb.Helper()
	if received != expected {
		tb.Errorf("Expected %s, but got %s", received, expected)
	}
}

func assertError(tb testing.TB, err error, message string) {
	tb.Helper()
	if err == nil {
		tb.Fatal("didn't get an error message but expected one")
	}

	if err.Error() != message {
		tb.Errorf("error message mismatch %q but wanted %q", err.Error(), message)
	}
}

func assertNoError(t testing.TB, err error) {
	t.Helper()
	if err != nil {
		t.Fatal("got an error but didn't want one")
	}
}

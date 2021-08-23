package sum

import (
	"reflect"
	"testing"
)

func TestSum(t *testing.T) {
	t.Run("should add all numbers in array up", func(t *testing.T) {
		sumArray := []int{5, 5}
		received := Sum(sumArray)
		expected := 10

		if received != expected {
			t.Errorf("sum of %d is not %d, %v", received, expected, sumArray)
		}
	})
}

func TestSumAll(t *testing.T) {
	t.Run("should total all array of numbers into separate return obj", func(t *testing.T) {
		sumArray1 := []int{2, 3}
		sumArray2 := []int{3, 4}

		received := SumAll(sumArray1, sumArray2)
		expected := []int{5, 7}

		if !reflect.DeepEqual(received, expected) {
			t.Errorf("sum of %v is not %v", received, expected)
		}
	})
}

func TestSumAllTails(t *testing.T) {
	t.Run("should add up all numbers at the tail of array", func(t *testing.T) {
		sumArray1 := []int{2, 3}
		sumArray2 := []int{3, 4}

		received := SumAllTail(sumArray1, sumArray2)
		expected := []int{3, 4}

		if !reflect.DeepEqual(received, expected) {
			t.Errorf("sum of %v is not %v", received, expected)
		}
	})

	t.Run("should be able to sum empty arrays", func(t *testing.T) {
		sumArray1 := []int{}
		sumArray2 := []int{3, 4}

		received := SumAllTail(sumArray1, sumArray2)
		expected := []int{0, 4}

		if !reflect.DeepEqual(received, expected) {
			t.Errorf("sum of %v is not %v", received, expected)
		}
	})
}

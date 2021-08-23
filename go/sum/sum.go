package sum

func Sum(nums []int) int {
	total := 0
	for _, num := range nums {
		total += num
	}

	return total
}

func SumAll(numArrays ...[]int) []int {
	var totalArray []int

	for _, numArray := range numArrays {
		totalArray = append(totalArray, Sum(numArray))
	}

	return totalArray
}

func SumAllTail(numArrays ...[]int) []int {
	var totalArray []int

	for _, numArray := range numArrays {
		if len(numArray) == 0 {
			totalArray = append(totalArray, 0)
		} else {
			totalArray = append(totalArray, Sum(numArray[1:]))
		}
	}

	return totalArray
}

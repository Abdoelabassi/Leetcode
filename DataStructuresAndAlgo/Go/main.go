package main

import "fmt"

// MergeSort sorts a slice of integers using the merge sort algorithm
func MergeSort(arr []int) []int {
	// Base case: arrays with 0 or 1 elements are already sorted
	if len(arr) <= 1 {
		return arr
	}

	// Find the middle point to divide the array into two halves
	mid := len(arr) / 2
	
	// Recursively sort the two halves
	left := MergeSort(arr[:mid])
	right := MergeSort(arr[mid:])
	
	// Merge the sorted halves
	return merge(left, right)
}

// merge combines two sorted arrays into a single sorted array
func merge(left, right []int) []int {
	result := make([]int, 0, len(left)+len(right))
	
	// Indexes for left and right arrays
	i, j := 0, 0
	
	// Compare elements from both arrays and add the smaller one to result
	for i < len(left) && j < len(right) {
		if left[i] <= right[j] {
			result = append(result, left[i])
			i++
		} else {
			result = append(result, right[j])
			j++
		}
	}
	
	// Add any remaining elements from left array
	for i < len(left) {
		result = append(result, left[i])
		i++
	}
	
	// Add any remaining elements from right array
	for j < len(right) {
		result = append(result, right[j])
		j++
	}
	
	return result
}

func main() {
	// Example usage
	unsortedArray := []int{38, 27, 43, 3, 9, 82, 10}
	fmt.Println("Unsorted array:", unsortedArray)
	
	sortedArray := MergeSort(unsortedArray)
	fmt.Println("Sorted array:", sortedArray)
}
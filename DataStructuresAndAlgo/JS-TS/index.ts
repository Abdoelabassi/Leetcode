/**
 * Merge function to combine two sorted arrays into one sorted array
 * @param left The left sorted array
 * @param right The right sorted array
 * @returns A new sorted array containing all elements from left and right
 */
function merge(left: number[], right: number[]): number[] {
  const result: number[] = [];
  let leftIndex = 0;
  let rightIndex = 0;

  // Compare elements from both arrays and add the smaller one to result
  while (leftIndex < left.length && rightIndex < right.length) {
    if (left[leftIndex] <= right[rightIndex]) {
      result.push(left[leftIndex]);
      leftIndex++;
    } else {
      result.push(right[rightIndex]);
      rightIndex++;
    }
  }

  // Add any remaining elements from left array
  while (leftIndex < left.length) {
    result.push(left[leftIndex]);
    leftIndex++;
  }

  // Add any remaining elements from right array
  while (rightIndex < right.length) {
    result.push(right[rightIndex]);
    rightIndex++;
  }

  return result;
}

/**
 * Merge Sort implementation
 * @param arr The array to sort
 * @returns A new sorted array
 */
function mergeSort(arr: number[]): number[] {
  // Base case: arrays with 0 or 1 elements are already sorted
  if (arr.length <= 1) {
    return arr;
  }

  // Find the middle point to divide the array into two halves
  const middle = Math.floor(arr.length / 2);

  // Recursively sort the two halves
  const left = mergeSort(arr.slice(0, middle));
  const right = mergeSort(arr.slice(middle));

  // Merge the sorted halves
  return merge(left, right);
}

// Example usage
const unsortedArray = [38, 27, 43, 3, 9, 82, 10];
console.log("Unsorted array:", unsortedArray);

const sortedArray = mergeSort(unsortedArray);
console.log("Sorted array:", sortedArray);

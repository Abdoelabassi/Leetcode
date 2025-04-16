const std = @import("std");

// Function to merge two sorted arrays
fn merge(allocator: std.mem.Allocator, left: []const i32, right: []const i32) ![]i32 {
    var result = try allocator.alloc(i32, left.len + right.len);
    
    var i: usize = 0; // Index for left array
    var j: usize = 0; // Index for right array
    var k: usize = 0; // Index for result array
    
    // Compare elements from both arrays and add the smaller one to resultcd .
    while (i < left.len and j < right.len) {
        if (left[i] <= right[j]) {
            result[k] = left[i];
            i += 1;
        } else {
            result[k] = right[j];
            j += 1;
        }
        k += 1;
    }
    
    // Add any remaining elements from left array
    while (i < left.len) {
        result[k] = left[i];
        i += 1;
        k += 1;
    }
    
    // Add any remaining elements from right array
    while (j < right.len) {
        result[k] = right[j];
        j += 1;
        k += 1;
    }
    
    return result;
}

// MergeSort function to sort an array using the merge sort algorithm
fn mergeSort(allocator: std.mem.Allocator, arr: []const i32) ![]i32 {
    // Base case: arrays with 0 or 1 elements are already sorted
    if (arr.len <= 1) {
        return allocator.dupe(i32, arr);
    }
    
    // Find the middle point to divide the array into two halves
    const mid = arr.len / 2;
    
    // Recursively sort the two halves
    const left = try mergeSort(allocator, arr[0..mid]);
    defer allocator.free(left);
    
    const right = try mergeSort(allocator, arr[mid..]);
    defer allocator.free(right);
    
    // Merge the sorted halves
    return merge(allocator, left, right);
}

pub fn main() !void {
    // Get the standard output
    const stdout = std.io.getStdOut().writer();
    
    // Create an arena allocator
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();
    
    // Example array to sort
    const unsortedArray = [_]i32{ 38, 27, 43, 3, 9, 82, 10 };
    
    try stdout.print("Unsorted array: ", .{});
    for (unsortedArray) |num| {
        try stdout.print("{} ", .{num});
    }
    try stdout.print("\n", .{});
    
    // Sort the array using merge sort
    const sortedArray = try mergeSort(allocator, &unsortedArray);
    // Note: We don't need to free sortedArray as we're using an arena allocator
    
    try stdout.print("Sorted array: ", .{});
    for (sortedArray) |num| {
        try stdout.print("{} ", .{num});
    }
    try stdout.print("\n", .{});
}

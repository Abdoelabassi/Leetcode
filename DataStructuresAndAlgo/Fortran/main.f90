program merge_sort_demo
    implicit none
    
    integer, parameter :: n = 7
    integer :: arr(n) = [38, 27, 43, 3, 9, 82, 10]
    integer :: i
    
    ! Print the unsorted array
    print *, "Unsorted array:"
    do i = 1, n
        write(*, '(I5)', advance='no') arr(i)
    end do
    print *, ""
    
    ! Sort the array using merge sort
    call merge_sort(arr, 1, n)
    
    ! Print the sorted array
    print *, "Sorted array:"
    do i = 1, n
        write(*, '(I5)', advance='no') arr(i)
    end do
    print *, ""
    
contains

    ! Recursive merge sort function
    recursive subroutine merge_sort(a, left, right)
        integer, intent(inout) :: a(:)
        integer, intent(in) :: left, right
        integer :: mid
        
        ! Base case: if array segment has 1 or 0 elements, it's already sorted
        if (left < right) then
            ! Find the middle point to divide the array
            mid = (left + right) / 2
            
            ! Recursively sort the first and second halves
            call merge_sort(a, left, mid)
            call merge_sort(a, mid + 1, right)
            
            ! Merge the sorted halves
            call merge(a, left, mid, right)
        end if
    end subroutine merge_sort
    
    ! Merge two sorted subarrays into one
    subroutine merge(a, left, mid, right)
        integer, intent(inout) :: a(:)
        integer, intent(in) :: left, mid, right
        integer :: i, j, k
        integer :: n1, n2
        integer, allocatable :: L(:), R(:)
        
        ! Size of left and right subarrays
        n1 = mid - left + 1
        n2 = right - mid
        
        ! Create temporary arrays
        allocate(L(n1), R(n2))
        
        ! Copy data to temporary arrays L and R
        do i = 1, n1
            L(i) = a(left + i - 1)
        end do
        
        do j = 1, n2
            R(j) = a(mid + j)
        end do
        
        ! Merge the temporary arrays back into a(left..right)
        i = 1    ! Initial index of first subarray
        j = 1    ! Initial index of second subarray
        k = left ! Initial index of merged subarray
        
        ! Compare elements from both arrays and add the smaller one
        do while (i <= n1 .and. j <= n2)
            if (L(i) <= R(j)) then
                a(k) = L(i)
                i = i + 1
            else
                a(k) = R(j)
                j = j + 1
            end if
            k = k + 1
        end do
        
        ! Copy the remaining elements of L, if any
        do while (i <= n1)
            a(k) = L(i)
            i = i + 1
            k = k + 1
        end do
        
        ! Copy the remaining elements of R, if any
        do while (j <= n2)
            a(k) = R(j)
            j = j + 1
            k = k + 1
        end do
        
        ! Deallocate temporary arrays
        deallocate(L, R)
    end subroutine merge
    
end program merge_sort_demo
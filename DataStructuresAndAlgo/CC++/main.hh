#pragma ounce

#include <vector>



/**
 * merge - merge two lists
 * @list_a: first half
 * @list_b: second half
 * Returns: merged list
 */
template<typename T>
std::vector<T> merge(std::vector<T> &list_a, std::vector<T> &list_b){
    size_t i, j = 0;
    std::vector<T> merged_list;
    while (i < list_a.size() && j < list_b.size() ){
        if (list_a[i] < list_b[j]){
            merged_list.push_back(list_a[i]);
            i += 1;
        }else{
            merged_list.push_back(list_b[j]);
            j += 1;
        }
    }
    while (i < list_a.size()){
        merged_list.push_back(list_a[i]);
        i += 1;
    }
    while (j < list_b.size())
    {
        merged_list.push_back(list_b[j]);
        j += 1;
    }
    return merged_list;
}


/**
 * merge_sort - sorting algorithm that uses merging
 * @list: vector of elements of ints, floats, doubles...
 * Return: megred-sorted list
 */
template<typename T>
std::vector<T> merge_sort(std::vector<T> &list){
    if (list.size() == 1)
        return list;
    int mid = (int)(list.size()/2);
    std::vector<T> first_half(list.begin(), list.begin() + mid);
    std::vector<T> second_half(list.begin() + mid, list.end());
    std::vector<T> half_a = merge_sort(first_half);
    std::vector<T> half_b = merge_sort(second_half);
    return merge(half_a, half_b);
}
#include "count-subarrays-of-length-three-with-a-condition.hh"


int main(){

    std::vector<int> nums = {1, 2, 3, 4, 5};
    Solution solution(nums);
    std::map<int, std::vector<int>> result = solution.countSubArray(nums);
    // loop throught the map
    for (auto it = result.begin(); it != result.end(); ++it) {
        std::cout << "Key: " << it->first << " Values: ";
        for (auto vec_it = it->second.begin(); vec_it != it->second.end(); ++vec_it) {
            std::cout << *vec_it << " ";
        }
        std::cout << std::endl;
    }




    return 0;
}
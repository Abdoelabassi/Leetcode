#ifndef COUNT_SUBARRAYS_OF_LENGTH_THREE_WITH_A_CONDITION_HH
#define COUNT_SUBARRAYS_OF_LENGTH_THREE_WITH_A_CONDITION_HH

#include <iostream>
#include <vector>
#include <string>
#include <map>

/**
 * Given an integer array nums, return the 
 * number of subarrays of length 3 such that the sum of 
 * the first and third numbers equals exactly half of the second number.

 */

 class Solution {
    private:
    std::vector<int> nums;
    public:
    Solution(std::vector<int>& nums): nums(nums) {}
    ~Solution(){}
    std::map<int, std::vector<int>> countSubArray(std::vector<int>& nums){
        int n = nums.size();
        std::map<int, std::vector<int>> result_map;
        for (int i = 1; i < n - 1; ++i) {
            if (nums[i] == (nums[i-1] + nums[i-2])*2) {
                result_map[nums[i]].push_back(nums[i-1]);
                result_map[nums[i]].push_back(nums[i]);
                result_map[nums[i]].push_back(nums[i+1]);
            }
        }
        return result_map;


        

    }
 };


 #endif

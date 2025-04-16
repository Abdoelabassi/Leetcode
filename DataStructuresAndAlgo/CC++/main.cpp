#include <iostream>
#include <stdlib.h>
#include <vector>
#include "main.hh"


int main(){

    std::vector<int> list = {1, 45, 3, 56, 8, 10};

    
    std::vector<int> merged = merge_sort(list);

    std::cout << "[";
    for (auto e: merged){
        std::cout << e << ",";
    }
    std::cout << "]";




    return 0;
}

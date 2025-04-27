#pragma ounce

#include <iostream>
#include <stdlib.h>
#include <string>
#include <vector>


class Node{
    private:
        std::string data;
    public:
    Node(const std::string &data);
    ~Node();

    Node* next;
    std::string getData() {return data;}

    void tarverse(Node* n);

};

#include "singlylinkedlist.hh"


Node::Node(const std::string& data)
: data(data)
{}

Node::~Node()
{}

void Node::tarverse(Node* n){
    Node* current = n;
    while (current){
        printf("you visited: %s\n", current->getData());
        current = current->next;
    }
}
#include "singlylinkedlist.hh"


int main(int argc, char** argv){
    (void*)argc;
    (void*)argv;

    Node* n1 = new Node("google.com");
    Node* n2 = new Node("youtube.com");
    Node* n3 = new Node("twitch.com");
    
    n1->traverse(n1);
}
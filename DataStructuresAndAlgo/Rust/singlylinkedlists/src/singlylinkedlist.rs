use std::rc::Rc;
use std::cell::{Ref, RefCell};


struct Node<T>{
    data: T,
    next: Option<Box<Node<T>>>
}

impl<T> Node<T>{
    fn new(data: T) -> Self{
        Node {
            data,
            next: None
        }
    }
}
type Link<T> = Option<Box<Node<T>>>;
pub struct SinglyLinkedlist<T>{
    head: Link<T>,
    tail: Option<*mut Node<T>>
}

impl<T> SinglyLinkedlist<T>{
    pub fn new() -> Self{
        SinglyLinkedlist {
            head: None,
            tail: None
        }
    }

    // Add a new item to the front of the list
    pub fn push_front(&mut self, value: T) {
        let new_node = Box::new(Node::new(value));
        self.head = Some(new_node);
    }

    // Return an iterator over the list
    pub fn iter(&self) -> Iter<'_, T> {
        Iter {
            next: self.head.as_deref(),
        }
    }


}

// Iterator implementation for our linked list
pub struct Iter<'a, T> {
    next: Option<&'a Node<T>>,
}

impl<'a, T> Iterator for Iter<'a, T> {
    type Item = &'a T;

    fn next(&mut self) -> Option<Self::Item> {
        // Get the current node
        self.next.map(|node| {
            // Update next to point to the next node
            self.next = node.next.as_deref();
            // Return a reference to the current value
            &node.data
        })
    }
}

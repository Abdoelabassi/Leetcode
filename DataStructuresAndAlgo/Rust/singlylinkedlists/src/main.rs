mod singlylinkedlist;

use singlylinkedlist::SinglyLinkedlist;

fn main() {

        let mut links:SinglyLinkedlist<String> = SinglyLinkedlist::new();
        links.push_front(String::from("google.com"));
        links.push_front(String::from("youtube.com"));
        links.push_front(String::from("twitch.com"));

        println!("list the elements of the list");

        for link in links.iter(){
                println!("link: {}", link);
        }


    
}
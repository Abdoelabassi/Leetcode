
type Tree = Option<Box<Node>>;
struct Node{
    pub value: u64,
    left: Tree,
    right: Tree
}
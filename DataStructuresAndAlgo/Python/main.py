from linkedlist import SinglyLinkedList
from doublylinkedlist import DoublyLinkedList

print("Singly Linked List")
print("#"*80)
links: SinglyLinkedList = SinglyLinkedList()
print(links)
print()
print("#"*86)
links.append("google.com")
links.append("youtube")
links.append("twitch.com")
links.append("kick.com")
links.append("mistral.ai")
links.append("claude.ai")

print("the size of the list before deletion: ", links.size())

print("listing the items before deletion: ")
print(links)

links.delete("kick.com")

print("the size of the list after deletion: ", links.size())
print("listing the items after deletion")
print(links)

###############################################
print()

print("#"*80)
print("checking if some items exist: ")
item1 = "kick.com"
item2 = "x.com"

if links.search(item1):
    print(f"{item1} exists.")
else:
    print(f"{item1} doesn't exists.")

if links.search(item2):
    print(f"{item2} exists.")
else:
    print(f"{item2} doesn't exists.")


print("#"*80)
print("Doubly Linked List")
links2: DoublyLinkedList = DoublyLinkedList()
links2.append_at_start("google.com")
links2.append_at_start("youtube")
links2.append_at_start("twitch.com")
links2.append_at_start("kick.com")
links2.append_at_start("mistral.ai")
links2.append_at_start("claude.ai")
links2.append("gemini.com")
print("the size of the list before deletion: ", links2.size())
print(links2)

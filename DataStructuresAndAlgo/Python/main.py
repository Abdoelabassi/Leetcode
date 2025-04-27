from linkedlist import SinglyLinkedList


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
current = links.head
while current:
    print("you visited: ", current.data)
    current = current.next
print("#"*80)

links.delete("kick.com")

print("the size of the list after deletion: ", links.size())
print("listing the items after deletion")
current = links.head
while current:
    print("you visited: ", current.data)
    current = current.next

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

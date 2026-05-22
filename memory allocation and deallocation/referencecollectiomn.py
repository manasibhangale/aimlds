"""Reference counting is a memory management technique used to keep track of how many references (or pointers) point to a particular object in memory.

🔹 How it works
Every object has a reference count.
When a new reference points to the object → count increases.
When a reference is removed or goes out of scope → count decreases.
When the reference count reaches zero, the object is automatically deallocated (freed)."""
import sys
a=[]
print(sys.getrefcount(a)) #2
b=a
print(sys.getrefcount(b)) #3
del b
print(sys.getrefcount(b)) #not defined



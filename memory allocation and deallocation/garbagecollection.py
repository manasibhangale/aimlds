"""Garbage Collection (GC) is an automatic memory management process that identifies and removes objects from memory that are no longer being used by a program.

Instead of the programmer manually freeing memory, the system automatically reclaims unused memory.

🔹 Why Garbage Collection is Needed

When programs create objects dynamically, memory gets allocated.
If unused memory is not released:

memory leaks occur,
RAM usage increases,
program performance degrades.

Garbage collection solves this automatically."""
import gc
gc.enable()
gc.disable()
print(gc.collect())
print(gc.get_stats())
print(gc.garbage)
"""# Process, Program and Thread

## 1. Program

A **program** is a set of instructions written in a programming language to perform a specific task.

### Key Points:
- It is a passive entity.
- Stored on disk (not executing).
- Becomes active only when executed.
- Example: `calculator.py`, `chrome.exe`

---

## 2. Process

A **process** is a program that is currently in execution.

### Key Points:
- It is an active entity.
- Has its own memory space.
- Managed by the Operating System.
- One program can have multiple processes.

### Memory Structure of Process:
- Code (text)
- Data
- Heap (dynamic memory)
- Stack (function calls)

### Example:
When you open Chrome, it becomes a process.

---

## 3. Thread

A **thread** is a lightweight sub-unit of a process.

### Key Points:
- A process can have multiple threads.
- Threads share the same memory of the process.
- Each thread has its own stack.
- Faster to create than processes.

### Example:
In a browser:
- Thread 1 → UI rendering
- Thread 2 → Network calls
- Thread 3 → Video playback

---

## Comparison Table

| Feature | Program | Process | Thread |
|--------|--------|--------|--------|
| Nature | Passive | Active | Active |
| Execution | No | Yes | Yes |
| Memory | No allocation | Separate memory | Shared memory |
| Unit | Code file | Running program | Sub-part of process |
| Speed | N/A | Slower | Faster |

---

## Simple Analogy

- Program → Recipe
- Process → Cooking the recipe
- Thread → Multiple chefs cooking together in same kitchen"""
import threading
import time

def read_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"numbers:{i}")
def read_letters():
    for i in "abcd":
        time.sleep(2)
        print(f"letters:{i}")
read_numbers()
read_letters()
t=time.time()
finished_time=time.time()-t
print(finished_time)

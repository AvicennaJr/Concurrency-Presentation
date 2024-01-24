# Concurrency In Python
How to speed up your Python code by running it concurrently.

---

## What Is Concurrency
Refers to simultaneous occurrence.

In Python they are called by different names:
- Threads
- Processes
- Task

But at a high level they all refer to a sequence of instructions that run in order.

---

## Ways To Achieve Concurrency In Python
- Threading
- Asyncio
- Multiprocessing

Threading and asyncio both run on a single processor and therefore only run one instruction at a time.

Multiprocessing runs on multiple processors and therefore can run multiple instructions at a time.

---

## Threading
Known as pre-emptive multitasking or pre-emptive scheduling.

The operating system knows about each thread and can interrupt it at any time to start running a different thread.

Pre-emptive multitasking since the operating system can pre-empt (halt) your thread to make the switch.

A computer operating system uses a set criteria to determine how long to run a specific computer task before letting another computer task make use of its computer resources

---

## Asyncio
Refered to as cooperative multitasking or non-preemptive multitasking.

The operating system does not know about each task and therefore cannot interrupt it.

The task must yield control back to the operating system. They do this by announcing when they are ready to be switched out.

---

## Multiprocessing

With multiprocessing, each process has its own memory space (as opposed to threads which share the same memory space).

Think of it as if each process runs in its own Python interpreter.

Because they are different processes, it means they can run in different cores ergo _they run at the same time_.

---

## Why Concurrency

- Improve performance. Python can be slow 🐢🕓
- Make your code more responsive (eg GUI)
- Make your code more scalable (eg multiple requests in a web server)
- Resource sharing

---

## A Demonstration

Here is a simple synchronous program:

```python
def do_first():
    print("Running do_first")
    ...

def do_second():
    print("Running do_second")
    ...

def main():
    do_first()
    do_second()

main()
```

---

## Asynchronous Execution

To make a program async you need to:
- Add `async` keyword in front of the function definition
- Add `await` keyword when you call your async function 
- Create tasks from the `async` functions you wish to start asynchronously
- Call `asyncio.run()` to start the asynchronous section of your program

---

## Asynchronous Execution

```python
import asyncio

async def do_first():
    print("Running do_first block 1")

    # Release execution
    await asyncio.sleep(0)

    print("Running do_first block 2")

async def do_second():
    print("Running do_second block 1")
    ...
    
    # Release execution
    await asyncio.sleep(0)

    print("Running do_second block 2")
    ...

async def main():
    task_1 = asyncio.create_task(do_first())
    task_2 = asyncio.create_task(do_second())
    await asyncio.wait([task_1, task_2])


asyncio.run(main())
```

---

## Threading

In threading, we execute one line of code at a time but we constantly change which line is run.

This is done using threading library.

We first create some threads, start them and then wait them to finish (using join, for example).

---

## Threading

```python
import threading

def do_first():
    print("Running do_first line 1")
    print("Running do_first line 2")
    print("Running do_first line 3")
    ...

def do_second():
    print("Running do_second line 1")
    print("Running do_second line 2")
    print("Running do_second line 3")
    ...

def main():
    t1 = threading.Thread(target=do_first)
    t2 = threading.Thread(target=do_second)

    # Start threads
    t1.start(), t2.start()

    # Wait threads to complete
    t1.join(), t2.join()

main()
```

---

## Multiprocessing

In multiprocessing we actually run multiple lines of Python code at one time.

We use multiple processes to achieve this.

In order to use multiprocessing, you need to:
    - create processess 
    - set them running 
    - wait for them to finish (using join, for example).

---

## Multiprocessing

```python
import multiprocessing

def do_first():
    print("Running do_first line 1")
    print("Running do_first line 2")
    print("Running do_first line 3")
    ...

def do_second():
    print("Running do_second line 1")
    print("Running do_second line 2")
    print("Running do_second line 3")
    ...

def main():
    t1 = multiprocessing.Process(target=do_first)
    t2 = multiprocessing.Process(target=do_second)

    # Start processes
    t1.start(), t2.start()

    # Wait processes to complete
    t1.join(), t2.join()

main()
```

---

## When To Use What

### Asyncio

- I/O bound operations. Tasks like reading/writing large files, making HTTP requests etc

- When you need to scale to thousands of tasks (threads are too heavy)

### Threading

- Parallelism for I/O bound operations eg fetching data from multiples sources simultaneously

- Responsive GUIs to make interfaces more responsive 

### Multiprocessing

- CPU bound operations eg image processing, video processing, machine learning etc

- When you need to isolate memory between processes

- Parallel computation by splitting tasks into independent chunks

---

## Some Gotchas

- Asyncio needs libraries that support it. For example if you have a database query but your database client (eg sqlite3 or psycopg2) does not support async, it means you cannot run multiple queries at the same time.

- Asyncio is not thread safe, so you cannot combine the two.

- Threading has a problem of multiple threads operating on the same data. There is a risk of corruption or crash (race conditions)

- Multiprocessing is heavy on memory. Each process has its own memory space and therefore you need to be careful when using it.

---

## References

- Multiprocessing : https://docs.python.org/3/library/multiprocessing.html
- Threading : https://docs.python.org/3/library/threading.html

- Asyncio : https://docs.python.org/3/library/asyncio.html

- Real Python : https://realpython.com/python-concurrency/

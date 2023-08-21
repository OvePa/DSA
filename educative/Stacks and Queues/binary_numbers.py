from queue import MyQueue

"""
1.Start with Enqueuing 1
2.Dequeue a number from queue
3.append 0 to it and enqueue it back to queue.
4.Perform step 2 but with appending 1 to the
  origional number and enqueue back to queue.

Queue takes integer values so before enqueueing it make
sure to convert String to integer. Size of Queue should
be 1 more than number because for a single number we're
enqueing two variations of it , one with appended 0
while other with 1 being appended.
"""


def find_bin(number):
    result = []
    queue = MyQueue()
    queue.enqueue(1)
    for i in range(number):
        result.append(str(queue.dequeue()))
        s1 = result[i] + "0"
        s2 = result[i] + "1"
        queue.enqueue(s1)
        queue.enqueue(s2)

    return result


if __name__ == "__main__":
    print(find_bin(10))

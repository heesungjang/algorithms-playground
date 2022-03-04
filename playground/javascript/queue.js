class Node {
  constructor(value, next) {
    this.value = value;
    this.next = next;
  }
}

class Queue {
  constructor() {
    this.front = null;
  }
  push(value) {
    // 큐가 비있을때
    if (!this.front) {
      let newNode = new Node(value, null);
      this.front = newNode;
      return;
    }

    // 큐에 값있을때
    if (this.front) {
      let currNode = this.front;

      while (currNode.next !== null) {
        currNode = currNode.next;
      }
      currNode.next = new Node(value, null);
    }
  }
  pop() {
    if (!this.front) {
      return;
    }
    let currFrontNode = this.front;
    this.front = currFrontNode.next;

    return currFrontNode.value;
  }
  isEmpty() {
    return this.front === null;
  }
}

const queue = new Queue();

queue.push(1);
queue.push(2);
console.log(queue.isEmpty());
console.log(queue.pop());
console.log(queue.pop());
console.log(queue.pop());

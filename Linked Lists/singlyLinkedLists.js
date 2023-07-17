// class Node {
//     constructor(data, next = null) {
//         this.data = data;
//         this.next = next;

//     }

//     toString(self) {
//         return (str(self.data));
//     }
// }

// class LinkedList {
//     constructor() {
//         this.head = null;
//     }
//     getSize() {
//         if (this.head === null) {
//             return -1;
//         }
//         let counter = 0;
//         let current = this.head;
//         while (current) {
//             counter++;
//             current = current.next;
//         }
//         return counter;
//     }
//     getMax() {
//         if (this.head === null) {
//             return -1;
//         }
//         let myMax = this.head.value;
//         while (current) {
//             myMax = max(myMax, current.value);
//         }
//         return myMax;
//     }
//     getMin() {
//         if (this.head === null) {
//             return -1;
//         }
//         let myMin = this.head.value;
//         while (current) {
//             myMin = min(myMin, current.value);
//         }
//         return myMin;
//     }

//     insertNode(value, pos = null) {
//         let size = this.getSize();
//         if ((pos !== null) && (pos < 0)) {
//             console.log("Out of bounds");
//             return;
//         }
//         if (pos > size) {
//             pos = size;
//         }
//         let target = new Node(value);

//         if (pos === null) {
//             if (this.head === null) {
//                 this.head = target;
//                 return;
//             } else {
//                 let current = this.head;
//                 while (current.next) {
//                     current = current.next;

//                 }
//                 current.next = target;
//                 return;
//             }
//         } else if (pos === 0) {
//             target.next = this.head;
//             this.head = target;
//             return;
//         } else {
//             let count = 1;
//             let current = this.head;
//             while (count < pos) {
//                 current = current.next;
//                 count++;
//             }
//             let new_next = current.next;
//             current.next = target;
//             target.next = new_next;
//             return;
//         }


//     }
//     deleteNode(value) {
//         if (this.head.data === value) {
//             let old_head = this.head;
//             this.head = this.head.next;
//             old_head.next = null;
//         } else {
//             let current = this.head;
//             while (this.current.next.data !== value) {
//                 current = current.next;
//                 if (current.next === null) {
//                     console.log("Value not found");
//                     return;
//                 }
//             }
//             let to_delete = current.next;
//             current.next = to_delete.next;
//             to_delete.next = null;
//             return;
//         }
//     }
//     toString() {
//         let myStr = "";
//         let current = this.head;
//         while (current) {
//             if (current.next) {
//                 myStr += str(current.data);
//             }
//             myStr += str(current.data) + " => ";
//             current = current.next;
//         }
//         return `${myStr} \n its size is ${this.getSize()} \n The head is ${this.head} \n Max val is ${this.getMax()} \n Min val ${this.getMin()}`;
//     }

// }

// let myLL = new LinkedList();
// myLL.insertNode(1);
// myLL.insertNode(2);
// myLL.insertNode(3);
// myLL.insertNode(4, 2);

// console.log(myLL.toString());

class Node {
    constructor(data, next = null) {
        this.data = data;
        this.next = next;
    }

    toString() {
        return this.data.toString();
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
    }

    isEmpty() {
        return !this.head;
    }

    size() {
        let count = 0;
        let current = this.head;
        while (current) {
            count++;
            current = current.next;
        }
        return count;
    }

    append(data) {
        let newNode = new Node(data);
        if (this.isEmpty()) {
            this.head = newNode;
        } else {
            let current = this.head;
            while (current.next) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    prepend(data) {
        let newNode = new Node(data);
        newNode.next = this.head;
        this.head = newNode;
    }

    insert(data, index) {
        if (index < 0 || index > this.size()) {
            return;
        }
        if (index === 0) {
            this.prepend(data);
            return;
        }
        let newNode = new Node(data);
        let current = this.head;
        let count = 0;
        while (count < index - 1) {
            current = current.next;
            count++;
        }
        newNode.next = current.next;
        current.next = newNode;
    }

    delete(index) {
        if (index < 0 || index >= this.size()) {
            return;
        }
        if (index === 0) {
            this.head = this.head.next;
            return;
        }
        let current = this.head;
        let count = 0;
        while (count < index - 1) {
            current = current.next;
            count++;
        }
        current.next = current.next.next;
    }

    toString() {
        let list = [];
        let current = this.head;
        while (current) {
            list.push(current.toString());
            current = current.next;
        }
        return list.join(" -> ");
    }
}

let myList = new SinglyLinkedList();
myList.append(1);
myList.append(2);
myList.append(3);
myList.prepend(0);
console.log(myList.toString()); // 0 -> 1 -> 2 -> 3
myList.insert(4, 2);
console.log(myList.toString()); // 0 -> 1 -> 4 -> 2 -> 3
myList.delete(1);
console.log(myList.toString()); // 1 -> 4 -> 2 -> 3
#Q.1|
'''def stack_expression(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])
    tokens = expression.split()

    
        

   
    for token in reversed(tokens):
        if token in operators:
            
            operand1 = stack.pop()
            operand2 = stack.pop()

            
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2

            stack.append(result)
        else:
            
            stack.append(int(token))

    
    return stack[0]

expression = "+ 9 * 2 6"
result =stack_expression(expression)
print("result is",result)

#Q.2|
def evaluate_postfix_expression(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])
    tokens = expression.split()
    print(tokens)

    for token in tokens:
        if token in operators:
            
            operand2 = stack.pop()
            operand1 = stack.pop()

           
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2

            stack.append(result)
        else:
            
            stack.append(int(token))

    
    return stack[0]

expression = "2 3 +"
result = evaluate_postfix_expression(expression)
print("The result is",result)

#Q.3|
stack=[]

def display():
    print(stack)
    

def push():
    data=int(input("Enter the data: "))
    stack.append(data)
    print("data is push into the stack.")

while True:
    print("1-Display")
    print("2-push")
    a=int(input("What you want to do?(1/2): "))
    if a==1:
        display()
    elif a==2:
        push()
    
#Q.4|
stack=[]

def display():
    print(stack)
    

def push():
    data=int(input("Enter the data: "))
    stack.append(data)
    print("data is push into the stack.")

def pop():
    temp=stack[-1]
    stack.pop()
    print(temp,"is pop")

while True:
    print("1-Display")
    print("2-push")
    print("3-pop")
    a=int(input("What you want to do?(1/2/3): "))
    if a==1:
        display()
    elif a==2:
        push()
    elif a==3:
        pop()

#Q.5|
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        print(item,"is enqueue")

    

    def display(self):
        print("Queue:", self.queue)


# Example usage
queue = Queue()

while True:
    print("1-enqueue")
    print("2-display")
    a=int(input("Enter what you want to do?(1/2): "))
    
    if a==1:
        queue.enqueue(int(input("Enter the number: ")))
    
    elif a==2:
        queue.display()'''

#Q.6|
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        print(item,"is enqueue.")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
        

    
    def display(self):
        print("Queue:", self.queue)



queue = Queue()
while True:
    print("1-enqueue")
    print("2-display")
    print("3-dequeue")
    a=int(input("Enter what you want to do?(1/2/3): "))
    
    if a==1:
        queue.enqueue(int(input("Enter the number: ")))
    
    elif a==2:
        queue.display()
    
    elif a==3:
        queue.dequeue()
        print("data is dequeue")






   
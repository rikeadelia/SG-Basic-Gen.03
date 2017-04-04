class Stack:

     def __init__(self):
          self.items = []  
     def isEmpty(self):
          return self.items == []  
     def push(self, item):
          self.items.append(item)  
     def pop(self):
          return self.items.pop()  
     def peek(self):
          return self.items[len(self.items)-1]  
     def size(self):
          return len(self.items)

s = Stack()
word = "()(()())"
i = 0;
for each in word:
	if(each == "("):
		s.push(each)
	elif(each == ")"):
		if(s.isEmpty()):
			break
		else:
			s.pop()
	i+=1;

if(s.isEmpty() and i==len(word)):
	print ("VALID")
else:
	print ("TIDAK VALID")
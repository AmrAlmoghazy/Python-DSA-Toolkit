class Array:
    def __init__(self, capacity):
        self.length= 0          
        self.capacity =capacity      
        self.array =[None]*self.capacity  

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        if idx < 0 or idx >= self.length:
            print("Index out of range")
        return self.array[idx]

    def append(self, value):
        if self.length == self.capacity:
            print("array is full")
            return None
        self.array[self.length] = value
        self.length+= 1

    def pop(self):
        if self.length== 0:
            print("empty array")
        val= self.array[self.length-1]
        self.array[self.length-1] = None  
        self.length-= 1
        return val

    def __str__(self):
        return "[" + ", ".join(str(self.array[i]) for i in range(self.length)) + "]"


arr = Array(5)
arr.append(1)
arr.append(2)
arr.append(3)
print(arr)  # Output: [1, 2, 3]
arr.pop()
print(arr)  # Output: [1, 2]

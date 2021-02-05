class calculator:
    def __init__(self, num):
        self.result = num
    def add(self, num):
        self.result += num
        return self.result
    
    def min(self, num):
        self.result -= num
        return self.result
    
    def div(self, num):
        self.result = self.result/ num
        return self.result
    
    def mul(self, num):
        self.result = self.result*num
        return self.result

def hello():
    print("hello ")
    
if __name__ == '__main__':
    print("hello")
    
    
    
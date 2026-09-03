class MinStack(object):
    def __init__(self):
        self.array = []
        self.array_2 = []


    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.array.append(value)
        if len(self.array_2) == 0:
            self.array_2.append(value)
        else:
            if value <= self.array_2[-1]:
                self.array_2.append(value)

    def pop(self):
        """
        :rtype: None
        """
        a = self.array[-1]
        self.array.pop()
        b = self.array_2[-1]
        if a == b:
            self.array_2.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.array[-1]
    def getMin(self):
        """
        :rtype: int
        """
        return self.array_2[-1]  


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin(

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
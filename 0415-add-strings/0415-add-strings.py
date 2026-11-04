class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        n = max(len(num1), len(num2))

        num1 = num1.zfill(n) 
        num2 = num2.zfill(n)      

        carry = 0
        result = ""

        for i in range(n-1, -1, -1):
            total = int(num1[i]) + int(num2[i]) + carry
            carry = total // 10
            result = str(total % 10) + result 

        if carry != 0:
            result =  str(carry) + result 

        return result 
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
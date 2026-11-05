class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        m = len(num1)
        n = len(num2)
        arr = (m+n)*[0]
    
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                d1 = ord(num1[i]) - ord('0')
                d2 = ord(num2[j]) - ord('0')
                p1 = i + j
                p2 = i + j + 1

                total = d1 * d2 + arr[p2]
                arr[p1] += total // 10
                arr[p2] = total % 10
        s = ""
        for nemo in arr:
            s = s + str(nemo)       

        s = s.lstrip('0')         

        if s == "":
            return "0"
        return s



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
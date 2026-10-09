class Solution(object):

    def mark_inf(self, matrix, row, col, r, c):
        for i in range(r):
            if matrix[i][col] != 0:
                matrix[i][col] = float('inf')
        for j in range(c):
            if matrix[row][j] != 0:
                matrix[row][j] = float('inf')

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None
        """

        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(c):

                if matrix[i][j] == 0:
                    self.mark_inf(matrix, i, j, r, c)

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
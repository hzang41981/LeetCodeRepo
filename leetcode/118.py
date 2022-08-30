from collections import deque
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1,numRows):
            ttl = i + 1
            line = [1 for _ in range(ttl)]
            for j in range(1, ttl-1):
                line[j] = res[-1][j-1] + res[-1][j]
            res.append(line)
        return res

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return root
        res = []
        stack = deque()
        stack.append(root)
        left_to_right = True
        while stack:
            len_s = len(stack)
            line = []
            for i in range(len_s):
                line.append(stack.val)
                curr = stack.pop_left()
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
            if left_to_right:
                res.append(line)
            else:
                res.append(reversed(line))
            left_to_right = not left_to_right
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
# Last updated: 8/4/2025, 10:46:23 PM
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # O(n), O(n)
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node, cur_max, cur_min):
            if not node:
                return cur_max - cur_min

            # Update the current path's maximum and minimum
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)

            # Recurse into the left and right children
            left_diff = dfs(node.left, cur_max, cur_min)
            right_diff = dfs(node.right, cur_max, cur_min)

            # Return the maximum difference found in either subtree
            return max(left_diff, right_diff)

        # Initial call to dfs with the root's value as both max and min
        return dfs(root, root.val, root.val)
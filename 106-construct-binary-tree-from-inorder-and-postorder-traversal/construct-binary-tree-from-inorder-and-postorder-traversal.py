class Solution:
    def buildTree(self, inorder, postorder):
        # Map value -> index in inorder
        index = {value: i for i, value in enumerate(inorder)}

        def build(in_left, in_right):
            if in_left > in_right:
                return None

            # Last element in postorder is the root
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # Find root's position in inorder
            mid = index[root_val]

            # Build right subtree first because we are
            # consuming postorder from the end.
            root.right = build(mid + 1, in_right)
            root.left = build(in_left, mid - 1)

            return root

        return build(0, len(inorder) - 1)
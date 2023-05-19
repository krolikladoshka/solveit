class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []

        for file in path.split('/'):
            if file == '':
                continue
            if file == '..':
                if path_stack:
                    path_stack.pop()
            elif file == '.':
                continue
            else:
                path_stack.append(file)

        return f'/{"/".join(path_stack)}'

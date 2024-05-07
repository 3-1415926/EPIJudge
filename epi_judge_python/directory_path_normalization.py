from test_framework import generic_test


SEP = "/"

def shortest_equivalent_path(path: str) -> str:
    stack = []
    if path.startswith(SEP):
        stack.append("")
    for part in path.split(SEP):        
        if part == "..":
            if not stack or stack[-1] == "..":
                stack.append(part)
            elif not stack.pop():
                raise ValueError()
        elif part and part != ".":
            stack.append(part)
    return SEP.join(stack) if stack != [""] else SEP


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))

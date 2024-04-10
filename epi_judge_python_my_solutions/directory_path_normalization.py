from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    stack = []
    if path.startswith('/'):
        stack.append('')
    for p in path.split('/'):
        if p in ('', '.'):
            continue
        if p == '..' and len(stack) > 0 and stack[-1] not in ('', '..'):
            stack.pop()
        else:
            stack.append(p)
    if len(stack) == 1 and stack[0] == '':
        stack[0] = '/'
    return '/'.join(stack)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))

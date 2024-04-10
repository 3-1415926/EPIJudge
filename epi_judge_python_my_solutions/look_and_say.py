from test_framework import generic_test


def look_and_say(n: int) -> str:
    if n <= 0: return ''
    result = '1'
    for _ in range(1, n):
        new_result = []
        start = 0
        for i in range(len(result)):
            if result[i] != result[i+1:i+2]:
                new_result.append(str(i + 1 - start) + result[start])
                start = i + 1
        result = ''.join(new_result)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))

from testCases import *


def main():
    result = 0
    result += test_the()
    result += test_num()
    result += test_sym()
    result += test_bignum()
    result += test_data()
    result += test_stats()
    print(result, " tests failed")
    print(6 - result, " tests passed")
    return result


if __name__ == '__main__':
    main()

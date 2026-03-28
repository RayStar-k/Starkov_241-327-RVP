def wrapper(f):
    def fun(l):
        normalized = []
        for phone in l:
            digits = ''.join(filter(str.isdigit, phone))
            if len(digits) == 11:
                digits = digits[1:]
            elif len(digits) == 10:
                pass
            else:
                digits = digits[-10:]
            formatted = f"+7 ({digits[:3]}) {digits[3:6]}-{digits[6:8]}-{digits[8:]}"
            normalized.append(formatted)
        return f(normalized)
    return fun

@wrapper
def sort_phone(l):
    return sorted(l)

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    print(*sort_phone(l), sep='\n')

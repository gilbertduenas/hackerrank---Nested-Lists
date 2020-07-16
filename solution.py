# frankencode....

if __name__ == '__main__':
    roster = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())

        roster[name] = score

    last = min(roster, key=roster.get)
    roster.pop(last) 

    second = min(roster.values())
    second_to_last = sorted([k for k, v in roster.items() if v == second])

    for i in second_to_last:
        print(i)

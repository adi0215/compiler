import collections

ss = set()
mp = collections.defaultdict(list)
f = {}
g = collections.defaultdict(list)
num = -1


def dfs(i, org, last, mp):
    global ss
    rtake = False
    for r in mp[i]:
        take = True
        for s in r:
            if s == i:
                break
            if not take:
                break
            if not ('A' <= s <= 'Z') and s != 'e':
                ss.add(s)
                break
            elif s == 'e':
                if org == i or i == last:
                    ss.add(s)
                rtake = True
                break
            else:
                take = dfs(s, org, r[-1], mp)
                rtake |= take
    return rtake


def dfs2(c, way, last, curr):
    global f, g, num
    
    mp2 = collections.defaultdict(set)
    rep = -2
    if last != -1:
        for q in g[last]:
            if q[1] == way:
                rep = q[0]
                mp2 = f[q[0]]
    flattened_curr = [item for sublist in curr for item in sublist]
    mp2[c].add(tuple(flattened_curr))

    
    count = 10
    while count > 0:
        for key, value in mp2.items():
            for r in value:
                if isinstance(r, list) and len(r) > 1 and r[1]:
                    if r[1][0] >= 'A' and r[1][0] <= 'Z':
                        for s in mp[r[1][0]]:
                            st, emp = list(s), []
                            value.add((emp, st))
        count -= 1

    for key, value in f.items():
        if value == mp2:
            g[last].append((key, way))
            return

    if rep == -2:
        num += 1
        f[num] = mp2
        if last != -1:
            g[last].append((num, way))
    else:
        f[rep] = mp2

    cc = num
    for key, value in mp2.items():
        for r in value:
            if isinstance(r, list) and len(r) > 1 and r[1]:
                r[0].append(r[1][0])
                r[1].popleft()
                if r[1]:
                    dfs2(key, r[0][-1], cc, r)


def main():
    global ss, mp, num
    g={}
    start = ''
    flag = False

    print("Grammar:")

    with open("ourgrammer.txt", "r") as fin:
        for line in fin:
            if not flag:
                start = line[0]
                flag = True
            print(line)

            temp = []
            s = line[0]
            for i in range(3, len(line)):
                if line[i] == '|':
                    mp[s].append(temp)
                    temp = []
                else:
                    temp.append(line[i])
            mp[s].append(temp)

    fmp = collections.defaultdict(set)
    
    for key, value in mp.items():
        ss.clear()
        dfs(key, key, key, mp)
        for x in ss:
            fmp[key].add(x)
    # print(type(g))
    print("\nFIRST:")
    for key, value in fmp.items():
        ans = f"{key} = {{{', '.join(value)}}}"
        print(ans)

    gmp = {start: {'$'}}
    count = 10

    for key, value in mp.items():
        for r in value:
            for i in range(len(r) - 1):
                if 'A' <= r[i] <= 'Z':
                    if not ('A' <= r[i + 1] <= 'Z'):
                        gmp.setdefault(r[i], set()).add(r[i + 1])
                    else:
                        temp = r[i + 1]
                        j = i + 1
                        while 'A' <= temp <= 'Z':
                            if 'e' in fmp[temp]:
                                for g in fmp[temp]:
                                    if g == 'e':
                                        continue
                                    gmp[r[i]].add(g)
                                j += 1
                                if j < len(r):
                                    temp = r[j]
                                    if not ('A' <= temp <= 'Z'):
                                        gmp[r[i]].add(temp)
                                        break
                                else:
                                    for g in gmp[key]:
                                        gmp[r[i]].add(g)
                                    break
                            else:
                                for g in fmp[temp]:
                                    gmp[r[i]].add(g)
                                break

                if 'A' <= r[-1] <= 'Z':
                    for g in gmp[key]:
                        gmp[r[i]].add(g)

    print("\nFOLLOW:")
    for key, value in gmp.items():
        ans = f"{key} = {{{', '.join(value)}}}"
        print(ans)

    temp = "." + start
    emp, st = [], [start]
    dfs2('!', 'k', -1, (emp, st))

    print("\nProductions:")
    cc = 1
    action, go = set(), set()
    pos = {}

    for key, value in mp.items():
        go.add(key)
        for r in value:
            print(f"r{cc}: {key} -> {''.join(r)}")
            temp = []
            for s in r:
                temp.append(s)
                if 'A' <= s <= 'Z':
                    go.add(s)
                else:
                    action.add(s)
            pos[(key, tuple(temp))] = cc
            cc += 1

    print("\nGraph:")
    for key, value in f.items():
        print(f"\nI{key}:")
        for k, v in value.items():
            for r in v:
                if len(r) >= 2:
                    ans = f"{k} -> {''.join(r[0])}.{''.join(r[1])}|"
                else:
                    ans = f"{k} -> {''.join(r[0])}|"

                ans = ans.replace('!', start + "'")
                print(ans[:-1])

    print("\nEdges:")
    # print(type(g))
    for key, value in g.items():
        for r in value:
            print(f"I{key} -> {r[1]} -> I{r[0]}")

    action.add('$')
    print("\nParsing Table:")
    print("St.\t\tAction & Goto")

    tot = len(f)
    print("\t", end="")
    for q in action:
        print(q, end="\t")
    for q in go:
        print(q, end="\t")
    print()

    for i in range(tot):
        print(f"I{i}\t", end="")
        for q in action:
            if i in g:
                flag = False
                for r in g[i]:
                    if r[1] == q:
                        print(f"S{r[0]}\t", end=" ")
                        flag = True
                        break
                if not flag:
                    print(" - \t", end="")
            else:
                flag = False
                for r in f[i]:
                    if len(r) > 1:
                        print(f"r[1]: {r[1]}")
                        if len(r[1]) > 0 and '!' in r[1][0]:
                            # Your code here

                            if q == '$':
                                print("AC\t", end=" ")
                                flag = True
                            else:
                                print("-\t", end="")
                if not flag:
                    for r in f[i]:
                        ccc = r[0]
                        if len(r) > 1 and len(r[1]) > 0:
                            chk = r[1][0]
                            # Rest of your code

                        cou = 1
                        if ccc in gmp:
                            for r in gmp[ccc]:
                                if q == r:
                                    print(f"r{pos[(ccc, chk)]}\t", end=" ")
                                cou += 1
        for q in go:
            if i in g:
                flag = False
                for r in g[i]:
                    if r[1] == q:
                        print(f"{r[0]}\t", end=" ")
                        flag = True
                        break
                if not flag:
                    print("-\t", end="")
            else:
                print(" - \t", end="")
        print()


if __name__ == "__main__":
    main()

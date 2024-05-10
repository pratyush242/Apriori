
def items_maker(prev_f, k):
    from itertools import combinations
    
    items = []
    s = len(prev_f)
    for i in range(s):
        for j in range(i + 1, s):
            if prev_f[i][:k - 2] == prev_f[j][:k - 2]:
                jointy = sorted(set(prev_f[i]) | set(prev_f[j]))
                flag = True
                for part in combinations(jointy, k - 1):
                    if k == 2:
                        if list(sorted(part))[0] not in prev_f:
                            flag = False
                            break
                    else:
                        if list(sorted(part)) not in prev_f:
                            flag = False
                            break
                if flag:
                    items.append(jointy)
    print(items)
    return items

def apriori(filename, minsup):
    transactions = []
    with open(filename, 'r') as file:
        apriori_result = {1:{"c":{},"f":{}}}
        
        transactions = []
        for line in file:
            transaction = set()
            for item in line:
                if ord("A")<=ord(item)<=ord("Z"):
                    transaction.add(item)
                    apriori_result[1]["c"][item] = apriori_result[1]["c"].get(item,0)+1


            if transaction:
                transactions.append(transaction)
        newd = {}
        for i,j in apriori_result[1]["c"].items():
            if apriori_result[1]["c"][i]>=minsup:
                newd[i] = j
        apriori_result[1]["f"] = newd
    k = 2

    print(transactions)
    meow = list(apriori_result[1]['f'].keys())
    while True:
        
        items = items_maker(meow,k)
        valid_items = {}
        for item in items:
            key = ""
            for m in item:
                key+=m
            valid_items[key] = 0
        for transaction in transactions:
            for item in items:
                if set(item).issubset(transaction):
                    key = ""
                    for m in item:
                        key+=m
                    valid_items[key] += 1
        if not valid_items:
            break
        d = {}
        for i,j in valid_items.items():
            if j>=minsup:
                d[i] = j
        
        meow = []
        for i in d:
            g = []
            for j in i:
                g.append(j)
            meow.append(g)    
        hello = {"c":valid_items,"f":d}
        apriori_result[k] = hello    

        k+=1
    return apriori_result
    
# filename = "/Users/pratyushthakur/Downloads/hw5_sample_input_1.txt"
# print(apriori(filename, 3))

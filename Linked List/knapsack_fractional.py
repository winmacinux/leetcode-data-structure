class Item:
    def __init__(self, wt, val, index):
        self.wt = wt
        self.val = val
        self.index = index
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost


def getMaxValue(C, wt, val):

    items = []
    for i in range(len(wt)):
        items.append(Item(wt[i], val[i], i))

    # sorting items by cost
    items.sort(reverse=True)

    totalValue = 0
    
    for item in items:
        curWt = int(item.wt)
        curVal = int(item.val)
        if C - curWt >= 0:
            C -= curWt
            totalValue += curVal
        else:
            fraction = C / curWt
            totalValue += curVal * fraction
            C = int(C - (curWt * fraction))
            break
    return totalValue

# Driver Code
if __name__ == "__main__":
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    C = 50
    result = getMaxValue(C, wt, val)
    print(result)
    pass



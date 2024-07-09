import sys


def achieve_max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            max_profit = max(max_profit, prices[i] - min_price)
    return max_profit


def main():
    input = sys.stdin.read
    data = input().strip()
    prices = list(map(int, data[data.index('[') + 1:data.index(']')].split(',')))
    p = achieve_max_profit(prices)
    print(p)


if __name__ == "__main__":
    main()

# Time Complexity
# O(N): We only iterate through the list of prices once. 
# Space Complexity
# O(1): We use only a few extra variables (min_price, max_profit), regardless of the input size.

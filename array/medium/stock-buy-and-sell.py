def stock_buy_and_sell(nums):
    max_profit = 0
    min_price = float('inf')
    for i in range(len(nums)):
        min_price = min(min_price, nums[i])
        max_profit = max(max_profit, nums[i] - min_price)
    return max_profit


if __name__ == '__main__':
    nums1, nums2 = [7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]
    print(stock_buy_and_sell(nums1))
    print(stock_buy_and_sell(nums2))

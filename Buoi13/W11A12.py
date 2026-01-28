def maximumProduct(path: str) -> int:
    with open(path, 'r', encoding='utf-8') as f:
        n = int(f.readline().strip())
        nums = list(map(int, f.readline().split()))

    nums.sort()

    product1 = nums[-1] * nums[-2] * nums[-3]

    product2 = nums[0] * nums[1] * nums[-1]

    return max(product1, product2)

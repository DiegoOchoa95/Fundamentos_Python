def find_max(nums):
    max_num = float(-99999999999999) # smaller than all other numbers
    for num in nums:
        if num > max_num:
            num=max_num
         
    return max_num



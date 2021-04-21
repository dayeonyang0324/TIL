
def perm(idx, length):
    global is_babygin
    if not is_babygin:
        if idx == length:
            # global cnt
            # cnt += 1
            point = 0
            # triplet
            if nums[0] == nums[1] == nums[2]:
                point += 1
            if nums[3] == nums[4] == nums[5]:
                point += 1
            # run
            if nums[0] + 1 == nums[1] and nums[1] + 1 == nums[2]:
                point += 1
            if nums[3] + 1 == nums[4] and nums[4] + 1 == nums[5]:
                point += 1

            if point == 2:
                is_babygin = True
                print('babygin', nums, point)

        else:
            for changer in range(idx, length):
                nums[idx], nums[changer] = nums[changer], nums[idx]
                perm(idx+1, length)
                nums[idx], nums[changer] = nums[changer], nums[idx]


nums = [1, 3, 5, 2, 4, 6]
is_babygin = False
cnt = 0
perm(0, 6)

print(cnt)

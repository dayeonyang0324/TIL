#연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
#해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면 YYYY/MM/DD형식으로 출력하고,
#날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
T = int(input())
for tc in range(1, T+1):
    nums = input()
    year = int(nums[0:4])
    month = int(nums[4:6])
    day = int(nums[6:8])
    
    #다른 문제들과 다르게 변수가 3개이지만 한개라도 만족하지 못하면 -1을 반환해야하므로 
    #tc 값을 먼저 프린트한 후 앞으로 나올 값들을 연달아 프린트하는 방식으로 구해야 한다. 
    print("#%d " %(tc), end = '')
    
    #프린트 값에서 0111과 같이 0이 앞에 있으면 format문에서는 0을 제외한 111만 프린트 되었다.
    #%을 사용해서 자릿수를 4로 정해줘야해서 애를 먹었다. 
    if 1 <= month <= 12:
        if month == 2:
            if 28 >= day >= 1:
                print("%.4d/%.2d/%.2d" % (year, month, day))
            else:
                print(-1)
        elif month == 4 or month == 6 or month == 9 or month == 10:
            if 30 >= day >= 1:
                print("%.4d/%.2d/%.2d" % (year, month, day))
            else:
                print(-1)
        else:
            if 31 >= day >= 1:
                print("%.4d/%.2d/%.2d" % (year, month, day))
            else:
                print(-1)
    else:
        print(-1)
        
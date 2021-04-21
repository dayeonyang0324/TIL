arr = [1, 2, 4]
print(arr[1])
arr[1] = 4
print(arr)

str1 = '123'
str1[1] = '4'
#오류남

str1.replace('1','4')
#변화는 하지만 다시 str1을 프린트하면 바뀌지 않고 그대로임

str1.split('2')
#2를 기준으로 나눠지고 리스트에 들어가서 반환됨
#['1', '3']


#ord('0') = 48, ord('A') = 65, ord('a') = 97

line2 = '안녕하세여'
print(line2.find('녕')) #오류없이 -1값 반환
print(line2.index('녕')) #없으면 오류
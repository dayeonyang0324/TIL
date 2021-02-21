### 1. 문서 불러와서 데이터 추출하기

문서 입력 

```
새로운 변수명 지정 = open('폴더/파일명', encoding='utf-8')
```

json을 dict로 바꾸기

```
imiport json
music_dict = json.load(새로운 변수명)
```

```
import pprint
pprint.pprint(music_dict)
```

dict의 key값 접근 : 변수명[''], .grt('')

```
singer = music_dict['singer'] 
title = music_dict.get('title')
```

함수 만들기

```
def music_info(music_dict):
    result = {}
    singer = music_dict['singer'] 
    title = music_dict.get('title')
    
    result['singer'] = singer
    result['title'] = title
    return result

music_info(music_dict)
```

```
#코드 정리



# data 폴더 안에 들어있는 music.json 파일 여는 코드
새로운 변수명 지정 = open('data/music.json', encoding='utf-8')
# 불러온 json을 파이썬에서 쓸 수 있도록 dict로 변환
music_dict = json.load(새로운 변수명)


def music_info(music_dict):
    #결과값 반환을 위한 dict구조
    result = {}
    
    #인자로 들어온 music_dict에서 원하는 데이터만 추출
    sin = music_dict['singer'] 
    tit = music_dict.get('title')
    
    #결과값 dict에 데이터를 구조화. [내가 원하는 키값] = 가져온 데이터
    result['singer'] = sin
    result['title'] = tit
    return result

music_info(music_dict) # 결과는 {싱어:, 타이틀:이 딕셔너리 형태로 나옴}
```



### 2. 리스트 내의 데이터 여러개 딕셔너리로 추출하기

```
import json
import pprint

새로운 변수명 지정 = open('data/musicㄴ.json', encoding='utf-8')
musics_list = json.load(새로운 변수명)

def music_info(musics_list):
    result = []
    for music in musics_list:
        info = {}
        singer = music.get('singer')
        title = music.get('title')
        info['singer'] = singer
        info['title'] = title
        
        result += [info]
    
    
    
mucic_info(musics_list) #결과로 리스트[] 안에 {}여러개의 딕셔너리가 존재함

```


## 클래스를 활용한 url 만들기

- request를 활용해보기

```python
import requests

from pprint import pprint
url = '~'

response = requests.get(url)
response_dict = response.json()
```

- request를 통해 클래스를 만들고 함수를 활용해보기

```python
import requests

#클래스를 만들어준다
class URLMarker():
    base_url = '~'
    
    #생성자는 key값으로 주어준다
    def __init__(self, key):
        self.key = key
        
    #get_url함수를 만들어준다    
    def get_url(self, category, feature, **kwargs):
        #카테고리와 피쳐를 필수적인 값으로 받아오고 kwargs를 통해 다른 요소등를 받아 올 수 있다. 그런 후 키값을 더해준다
        url = f'{URLMaker.base_url}/{category}/{feature}'
        url += f'?api_key={self.key}'
        
        #kwargs의 경우 해당하는 키벨류를 나열하여 하나씩 뒤에 더해준다
        for k, v in kwargs.items():
            url += f'&{k}={v}'
        #url을 출력한다.
        return url
    
    
    #영화의 id로 제목을 불러올 수 있는 함수 생성
    def movie_id(self, title):
        #위에서 만든 get_url함수를 사용해서 새로운 값을 지정한다. 마지막에 타이틀값을 추가해준다
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
        
        #받은 url을 제이슨을 사용해서 딕셔너리 형태로 만들어준다
        res = requests.get(url)
        #print(type(res.json())) #dict로 바꿔줌 .text쓰면 str이라고 나옴
        movie_dict = res.json()
        
        #받은 딕셔너리에서 id를 뽑아오는데 이 위치는 results의 첫번쩨 항목의 id에 해당하는 key를 불러온다.
        if movie_dict.get('results'):
            return movie_dict.get('results')[0].get('id')
        else:
            return None
        
#클래스 생성자에 들어갈 키값을 설정한다.      
maker = URLMarker('키값')        
print(maker.get_url('movie','top_rated', region='KR'))
print(maker.movie_id('기생충'))

```

```python
#위에서 만든 클래스를 불러온다
import requests
from 파일 import URLMaker
from pprint import pprint

#목록에서 제목들만 뽑아오는 함수를 만든다
def top_rated_movie():
    maker = URLMaker('키값입력')
    url = maker.get_url('movie', 'top_rated')
    res = requests.get(url)
    movie_dict = res.json()
    
    movie_list = movie_dict.get('results')
    
    result = []
    for movie in movie_list:
        result.append(movie.get('title')
    return result
    
print(top_rated_movie) #제목만 뽑아오는 함수
```


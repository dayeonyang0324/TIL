### 프로그래머스 MySQL 풀이 - String, Date

<hr>

- 루사와 엘라 찾기

  - `in` 을 사용해 목록의 포함여부를 확인할 수 있다.

```sql
SELECT ANIMAL_ID, NAME,	SEX_UPON_INTAKE FROM ANIMAL_INS
WHERE NAME in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID;
```

- 이름에 el이 들어가는 동물 찾기

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE NAME LIKE '%el%' and ANIMAL_TYPE = 'Dog'
ORDER BY NAME;
```

- 중성화 여부 파악하기
  - if절 (조건, 참일떄, 거짓일때)

```sql
SELECT ANIMAL_ID, NAME, if(sex_upon_intake like 'Intact%', 'X', 'O')
from ANIMAL_INS 
order by ANIMAL_ID;
```

- 오랜 기간 보호한 동물(2)
  - 시간도 연산자를 통해 계산할 수 있다.

```sql
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME FROM ANIMAL_OUTS 
JOIN ANIMAL_INS
ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID

ORDER BY ANIMAL_OUTS.DATETIME - ANIMAL_INS.DATETIME DESC
LIMIT 2;
```

- DATETIME에서 DATE로 형 변환
  - `DATE_FORMAT(칼럼명 or now() ,'%Y-%m-%d') ` 을 사용해 `년-월-일 시-분-초`를 `년-월-일`로 바꿀 수 있다.

```sql
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS '날짜' FROM ANIMAL_INS 
ORDER BY ANIMAL_ID;
```


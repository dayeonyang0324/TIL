### 프로그래머스 MySQL 풀이 - GROUP BY

<hr>

- 고양이와 개는 몇 마리 있을까

```sql
SELECT ANIMAL_TYPE, count(ANIMAL_TYPE) FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC;
```

- 동명 동물 수 찾기
  - NULL 값을 찾기 위해서는 `IS NOT`를 사용해야 한다.
  - `WHERE`과 `HAVING ` 차이
    - WHERE :: WHERE는 항상 from 테이블 뒤에 위치하여 모든 칼럼에 적용되고, 조건에는 비교연산자를 사용하여 구체적인 조건을 줄 수 있다.
    - HAVING :: HAVING은 group by 뒤에 위치하여 그룹화 된 상태의 조건을 줄때 사용한다. 마찬가지로 비교연산자를 사용해 구체적인 조건을 줄 수 있다.

```sql
SELECT NAME, COUNT(NAME) FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME ASC;
```

- 입양 시각 구하기(1)
  - GROUP BY > HAVING
  - DATETIME(년-월-일 시-분-초)의 특정한 영역을 가져오는 방법 :: YEAR(DATETIME), DAY(DATETIME), HOUR(DATETIME), MINUTE(DATETIME)

```sql
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR BETWEEN 9 AND 19
ORDER BY HOUR;
```

- 입양 시각 구하기(2)
  - NULL값이 아닌 아예 없는 행을 추가하기 위해서는 하나의 테이블을 만들어 `join`해야한다. 
  - `WITH RECURSIVE` 을 사용하여 `SELECT`를 통해 테이블을 만들고 `join`을 당하게(?) 만들면 된다

```sql
WITH RECURSIVE cte AS
    (
      SELECT 0 AS HOUR
      UNION ALL
      SELECT HOUR + 1 FROM cte WHERE HOUR < 23
    )

SELECT cte.HOUR AS HOUR, count(ANIMAL_ID) AS COUNT FROM cte
LEFT JOIN ANIMAL_OUTS 
ON cte.hour = HOUR(ANIMAL_OUTS.DATETIME)
GROUP BY HOUR;
```


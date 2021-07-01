### 프로그래머스 MySQL 풀이 - SUM, MAX, MIN

<hr>

- 최댓값 구하기

```sql
SELECT DATETIME FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1;
```

- 최솟값 구하기

```sql
SELECT DATETIME FROM ANIMAL_INS
ORDER BY DATETIME ASC
LIMIT 1;
```

- 동물 수 구하기

```sql
SELECT count(*) FROM ANIMAL_INS;
```

- 중복 제거하기

```sql
# distinct 하면 중복제거 & null 값 제거된다
SELECT count(DISTINCT(NAME)) FROM ANIMAL_INS;
```


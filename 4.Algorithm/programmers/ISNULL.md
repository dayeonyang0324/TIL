### 프로그래머스 MySQL 풀이 - IS NULL

<hr>

- 이름이 없는 동물의 아이디

```sql
SELECT ANIMAL_ID FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID ASC;
```

- 이름이 있는 동물의 아이디

```sql
SELECT ANIMAL_ID FROM ANIMAL_INS
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID ASC;
```

- NULL 처리하기
  - `IFNULL(칼럼명, 바꿀내용)`을 사용하여 NULL 값을 대체할 수 있다.

```sql
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE FROM ANIMAL_INS;
```




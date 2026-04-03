-- 코드를 입력하세요
SELECT book_id, date_format(published_date, '%Y-%m-%d') as published_date
from book
WHERE CATEGORY = '인문' AND YEAR(PUBLISHED_DATE) = 2021
order by published_date asc;
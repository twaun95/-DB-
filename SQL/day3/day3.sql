--4장 단일행 함수(SINGLE ROW FUNCTION) : 1개의 입력->1개의 결과 P.141

--문자함수(UPPER, LOWER, INITCAP, CONCAT, 
--UPPER, LOWER
SELECT LAST_NAME, UPPER(LAST_NAME)
FROM EMPLOYEES
WHERE EMPLOYEE_ID=200;

SELECT LAST_NAME, UPPER(LAST_NAME)
FROM EMPLOYEES
WHERE LAST_NAME = 'Whalen';

SELECT LAST_NAME, UPPER(LAST_NAME)
FROM EMPLOYEES
WHERE LAST_NAME = 'WHALEN';

SELECT LAST_NAME, UPPER(LAST_NAME)
FROM EMPLOYEES
WHERE UPPER(LAST_NAME) = 'WHALEN';

SELECT LAST_NAME, LOWER(LAST_NAME)
FROM EMPLOYEES
WHERE LOWER(LAST_NAME) = 'whalen';


--INITCAP(첫 글자 대문자)
SELECT INITCAP('NEW YEAR') FROM DUAL;


--CONCAT(합쳐주기) 단, 두개만 가능! 3개
SELECT FIRST_NAME, LAST_NAME, CONCAT(FIRST_NAME, LAST_NAME) AS NAME 
FROM EMPLOYEES;

SELECT CONCAT('A', 'B') AS NAME FROM DUAL;
SELECT CONCAT('A', 'B', 'C') AS NAME FROM DUAL;
SELECT 'A'||'B'||'C' AS NAME FROM DUAL;


--SUBSTR(문자열 뽑아내기) (A,1,2) 인수 A의 1번째부터 2개를 뽑아내기
SELECT LAST_NAME, SUBSTR(LAST_NAME,3,2) AS NAME
FROM EMPLOYEES
WHERE EMPLOYEE_ID=200;
-- (-값)은 뒤에서부터 시작
SELECT LAST_NAME, SUBSTR(LAST_NAME,-3,2) AS NAME
FROM EMPLOYEES
WHERE EMPLOYEE_ID=200;

SELECT LAST_NAME, SUBSTR(LAST_NAME,-3,2) AS NAME
FROM EMPLOYEES
WHERE SUBSTR(LAST_NAME,3,2) = 'al';


--LENGTH(글자수) , 스페이스 포함, NULL은 사용x
SELECT LAST_NAME, LENGTH(LAST_NAME) AS NAME
FROM EMPLOYEES
WHERE EMPLOYEE_ID=200;

SELECT LENGTH('ABC DE') FROM DUAL;


--INSTR(검색기능) (A,'a',2,3) A문자의 2번째부터 시작해서 3번째로 a가 나오는 위치
SELECT LAST_NAME, INSTR(LAST_NAME, 'a',2,1) AS NAME
FROM EMPLOYEES
WHERE DEPARTMENT_ID=30;


--LPAD (전체길이 정해주고 왼쪽을 패딩)
SELECT LAST_NAME, LPAD(LAST_NAME, 10,'*')
FROM employees
WHERE DEPARTMENT_ID=30;

--RPAD
SELECT LAST_NAME, RPAD(LAST_NAME, 10,'*')
FROM employees
WHERE DEPARTMENT_ID=30;


--TRIM(잘라내기) -중간은 안됨
SELECT TRIM(LEADING 'A' FROM 'ABCDEFGA') FROM DUAL; --맨앞
SELECT TRIM(TRAILING 'A' FROM 'ABCDEFGA') FROM DUAL; --끝
SELECT TRIM(BOTH 'A' FROM 'ABCDEFGA') FROM DUAL; --맨앞,끝


--REPLACE
SELECT REPLACE('ABCAEFGA','A','Z') FROM DUAL;
SELECT REPLACE('ABCAEFGA','A','') FROM DUAL;
SELECT LENGTH(REPLACE('ABCAEFGA','A','')) FROM DUAL;



--숫자함수

--ROUND 소수 몇째 짜리까지 반올림
SELECT ROUND(123.4567, 2) FROM DUAL;
SELECT ROUND(654.321, -2) FROM DUAL;
SELECT ROUND(123.4567, 0) FROM DUAL;
SELECT ROUND(123.4567) FROM DUAL;

--TRUNC(반올림 말고 그냥 날리기)
SELECT TRUNC(123.4567, 2) FROM DUAL;
SELECT TRUNC(654.321, -2) FROM DUAL;
SELECT TRUNC(123.4567, 0) FROM DUAL;
SELECT TRUNC(123.4567) FROM DUAL;

--MOD(나머지)
SELECT MOD(15,2) FROM DUAL;

--CEIL(해당 수보다 큰 최소 정수값)
SELECT CEIL(5.3) FROM DUAL;

--FLOOR(해당 수보다 작은 최대 정수값)
SELECT FLOOR(5.3) FROM DUAL;

--시간포맷 변경( 연도 : RRRR,YYYY의 차이)

ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY/MM/DD';
SELECT SYSDATE FROM DUAL;

SELECT EMPLOYEE_ID, LAST_NAME, HIRE_DATE
FROM EMPLOYEES
WHERE HIRE_DATE >= '2004/03/01';


SELECT SESSIONTIMEZONE, CURRENT_DATE FROM DUAL;
-- SYSDATE를 이용한 현재 날짜는 데이타베이스 시스템이 설치가 되어 있는 장소의 현재 날짜.
-- CURRENT_DATE는 SQL 작업을 하고 있는 사용자가 있는 장소의 현재 날짜.

SELECT LAST_NAME, (SYSDATE-HIRE_DATE)/7 AS WEEK
FROM EMPLOYEES
WHERE DEPARTMENT_ID = 90;

SELECT LAST_NAME, TO_CHAR(HIRE_DATE,'YYYY/MM/DD HH24:MI:SS'), TO_CHAR(HIRE_DATE+1/24/60/60,'YYYY/MM/DD HH24:MI:SS')
FROM EMPLOYEES
WHERE DEPARTMENT_ID = 90;

--MONTH_BETWEEN(월수 차이)
SELECT HIRE_DATE, MONTHS_BETWEEN(SYSDATE, HIRE_DATE) FROM EMPLOYEES
WHERE DEPARTMENT_ID = 90;

--ADD_MONTHS
SELECT EMPLOYEE_ID, HIRE_DATE, ADD_MONTHS(HIRE_DATE,5) FROM EMPLOYEES
WHERE department_id = 90;

SELECT ADD_MONTHS(SYSDATE,5) AS "AFTER 5M" FROM DUAL;

--NEXT_DAY(해달날짜 다음에 오는 요일의 날짜)
SELECT NEXT_DAY('2020/12/31','목') FROM DUAL;

--LAST_DAY(그 달의 마지막 날짜)
SELECT LAST_DAY('2020/9/2') FROM DUAL;
--날짜를 반올림 (YEAR:6개월기준/MONTH:15일 기준)
SELECT ROUND(TO_DATE('2020/05/16', 'YYYY/MM/DD'), 'MONTH') FROM DUAL;
SELECT ROUND(TO_DATE('2020/05/15', 'YYYY/MM/DD'), 'MONTH') FROM DUAL;
SELECT ROUND(TO_DATE('2020/05/15', 'YYYY/MM/DD'), ' YEAR') FROM DUAL;
--TRUNC : 그 달의 첫 날
SELECT TRUNC(TO_DATE('2020/05/15', 'YYYY/MM/DD'), 'MONTH') FROM DUAL;
SELECT TRUNC(TO_DATE('2020/05/15', 'YYYY/MM/DD'), 'YEAR') FROM DUAL;


--변환함수 및 조건부 표현식  171P
--TO_CHAR, TO_NUMBER, TO_DATE....

--TO_CHAR  변환함수: 숫자데이타 혹은 날짜 데이타를 문자 데이타로 변환.
--숫자->문자 9는 숫자를 나타내줌 9의 개수 만큼
SELECT EMPLOYEE_ID, SALARY, TO_CHAR(SALARY, '$999,999,99')
FROM EMPLOYEES
WHERE DEPARTMENT_ID = 90;

SELECT EMPLOYEE_ID, SALARY, TO_CHAR(SALARY, '$000,000,00')
FROM EMPLOYEES
WHERE DEPARTMENT_ID = 90;

--L:LOCAL CURRENCY
SELECT EMPLOYEE_ID, SALARY, TO_CHAR(SALARY, 'L000,000,00')
FROM EMPLOYEES
WHERE DEPARTMENT_ID = 90;


--날짜 -> 문자
SELECT EMPLOYEE_ID, HIRE_DATE, TO_CHAR(HIRE_DATE, 'YEAR/MONTH/DAY HH24:MI:SS')
FROM EMPLOYEES
WHERE DEPARTMENT_ID = 90;


-- TO_NUMBER(문자->숫자)
SELECT EMPLOYEE_ID, LAST_NAME, SALARY
FROM EMPLOYEES
WHERE SALARY > TO_NUMBER('$9000.00','$9999.99');

--TO_DATE(문자->날짜)
--다음은 기본 날짜 형식에 따른 날짜 비교
SELECT EMPLOYEE_ID, HIRE_DATE
FROM EMPLOYEES
WHERE HIRE_DATE <= '2002-07-22';
--기본 날짜 형식을 모를 때 TO_DATE를 사용하여 날짜 데이터로 인식할 수 있게끔 한다.
SELECT EMPLOYEE_ID, HIRE_DATE
FROM EMPLOYEES
WHERE HIRE_DATE <= TO_DATE('07-22-2002', 'MM-DD-YYYY');

SELECT LAST_NAME, HIRE_DATE
FROM EMPLOYEES
WHERE HIRE_DATE = TO_DATE('5월   24 2007', 'Month DD YYYY');


--일반함수 NVL, NVL2, NULLIF, COALESCE

--NVL함수 : NULL인 상태를 특정 데이타로 변환하는 함수.(.단, 두개의 데이터 타입이 같아야함)
SELECT EMPLOYEE_ID, COMMISSION_PCT, NVL(COMMISSION_PCT,0)
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN(50,80);
--COMMISSION_PCT를 문자열로 바꾼후 사용
SELECT EMPLOYEE_ID, COMMISSION_PCT, LPAD(NVL(TO_CHAR(COMMISSION_PCT),'NO DATA'),15,' ')
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN(50,80);
--NULL값을 계산이 안됨
SELECT EMPLOYEE_ID, SALARY, COMMISSION_PCT, SALARY+COMMISSION_PCT SUM_SAL
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN(50,80);
--NVL로 NULL값들을 0으로 바꾸어주어 계산이 되게끔 한다.
SELECT EMPLOYEE_ID, SALARY, COMMISSION_PCT, SALARY+NVL(COMMISSION_PCT,0) SUM_SAL
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN(50,80);

--NVL2(COLUM, 'DATA', 'NO DATA')
SELECT EMPLOYEE_ID, SALARY, COMMISSION_PCT, NVL2(COMMISSION_PCT,1,'0') CHECK_NULL
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN(50,80);


--NULLIF(두 개의 값을 비교해서 같으면 NULL
SELECT FIRST_NAME, LENGTH(FIRST_NAME), LAST_NAME, LENGTH(LAST_NAME),
NULLIF(LENGTH(FIRST_NAME), LENGTH(LAST_NAME)) RESULT
FROM EMPLOYEES;

--COALESCE(A.B,C,D,,,,,) 1.A의 NULL여부, NULL이아니면 A결과 NULL이면 2.B의 NULL여부, NULL이 아니면 B결과 NULL이면 프린트X
SELECT LAST_NAME, SALARY, COMMISSION_PCT,
COALESCE((SALARY+(COMMISSION_PCT*SALARY)), SALARY+2000) RESULT
FROM EMPLOYEES;

SELECT COALESCE(NULL,NULL,1) FROM DUAL;
SELECT COALESCE(1,2,3) FROM DUAL;

--조건부
--CASE EXPRESSION
SELECT LAST_NAME, JOB_ID, SALARY,
CASE JOB_ID
WHEN 'IT_PROG' THEN 1
WHEN 'ST_CLERK' THEN 2
WHEN 'SA_REP' THEN 3
ELSE SALARY
END "REVISED_SALARY" 
FROM EMPLOYEES;

--OTHER VERSION
SELECT LAST_NAME, SALARY,
(CASE WHEN SALARY<5000 THEN 'LOW'
WHEN SALARY=5000 THEN 'M'
WHEN SALARY>5000 THEN 'G'
ELSE 'EXCELLENT' END) AS RESULT
FROM EMPLOYEES;

--DECODE - CASE와 거의 비슷, 더욱 보기 간편
SELECT LAST_NAME, JOB_ID, SALARY,
DECODE(JOB_ID,
'IT_PROG', 1,
'ST_CLERK', 2,
'SA_REP', 3,
SALARY) REVISED_SALARY
FROM EMPLOYEES;




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
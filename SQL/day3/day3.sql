--4�� ������ �Լ�(SINGLE ROW FUNCTION) : 1���� �Է�->1���� ��� P.141

--�����Լ�(UPPER, LOWER, INITCAP, CONCAT, 
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


--INITCAP(ù ���� �빮��)
SELECT INITCAP('NEW YEAR') FROM DUAL;


--CONCAT(�����ֱ�) ��, �ΰ��� ����! 3��
SELECT FIRST_NAME, LAST_NAME, CONCAT(FIRST_NAME, LAST_NAME) AS NAME 
FROM EMPLOYEES;

SELECT CONCAT('A', 'B') AS NAME FROM DUAL;
SELECT CONCAT('A', 'B', 'C') AS NAME FROM DUAL;
SELECT 'A'||'B'||'C' AS NAME FROM DUAL;


--SUBSTR(���ڿ� �̾Ƴ���) (A,1,2) �μ� A�� 1��°���� 2���� �̾Ƴ���
SELECT LAST_NAME, SUBSTR(LAST_NAME,3,2) AS NAME
FROM EMPLOYEES
WHERE EMPLOYEE_ID=200;
-- (-��)�� �ڿ������� ����
SELECT LAST_NAME, SUBSTR(LAST_NAME,-3,2) AS NAME
FROM EMPLOYEES
WHERE EMPLOYEE_ID=200;

SELECT LAST_NAME, SUBSTR(LAST_NAME,-3,2) AS NAME
FROM EMPLOYEES
WHERE SUBSTR(LAST_NAME,3,2) = 'al';


--LENGTH(���ڼ�) , �����̽� ����, NULL�� ���x
SELECT LAST_NAME, LENGTH(LAST_NAME) AS NAME
FROM EMPLOYEES
WHERE EMPLOYEE_ID=200;

SELECT LENGTH('ABC DE') FROM DUAL;


--INSTR(�˻����) (A,'a',2,3) A������ 2��°���� �����ؼ� 3��°�� a�� ������ ��ġ
SELECT LAST_NAME, INSTR(LAST_NAME, 'a',2,1) AS NAME
FROM EMPLOYEES
WHERE DEPARTMENT_ID=30;


--LPAD (��ü���� �����ְ� ������ �е�)
SELECT LAST_NAME, LPAD(LAST_NAME, 10,'*')
FROM employees
WHERE DEPARTMENT_ID=30;

--RPAD
SELECT LAST_NAME, RPAD(LAST_NAME, 10,'*')
FROM employees
WHERE DEPARTMENT_ID=30;


--TRIM(�߶󳻱�) -�߰��� �ȵ�
SELECT TRIM(LEADING 'A' FROM 'ABCDEFGA') FROM DUAL; --�Ǿ�
SELECT TRIM(TRAILING 'A' FROM 'ABCDEFGA') FROM DUAL; --��
SELECT TRIM(BOTH 'A' FROM 'ABCDEFGA') FROM DUAL; --�Ǿ�,��


--REPLACE
SELECT REPLACE('ABCAEFGA','A','Z') FROM DUAL;
SELECT REPLACE('ABCAEFGA','A','') FROM DUAL;
SELECT LENGTH(REPLACE('ABCAEFGA','A','')) FROM DUAL;



--�����Լ�

--ROUND �Ҽ� ��° ¥������ �ݿø�
SELECT ROUND(123.4567, 2) FROM DUAL;
SELECT ROUND(654.321, -2) FROM DUAL;
SELECT ROUND(123.4567, 0) FROM DUAL;
SELECT ROUND(123.4567) FROM DUAL;

--TRUNC(�ݿø� ���� �׳� ������)
SELECT TRUNC(123.4567, 2) FROM DUAL;
SELECT TRUNC(654.321, -2) FROM DUAL;
SELECT TRUNC(123.4567, 0) FROM DUAL;
SELECT TRUNC(123.4567) FROM DUAL;

--MOD(������)
SELECT MOD(15,2) FROM DUAL;

--CEIL(�ش� ������ ū �ּ� ������)
SELECT CEIL(5.3) FROM DUAL;

--FLOOR(�ش� ������ ���� �ִ� ������)
SELECT FLOOR(5.3) FROM DUAL;

--�ð����� ����( ���� : RRRR,YYYY�� ����)

ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY/MM/DD';
SELECT SYSDATE FROM DUAL;

SELECT EMPLOYEE_ID, LAST_NAME, HIRE_DATE
FROM EMPLOYEES
WHERE HIRE_DATE >= '2004/03/01';


SELECT SESSIONTIMEZONE, CURRENT_DATE FROM DUAL;
-- SYSDATE�� �̿��� ���� ��¥�� ����Ÿ���̽� �ý����� ��ġ�� �Ǿ� �ִ� ����� ���� ��¥.
-- CURRENT_DATE�� SQL �۾��� �ϰ� �ִ� ����ڰ� �ִ� ����� ���� ��¥.

SELECT LAST_NAME, (SYSDATE-HIRE_DATE)/7 AS WEEK
FROM EMPLOYEES
WHERE DEPARTMENT_ID = 90;

SELECT LAST_NAME, TO_CHAR(HIRE_DATE,'YYYY/MM/DD HH24:MI:SS'), TO_CHAR(HIRE_DATE+1/24/60/60,'YYYY/MM/DD HH24:MI:SS')
FROM EMPLOYEES
WHERE DEPARTMENT_ID = 90;

--MONTH_BETWEEN(���� ����)
SELECT HIRE_DATE, MONTHS_BETWEEN(SYSDATE, HIRE_DATE) FROM EMPLOYEES
WHERE DEPARTMENT_ID = 90;

--ADD_MONTHS
SELECT EMPLOYEE_ID, HIRE_DATE, ADD_MONTHS(HIRE_DATE,5) FROM EMPLOYEES
WHERE department_id = 90;

SELECT ADD_MONTHS(SYSDATE,5) AS "AFTER 5M" FROM DUAL;

--NEXT_DAY(�ش޳�¥ ������ ���� ������ ��¥)
SELECT NEXT_DAY('2020/12/31','��') FROM DUAL;

--LAST_DAY(�� ���� ������ ��¥)
SELECT LAST_DAY('2020/9/2') FROM DUAL;
--��¥�� �ݿø� (YEAR:6��������/MONTH:15�� ����)
SELECT ROUND(TO_DATE('2020/05/16', 'YYYY/MM/DD'), 'MONTH') FROM DUAL;
SELECT ROUND(TO_DATE('2020/05/15', 'YYYY/MM/DD'), 'MONTH') FROM DUAL;
SELECT ROUND(TO_DATE('2020/05/15', 'YYYY/MM/DD'), ' YEAR') FROM DUAL;
--TRUNC : �� ���� ù ��
SELECT TRUNC(TO_DATE('2020/05/15', 'YYYY/MM/DD'), 'MONTH') FROM DUAL;
SELECT TRUNC(TO_DATE('2020/05/15', 'YYYY/MM/DD'), 'YEAR') FROM DUAL;


--��ȯ�Լ� �� ���Ǻ� ǥ����  171P
--TO_CHAR, TO_NUMBER, TO_DATE....

--TO_CHAR  ��ȯ�Լ�: ���ڵ���Ÿ Ȥ�� ��¥ ����Ÿ�� ���� ����Ÿ�� ��ȯ.
--����->���� 9�� ���ڸ� ��Ÿ���� 9�� ���� ��ŭ
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


--��¥ -> ����
SELECT EMPLOYEE_ID, HIRE_DATE, TO_CHAR(HIRE_DATE, 'YEAR/MONTH/DAY HH24:MI:SS')
FROM EMPLOYEES
WHERE DEPARTMENT_ID = 90;


-- TO_NUMBER(����->����)
SELECT EMPLOYEE_ID, LAST_NAME, SALARY
FROM EMPLOYEES
WHERE SALARY > TO_NUMBER('$9000.00','$9999.99');

--TO_DATE(����->��¥)
--������ �⺻ ��¥ ���Ŀ� ���� ��¥ ��
SELECT EMPLOYEE_ID, HIRE_DATE
FROM EMPLOYEES
WHERE HIRE_DATE <= '2002-07-22';
--�⺻ ��¥ ������ �� �� TO_DATE�� ����Ͽ� ��¥ �����ͷ� �ν��� �� �ְԲ� �Ѵ�.
SELECT EMPLOYEE_ID, HIRE_DATE
FROM EMPLOYEES
WHERE HIRE_DATE <= TO_DATE('07-22-2002', 'MM-DD-YYYY');

SELECT LAST_NAME, HIRE_DATE
FROM EMPLOYEES
WHERE HIRE_DATE = TO_DATE('5��   24 2007', 'Month DD YYYY');


--�Ϲ��Լ� NVL, NVL2, NULLIF, COALESCE

--NVL�Լ� : NULL�� ���¸� Ư�� ����Ÿ�� ��ȯ�ϴ� �Լ�.(.��, �ΰ��� ������ Ÿ���� ���ƾ���)
SELECT EMPLOYEE_ID, COMMISSION_PCT, NVL(COMMISSION_PCT,0)
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN(50,80);
--COMMISSION_PCT�� ���ڿ��� �ٲ��� ���
SELECT EMPLOYEE_ID, COMMISSION_PCT, LPAD(NVL(TO_CHAR(COMMISSION_PCT),'NO DATA'),15,' ')
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN(50,80);
--NULL���� ����� �ȵ�
SELECT EMPLOYEE_ID, SALARY, COMMISSION_PCT, SALARY+COMMISSION_PCT SUM_SAL
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN(50,80);
--NVL�� NULL������ 0���� �ٲپ��־� ����� �ǰԲ� �Ѵ�.
SELECT EMPLOYEE_ID, SALARY, COMMISSION_PCT, SALARY+NVL(COMMISSION_PCT,0) SUM_SAL
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN(50,80);

--NVL2(COLUM, 'DATA', 'NO DATA')
SELECT EMPLOYEE_ID, SALARY, COMMISSION_PCT, NVL2(COMMISSION_PCT,1,'0') CHECK_NULL
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN(50,80);


--NULLIF(�� ���� ���� ���ؼ� ������ NULL
SELECT FIRST_NAME, LENGTH(FIRST_NAME), LAST_NAME, LENGTH(LAST_NAME),
NULLIF(LENGTH(FIRST_NAME), LENGTH(LAST_NAME)) RESULT
FROM EMPLOYEES;

--COALESCE(A.B,C,D,,,,,) 1.A�� NULL����, NULL�̾ƴϸ� A��� NULL�̸� 2.B�� NULL����, NULL�� �ƴϸ� B��� NULL�̸� ����ƮX
SELECT LAST_NAME, SALARY, COMMISSION_PCT,
COALESCE((SALARY+(COMMISSION_PCT*SALARY)), SALARY+2000) RESULT
FROM EMPLOYEES;

SELECT COALESCE(NULL,NULL,1) FROM DUAL;
SELECT COALESCE(1,2,3) FROM DUAL;

--���Ǻ�
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

--DECODE - CASE�� ���� ���, ���� ���� ����
SELECT LAST_NAME, JOB_ID, SALARY,
DECODE(JOB_ID,
'IT_PROG', 1,
'ST_CLERK', 2,
'SA_REP', 3,
SALARY) REVISED_SALARY
FROM EMPLOYEES;




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
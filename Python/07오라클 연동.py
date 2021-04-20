{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# mc 계정생성 - system 계정에서\n",
    "create user mc identified by mc;\n",
    "grant create session, create table, create view, create sequence to mc;\n",
    "alter user mc default tablespace users;\n",
    "alter user mc quota unlimited on users;\n",
    "\n",
    "# 테이블 생성 - mc 계정에서\n",
    "create table dbtest(\n",
    "id varchar2(30) primary key,\n",
    "passwd varchar2(30) not null,\n",
    "name varchar(50) not null,\n",
    "tel varchar(15),\n",
    "address varchar2(100)\n",
    ");\n",
    "\n",
    "insert into dbtest values( 'aaa', '111', '홍길동', '1111-2222', '서울시' );\n",
    "insert into dbtest values( 'bbb', '111', '이순신', '2222-2222', '수원시' );\n",
    "insert into dbtest values( 'ccc', '111', '김유신', '3333-2222', '안산시' );\n",
    "insert into dbtest values( 'ddd', '111', '대조영', '5555-2222', '인천시' );\n",
    "insert into dbtest values( 'eee', '111', '강감찬', '6666-2222', '의정부시' );\n",
    "commit;\n",
    "\n",
    "select * from dbtest;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "aaa\n",
      "('aaa', '111', '홍길동', '1111-2222', '서울시')\n",
      "회원수 :  5\n",
      "('aaa', '111', '홍길동', '1111-2222', '서울시')\n"
     ]
    }
   ],
   "source": [
    "# select\n",
    "import cx_Oracle\n",
    "dsn = cx_Oracle.makedsn( 'localhost', '1521', 'xe' )\n",
    "con = cx_Oracle.connect( 'mc', 'mc', dsn )\n",
    "cursor = con.cursor()\n",
    "\n",
    "sql = \"select * from dbtest\"\n",
    "rows = cursor.execute( sql )\n",
    "\n",
    "# print( type( rows ) )                       # cx_Oracle.Cursor\n",
    "# for row in rows :                           # 반복문 실행 후 cursor가 맨 끝으로 이동\n",
    "# #     print( type( row ) )                  # tuple\n",
    "#     for column in row :\n",
    "#         print( column, end=' ' )\n",
    "#     print()        \n",
    "\n",
    "users = cursor.fetchall()    \n",
    "print( users[0][0] )\n",
    "print( users[0] )                             # ('aaa', '111', '홍길동', '1111-2222', '서울시')\n",
    "\n",
    "sql = \"select count(*) from dbtest\"\n",
    "cursor.execute( sql )\n",
    "count = cursor.fetchone()[0]\n",
    "print( '회원수 : ', count )\n",
    "\n",
    "sql = \"select * from dbtest where id='aaa'\"    \n",
    "cursor.execute( sql )\n",
    "# user = cursor.fetchall()                   # list\n",
    "user = cursor.fetchone()                     # tuple    \n",
    "print( user )\n",
    "con.close()  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "탈퇴했습니다\n",
      "aaa 111 홍길동 1111-2222 서울시 \n",
      "bbb 111 이순신 2222-2222 수원시 \n",
      "ccc 111 김유신 3333-2222 안산시 \n",
      "ddd 111 대조영 5555-2222 인천시 \n",
      "eee 111 강감찬 6666-2222 의정부시 \n"
     ]
    }
   ],
   "source": [
    "# insert / delete\n",
    "import cx_Oracle\n",
    "dsn = cx_Oracle.makedsn( 'localhost', '1521', 'xe' )\n",
    "con = cx_Oracle.connect( 'mc', 'mc', dsn )\n",
    "cursor = con.cursor()\n",
    "\n",
    "# 한명\n",
    "user = ( 'fff', '111', '안중근', '1111-3333', '일산시' )           # id primary 제약조건 위배 \n",
    "sql = \"insert into dbtest values(:1, :2, :3, :4, :5 )\"\n",
    "cursor.execute( sql, user )\n",
    "con.commit()\n",
    "\n",
    "# 여러명\n",
    "\n",
    "# delete\n",
    "sql = \"select * from dbtest where id='fff'\"\n",
    "cursor.execute( sql )\n",
    "user = cursor.fetchone()\n",
    "if user == None :\n",
    "    print( '입력한 아이디가 없습니다' )\n",
    "else :\n",
    "    if user[1] == '111' :\n",
    "        sql = \"delete from dbtest where id=:idx\"\n",
    "        cursor.execute( sql, idx='fff' )\n",
    "        print( '탈퇴했습니다' )\n",
    "    else :\n",
    "        print( '입력한 비밀번호가 다릅니다' )\n",
    "con.commit()\n",
    "\n",
    "# 확인\n",
    "sql = \"select * from dbtest order by id\"\n",
    "rows = cursor.execute( sql )\n",
    "for row in rows :\n",
    "    for column in row :\n",
    "        print( column, end=' ' )\n",
    "    print()     \n",
    "\n",
    "con.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "수정됐습니다\n",
      "aaa 999 홍길동 9999-9999 평택시 \n",
      "bbb 111 이순신 2222-2222 수원시 \n",
      "ccc 111 김유신 3333-2222 안산시 \n",
      "ddd 111 대조영 5555-2222 인천시 \n",
      "eee 111 강감찬 6666-2222 의정부시 \n"
     ]
    }
   ],
   "source": [
    "# update\n",
    "import cx_Oracle\n",
    "dsn = cx_Oracle.makedsn( 'localhost', '1521', 'xe' )\n",
    "con = cx_Oracle.connect( 'mc', 'mc', dsn )\n",
    "cursor = con.cursor()\n",
    "\n",
    "idx = 'aaa'\n",
    "passwd = '999'\n",
    "tel = '9999-9999'\n",
    "address = '평택시'\n",
    "\n",
    "# sql = \"update dbtest set passwd=:pd, tel=:t, address=:addr where id=:idx\"\n",
    "# cursor.execute( sql, pd=passwd, t=tel, addr=address, idx=idx )\n",
    "sql = \"update dbtest set passwd='\"+passwd+\"', tel='\"+tel+\"', address='\"+address+\"' where id='\"+idx+\"'\"\n",
    "cursor.execute( sql )\n",
    "con.commit()\n",
    "print( \"수정됐습니다\" )\n",
    "\n",
    "# 확인\n",
    "sql = \"select * from dbtest order by id\"\n",
    "rows = cursor.execute( sql )\n",
    "for row in rows :\n",
    "    for column in row :\n",
    "        print( column, end=' ' )\n",
    "    print()     \n",
    "con.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

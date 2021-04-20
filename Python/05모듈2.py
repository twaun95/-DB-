{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 모듈\n",
    "# .py 확장자인 파일 하나\n",
    "# 일반변수 일반함수 클래스\n",
    "\n",
    "# 모듈이 같은 폴더 있는 경우\n",
    "\n",
    "# import 모듈명\n",
    "import mymodule\n",
    "print( mymodule.msg )                    # 모듈명.변수\n",
    "mymodule.hello()                         # 모듈명.일반함수\n",
    "\n",
    "user = mymodule.User( '홍길동', 30 )     # 모듈명.클래스\n",
    "print( user.getName() )\n",
    "print( user.getAge() )\n",
    "\n",
    "# import 모듈명 as 모듈별칭\n",
    "print()\n",
    "import mymodule as mm\n",
    "print( mm.msg )\n",
    "mm.bye()\n",
    "user = mm.User( '이순신', 20 )\n",
    "print( user.getName() )\n",
    "print( user.getAge() )\n",
    "\n",
    "# from 모듈명 import 변수 or 함수     모듈 이름을 생략하고 사용 가능\n",
    "print()\n",
    "from mymodule import msg, hello, bye\n",
    "print( msg )\n",
    "hello()\n",
    "bye()\n",
    "\n",
    "# from 모듈명 import 이름 as 별칭\n",
    "from mymodule import User as us\n",
    "user = us( '김유신', 10 )\n",
    "print( user.getName() )\n",
    "print( user.getAge() )\n",
    "\n",
    "# from 모듈명 import *               해당 모듈의 __ 로 시작하는 이름을 제외한 모든 이름 사용 가능\n",
    "print()\n",
    "from mymodule import *\n",
    "user = User( '강감찬', 40 )\n",
    "print( user.getName() )\n",
    "print( user.getAge() )\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 모듈이 다른 폴더 있는 경우\n",
    "# 모듈          py 파일하나\n",
    "# 패키지        폴더. __init__.py 파일이 존재해야 인식. 3.3 버전 부터는 없어도 된다.\n",
    "\n",
    "# import 패키지명.모듈명\n",
    "import module.mymodule\n",
    "print( module.mymodule.msg )\n",
    "module.mymodule.hello()\n",
    "user = module.mymodule.User( '홍길동', 30 )\n",
    "print( user.getName() )\n",
    "print( user.getAge() )\n",
    "\n",
    "# import 패키지명.모듈명 as 모듈별칭\n",
    "print()\n",
    "import module.mymodule as mm\n",
    "print( mm.msg )\n",
    "mm.bye()\n",
    "user = mm.User( '이순신', 40 )\n",
    "print( user.getName() )\n",
    "print( user.getAge() )\n",
    "\n",
    "# from 패키지명.모듈명 import 변수 or 함수      \n",
    "print()\n",
    "from module.mymodule import msg, hello, bye\n",
    "hello()\n",
    "bye()\n",
    "\n",
    "# from 패키지명.모듈명 import 이름 as 별칭\n",
    "from module.mymodule import User as us\n",
    "user = us( '김유신', 20 )\n",
    "print( user.getName() )\n",
    "print( user.getAge() )\n",
    "\n",
    "# from 패키지명.모듈명 import *     \n",
    "print()\n",
    "from module.mymodule import *\n",
    "print( msg )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# OS SYS 모듈\n",
    "import os\n",
    "import sys\n",
    "# print( os.getcwd() )           # 현재디렉토리 경로\n",
    "# print( os.listdir( 'c:\\\\' ) )\n",
    "# print( sys.path )              # 환경변수\n",
    "# print( sys.modules )\n",
    "print( sys.version_info )\n",
    "print( sys.version_info.major )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Windows-10-10.0.19041-SP0\n",
      "C:\\Users\\filma\\test.log\n"
     ]
    }
   ],
   "source": [
    "# logging 모듈\n",
    "import os, platform, logging\n",
    "print( platform.platform() )\n",
    "\n",
    "logfile = ''\n",
    "if platform.platform().startswith( 'Windows' ) :\n",
    "    logfile = os.path.join( os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log' )\n",
    "else :\n",
    "    logfile = os.path.join( os.getenv('HOME'), 'test.log' )\n",
    "print( logfile )    \n",
    "    \n",
    "logging.basicConfig( \\\n",
    "    level=logging.ERROR, \\\n",
    "    format='%(asctime)s - %(levelname)s - %(message)s', \\\n",
    "    filename=logfile, \\\n",
    "    filemode='w' )    \n",
    "logging.error( '에러발생' )\n",
    "logging.warning( '경고발생' )\n",
    "logging.info( '정보' )\n",
    "logging.debug( '디버그 정보' )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2021-02-03\n",
      "2021 년 2 월 3 일\n",
      "2021-02-03 09:52:18.652593\n",
      "2021-03-05\n"
     ]
    }
   ],
   "source": [
    "# 시간 모듈\n",
    "from datetime import datetime, timedelta, date, time\n",
    "now = date.today()\n",
    "print( now )\n",
    "print( now.year, '년', now.month, '월', now.day, '일')\n",
    "\n",
    "print( datetime.today() )\n",
    "# print( now + 30 )\n",
    "print( now + timedelta( 30 ) )\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "26 23 14 30 10 12 \n",
      "36 41 8 18 43 41 \n",
      "[4, 12, 23, 27, 28, 32]\n",
      "[5, 15, 25, 33, 38, 44]\n",
      "[9, 10, 15, 30, 42, 45]\n",
      "[12, 16, 18, 24, 25, 39]\n",
      "[1, 13, 24, 25, 38, 45]\n",
      "[1, 4, 8, 15, 36, 42]\n",
      "[6, 8, 17, 18, 34, 35]\n",
      "[9, 15, 19, 22, 28, 38]\n",
      "[4, 8, 9, 34, 37, 38]\n",
      "[6, 12, 13, 25, 29, 37]\n",
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
      "[9, 6, 7, 8, 3, 1, 5, 2, 10, 4]\n"
     ]
    }
   ],
   "source": [
    "# 난수\n",
    "import random\n",
    "for i in range(0, 6) :\n",
    "    print( int( random.random()*45 ) + 1, end=' ' )          # 1~100\n",
    "print()    \n",
    "for i in range(0, 6) :\n",
    "    print( random.randint( 1, 46 ), end=' ' )\n",
    "print()    \n",
    "for i in range( 0, 10 ) :\n",
    "    print( sorted( random.sample( range(1, 46), 6 ) ) )\n",
    "    \n",
    "m = [ i for i in range( 1, 11) ]    \n",
    "print( m )\n",
    "random.shuffle( m )\n",
    "print( m )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "이름 :  김유신\n",
      "나이 :  30\n",
      "김유신 20\n",
      "이순신 30\n",
      "홍길동 10\n"
     ]
    }
   ],
   "source": [
    "# 피클링           객체단위입출력\n",
    "class User :\n",
    "    def __init__( self, name='', age=0 ) :\n",
    "        self.name = name\n",
    "        self.age = age\n",
    "    def getName( self ) :\n",
    "        return self.name\n",
    "    def getAge( self ) :\n",
    "        return self.age\n",
    "\n",
    "kim = User( '김유신', 30 )    \n",
    "\n",
    "import pickle\n",
    "with open( 'user.txt', 'wb' ) as f :\n",
    "    pickle.dump( kim, f )\n",
    "with open( 'user.txt', 'rb' ) as f :\n",
    "    user = pickle.load( f )\n",
    "print( '이름 : ', user.getName() )    \n",
    "print( '나이 : ', user.getAge() )\n",
    "\n",
    "users = [User('김유신', 20), User('이순신', 30), User('홍길동', 10)]   \n",
    "with open( 'user.txt', 'wb' ) as f :\n",
    "    pickle.dump( users, f )\n",
    "with open( 'user.txt', 'rb' ) as f :\n",
    "    us = pickle.load( f )\n",
    "for u in us :\n",
    "    print( u.getName(), u.getAge() )    \n"
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

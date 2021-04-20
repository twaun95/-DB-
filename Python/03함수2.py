{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "### 함수 Function ###\n",
    "# 사용자 정의 함수 \n",
    "\n",
    "# 일반함수\n",
    "# class 클래스명 :\n",
    "#     멤버함수\n",
    "\n",
    "# C - 일반함수, 멤버함수\n",
    "# 반환형 함수명( 매개변수 ) {\n",
    "#     실행문;\n",
    "#     return 값;\n",
    "# }\n",
    "\n",
    "# Java - 멤버함수(메서드)\n",
    "# 접근제한자 반환형 함수명( 매개변수 ) {\n",
    "#     실행문;\n",
    "#     return 값;\n",
    "# }\n",
    "\n",
    "# Python - 일반함수, 멤버함수\n",
    "# def 함수명( 매개변수 ) :\n",
    "#     실행문\n",
    "#     return 값\n",
    "\n",
    "# 여러 값을 리턴할 수 있다. 튜플 리턴\n",
    "# 반환 값이 없을 경우 None 이 반환\n",
    "# return을 여러 번 사용할 수는 없다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Ptyhon!!!!!\n",
      "Hello Ptyhon!!!!!\n",
      "Hello Ptyhon!!!!!\n",
      "Hello Ptyhon\n",
      "Hello Ptyhon\n",
      "Hello Ptyhon\n"
     ]
    }
   ],
   "source": [
    "# 반복되는 내용을 묶어서 처리. 재활용 재사용\n",
    "# 선언 구현 호출해야 한다\n",
    "# 반드시 호출한 자리로 돌아온다.\n",
    "# 모든 함수는 return 이 있다. 단 리턴값이 없으면 생략가능하다.\n",
    "\n",
    "print( 'Hello Ptyhon!!!!!' )\n",
    "print( 'Hello Ptyhon!!!!!' )\n",
    "print( 'Hello Ptyhon!!!!!' )\n",
    "\n",
    "def sub() :                        # 선언\n",
    "    print( 'Hello Ptyhon' )        # 구현\n",
    "    return                         # 값이 없을 때는 생략 가능\n",
    "sub()                              # 호출 \n",
    "sub()\n",
    "sub()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "합 : 7\n",
      "합 : 7\n",
      "합 : 30\n"
     ]
    }
   ],
   "source": [
    "# 매개변수\n",
    "def hap() :\n",
    "    a, b = 5, 2\n",
    "    print( '합 :', a+b )\n",
    "hap() \n",
    "\n",
    "def hap( a, b ) :              # 매개변수 인수 argument\n",
    "    print( '합 :', a+b )\n",
    "hap( 5, 2 )                    # 인자 parameter\n",
    "hap( 10, 20 )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "합 : 7\n",
      "합 : AB\n",
      "합 : 9.8\n",
      "합 :  7\n"
     ]
    }
   ],
   "source": [
    "# 오버로드        함수의 이름이 같아도 매개변수 자료형이 다르거나 개수가 다르거나 순서가 다르면\n",
    "#                 다른 함수로 취급\n",
    "# int hap( int a, int b ) {}                 hap( 10, 20 )\n",
    "# float hap( float a, float b ) {}           hap( 5.5, 10.7 )\n",
    "\n",
    "# 파이썬 오버로드가 없다\n",
    "def hap( a, b ) :\n",
    "    print( '합 :', a+b )\n",
    "hap( 5, 2 )\n",
    "hap( 'A', 'B' )\n",
    "hap( 5.5, 4.3 )\n",
    "# hap( 5, 3, 2 )\n"
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
      "합 :  0\n",
      "합 :  7\n",
      "합 :  5\n",
      "합 :  23\n",
      "합 :  5\n"
     ]
    }
   ],
   "source": [
    "# 개수가 다른 경우        매개변수의 초기값\n",
    "def hap( a=0, b=0, c=0 ) :\n",
    "    print( '합 : ', a+b+c )\n",
    "hap()\n",
    "hap( 5, 2 )   \n",
    "hap( 5 )\n",
    "hap( 5, 8, 10 )\n",
    "# hap( 5, 8, 10, 4 )\n",
    "\n",
    "# def hap( a=0, b=0, c ) :\n",
    "#     print( '합 : ', a+b+c )\n",
    "# hap( 5 )                # a의 값\n",
    "\n",
    "def hap( a, b=0, c=0 ) :\n",
    "    print( '합 : ', a+b+c )\n",
    "hap( 5 )                  # 최소한 값 하나는 필요"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
      "7\n",
      "(7, 3, 10, 2.5)\n",
      "7 3 10 2.5\n"
     ]
    }
   ],
   "source": [
    "# return\n",
    "def hap( a, b ) :\n",
    "    print( a + b )\n",
    "    return                     # 값이 없을 때는 생략\n",
    "hap( 5, 2 )    \n",
    "\n",
    "def hap( a, b ) :\n",
    "    return a + b\n",
    "print( hap( 5, 2 ) ) \n",
    "\n",
    "def calc( a, b ) :\n",
    "    return (a+b, a-b, a*b, a/b);\n",
    "print( calc( 5, 2 ) )\n",
    "a, b, c, d = calc( 5, 2 )\n",
    "print( a, b, c, d )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "8\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "# Varialble Argument\n",
    "# *param\n",
    "\n",
    "def hap( *param ) :\n",
    "    sum = 0\n",
    "    for i in param :\n",
    "        sum += i\n",
    "    return sum\n",
    "print( hap( 2 ) )\n",
    "print( hap( 5, 3 ) )\n",
    "print( hap( 2, 5, 3 ) )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ABC\n",
      "BA\n",
      "C\n",
      "A\n",
      "14\n",
      "-4\n",
      "a 5\n",
      "b 2\n",
      "d 7\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "# 매개변수 지정 호출             \n",
    "def hap( a, b='', c='' ) :\n",
    "    return a+b+c;\n",
    "\n",
    "print( hap( 'A', 'B', 'C' ) )\n",
    "print( hap( b='A', a='B' ) )\n",
    "print( hap( a='C' ) )\n",
    "print( hap( a='A' ) )\n",
    "print( hap( 5, 2, 7 ) )\n",
    "\n",
    "# 키워드 인수\n",
    "def cha( a=0, b=0, c=0, d=0 ) :\n",
    "    return a-b-c-d;\n",
    "print( cha( a=5, b=2, d=7 ) )\n",
    "\n",
    "# 키워드 인수 사전\n",
    "# **param   \n",
    "def gop( **param ) :            # dictionry \n",
    "    for key, value in param.items() :\n",
    "        print( key, value )\n",
    "print( gop( a=5, b=2, d=7 ) )\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10AB\n",
      "10ABC\n",
      "10ABCc10d20e30\n",
      "ABCFc10d20\n",
      "0c10d20\n",
      "10ABC\n",
      "10fAbBdD\n"
     ]
    }
   ],
   "source": [
    "# 순서가 중요하다\n",
    "# def hap( *args, a=0 ) :\n",
    "#     pass;\n",
    "\n",
    "def hap( a=0, *args ) :\n",
    "    sum = ''\n",
    "    for i in args :\n",
    "        sum += i;\n",
    "    return str(a) + sum    \n",
    "print( hap( 10, 'A', 'B' ) )\n",
    "print( hap( 10, 'A', 'B', 'C' ) )\n",
    "\n",
    "def hap( a=0, *args, **params ) :\n",
    "    sum = ''\n",
    "    for i in args :\n",
    "        sum += i;\n",
    "    for key, value in params.items() :\n",
    "        sum += ( str(key) + str( value ) )\n",
    "    return str(a) + sum \n",
    "\n",
    "print( hap( 10, 'A', 'B', 'C', c=10, d=20, e=30 ) )\n",
    "print( hap( 'A', 'B', 'C', 'F', c=10, d=20 ) )\n",
    "print( hap( c=10, d=20 ) )    \n",
    "print( hap( 10, 'A', 'B', 'C' ) )   \n",
    "print( hap( 10, f='A', b='B', d='D' ) )   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "100\n",
      "10\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "# 지역변수 전역변수\n",
    "a = 100                # 전역변수 생성\n",
    "def disp() :    \n",
    "    a = 10             # 지역변수 생성  \n",
    "    print( a )         # 지역변수  10\n",
    "disp()    \n",
    "print( a )             # 전역변수  100\n",
    "   \n",
    "def disp() : \n",
    "    global a\n",
    "    a = 10             # 전역변수 수정   지역변수 생성 X\n",
    "    print( a )         # 전역변수  10\n",
    "disp()    \n",
    "print( a )             # 전역변수  10    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "5\n",
      "True\n",
      "False\n",
      "True\n",
      "False\n",
      "True\n",
      "\n",
      "True\n",
      "False\n",
      "True\n",
      "True\n",
      "False\n",
      "\n",
      "2.5\n",
      "2\n",
      "1\n",
      "(2, 1)\n",
      "\n",
      "y\n",
      "P\n",
      "98\n",
      "10\n",
      "25\n",
      "25\n",
      "[10, 34, 40, 65, 98]\n"
     ]
    }
   ],
   "source": [
    "# 간단한 내장함수\n",
    "print( abs( 5 ) )                # 절대값\n",
    "print( abs( -5 ) )\n",
    "\n",
    "print( all( [True, True, True] ) )\n",
    "print( all( [True, False, True] ) )\n",
    "print( all( [1, 2, 3, 4] ) )     # 0이 아닌 값은 다 참\n",
    "print( all( [0, 2, 3, 4] ) )     \n",
    "print( all( ['ABC', 'DEF', 'HIJ'] ) )    \n",
    "\n",
    "print()\n",
    "print( any( [True, False, False] ) )\n",
    "print( any( [False, False, False] ) )\n",
    "print( any( [1, 2, 'A', '월'] ) )\n",
    "print( any( ['0'] ) )          # 참\n",
    "print( any( [0] ) )            # 거짓\n",
    "\n",
    "print()\n",
    "print( 5 / 2 )\n",
    "print( 5 // 2 )               # 몫\n",
    "print( 5 % 2 )                # 나머지\n",
    "print( divmod( 5, 2 ) )       # 몫 나머지\n",
    "a, b = divmod( 5, 2 )\n",
    "\n",
    "print()\n",
    "print( max( 'Python' ) )\n",
    "print( min( 'Python' ) )\n",
    "\n",
    "print( max( [10, 40, 98, 34, 65] ) )\n",
    "print( min( [10, 40, 98, 34, 65] ) )\n",
    "\n",
    "print( 5**2 )\n",
    "print( pow( 5, 2 ) )\n",
    "\n",
    "print( sorted( [10, 40, 98, 34, 65] ) )\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "# 람다함수\n",
    "# def hap( a, b ) :\n",
    "#     return a+b\n",
    "# print( hap( 5, 2 ) )\n",
    "\n",
    "hap = lambda a, b : a+b\n",
    "print( hap( 5, 2 ) )\n",
    "\n",
    "print( ( lambda a, b : a+b )( 5, 2 ) )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "<filter object at 0x0000020FA6AED288>\n",
      "[2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "# filter\n",
    "# def even( x ) :\n",
    "#     return x%2==0\n",
    "# print( even( 2 ) )\n",
    "\n",
    "even = lambda x : x%2==0\n",
    "print( even( 2 ) )\n",
    "\n",
    "print( filter( even, range(1, 11 ) ) )\n",
    "print( list( filter( even, range(1, 11 ) ) ) )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 9, 25, 49, 81]\n",
      "2550\n"
     ]
    }
   ],
   "source": [
    "# map 처리한 데이터를 list로 묶어서 \n",
    "print( list( map( lambda x : x*x, range(1, 11, 2) ) ) )\n",
    "\n",
    "# 1~100까지 합을 출력  2550\n",
    "print( sum( list( filter( lambda x : x%2==0, range(1, 101) ) ) ) )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55\n",
      "3628800\n",
      "-53\n"
     ]
    }
   ],
   "source": [
    "# reduce    누적\n",
    "from functools import reduce\n",
    "print( reduce( lambda x, y : x+y, range( 1, 11 ) ) )\n",
    "print( reduce( lambda x, y : x*y, range( 1, 11 ) ) )\n",
    "print( reduce( lambda x, y : x-y, range( 1, 11 ) ) )"
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

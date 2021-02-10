{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.series.Series'>\n",
      "RangeIndex(start=0, stop=10, step=1)\n",
      "[11 12 13 14 15 16 17 18 19 20]\n",
      "int64\n",
      "Index(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], dtype='object')\n",
      "[11 12 13 14 15 16 17 18 19 20]\n",
      "11\n",
      "12\n",
      "12\n",
      "a    11\n",
      "b    12\n",
      "c    13\n",
      "d    14\n",
      "e    15\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "# Series                  1차원. 데이터베이스 한 행을 관리. 레코드 -> C 구조체\n",
    "s = pd.Series( [ i for i in range( 11, 21 ) ] )\n",
    "print( type( s ) )\n",
    "print( s.index )\n",
    "print( s.values )\n",
    "print( s.dtype )\n",
    "\n",
    "s = pd.Series( [ i for i in range( 11, 21 ) ], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] )\n",
    "# print( s )\n",
    "print( s.index )\n",
    "print( s. values )\n",
    "print( s[0] )\n",
    "print( s['b'] )\n",
    "print( s.b )\n",
    "print( s[0:5] )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "dict_keys(['a', 'c', 'd', 'b', 'f'])\n",
      "dict_values([10, 20, 50, 30, 60])\n",
      "dict_items([('a', 10), ('c', 20), ('d', 50), ('b', 30), ('f', 60)])\n",
      "<class 'pandas.core.series.Series'>\n",
      "10\n",
      "10\n",
      "10\n",
      "<class 'numpy.ndarray'>\n",
      "<class 'pandas.core.indexes.base.Index'>\n"
     ]
    }
   ],
   "source": [
    "# Dictionary -> Series\n",
    "dd = {'a':10, 'c':20, 'd':50, 'b':30, 'f':60}\n",
    "# print( type( dd ) )\n",
    "# print( dd[0] )                  # 에러\n",
    "print( dd['a'] )\n",
    "# print( dd.a )                   # 에러\n",
    "# print( dd[0:5] )                # 에러\n",
    "print( dd.keys() )\n",
    "print( dd.values() )\n",
    "print( dd.items() )\n",
    "\n",
    "ss = pd.Series( dd )\n",
    "print( type( ss ) )\n",
    "print( ss.a )\n",
    "print( ss[0] )\n",
    "print( ss['a'] )\n",
    "print( type( ss.values ) )       # numpy.ndarray\n",
    "print( type( ss.index ) )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'dict'>\n",
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex(start=0, stop=5, step=1)\n",
      "Index(['name', 'age', 'tel'], dtype='object')\n",
      "[['kim' 20 '1111-1111']\n",
      " ['lee' 30 '1111-2222']\n",
      " ['park' 25 '3333-1111']\n",
      " ['jung' 35 '2222-3333']\n",
      " ['hong' 15 '3333-2222']]\n",
      "<class 'numpy.ndarray'>\n",
      "     name  age        tel\n",
      "num                      \n",
      "0     kim   20  1111-1111\n",
      "1     lee   30  1111-2222\n",
      "2    park   25  3333-1111\n",
      "3    jung   35  2222-3333\n",
      "4    hong   15  3333-2222\n",
      "RangeIndex(start=0, stop=5, step=1, name='num')\n",
      "Index(['name', 'age', 'tel'], dtype='object')\n",
      "user  name  age        tel\n",
      "num                       \n",
      "0      kim   20  1111-1111\n",
      "1      lee   30  1111-2222\n",
      "2     park   25  3333-1111\n",
      "3     jung   35  2222-3333\n",
      "4     hong   15  3333-2222\n",
      "Index(['name', 'age', 'tel'], dtype='object', name='user')\n"
     ]
    }
   ],
   "source": [
    "# DataFrame            정형데이터\n",
    "# Dictionary -> DataFrame\n",
    "d = {'name':['kim', 'lee', 'park', 'jung', 'hong'], \\\n",
    "     'age':[20, 30, 25, 35, 15], \\\n",
    "     'tel':['1111-1111', '1111-2222', '3333-1111', '2222-3333', '3333-2222'] }\n",
    "print( type( d ) )\n",
    "df = pd.DataFrame( d )\n",
    "print( type( df ) )\n",
    "# print( df )\n",
    "print( df.index )\n",
    "print( df.columns )\n",
    "print( df.values )\n",
    "print( type( df.values ) )          # numpy.ndarray\n",
    "\n",
    "df.index.name = 'num'\n",
    "print( df )\n",
    "print( df.index )\n",
    "print( df.columns )                 # ['name', 'age', 'tel']\n",
    "\n",
    "df.columns.name = 'user'\n",
    "print( df )\n",
    "print( df.columns )                 # ['name', 'age', 'tel'], dtype='object', name='user'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'numpy.ndarray'>\n",
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index(['count', 'unique', 'top', 'freq'], dtype='object')\n",
      "Index(['name', 'age', 'tel'], dtype='object')\n",
      "   name  age        tel\n",
      "a   kim   20  1111-1111\n",
      "b   lee   30  1111-2222\n",
      "c  park   25  3333-1111\n",
      "d  jung   35  2222-3333\n",
      "e  hong   15  3333-2222\n"
     ]
    }
   ],
   "source": [
    "# Numpy -> DataFrame\n",
    "# index columns 직접 설정해야 한다\n",
    "import numpy as np\n",
    "nd = np.array( [['kim', 20, '1111-1111'],\n",
    "                ['lee', 30, '1111-2222'], \n",
    "                ['park', 25, '3333-1111'], \n",
    "                ['jung', 35, '2222-3333'],\n",
    "                ['hong', 15, '3333-2222']] )\n",
    "print( type( nd ) )\n",
    "\n",
    "df = pd.DataFrame( nd )\n",
    "print( type( df ) )\n",
    "# print( df )\n",
    "df = pd.DataFrame( nd, index=['a', 'b', 'c', 'd', 'e'] )\n",
    "# print( df )\n",
    "df = pd.DataFrame( nd, index=['a', 'b', 'c', 'd', 'e'],  columns=['name', 'age', 'tel'] )\n",
    "# print( df )\n",
    "# print( df.describe() )\n",
    "desc = df.describe()\n",
    "print( desc.index )\n",
    "print( desc.columns )\n",
    "\n",
    "df = pd.DataFrame( [['kim', 20, '1111-1111'],\n",
    "                    ['lee', 30, '1111-2222'], \n",
    "                    ['park', 25, '3333-1111'], \n",
    "                    ['jung', 35, '2222-3333'],\n",
    "                    ['hong', 15, '3333-2222']], \\\n",
    "                  index=['a', 'b', 'c', 'd', 'e'], \\\n",
    "                  columns=['name', 'age', 'tel'] )\n",
    "print( df )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "  name  age        tel address\n",
      "a  kim   20  1111-1111      서울\n",
      "b  lee   30  1111-2222      수원\n"
     ]
    }
   ],
   "source": [
    "# print( df['name'] )                   # 결과 1차원  []\n",
    "# print( df[['name', 'age']] )          # 결과 2차원  [[]]\n",
    "# print( df[['name', 'tel']])\n",
    "# print( df[['name':'tel']] )           # 에러\n",
    "# print( df[['name', 'age', 'tel']] )   \n",
    "# print( df.name, df.age )\n",
    "# print( df[:] )\n",
    "\n",
    "# List [행][열]     Numpy[행,열]     Pandas[행][열]\n",
    "# print( df[0:2]['name'])\n",
    "# print( df[0:1]['age'] )\n",
    "# print( df['a':'c']['age'] )\n",
    "df['address'] = ['서울', '수원', '안산', '일산', '인천']\n",
    "# print( df )\n",
    "df['adult'] = df['age'] >= 20\n",
    "\n",
    "print( df['adult'][0] )\n",
    "\n",
    "del df['adult']\n",
    "# print( df )\n",
    "\n",
    "print( df[0:2][0:2] )                     # 컬럼이 모두 출력"
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
      "    a   b   c   d\n",
      "0  10  11  12  13\n",
      "1  14  15  16  17\n",
      "2  18  19  20  21\n",
      "3  22  23  24  25\n",
      "15\n",
      "    a   b\n",
      "0  10  11\n",
      "1  14  15\n",
      "    a   b   c\n",
      "0  10  11  12\n",
      "1  14  15  16\n",
      "    c   d\n",
      "2  20  21\n",
      "3  24  25\n"
     ]
    }
   ],
   "source": [
    "# iloc\n",
    "df = pd.DataFrame( np.arange(10, 26).reshape(4,4), columns=['a', 'b', 'c', 'd'] )\n",
    "print( df )\n",
    "# print( df[0:1] )\n",
    "# print( df[['a', 'c']])\n",
    "# print( df[['a':'c']] )          # 에러\n",
    "# print( df[1][0:2] )             # 에러\n",
    "# print( df[1]['a','c'] )         # 에러\n",
    "# print( df[1][['a','c']] )       # 에러\n",
    "\n",
    "# print( df[1,1] )                # 에러\n",
    "# print( df.loc[1,1] )            # 에러\n",
    "print( df.iloc[1, 1])\n",
    "print( df.iloc[0:2, 0:2])         # List [행][열]     Numpy[행,열]     Pandas[행][열]\n",
    "print( df.iloc[0:2, :-1] )\n",
    "print( df.iloc[2:, 2:] )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   name   age        tel\n",
      "가   kim  20.0  1111-1111\n",
      "나   lee  30.0  1111-2222\n",
      "다  park  25.0  3333-1111\n",
      "라  jung  35.0  2222-3333\n",
      "마  hong  15.0  3333-2222\n",
      "바   lim  19.0  2222-1111\n"
     ]
    }
   ],
   "source": [
    "# loc\n",
    "# print( df.loc[0:2, 'a':'c'] )\n",
    "# print( df.loc[:,:] )\n",
    "# print( df.loc[1,'a'] )\n",
    "\n",
    "d = {'name':['kim', 'lee', 'park', 'jung', 'hong'], \\\n",
    "     'age':[20, 30, 25, 35, 15], \\\n",
    "     'tel':['1111-1111', '1111-2222', '3333-1111', '2222-3333', '3333-2222'] }\n",
    "\n",
    "df1 = pd.DataFrame( d, index = ['가', '나', '다', '라', '마'] )\n",
    "# print( df1 )\n",
    "# print( df1.loc['가':'다', 'name':'age'] )\n",
    "# print( df1.loc[0:2, 'name'] )        # 에러\n",
    "# print( df1.loc['가', 'name'] )\n",
    "# print( df1.loc[:,:] )\n",
    "\n",
    "# 열추가 행추가\n",
    "df1.loc['바'] = ['lim', 19, '2222-1111']\n",
    "df1['address'] = ['서울', '대전', '부산', '광주', '울산', '전주']\n",
    "df1.loc[:, 'salary'] = [5000, 3000, 4000, 2500, 4500, 3500 ]\n",
    "df1.loc['사',['name', 'age', 'tel', 'address', 'salary']] = [ 'choi', 25, '3333-5555', '청주', 5000 ]\n",
    "\n",
    "# 열삭제 행삭제\n",
    "del df1['address']                        # 원본 수정\n",
    "df1 = df1.drop( 'salary', axis=1 )\n",
    "df1 = df1.drop( '사', axis=0 )\n",
    "\n",
    "print( df1 )"
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
      "   name   age        tel\n",
      "가   kim  20.0  1111-1111\n",
      "나   lee  30.0  1111-2222\n",
      "다  park  25.0  3333-1111\n",
      "라  jung  35.0  2222-3333\n",
      "마  hong  15.0  3333-2222\n",
      "바   lim  19.0  2222-1111\n",
      "   name   age        tel\n",
      "가   kim  20.0  1111-1111\n",
      "다  park  25.0  3333-1111\n",
      "마  hong  15.0  3333-2222\n",
      "   name        tel\n",
      "가   kim  1111-1111\n",
      "다  park  3333-1111\n",
      "마  hong  3333-2222\n",
      "   name   age        tel\n",
      "바   lim  19.0  2222-1111\n",
      "마  hong  15.0  3333-2222\n",
      "라  jung  35.0  2222-3333\n",
      "다  park  25.0  3333-1111\n",
      "나   lee  30.0  1111-2222\n",
      "가   kim  20.0  1111-1111\n",
      "         tel   age  name\n",
      "바  2222-1111  19.0   lim\n",
      "마  3333-2222  15.0  hong\n",
      "라  2222-3333  35.0  jung\n",
      "다  3333-1111  25.0  park\n",
      "나  1111-2222  30.0   lee\n",
      "가  1111-1111  20.0   kim\n"
     ]
    }
   ],
   "source": [
    "# print( df1.iloc[:, :] )\n",
    "# print( df1.iloc[0:2, 0:2] )\n",
    "# print( df1.iloc[1,1] )\n",
    "# print( df1.iloc['가':'다', 'name':'age'] )        에러\n",
    "print( df1.iloc[::, :] )                            # 시작:끝:증감값\n",
    "print( df1.iloc[0::2, :] )\n",
    "print( df1.iloc[::2, ::2] )\n",
    "print( df1.iloc[::-1, :])                           # 반대로\n",
    "print( df1.iloc[::-1, ::-1])                        # 반대로"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   name   age        tel\n",
      "가   kim  20.0  1111-1111\n",
      "나   lee  30.0  1111-2222\n",
      "다  park  25.0  9999-9999\n",
      "라  jung  35.0  2222-3333\n",
      "마  hong  15.0  3333-2222\n",
      "바   lim  19.0  9999-9999\n"
     ]
    }
   ],
   "source": [
    "# 수정\n",
    "# print( df1[0][2] )\n",
    "# print( df1['name'][0] )                  # [열][행]\n",
    "# df1['tel'][0] = '9999-9999'                # 경고\n",
    "df1.iloc[2,2] = '9999-9999'\n",
    "df1.loc['바', 'tel'] = '9999-9999'\n",
    "print( df1 )"
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
      "   name   age        tel address\n",
      "가   kim  20.0  1111-1111      수원\n",
      "나   lee  30.0  1111-2222      수원\n",
      "다  park  25.0  9999-9999      수원\n",
      "라  jung  35.0  2222-3333      수원\n",
      "마  hong  15.0  3333-2222      수원\n",
      "바   lim  19.0  9999-9999      수원\n",
      "   name   age\n",
      "나   lee  30.0\n",
      "다  park  25.0\n"
     ]
    }
   ],
   "source": [
    "# Boolean Indexing\n",
    "# df1 = df1.drop( 3, axis=1 )\n",
    "# df1 = df1.drop( 2, axis=0 )\n",
    "\n",
    "\n",
    "# print( df1.loc['가':'다', 'name':'age'] )\n",
    "# print( df1.loc['가':'다', ['name','tel']] )\n",
    "\n",
    "# print( df1.loc[ df1['age'] >= 25, 'name':'age' ] )\n",
    "# df2 = df1.loc[ df1['age'] >= 25, 'name':'age' ]\n",
    "# print( df2 )\n",
    "\n",
    "# print( df1.loc[ df1['name'] == 'kim', ['name','tel'] ] )\n",
    "\n",
    "df1.loc[:,'address'] = ''\n",
    "# df1['address'] = ''\n",
    "df1.loc[ df1['address'] == '', 'address'] = '서울'\n",
    "\n",
    "df1.loc[:, 'address'] = None\n",
    "df1.loc[ df1['address'].isnull(), ['address']] = '수원'\n",
    "\n",
    "print( df1 )\n",
    "\n",
    "print( df1.loc[ (df1['age']>=25) & (df1['age']<=30), ['name','age'] ] )\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1월     False\n",
      "2월     False\n",
      "3월     False\n",
      "4월     False\n",
      "5월     False\n",
      "6월     False\n",
      "7월     False\n",
      "8월     False\n",
      "9월     False\n",
      "10월    False\n",
      "12월     True\n",
      "Name: 2020, dtype: bool\n",
      "         2018      2019      2020  2021\n",
      "1월   1.697287 -0.203268 -1.576399   1.0\n",
      "2월  -1.153150  0.023844 -0.366072   3.0\n",
      "3월   0.777096 -0.730992 -2.056126  -4.0\n",
      "4월   0.286632  0.947788 -0.699996   NaN\n",
      "5월  -0.790142  0.084456 -1.144071   2.0\n",
      "6월  -1.653477  1.232188 -0.600124   NaN\n",
      "7월  -2.718446 -0.336595  0.511384   0.1\n",
      "8월   0.544666 -1.339653  0.480534   0.5\n",
      "9월  -0.750757  0.434551  0.509253   NaN\n",
      "10월 -0.672255 -2.414402 -1.183490   1.0\n",
      "12월       NaN  0.700000       NaN   NaN\n"
     ]
    }
   ],
   "source": [
    "# 결측치 제거\n",
    "data = np.random.randn( 10, 3 )\n",
    "df2 = pd.DataFrame( data )\n",
    "df2.columns = ['2018', '2019', '2020']\n",
    "df2.index = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월']\n",
    "df2['2021'] = [ 1., 3, -4, np.NaN, 2., np.NaN, 0.1, 0.5, np.NaN, 1. ]\n",
    "df2.loc['11월', :] = [ np.NaN, np.NaN, np.NaN, np.NaN] \n",
    "df2.loc['12월', :] = [ np.NaN, 0.7, np.NaN, np.NaN] \n",
    "\n",
    "# 제거\n",
    "# print( df2.dropna( how='all' ) )\n",
    "# print( df2.dropna( how='any' ) )\n",
    "df2.dropna( how='all', inplace=True )\n",
    "\n",
    "# 대체\n",
    "# print( df2['2021'].fillna( value=0.0 ) )\n",
    "# print( df2.fillna( value=10.0 ) )\n",
    "# df2['2021'].fillna( value=np.mean( df2['2021'] ), inplace=True )\n",
    "print( df2['2020'].isnull() )\n",
    "\n",
    "print( df2 )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         2018      2019      2020  2021\n",
      "1월  -0.350925 -1.550491 -0.812903   1.0\n",
      "2월   3.243104 -1.046351  1.230532   3.0\n",
      "5월  -0.724057  0.087019 -0.481029   2.0\n",
      "10월  0.194873  1.020260 -0.140905   1.0\n"
     ]
    }
   ],
   "source": [
    "# DataFram 분석용 함수\n",
    "data = np.random.randn( 10, 3 )\n",
    "df3 = pd.DataFrame( data )\n",
    "df3.columns = ['2018', '2019', '2020']\n",
    "df3.index = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월']\n",
    "df3['2021'] = [ 1., 3, -4, np.NaN, 2., np.NaN, 0.1, 0.5, np.NaN, 1. ]\n",
    "df3.loc['11월', :] = [ np.NaN, np.NaN, np.NaN, np.NaN] \n",
    "df3.loc['12월', :] = [ np.NaN, 0.7, np.NaN, np.NaN] \n",
    "\n",
    "# print( df3.count() )                  # NA 제외\n",
    "# print( df3.count( axis=1 ) )          # NA 제외\n",
    "# print( df3.min() )\n",
    "# print( df3.min( axis=1 ) )\n",
    "# print( df3.max() )\n",
    "# print( df3.max( axis=1 ) )\n",
    "# print( df3.sum() )\n",
    "# print( df3.mean() )\n",
    "# print( df3.median() )\n",
    "\n",
    "# print( df3.mad() )           # 거리. 음수\n",
    "# print( df3.var() )           # 분산\n",
    "# print( df3.std() )           # 표준편차\n",
    "\n",
    "# print( df3.cumsum() )\n",
    "\n",
    "# print( df3.idxmin() )\n",
    "# print( df3.idxmax() )\n",
    "# print( df3['2019'].argmin() )\n",
    "# print( df3['2019'].argmax() )\n",
    "\n",
    "# print( df3['2018'].corr( df3['2019'] ) )            # 상관계수\n",
    "# # 1 가까울수록 높고 0 가까울수록 낮다\n",
    "# print( df3['2018'].cov( df3['2019'] ) ) \n",
    "\n",
    "# print( df3.sort_index( axis=1, ascending=False ) )\n",
    "# print( df3.sort_index( axis=0, ascending=False ) )\n",
    "# print( df3.sort_values( by='2018', axis=0, ascending=False ) )\n",
    "# print( df3.sort_values( by='10월', axis=1, ascending=False ) )\n",
    "\n",
    "# print( df3['2019'].unique() )              # 중복제거한 값    NaN 도 출력\n",
    "# print( df3['2019'].value_counts() )        # 빈도수. NaN은 제외\n",
    "\n",
    "# print( df3['2021'].isin( [1., 2., 3., 4., 5.] ) )\n",
    "print( df3.loc[ df3['2021'].isin( [1., 2., 3., 4., 5.] ) ] )\n",
    "\n",
    "\n",
    "# print( df3 )"
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

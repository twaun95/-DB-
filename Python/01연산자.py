import numpy as np   
nums = np.arange(5)   
result = np.add.accumulate(nums)   
print(result)

import keyword
print( keyword.kwlist )
print( len( keyword.kwlist ) )

# 자료형
print( type( 10 ) )
print( type( 123456787892123432434534546456 ) )
print( type( 10.5 ) )
print( type( 'ABC' ) )
print( type( '10' ) )
print( 5 / 2 )
print( 5 // 2 )
print( type( 5 / 2 ) )
print( type( 5 // 2 ) )

a = "ABC"
b = "CDE"
print( a, b )
print( a + b )
print( "ABC" "CDE" )
print( "{} {}".format(a, b) )
print( "{1} {0}".format(a, b) )
print( 1234.567856785678 )
print( "{0:0.2f}".format( 1234.567856785678 ) )
print( "{0:10s}".format( "ABC" ) )

# in not~in is is~not
print( 'Hello' in 'Hello World!!!' )
print( 'Hello' not in 'Hello World!!!' )
print( 'Hello' is 'Hello' )
print( 'Hello' is 'Hello ' )
print( 'Hello' == 'Hello' )

print( 'A' + 'B' )
# print( 'A' - 'B' )

a = "Hello"
b = "Hello"
print( a == b )
print( a is b )
a += " Python"
b += " Python"
print( a == b )              # 내용
print( a is b )              # 주소

## 열거형 ##
# 문자열 #
name = "홍길동"
age = 20
print( "name : " + name )
print( "age : " + str( age ) )
print( "age :", age )
print( "=" * 20 )

print( "{0:<20}".format( name ) )
print( "{0:>20}".format( name ) )
print( "{0:^20}".format( name ) )
print( "{0:=^20}".format( name ) )

print( "name :", name, "\t", "age :", age )

print( str.count( "l" ) )
print( len( str ) )
print( str.find( "l" ) )
print( str.find( "!" ) )
print( str.index( "!" ) )
print( str.find( "x" ) )                  # -1
# print( str.index( "x" ) )               # ValueError   
print( ",".join( str ) )
print( ",".join( str.split() ) )

s = "     a   a    a       "
print( s )
print( s.lstrip() )
print( s.rstrip() )
print( s.strip() )

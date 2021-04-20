
### 변수 ###
## 연산자 ##
# 논리연산자 # 
c( T, T, F, F ) & c( T, F, T, F )     # TRUE FALSE FALSE FALSE
c( T, T, F, F ) | c( T, F, T, F )     # TRUE FALSE FALSE FALSE
c( T, T, F, F ) && c( T, F, T, F )    # TRUE  처음 하나만 비교
c( T, T, F, F ) || c( T, F, T, F )    # TRUE
c( F, T, F, F ) || c( F, F, T, F )    # FALSE

c( T, T, F, F ) + 1:4    

# 출력 #
print( 100 )
print( c( T, T, F, F ) + 1:4  )
cat( 100 )

# NA      SQL NULL
# NULL    Java NULL
# NaN     NaN
is.character( 'A' )       # T
is.character( 'ABC' )     # T
is.character( 10 )        # F
is.character( '월' )      # T
# is.character( A )       # 변수  

is.logical( T )
is.logical( F )
is.logical( 0 )           # false
is.logical( 1 )           # false
is.logical( '1' )         # false
1 && 1                    # TRUE        0 거짓 1 참
3 && 3                    # TRUE        0 이 아닌 값은 다 참

is.numeric( 5 )           # TRUE        숫자의 기본값은 실수
is.numeric( 5.5 )         # TRUE
is.double( 5 )            # TRUE
is.double( 5.5 )          # TRUE
is.integer( 5 )           # FALSE
is.integer( 5.5 )         # FALSE

is.na( NULL )             # logical(0) SQL NULL
is.na( 0 )
is.na( '' )

is.null( NULL )           # JAVA NULL
is.null( 0 )
is.null( '' )

is.nan( NULL )            # logical(0)       
is.nan( 0 )
is.nan( '' )
is.nan( 'ABC' )
is.nan( NaN )             # TRUE
is.nan( 0/0 )             # TRUE

# 강제형변환
# 자동형변환              큰자료형 > 작은자료형
is.character( as.character( 5 ) )     # 숫자 -> 문자
is.numeric( as.numeric( '10' ) )      # 문자 -> 숫자
is.numeric( as.numeric( 'ABC' ) )     # NA
is.double( 5 )    
is.integer( as.integer( 5 ) )         # 실수 -> 정수
is.logical( as.logical( 1 ) )         # 숫자 -> 논리값
is.logical( T )

a = 10
a <- 20
class( a )                # numeric
a <- 'ABC'
class( a )                # character
class( '10' )
class( 5.5 )
class( T )
class( c( 1, 2, 3 ) )
class( c( '1', '2', '3' ) )

class( c( '1', '2', '3', 4, 5 ) )       # character
class( c( 1, 2, 3, '4', '5' ) )         # character

### 리스트 ###
## 베열 ##
# Scala #
a <- 10               # 변수 메모리할당. 값 1개 저장
print( a )

# Vector #
# 1차월 배열          같은 자료형의 모임
? c
b <- c( 1, 2, 3, 'ABC' )
print( b[1] )
class( b )
mean( b )             # NA
is.vector( b )        # TRUE

d <- c( 56, 43, 78, 12, 91 )
class( d )            # numeric
is.vector( d )        # TRUE
mean( d )
median( d )           # sort() 포함
sort( d )
sum( d )
min( d )
max( d )

sqrt( d )             # 제곱근
round( sqrt( d ) )
round( sqrt( d ), 2 )
trunc( sqrt( d ) )    
cumsum( d )
cumprod( d )
cummax( d )           # 56 56 78 78 91
cummin( d )           # 56 43 43 12 12

order( d )            # 4 2 1 3 5
sort( d, decreasing=T )

e <- sort( d )
e[1]
e[1:3]

f <- e[ c(1, 2, 3) ]  # c 인덱스배열
f + 1
f ** 2

f[ f<50 ]             # 12 43
f[ c( T, F, T ) ]     # 12 56

names( f )
names( f ) <- c( 'A', 'B', 'C' )
f[1]
f['A']                # Map Dictionary
f
names( f ) <- letters[1:3]
f

g <- c( -5:5 )
g

h <- seq( 1, 10, 2 )
h <- seq( 10 )
h <- seq( 10, 2 )
h <- seq( to=10, by=2 )

# 랜덤
sample( 1:20, 5 )
sort( sample( 1:45, 6 ) )
sort( sample( 1:45, 6, replace=F ) )

# 벡터추가
d
h
append( d, h )
k <- append( h, d )
l <- replace( k, c( 2, 3), c( 40, 50 ) )

# 같은 값 발생
rep( 10, 5 )
rep( 1:3, 5 )         # 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3
rep( 1:3, each=5 )    # 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3

# 벡터 연산
a <- c( 1:3 )
b <- c( 4:6 )
a + b 
a - b
a + 1 
a * b
a / b
a %% b                # 나머지
a > b
a < b
a == b
a != b 
summary( a )
summary( sort( sample( 1:45, 6 ) ) )

# NA
d <- seq( 1, 10, 2 )
e <- c( 10, 20, NA, 40, NA )
d + e                   # NA 연산 불가
sum( e )                # NA
sum( e, na.rm=T )
mean( e, na.rm=T )

f <- na.omit( e )
f
length( f )

d + f

ls()
rm( list= ls())
ls()
rm( list=ls() )

a <- sample(1:10)
a
a <- sample(1:10, replace=T) #중복 o
a

a <- sample( -20:20, 20, replace=F )
a
a[ a>0 ]
which( a>0 )          # sort 된 상태
min( a )
max( a )
which.max( a )
which.min( a )

month.name
month.korname <- c('1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월')

month.korname
month.korname[5]


# Matrix #
# 2차원 배열    1차원 배열의 집합
v1 <- c( 1, 2, 3 )
v2 <- c( 4, 5, 6 )
v3 <- c( 7, 8, 9 )
m1 <- c( v1, v2, v3 )
m1
m2 <- rbind( v1, v2, v3 )     # row 행기반
m2
m3 <- cbind( v1, v2, v3 )     # column 열기반
m3

# [행, 열]                    # [행][열]
m2
m2[2, 2]
m2[1:3]
m2[1:2, 1:2]
m2[, 3]

rownames( m2 ) <- LETTERS[1:3]
colnames( m2 ) <- c( '가', '나', '다' )
m2
m2['B', '나']
# m2['A':'B']                 # 이름으로 indexing 불가
m2[1:3]
rownames( m2 ) <- NULL
colnames( m2 ) <- NULL
m2

# matrix
rm( list=ls() )
m1 <- matrix( LETTERS )        # 26행, 1열
m1
# m2 <- matrix( LETTERS, nrow=5, ncol=5 )       # 에러 발생
m2 <- matrix( LETTERS[1:25], nrow=5, ncol=5 )
m2

m3 <- matrix( c(1:25), nrow=5 )
m3
mean( m3 )                    # 전체
sum( m3 )
mean( m3[1, ] )
sum( m3[2, ])
mean( m3[, 2] )
sum( m3[, 3] )
sum( m3[, 1:2] )               # 1열 2열 전체행의 합계
rowSums( m3 )
colSums( m3 )

apply( m3, 1, sum )           # 1행
apply( m3, 1, mean )
apply( m3, 1, max )
apply( m3, 1, min )

apply( m3, 2, sum )           # 2열
apply( m3, 2, mean )
apply( m3, 2, max )
apply( m3, 2, min )


# array #
v1 <- c( 1:10 )
class( v1 )
v1 <- array( 1:10 )
class( v1 )

v2 <- matrix( 1:25, nrow=5 )
class( v2 )                       # "matrix" "array" 
v2
v2 <- array( 1:25, dim=c(5,5) )
class( v2 )                       # "matrix" "array" 
v2

v3 <- array( 1:45, dim=c(3,3,5) )
class( v3 )                       # "array"
v3


# Factor #
v <- c( 1:10 )
summary( v )  
f <- factor( v )
class( f )
summary( f )

d <- c( '월', '금', '수', '화', '목', '월', '월', '화', '금' )
f1 <- factor( sort( d ) )
f1
summary( f1 )


## DataFrame #

v1 <- c(1,2,3)
v2 <- c(4,5,6)
v3 <- c(7,8,9)

m1 <- rbind(v1,v2,v3)
m1
m1[1,]
m1[,1]

s <- sample(0:19, replace=F)
s
which(s>0)

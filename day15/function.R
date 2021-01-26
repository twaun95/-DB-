### 제어문 ###
## 조건문 ##


# if 참;


# if 참;
# else 거짓;
num <- sample( 1:10, 1 )
if( num %% 2 == 0 ) {
  print( "짝수" )         # 참
} else{
  print( "홀수" )         # 거짓
}


# if 참;
# else if 참;
# else if 참;
# else 거짓;

score <- sample( 1:100, 1 ) 
if( score >= 90 ) {
  cat( score, ': A학점' ) 
} else if( score >= 80 ) {
  cat( score, ': B학점' ) 
} else if( score >= 70 ) {
  cat( score, ': C학점' ) 
} else if( score >= 60 ) {
  cat( score, ': D학점' ) 
} else {                    # 나머지
  cat( score, ': F학점' )  
}

if( score >= 90 ) {               # 범위 조건. 조건문을 모두 실행.
  cat( score, ': A학점' ) 
}
if( score >=80 && score <90 ) {
  cat( score, ': B학점' ) 
}
if( score >=70 && score <80 ) {
  cat( score, ': C학점' ) 
}


# switch 함수

# year <- sample( 1:2050, 1 )
year <- 2021
level <- year %% 12
# paste( c("char1", "char2", ...), sep = "")
level <- paste( level, sep='' )
cat( '연도 : ', year )
switch( level,
        '1'='닭띠',
        '2'='개띠', 
        '3'='돼지띠', 
        '4'='쥐띠', 
        '5'='소띠', 
        '6'='호랑이띠', 
        '7'='토끼띠', 
        '8'='용띠', 
        '9'='뱀띠', 
        '10'='말띠',
        '11'='양띠',
        '원숭이띠')


## 반복문 ##

# for
# for( 초기값; 조건; 증감값 ) {}      지원안함
# for( i=1; i<11; i++ ) {}

# for( 변수 in 나열형 ) {}
for( i in c(1:10) ) {
  print( i )
}
for( i in seq( 1, 10, 2) ) {
  print( i )
}
rm( month )

for( i in month.name ) {            # Vector
  print( i )
}
class( month.name )

sum <- 0
for( i in c( 1:100 ) ) {
  sum <- sum + i
}
cat( '합 : ', sum )


# while
# do ~ while이 없다. 
# repeat 로 무한루프를 사용한다. 
# break, next(continue) 
# break~label, continue~label 은 사용할 수 없다.

# for( 초기값; 조건; 증감값 ) {}      지원안함
i <- 1              # 초기값      
while( i<11 ) {     # 조건
  print( i )
  i <- i+1          # 증감값
}


i <- 1              # 초기값      
while( i<11 ) {     # 조건        끝낼 때
  i <- i+1          # 증감값
  print( i )
}

i <- 0
while( TRUE ) {
  i <- i+1
  if( i>10 ) break;
  if( i%%2 == 1 ) next;       # continue 반복문의 처음으로 돌아가라
  print( i )
}

# 1 ~ 100 누적을 최초로 2000을 넘는 값, 합계를 출력
# 63 2016
i <- 0
sum <- 0
while( TRUE ) {
  i <- i + 1
  sum <- sum + i
  if( sum >= 2000 ) break;
}
cat( 'i : ', i, 'sum : ', sum )



### 사용자 정의 함수 ###

# 함수명 <- function([매개변수]) {
#   함수의 수행 코드
#   [return 값]			# return도 함수. 가급적 주도록 한다. 
# }

# 함수명( 매개변수 )
# 변수명 <- 함수명( 매개변수 ) 

# 반복적인 내용을 묶어서 처리
# 호출한 자리로 돌아 온다
# 재활용 재사용


print( 'Hello World!!!!!' )
print( 'Hello World!!!!!' )
print( 'Hello World!!!!!' )

sub <- function() {                 # 선언
  print( 'Hello World!!!' )         # 구현
  return()
}
sub()                               # 호출
sub()
sub()

# 매개변수        인수 인자 argument parameter
hap <- function() {
  a <- 2
  b <- 5
  print( a+b )
}
hap()

hap <- function( a, b ) {
  print( a+b )
}
hap( 5, 2 )
hap( 10, 20 )
# hap( 5 )                에러
# hap( 5, 2, 3 )          에러

# 매개변수의 초기값
cha <- function( a=0, b=0 ) {
  print( a-b )
}
cha( 5, 2 )
cha( 5 )

# Variable Argument
gob <- function( ... ) {          # ... 배열
  sum <- 1
  for( arg in c(...) ) {
     sum <- sum * arg
  }
  print( sum )
}
gob( 5 )
gob( 5, 3 )
gob( 5, 3, 2 )
gob( 5, 3, 2, 5 )
gob( 5, 3, 2, 'A' )
gob( 5, 3, 2, NULL )
gob( 5, 3, 2, NA )


msg <- function( ... ) {
  for( arg in c(...) ) {
    cat( arg, sep=''  )   
  }
}
msg( 'A' )
msg( 'A', 'B' )
msg( 'A', 'B', 'C' )
msg( 'A', 'B', 'C', 10 )


# 호출시 함수가 정의하고 있는 매개변수 사양에 맞춰서 아규먼트를 전달해야 한다.
# 리턴값이 없는 함수는 NULL이 리턴
# 리턴값은 return() 함수를 호출하여 처리 
# return()문이 생략된 경우에는 마지막 출력된 데이터 값이 자동으로 리턴	
# 아규먼트의 타입을 제한하려는 경우에는 is.xxxx() 함수를 활용
# 기본값을 갖는 매개변수 선언하여 선택적으로 전달되는 아규먼트를 처리할 수 있다.
# 아규먼트의 개수와 타입을 가변적으로 처리 가능하며 리턴값의 경우에도 선택적으로 처리가능하다.
# 함수 안에서 만들어진 지역변수는 함수 내에서만 사용 가능하다.
# 함수 안에서 만들어지지 않은 변수를 사용할 때는 전역 변수를 사용하는 결과가 된다.
# 함수 내에서 전역변수에 값을 저장하려는 경우 대입연산자로 <<-를 사용한다.

# 리턴
rm( list=ls() )

hap <- function( a=0, b=0 ) {
  print( a+b )
}
hap <- function( a=0, b=0 ) {
  return( a+b )
}
print( hap( 5, 2 ) )
sum <- hap( 10, 20 )
cat( '합 : ', sum )


# 전역변수 / 지역변수           영역 안에서 선언한 변수 영역 안에서만 사용
# 전역변수
hap <- function() {
  a <- 10                       # 지역변수
}
cha <- function() {
  b <- 20                       # 지역변수
  print( a-b )
}
cha()                           # a 변수 에러
print( b )                      # b 변수 에러


bb <- 100
bb <- 10        # 변수 하나. 수정

aa <- 100       # 전역변수
gop <- function() {
  aa <- 10      # 지역변수
  print( aa )   # 전역변수 / 지역변수       지역변수에 우선권
  
  aa <- 20      # 지역변수
  aa <<- 200    # 전역변수
}
print( aa )     # 전역변수
gop()


hap <- function( a=0, b=0 ) {
  print( a+b )
}
cha <- function( a=0, b=0 ) {
  print( a-b )
}
gop <- function( a=0, b=0 ) {
  print( a*b )
}
hap( 5, 2 )
cha( 5, 2 )
gop( 5, 2 )

a <- 5
b <- 2
hap <- function() {
  print( a+b )
}
cha <- function() {
  print( a-b )
}
gop <- function() {
  print( a*b )
}
hap()
cha()
gop()

### 예외처리 ###

# 에러      문법이 틀린 경우. 수정.
# 경고      문법은 맞다. 실행 시 문제가 발생. 요즘 언어들은 경로를 에러로 변경. 수정
# 예외      문법은 맞다. 실행 시 문제가 발생. 에러 X. 처리

catch <- function( a ) {
  tryCatch(
    {
      if( a == 0 ) error()
      else if( a == 1 ) warning()
      else print( '정상실행' )
    },
    error=function( e ){
      cat( '에러\n' )
    },
    warning=function( w ){
      cat( '경고\n' )
    },
    finally={
      print( "프로그램 끝" )
    }
  ) 
}
catch( 0 )
catch( 1 )
catch( 2 )
















### 데이터 처리 ###

## 파일입출력 ##
getwd()

# 텍스트 파일 #
rm(list=ls())
nums <- scan( 'sample_num.txt' )
class( nums )
nums
nums[1]

words <- scan( 'sample_ansi.txt', what='', encoding='UTF-8' )
words
class( words )
words[1]

words <- scan( 'sample_utf8.txt', what='', encoding='UTF-8' )
words
class( words )
words[1]

lines <- readLines( 'sample_utf8.txt', encoding='UTF-8' )
class( lines )
lines[1]
lines






## 데이터 전처리 ##
## dplyr 패키지 ##
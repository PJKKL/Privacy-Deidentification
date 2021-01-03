# 필요 라이브러리
library(readxl)
library(ggplot2) #시각화
library(tidyverse)
library(lubridate)
library(dplyr)

# csv 읽어오기
data <- read.csv("C:/Users/user/")

# 데이터 속성
str(data)

# 데이터 요약 정보(최소, 최대, 분위)
summary(data)

# 주소 자르기(첫 번째 문자와 두 번째 문자만 잘라서 저장
data$주소 <- substr(data$주소, 1, 2)


# 박스플롯
# 박스플롯 그림
boxplot(data$나이)

# 박스플롯 통계치
boxplot(data$나이)$stats

# boxplot(data$전년도.누적금액)
# boxplot(data$전년도.누적금액)$stats

# boxplot (점으로 나타낸 박스플롯)
ggplot(data, aes(x = 전년도.누적금액, y = 구매액)) + geom_boxplot()

# 히스토그램
ggplot(data, aes(x = 전년도.누적.구매횟수)) + geom_histogram()

# 히스토그램(너비를 1로)
ggplot(data, aes(x = 대분류)) + geom_histogram(binwidth = 1)
#ggplot(data, aes(x = 제품코드)) + geom_histogram()
#ggplot(data, aes(x = buying_hour)) + geom_histogram(binwidth = 1)


# 일정한 구조 생성
# 1 단위로 24까지
x_axis=seq(0,24,by=1)
# 1000 단위로 4만까지
y_axis=seq(0,40000,by=1000)

# x, y축을 사용자의 지정값으로 표시
axis(side=1,at=x_axis)
axis(side=2,at=y_axis_tick)

# 지수표기를 숫자표기로 바꿈
options(scipen=999)

# 콘솔창에서 값별로 테이블 출력
table(data$전년도.누적.구매횟수)

# 대분류가 1이고 중분류가 1인 값 카운트
length(which((data$대분류 == '1') & (data$중분류 == '1')))
# 대분류가 1이고 중분류가 2인 값 카운트
length(which((data$대분류 == '1') & (data$중분류 == '2')))
# 대분류가 1이고 중분류가 3인 값 카운트
length(which((data$대분류 == '1') & (data$중분류 == '3')))

# 구매액 숫자 확인
length(which((data$구매액 < 60000))) # 224029
length(which((data$구매액 < 60000) & data$구매액 >= 30000)) # 183327
#length(which((data$구매액 < 100000))) # 375051

length1 <- data %>% filter(구매액>=30000 & 구매액 < 60000)
median(length1$구매액) # 44400

length2 <- data %>% filter(구매액>=60000 & 구매액 < 100000)
median(length2$구매액) # 72500

length3 <- data %>% filter(구매액 >= 100000)
median(length3$구매액)

View(data)

length4 <- data %>% filter(구가 >= 100000)
median(length3$구매액)

# 대분류, 중분류, 세분류로 묶은 다음 각각의 값에 따라 카운트
ex3 <- data%>%group_by(대분류, 중분류, 세분류)%>%tally()

# n이 10보다 작은 값만 뽑아낸 다음 그 합을 구함
val2 <- ex4 %>% filter(n<10)
sum(val2$n)

# csv파일 쓰기
write.csv(new_dataset2, "C:/Users/user/Desktop/id/PRE/produceC.csv")


#ex9 <- data%>%group_by(나이, 제품코드)%>%tally()
#View(ex9)
#val3 <- ex9 %>% filter(n<=10)
#age_tpay <- data2%>%group_by(나이, 전년도.누적금액)%>%tally()

# data와 ex4를 제품코드 값을 기준으로 묶은 다음, new_dataset2의 n 값이 10보다 작으면 NA
new_dataset2 <- data %>% left_join(ex4, by = "제품코드")
for(num in 1:nrow(new_dataset2)){
  if(new_dataset2[num, "n"] < 10){
    new_dataset2[-num, "제품코드"] = NA
  }
}

new_dataset2 = new_dataset2[!is.na(new_dataset2$제품코드),]

new_dataset2$month <- substr(new_dataset2$최종구매일자, 6, 7)
new_dataset2$day <- substr(new_dataset2$최종구매일자, 9, 10)
View(new_dataset2$day)
new_dataset2 <- new_dataset2 %>%
  mutate(date = ifelse(day <= 10, "초",
                       ifelse(day <= 20 , "중", "후")))
new_dataset2$최종구매일자 <- paste(new_dataset2$month, new_dataset2$date)
data2 <- subset(new_dataset2, select = -c(day, month, date, n))


write.csv(data2, "C:/Users/user/Desktop/id/PRE/data444.csv")


new_dataset2 <- subset(new_dataset2, select = -n)

if (new_dataset2$최종.주문시간 != "최종.주문시간")
{
  new_dataset2$최종.주문시간 = NA
}

write.csv(new_dataset2, "C:/Users/user/Desktop/id/PRE/dataresult5.csv")

ex5<- data%>%group_by(제품코드, 나이)%>%tally()

ex5$나이 <- ifelse(ex5$나이 >= 80, "80대 이상",
         ifelse(ex5$나이 >= 70, "70대",
               ifelse(ex5$나이 >= 60, "60대",
                     ifelse(ex5$나이 >= 50, "50대",
                            ifelse (ex5$나이>=40, "40대",
                                    ifelse(ex5$나이 >= 30, "30대",
                                           ifelse(ex5$나이 >= 20, "20대")))))))


ex5<- ex6%>%group_by(제품코드, 나이)%>%tally()

ex7<- ex6%>%group_by(나이)%>%tally()

ex9 <- ex6%>%group_by(나이, 제품코드)%>%tally()

val3 <- ex9 %>% filter(n<10)

age20 <- val3 %>% filter(나이==">=80")

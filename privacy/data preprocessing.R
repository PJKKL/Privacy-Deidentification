# 필요 패키지 설치
# sqldf 먼저 설치 -> 설치 안되면 위쪽 두 패키지도 설치
# install.packages("DBI")
# install.packages("RSQLite")
# install.packages("sqldf")

# 필요 패키지 불러오기
library(sqldf)
library(dplyr)
library(ggplot2)

# CSV 파일 불러오기, 맨 위의 표 제목은 헤더로
df <- read.csv("C:/Users/user/Desktop/id/PRE/newdata_jibang.csv", header = TRUE)
df2 <- read.csv("C:/Users/user/Desktop/id/PRE/output2.csv", header = TRUE)
df4 <- read.csv("C:/Users/user/Desktop/id/PRE/newdata_jibang_1029", header = TRUE)


df3 <- read.csv("C:/Users/user/Desktop/id/PRE/newdata_jibang_1029.csv", header = TRUE)
View(df3)
View(df2)

# 최종구매일자의 달(ex. 2020-07-28 -> 7만 뽑아냄)
df$최종구매일자 <- substr(df$최종구매일자, 7, 7)

# 제품코드 10보다 작으면 NA 처리 및 삭제
#code <- df%>%group_by(제품코드)%>%tally()
#df <- df %>% left_join(code, by = "제품코드")
#replace(df$제품코드, df$n<15, NA) -> df$제품코드
#df = df[!is.na(df$제품코드),]

View(code)
View(df2)

# 입력 안되는 이름 바꾸고 SQL 쿼리문
df3 <- rename(df3, "전년도누적금액" = "전년도.누적금액")
df3 <- rename(df3, "전년도누적구매횟수" = "전년도.누적.구매횟수")

# 수량이 NULL인 것 삭제
replace(df$수량, df$수량 == "NULL", NA) -> df$수량
df = df[!is.na(df$수량),]

###############
# 세분류 포함 #
###############
df3$최종구매일자 <- substr(df3$최종구매일자, 7, 7)
code3 <- df3%>%group_by(대분류, 중분류, 세분류)%>%tally()
df3 <- df3 %>% left_join(code3, by = c("대분류", "중분류", "세분류"))

# 대분류, 중분류, 소분류 별로
code <- df%>%group_by(대분류, 중분류, 세분류)%>%tally()
df <- df %>% left_join(code, by = c("대분류", "중분류", "세분류"))
View(df)
sum(code$n<100)

#code <- df2%>%group_by(대분류, 중분류, 세분류)%>%tally()
#df2 <- df2 %>% left_join(code, by = c("대분류", "중분류", "세분류"))
write.csv(df2, "C:/Users/user/Desktop/id/PRE/daejungso.csv")
# 대분류, 중분류, 소분류 적은 것 삭제
replace(df$세분류, df$n<50, NA) -> df$세분류
df = df[!is.na(df$세분류),]


replace(df3$세분류, df3$n<50, NA) -> df3$세분류
df3 = df3[!is.na(df3$세분류),]

replace(df3$수량, df3$n!= "1", "1") -> df3$수량

anonymity1 <- sqldf("select count(*) from df group by 나이, 주소, 전년도누적금액, 전년도누적구매횟수, 대분류, 중분류, 세분류")
View(anonymity1)

anonymity2 <- sqldf("select count(*) from df group by 나이, 주소, 전년도누적금액, 전년도누적구매횟수, 성별")
View(anonymity2)

# 성별, 나이, 주소, 전년도.누적금액, 전년도.구매횟수, 최종구매일자, 구매액
anonymity3 <- sqldf("select 일련번호, count(*) from df group by 성별, 나이, 주소, 전년도누적금액, 전년도누적구매횟수, 최종구매일자, 구매액")
View(anonymity3)
sum(anonymity3$`count(*)`<3)

# 3 + 주말여부
anonymity4 <- sqldf("select 일련번호, count(*) from df group by 성별, 나이, 주소, 전년도누적금액, 전년도누적구매횟수, 최종구매일자, 구매액, 주말여부")
View(anonymity4)

sum(anonymity4$`count(*)`<3)

View(df3)
#4 : 모든 것 - 수량
anonymity5 <- sqldf("select *, count(*) as cnt from df3 group by 성별, 나이, 주소, 전년도누적금액, 전년도누적구매횟수, 최종구매일자, 구매액, 주말여부, 대분류, 중분류, 세분류")
View(anonymity5)

#sum(anonymity5$`count(*)`<2)

df <- df %>% left_join(anonymity5, by = c("성별", "나이", "주소", "전년도누적금액", "전년도누적구매횟수", "최종구매일자", "구매액", "주말여부", "대분류", "중분류", "세분류"))

df3 <- df3 %>% left_join(anonymity5, by = c("성별", "나이", "주소", "전년도누적금액", "전년도누적구매횟수", "최종구매일자", "구매액", "주말여부", "대분류", "중분류", "세분류"))
View(df3)

write.csv(df3, "C:/Users/user/Desktop/id/PRE/ohno2.csv")


###############
# 세분류 제외 #
###############

# 대분류, 중분류, 소분류 별로
code <- df%>%group_by(대분류, 중분류)%>%tally()
df <- df %>% left_join(code, by = c("대분류", "중분류"))

library(ggplot2)
View(code)

sum(code$n<100)

# 대분류, 중분류, 소분류 적은 것 삭제
replace(df$중분류, df$n<50, NA) -> df$중분류
df = df[!is.na(df$중분류),]

#4 : 모든 것 - 수량
anonymity6 <- sqldf("select *, count(*) from df group by 성별, 나이, 주소, 전년도누적금액, 전년도누적구매횟수, 최종구매일자, 구매액, 주말여부, 대분류, 중분류")
View(anonymity6)

sum(anonymity6$`count(*)`<3)

write.csv(anonymity6, "C:/Users/user/Desktop/id/PRE/newdata_result2.csv")

###########################
# 구간중앙값, 중간값 비교 #
###########################
# 데이터 불러오기
data <- read.csv("C:/Users/user/Desktop/id/PRE/data_v7.csv", header = TRUE)

#전년도 누적 구매횟수 0에서 30까지
gugan30to100 <- data %>% filter(전년도.누적.구매횟수 < 30)
median(gugan30to100$전년도.누적.구매횟수)
v1 <- gugan0to30$전년도.누적.구매횟수 - 15
v1 <- abs(v1)
sum(v1)
v2 <- gugan0to30$전년도.누적.구매횟수 - 5
v1 <- abs(v2)
sum(v2)

#전년도 누적 구매횟수 30에서 100까지
gugan30to100 <- data %>% filter(전년도.누적.구매횟수 >= 30 & 전년도.누적.구매횟수 < 100)
median(gugan30to100$전년도.누적.구매횟수)
v3 <- gugan30to100$전년도.누적.구매횟수 - 65
v3 <- abs(v3)
sum(v3)

v4 <- gugan30to100$전년도.누적.구매횟수 - 60
v4 <- abs(v4)
sum(v4)

#전년도 누적 구매횟수 100 이상
gugan100to2 <- data %>% filter(전년도.누적.구매횟수 >= 100 & 전년도.누적.구매횟수 < 3500)
gugan100to2 %>% summarise(n=n())
median(gugan100to2$전년도.누적.구매횟수)
v5 <- gugan100to2$전년도.누적.구매횟수 - (3500 - 100) / 2
v5 <- abs(v5)
sum(v5)

v6 <- gugan100to2$전년도.누적.구매횟수 - 1720
v6 <- abs(v6)
sum(v6)

#구매액 분포 보기
ggplot(data, aes(x = 구매액)) + geom_histogram(binwidth = 100) + xlim(0, 50000)
ggplot(data, aes(x = 구매액)) + geom_histogram(binwidth = 1) + xlim(0, 100000)

#구매액 0에서 50000원까지
aeck0to50000 <- data %>% filter(구매액 < 50000)
median(aeck0to50000$구매액) #43300

gumaeaeck1 <- aeck0to50000$구매액 - 25000
gumaeaeck1 <- abs(gumaeaeck1)
sum(gumaeaeck1) #2630109280

gumaeaeck2 <- aeck0to50000$구매액 - 43300
gumaeaeck2 <- abs(gumaeaeck2)
sum(gumaeaeck2) #1850538740

#구매액 50000원에서 100000원까지
aeck50000to100000 <- data %>% filter(구매액 > 50000 & 구매액 < 100000)
median(aeck50000to100000$구매액) #63400

gumaeaeck3 <- aeck50000to100000$구매액 - 75000
gumaeaeck3 <- abs(gumaeaeck3)
sum(gumaeaeck3) #3355914610

gumaeaeck4 <- aeck50000to100000$구매액 - 63400
gumaeaeck4 <- abs(gumaeaeck4)
sum(gumaeaeck4) #2465728870

#구매액 100000원에서 끝까지
aeck10to <- data %>% filter(구매액 > 100000 & 구매액 < max(data$구매액))
median(aeck10to$구매액) #141500

gumaeaeck5 <- aeck10to$구매액 - (max(data$구매액) - 100000) / 2
(max(data$구매액) - 100000) / 2
gumaeaeck5 <- abs(gumaeaeck5)
sum(gumaeaeck5) #222309051600

gumaeaeck6 <- aeck10to$구매액 - 141500
gumaeaeck6 <- abs(gumaeaeck6)
sum(gumaeaeck6) #5708020060

ohno2 <- read.csv("C:/Users/user/Desktop/id/PRE/ohno2.csv", header = TRUE)
replace(ohno2$수량, ohno2$수량 != "1", "1") -> ohno2$수량

View(ohno2)

write.csv(ohno2, "C:/Users/user/Desktop/id/PRE/ohno3.csv")

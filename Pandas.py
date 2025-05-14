import pandas as pd
# Pandas 는 서로 다른 유형들의 데이터들을 공통의 포맷으로 정리하는 것.
# 여러 포맷들을 하나로 통일하기 위해 Series 와 DataFrame 이라는 구조화된 data type 을 제공함.
# Series : 1D array 형태로, index 와 data value 는 일대일로 대응이 되는 구조. dictionary 와 list 를 series 로 변환가능
# DataFrame : 여러 개의 Series 들의 집합체.

df = pd.DataFrame([
    ['Apple', 7, 'Fruit'],
    ['Banana',3,'Fruit'],
    ['Beef',5,'Meal'],
    ['Beer',4,'Meal']],
    columns=['Name','Frequency','Type']
)

print(df)
print(df.groupby(['Type']).sum())

     Name  Frequency   Type
0   Apple          7  Fruit
1  Banana          3  Fruit
2    Beef          5   Meal
3    Beer          4   Meal
              Name  Frequency
Type
Fruit  AppleBanana         10
Meal      BeefBeer          9

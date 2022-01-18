def convert_c_to_f(cel_value):
    return cel_value * 9.0 / 5 + 32

test = "GGG" 
print(test)

# 이때 import fah_converter를 해주는 것만으로도 터미널에서 print(test)가
# 실행되는 것을 알 수 있다. 이를 방지해주기 위해서는 모듈을 호출할 때의 범위를 정해주어야 하는데,
# if __name__ == "__main__"을 통해 방지해 줄 수 있다.
import random

def get_lotto_numbers():
    lotto_numbers = []

    while True:
        if len(lotto_numbers) == 6: # 번호 6개 저장이 돼있으면 반복문 종료
            break
        number = random.randint(1, 45) # 1 ~ 45 사이의 정수를 랜덤으로 반환
        if number in lotto_numbers: # 반환받은 숫자가 이미 리스트에 저장된 숫자라면 그냥 지나감
        # if ~ in ~ : 요소가 있는지 검사
            continue
        else: # 반환받은 숫자가 리스트에 저장되지 않은 숫자라면 리스트에 저장
            lotto_numbers.append(number)
    return sorted(lotto_numbers) # 저장된 난수리스트를 오름차순으로 정렬하여 반환

if __name__ == "__main__":
    lotto_Numbers = get_lotto_numbers()
    print(lotto_Numbers)


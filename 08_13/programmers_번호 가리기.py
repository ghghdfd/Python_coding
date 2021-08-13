##번호 가리기

def solution(phone_number):
    answer = ''
    phone_number=phone_number.replace(phone_number[:-4],'*'*len(phone_number[:-4]))
    return phone_number

phone_number="01033334444"	
solution(phone_number)
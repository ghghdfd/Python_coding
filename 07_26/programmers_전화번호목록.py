## 전화번호 목록

def solution(phone):
    answer=True
    phone.sort()
    for i in range(len(phone)-1):
        if phone[i+1].startswith(phone[i]):
            answer=False
    return answer

phone=["119", "97674223", "1195524421"]
answer=solution(phone)
print(answer)
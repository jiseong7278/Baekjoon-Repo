def solution(a, b):
    answer = ''
    
    day = ("FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU")
    
    month_days = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    
    days_sum = 0
    
    for i in range(1, a):
        days_sum += month_days[i]
    
    days_sum += b
    
    friday_check = days_sum % 7
    
    answer = day[friday_check-1]
    
    return answer
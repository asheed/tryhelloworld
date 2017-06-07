from datetime import datetime
hour = datetime.now().hour
minute = datetime.now().minute

if hour < 12:
    ampm = '오전'
    print('오전입니다.')
else:
    ampm = '오후'

print("현재 시각은", ampm, hour - 12, "시", minute, "분 입니다.")


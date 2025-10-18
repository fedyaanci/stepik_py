n = int(input())

if n == 0:
    print("Вы можете стать первым, кто решит эту задачу")
else:
    student_mark = set()
    right_attempt = 0

    for _ in range(n):
        line = input()
        parts = line.split(':', 1)  # делим только по первому двоеточию
        nickname = parts[0]
        result = parts[1].strip()   # убираем пробелы в начале и конце

        if result == "Correct":
            student_mark.add(nickname)
            right_attempt += 1

    if len(student_mark) == 0:
        print("Вы можете стать первым, кто решит эту задачу")
    else:
        percent = int(right_attempt / n * 100+0.5)  # округление по математическим правилам
        print(f"Верно решили {len(student_mark)} учащихся")
        print(f"Из всех попыток {int(percent)}% верных")
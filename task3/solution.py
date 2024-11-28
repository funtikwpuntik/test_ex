
def validate(times: list, end: int, start: int) -> list:
    times = [[times[i], times[i + 1]] for i in range(0, len(times), 2)]
    times = sorted(times, key=lambda x: x[0])
    times = [i for i in times if i[0] < end and i[1] > start]
    times = [[start, i[1]] if i[0] < start else i for i in times]
    times = [[i[0], end] if i[1] > end else i for i in times]

    return times

def appearance(intervals: dict[str, list[int]]) -> int:
    start, end = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']

    sum_times = 0
    pupil = validate(pupil, start=start, end=end)
    tutor = validate(tutor, start=start, end=end)
    pupil_last = 0
    while True:
        a = []
        if pupil[0][0] < pupil_last:
            pupil = pupil[1:]
            continue
        if tutor[0][1] >= pupil[0][0] >= tutor[0][0]:
            a.append(pupil[0][0])
        elif tutor[0][0] >= pupil[0][0]:
            a.append(tutor[0][0])

        if tutor[0][1] >= pupil[0][1] >= tutor[0][0]:
            a.append(pupil[0][1])
            pupil_last = pupil[0][1]
            pupil = pupil[1:]
        elif pupil[0][1] >= tutor[0][1]:
            a.append(tutor[0][1])
            tutor = tutor[1:]
        if len(a) == 2:
            sum_times += a[1]-a[0]

        if len(pupil)==0 or len(tutor) == 0:
            break
    print(sum_times)
    return sum_times



tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
import math

def calculate_fee(fees, time):
    default_time, default_fee, unit_time, unit_fee = fees
    if time <= default_time:
        return default_fee
    else:
        return default_fee + math.ceil((time - default_time) / unit_time) * unit_fee
    
def calculate_time(clock1, clock2):
    hour1, min1 = map(int, clock1.split(":"))
    hour2, min2 = map(int, clock2.split(":"))
    if min2 < min1:
        return 60*(hour2 - hour1 - 1) + abs(min2 + (60-min1))
    else:
        return 60*(hour2 - hour1) + min2 - min1

def solution(fees, records):
    answer = []
    cars = set()
    cars_record = {}
    cars_fee = {}
    cars_time = {}
    
    for record in records:
        clock, car_num, in_out = record.split()

        if cars_record.get(car_num) is None:
            cars_record[car_num] = clock
        else:
            clock1 = cars_record[car_num]
            clock2 = clock
            del cars_record[car_num]
            time = calculate_time(clock1, clock2)
            if cars_time.get(car_num) is None:
                cars_time[car_num] = time
            else:
                cars_time[car_num] += time
        cars.add(car_num)        
        
    for car in cars:
        if cars_record.get(car) is not None:
            time = calculate_time(cars_record[car], '23:59')
            if cars_time.get(car) is None:
                cars_time[car] = time
            else:
                cars_time[car] += time
    cars = sorted(list(cars))
    for car in cars:
        answer.append(calculate_fee(fees, cars_time[car]))
    return answer

### 이전 풀이
import math
def solution(fees, records):
    answer = []
    times = []
            
    default_time, default_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]
    # print(default_time, default_fee, unit_time, unit_fee)

    temp = []
    for record in records:
        temp.append(record.split())
    records = temp.copy()
    records.sort(key = lambda x: x[1])

    # for record in records:
    #     print(record)
    # print()
    time = 0
    next_car = records[0][1]
    
    while records:

        # print(records)
        in_time, car, io = records[0][0], records[0][1], records[0][2]
        in_hour, in_minute = map(int, in_time.split(":"))
        records.pop(0)

        if not records: # 비어있으면
            hour = 23 - in_hour
            minute = 59 - in_minute
            time += (hour*60 + minute)
            times.append(time)
            break

        record = records[0]
        if record[1] != car:
            hour = 23 - in_hour
            minute = 59 - in_minute
            time += (hour*60 + minute)
            times.append(time)
            time = 0
            continue
            
        out_time = record[0]
        out_hour, out_minute = map(int, out_time.split(":"))
            
        hour = out_hour - in_hour
        if in_minute > out_minute:
            minute = 60 - (in_minute - out_minute)
            hour -= 1
        else:
            minute = out_minute - in_minute

        records.pop(0)
        if records:
            next_car = records[0][1]
            # print(f">>> current car:{car}, next car: {next_car}")
            time += (hour*60 + minute)
            if next_car != car:
                times.append(time)
                time = 0
        else: # 비어있으면 
            time += (hour*60 + minute)
            times.append(time)
    # print(times)


    for time in times:
        fee = 0
        fee += default_fee
        if time > default_time:
            fee += math.ceil((time - default_time)/unit_time) * unit_fee
        answer.append(fee)
    # print(answer)
    return answer


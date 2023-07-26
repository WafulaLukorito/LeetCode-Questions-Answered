def interview_times(list1, list2, time, bound1, bound2):
    
    total_span = span_generator(min(bound1[0], bound2[0]), max(bound1[1], bound2[1]))
    
    person1_engaged = set()
    for item in list1:
        person1_engaged.update(span_generator(item[0], item[1]))
    
    person2_engaged = set()
    for item in list2:
        person2_engaged.update(span_generator(item[0], item[1]))
        
    person1_free = total_span.difference(person1_engaged)
    person2_free = total_span.difference(person2_engaged)
    
    both_free = sorted(list(person1_free.intersection(person2_free)))
    
    first_three = []
    for i in range(min(3, len(both_free))):
        hour = str(int(both_free[i]))
        minute = "00" if both_free[i] % 1 == 0 else "30"
        first_three.append(hour + ":" + minute)
    
    return first_three


def span_generator(bound1, bound2):
    hour, minute = bound1.split(':')
    start = int(hour) + (0.5 if minute == "30" else 0)
    
    hour2, minute2 = bound2.split(':')
    stop = int(hour2) + (0.5 if minute2 == "30" else 0)
    
    span = set()
    while start < stop:
        span.add(start)
        start += 0.5
    
    return span
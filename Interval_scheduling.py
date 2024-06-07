
#Interval Scheduling

#Sort all activities ascending in order of their finishing time

#Add Compatible activities to the set 

def universityCareerFair(arrival, duration):
    act = sorted(
        list(zip(arrival, duration)),
        key=lambda p: (sum(p), p[1])
    )
    ans, end = 0, -float('inf')
    
    for arr, dur in act:
        if arr >= end:
            ans, end = ans + 1, arr + dur
    
    return ans
    
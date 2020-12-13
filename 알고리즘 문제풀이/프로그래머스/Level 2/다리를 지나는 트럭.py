def solution(bridge_length, weight, truck_weights):
    const_weight = truck_weights[0]
    t, i, cnt = 1, 1, 0
    times = [0] * len(truck_weights)
    while i < len(truck_weights):
        if weight >= const_weight + truck_weights[i]:
            const_weight += truck_weights[i]
            times[i-cnt] = t
            i += 1
        if t+1 - times[0] == bridge_length:
            const_weight -= truck_weights[cnt]
            cnt += 1
            times.pop(0)

        
        t += 1
    return t + bridge_length
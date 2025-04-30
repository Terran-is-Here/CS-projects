dataset = [0,2,3,4,5,12,2,5,23,1,5,2,5,6,3,2]
print(len(dataset))
window_radius = 2
peaks = [] 
def peak_detection(dataset):
    peaks = []
    for i in range(window_radius,len(dataset)-window_radius): #for every center  
        minimum_range = i-window_radius
        maximum_range = i+window_radius
        is_peak = True
        for j in range(minimum_range, maximum_range+1): #iterates through i-2, i-1, i+1, i+2 
            if j == i:
                continue
            if dataset[j] > dataset[i]: 
                is_peak=False
        if is_peak: 
            peaks.append(dataset[i])
    return peaks

peak_detection(dataset)
print(peaks)
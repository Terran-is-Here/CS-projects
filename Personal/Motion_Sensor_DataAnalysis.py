import csv
import pathlib
import matplotlib.pyplot as plt 
import sys
G = 9.81 #m/s^2 
M = 0.033 #kg 

class init_parameters:
    window_radius = 12 
    datafile_path = "C:\\Users\\plcau\\Documents\\Data\\Energy Lab\\bulk_datafile_"
    file_format = ".csv"



def convert_to_list(csv_object): 
    buffer = []
    for i in csv_object: 
        buffer.append(i)
    return buffer
def peak_detection(dataset):
    peaks = []
    for i in range(init_parameters.window_radius,len(dataset)-init_parameters.window_radius): #for every center  
        minimum_range = i-init_parameters.window_radius
        maximum_range = i+init_parameters.window_radius
        is_peak = True
        for j in range(minimum_range, maximum_range+1): #iterates through i-2, i-1, i+1, i+2 
            if j == i: #ignores comparison to self due to redundancy
                continue
            if dataset[j] > dataset[i]: 
                is_peak=False
        if is_peak: 
            peaks.append([i,dataset[i][0],dataset[i][1]]) 
    return peaks #returns [index in parent dataset, value]

correct_data = []

counter = 0
while True:
    print(counter)
    if pathlib.Path(f"{init_parameters.datafile_path}{counter}{init_parameters.file_format}").exists() == True: 
        counter += 1 
    else:
        init_parameters.datafile_path = f"{init_parameters.datafile_path}{counter}{init_parameters.file_format}"
        break
#returns how many datafiles exist, to iterate through all of them. 

with open("C:\\Users\\plcau\\Documents\\Data\\Energy Lab\\bulk_datafile_0.csv","r") as filetesting:
    testing = csv.reader(filetesting) #returns the CSV as a pseudo-2d list, [row][cell]
    peak_testing = peak_detection(convert_to_list(testing))



with open("C:\\Users\\plcau\\Documents\\Data\\Energy Lab\\outliers_datafile_1.csv","r") as filetesting: 
    testing = csv.reader(filetesting) #returns the CSV as a pseudo-2d list, [row][cell]
    print(testing)
    for i in peak_testing: #iterates through every row
        print(i)
        try: 
            if float(i[1]) > 0: 
                correct_data.append(i)
                print("Data Added.")
        except: #removes the first row. 
            print("Data Removes.")
            continue #checks value if its positive
print(correct_data)

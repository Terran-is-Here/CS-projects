from gdx import gdx
import matplotlib.pyplot as plt
# import numpy as np
import sys
import csv
import pathlib
gdx = gdx.gdx() #intitializes the thingy 

#Error Managed Input created from ICS3U Exercises
def EMInput(input_string, return_type ="str", error_message = "Error in input. Please try again."):
    while True:
        try: 
            inputted_value = eval(f"{return_type}(input(input_string))")
        except KeyboardInterrupt: 
            print("\nExiting program due to KeyboardInterrupt.")
            sys.exit() #re-implements forced exit on Ctrl+C KeyboardInterrupt errors.
        except ValueError: 
            print(error_message) # will handle type-matching errors, like inputting a string to a int()
        else:
            return inputted_value

#Configuration Settings
class init_parameters: 
    #offset calculation
    baseline_offset = 0 #Baseline Offset from the tabletop, calculated by initialize_baseline()
    baseline_setting_samples = 100 #Number of used by initialize_baseline in it's calculations.

    #File Saving
    datafile_path = "C:\\Users\\plcau\\Documents\\Data\\Energy Lab\\bulk_datafile_" #bulk data
    outlier_path = "C:\\Users\\plcau\\Documents\\Data\\Energy Lab\\outliers_datafile_"
    file_format = ".csv"

    #Sampling Behavior
    sampling_rate = 80 #Sensor Sample rate (in ms)
    measurement_amount = 1000 #Measurement amount taken in main experiment. 

    #Peak Detecting Behavior
    window_radius = 5 #window radius, actual window size is 2*window_radius + 1
plt.ion() #enables plot in real time updates

counter = 0
#file path checking
while True:
    print(counter)
    if pathlib.Path(f"{init_parameters.datafile_path}{counter}{init_parameters.file_format}").exists() == True: 
        counter += 1 
    else:
        init_parameters.datafile_path = f"{init_parameters.datafile_path}{counter}{init_parameters.file_format}"
        break
counter = 0
while True:
    if pathlib.Path(f"{init_parameters.outlier_path}{counter}{init_parameters.file_format}").exists() == True: 
        counter += 1 
    else:
        init_parameters.outlier_path = f"{init_parameters.outlier_path}{counter}{init_parameters.file_format}"
        break


#setting Go Direct Sensor to be used for data.
gdx.open(connection='usb')
gdx.select_sensors(5) #prompts the selection of sensors
gdx.start(init_parameters.sampling_rate) #starts collecting data, also sets sampling speed

# shorthand function essentially gdx.read()[0] * 100 for unit conversions
def get_data():
    buffer1 = gdx.read()
    return buffer1[0]*100 #converts from m to cm


#data peak detection, returns a table with peaks INCLUDING THEIR INDEX IN THE DATASET. 
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
            peaks.append([i,dataset[i]]) 
    return peaks #returns [index in parent dataset, value]


def initialize_baseline(): #to be ran first without interference; as to guage the height from the tabletop in order to differentiate/tell the height of the ball from said tabletop.
    s = True
    while s: 
        total = 0
        for i in range(init_parameters.baseline_setting_samples):  #Takes the average of the initial values...
            init_measurement = get_data()
            if init_measurement is not None:  #in the case data is none, disregard it. 
                total += init_measurement    
        while True:
            config_state = EMInput(f"Calculated Offset: ({total/init_parameters.baseline_setting_samples}cm)\n\tDoes this comply with the actual height of the sensor above the tabletop? (yes / no / y / n):", "str")
            if config_state.lower() == "yes" or config_state.lower() == "y": #if correct
                init_parameters.baseline_offset = total/init_parameters.baseline_setting_samples
                s = False
                break #break out of both loops
            else: #else break out of the input verification loop. 
                print("Restarting Configuration.")
                break


try: 
    initialize_baseline() #initialize baseline offset.
    values = []
    x_values = []
    fig, ax = plt.subplots()
    line, = ax.plot([], [])  # Create an empty line object
    ax.set_title("Newton Cradle Pendelum Height from Surface")
    ax.set_xlabel("Time (ms)")
    # ax.set_xscale("log")
    ax.set_ylabel("Distance(cm)")

    for i in range(init_parameters.measurement_amount):  # Iterate through the desired number of measurements
        measurement = get_data()
        print(measurement)
        if measurement is None:  # incase something goes wrong.
            break
        inverted_distance = init_parameters.baseline_offset -measurement
        values.append(inverted_distance)  # Assuming the distance is the first value in the tuple
        current_time_ms = i * init_parameters.sampling_rate
        x_values.append(current_time_ms)

        line.set_xdata(x_values)
        line.set_ydata(values)

        # Update the plot limits dynamically
        ax.relim()
        ax.autoscale_view(True, True, True)

        fig.canvas.draw()
        fig.canvas.flush_events()
    gdx.stop()
    gdx.close()

    #post measurement coding
    peak_value_buffer = peak_detection(values) #returns the peak values in the form of [index in parent dataset, value]
    peak_values = []
    for i in peak_value_buffer: #gets a subtable, that is every [index in parent dataset, value]
        i.append(x_values[i[0]]) #appends the time element into the peaks table., [index in parent dataset, value, ]
        peak_values.append(i) #readds sub table to a larger table for later use
        #datastructure: [[index in parent dataset, value, time in ms], [index in parent dataset, value, time in ms],...] 
    bulk_data = []
    for i in range(0,len(values)):
        bulk_data.append([values[i], x_values[i]]) #adds together the value at index I and the time value at index I

    #data writing, with paths already finished from the file_checker loops above. 
    print(f"Bulk data file will be stored at {init_parameters.datafile_path}")
    print(f"outlier data (peaks) file will be stored at {init_parameters.outlier_path}")
    with open(init_parameters.outlier_path,"w", newline="") as outlier_file: #writes outlier data
        csv_writer = csv.writer(outlier_file)
        csv_writer.writerow(['Index Found in Parent Table', 'Value (cms)', 'Time (ms)'])
        csv_writer.writerows(peak_value_buffer)
    with open(init_parameters.datafile_path,"w", newline="") as datafile: #writes bulk data
        csv_writer = csv.writer(datafile)
        csv_writer.writerow(['Value (cms)', 'Time (ms)'])
        csv_writer.writerows(bulk_data)
    input("Data Writing Done. Input Buffer to ensure this program keeps running.")    
    
        

except KeyboardInterrupt: 
    print("Keyboard Interrupt Exception, closing")
    gdx.stop()
    gdx.close()
    plt.ioff()  # Turn off interactive mode
    sys.exit()

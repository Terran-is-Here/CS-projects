from gdx import gdx
import matplotlib.pyplot as plt
# import numpy as np
import sys
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
    datafile_path = "C:\\Users\\plcau\\Documents\\Data\\Energy Lab\\bulk_datafile" #bulk data
    outlier_path = "C:\\Users\\plcau\\Documents\\Data\\Energy Lab\\outliers_datafile"
    file_format = ".csv"

    #Sampling Behavior
    sampling_rate = 100 #Sensor Sample rate (in ms)
    measurement_amount = 800 #Measurement amount taken in main experiment. 

    #Peak Detecting Behavior
    window_radius = 5 #window size for detecting peaks
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
print(f"Bulk data file will be stored at {init_parameters.datafile_path}")
print(f"outlier data (peaks) file will be stored at {init_parameters.outlier_path}")

'''import timeit
import subprocess
#import matplotlib.pyplot as plt

user_prog = 'c7_primegen.exe'
time_string = 'execution time : '
test_times = list()
trials = 5

user_times = list()
target_times = list()

#file_list = ['test_case' + str(i + 1) + '.txt' for i in range(3)]
file_list = ['c7_primegen.exe']

for i in file_list :
    for j in range(trials) :
        trial_output = subprocess.check_output("./" + user_prog, shell=True)
        #trial_output = subprocess.check_output("./output.exe " + i)
        
        #start_index is the beginning of exec time line in user code
        start_index = trial_output.find(time_string) + len(time_string)
        double_dtype_length = 8
        trial_time = float(trial_output[ start_index : start_index + double_dtype_length])
        
        test_times.append(trial_time)
    
    average_runtime = sum(test_times) / len(test_times)
    user_times.append(average_runtime)

print("user times are ", user_times)
'''

import timeit
import matplotlib.pyplot as plt

#add fn to read input size from test cases

n = [47854]
user_times = list()
target_times = list()

user_files = ['c7_primegen.exe"']
target_files = ['c7_primegen2.exe"']

test_times = list()
trials = 2

for i in user_files :
    c_exec = 'subprocess.call(".\\' + i + ', shell=True, stdout=subprocess.DEVNULL)'
    for j in range(trials) :
        trial_time = timeit.timeit(stmt=c_exec, setup='import subprocess', number=5)
        test_times.append(trial_time)
    
    average_runtime = sum(test_times) / len(test_times)
    user_times.append(average_runtime)

del test_times
test_times = list()

for i in target_files :
    c_exec = 'subprocess.call(".\\' + i + ', shell=True, stdout=subprocess.DEVNULL)'
    for j in range(trials) :
        trial_time = timeit.timeit(stmt=c_exec, setup='import subprocess', number=5)
        test_times.append(trial_time)
    
    average_runtime = sum(test_times) / len(test_times)
    target_times.append(average_runtime)


print(test_times)
print("user times are: ", user_times)
print("target times are: ", target_times)

plt.plot(n, user_times, 'ro', label='Your runtime')
plt.plot(n, target_times, 'bo', label='Ideal runtime')
plt.xlabel('size of input')
plt.ylabel('runtime in seconds')
plt.grid(True)
plt.legend(loc='upper left')

plt.show()
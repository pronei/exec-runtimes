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

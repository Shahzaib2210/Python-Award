
'''
# Pseudo Code
1 - Take input from user time taken for swiming in minutes and convert it into integer and store in swim variable.
2 - Take input from user time taken for cycling in minutes and convert it into integer and store in cycle variable.
3 - Take input from user time taken for running in minutes and convert it into integer and store in run variable.
4 - Add swiming, cycling and running time and store in total_time variable.
5 - Now Apply check if total_time is less than 100 then print "Provincial Colors".
6 - Check if total_time is greater then 100 and less then equal to 105 then print "Provincial Half Colors".
7 - Check if total_time is greater then 105 and less then equal to 110 then print "Provincial Scroll".
8 - else print "No Award".
'''

print("================= Swiming Time ========================================")

swim = int(input("Enter time taken for swimming in minutes : "))
print("Time taken for Swimming task: ",swim)

print("================= Cycling Time ========================================")

cycle = int(input("Enter time taken for cycling in minutes : "))
print("Time taken for Cycling task: ",cycle)

print("================= Running Time ========================================")

run = int(input("Enter time taken for running in minutes : "))
print("Time taken for Running task: ",run)

print("================= Total Time ==========================================")

# Calculating total time.
total_time = swim + cycle + run
print("Total time taken for triathlon: ",total_time)

if total_time < 100:
    print("Provincial Colors")
elif total_time > 100 and total_time <= 105:
    print("Provincial Half Colors")
elif total_time > 105 and total_time <= 110:
    print("Provincial Scroll")
else:
    print("No award")
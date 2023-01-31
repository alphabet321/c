def bully(process_list):
    coordinator = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if process_list[i][1] != 0:
                    print("\nELECTION MESSAGE is sent from" , (process_list[i][0]) , "to", (process_list[j][0]))
                    coordinator = process_list[i][0] 

                    if process_list[j][1] != 0:
                        print("OK MESSAGE received from ", (process_list[j][0]) ,"by", (process_list[i][0]))
                        if process_list[j][0] > coordinator:
                            coordinator = process_list[j][0] 
                    else:
                        print("NO RESPONSE from", (process_list[j][0]) ,"to", (process_list[i][0]))
    
    print("\nThe new COORDINATOR is process", coordinator)

    for i in range(n):
        if (coordinator != process_list[i][0]) and (process_list[i][1] != 0):
            print("\nCOORDINATOR MESSAGE is sent from" , coordinator , "to", (process_list[i][0]))



n = int(input("Enter the number of processes: "))
process_list = []

for i in range(n):
    print("Enter the status of the process", (i+1), ": ")
    s = int(input())
    process_list.append([i+1,s])

print("\nThe processes that are active:")
print("Process \t Status")
for i in range(n):
    print(" ", process_list[i][0], " \t\t ", process_list[i][1])

print("\nThe current COORDINATOR is process", n)

fail = int(input("\nEnter the process which fails: "))

for i in range(n):
    if (process_list[i][0] == fail):
        process_list[i][1] = 0

print("\nThe processes that are active:")
print("Process \t Status")
for i in range(n):
    print(" ", process_list[i][0], " \t\t ", process_list[i][1])

bully(process_list)

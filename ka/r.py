class process:
    def __init__(self, pid, status):
        self.pid = pid
        self.status = status
        self.next = None

class ring: # circular linked list
    def __init__(self):
        self.head = None
    
    def add_process(self, pid, status):
        p = process(pid, status)
        temp = self.head
        p.next = self.head

        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = p
        else:
            p.next = p
        self.head = p
    
    def display(self):
        print("Process \t Status")
        temp = self.head
        if self.head is not None:
            while(True):
                print(" ", temp.pid, " \t\t ", temp.status)
                temp = temp.next
                if(temp == self.head):
                    break
    
    def status_update(self, pid):
        temp = self.head
        if self.head is not None:
            while(True):
                if temp.pid == pid:
                    temp.status = 0
                else:
                    temp = temp.next
                if(temp == self.head):
                    break

    def change_head(self,pid):
        temp = self.head
        if self.head is not None:
            while(True):
                if temp.pid == pid:
                    self.head = temp
                    break
                else:
                    temp = temp.next
                if(temp == self.head):
                    break
    
    def election(self):
        temp = self.head
        election_message = []

        if self.head is not None:
            while(True):
                if temp.status != 0:
                    election_message.append(temp.pid)
                    temp = temp.next
                else:
                    temp = temp.next
                if(temp == self.head):
                    break
        
        election_message.append(election_message[0])
        for i in range(len(election_message)):
            print(election_message[i], end='->')
        print("\n\nThe new COORDINATOR is process", max(election_message))

        for i in range(len(election_message)-1):
            if (max(election_message) != election_message[i]):
                print("\nCOORDINATOR MESSAGE is sent from" , max(election_message) , "to", election_message[i])



process_list = ring()

n = int(input("Enter the number of processes: "))

for i in range(n):
    print("Enter the status of the process", (i+1), ": ")
    s = int(input())
    process_list.add_process(i+1, s)

print("\nThe processes that are active:")
process_list.display()

print("\nThe current COORDINATOR is process", n)

fail = int(input("\nEnter the process which fails: "))
process_list.status_update(fail)

print("\nThe processes that are active:")
process_list.display()

start = int(input("\nEnter the process which starts the election: "))
process_list.change_head(start)
process_list.election()



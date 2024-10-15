# Batch Processing

In a batch processing system, a job consisting of a set of cards was prepared in order for the user to interact with the computer system. 
The function of the system was to transfer control from one card to the next; the system resided entirely in memory and grouped operators 
into batches. The disadvantage of this type of system was that only one task could be executed until the previous one was finished, which 
caused the machine to be idle most of the time, which was inefficient.

Batch processing is the predecessor to modern operating systems. In this processing method, each process was assigned to a batch which would 
be would be attended secuentially until its finalization, thus, this processing method is not considered an operating system since interruptions 
could not be used on its advantage.

## Program Functionality

For this simulation, batches may contain up to 5 processes, meaning that if the total of processes is not a multiple of 5, the last batch 
may contain fewer processes. 

Batches will be executed sequentially, thus, a process form the next batch will not start its execution until the 5 processes from the previous 
batch have been fully processed.

Each process will have valuable control information, most of which will be randomly generated, such as:
1. Process ID
2. Process name
3. Operation (basic arithmetic)
4. Result
5. Batch number
6. Expected execution time
7. Elapsed execution time
8. Remaining execution time

The program will display valuable information such as the current batch, the process in execution and the list of completed processes.
There will also be a global timer and the execution of the program will end whenever there are no more remaining batches to execute.

It's important to highlight that this simulator will not consider Errors nor Interruptions during the process execution.

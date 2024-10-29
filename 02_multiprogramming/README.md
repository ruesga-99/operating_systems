# Multiprogramming Processing

In multiprogramming processing, interruptions are implemented that allow the execution of different tasks within a batch, in this way 
it is considered that this type of processing meets the requirements to be considered a pioneering operating system model. The addition 
of interruptions and error handling allows for greater efficiency and reduces problems such as process starvation that occurred with 
batch processing.

## Program Functionality

For this simulation, batches may contain up to 5 processes, meaning that if the total of processes is not a multiple of 5, the last batch 
may contain fewer processes. 

Batches will be executed sequentially, thus, a process form the next batch will not start its execution until the 5 processes from the previous batch have been fully processed.

Interruptions and Errors have been added to this simulation, whenever the user presses I or E respectively, the given funtion will be activated, whenever there's an interruption the porcess will be sent to the end of the queue on its own batch; on the other hand whenever an error occurs, the process will be terminated and the result won't be shown.

Each process will have valuable control information, most of which will be randomly generated, such as:

1. Process ID
2. Operation (basic arithmetic)
3. Result
4. Batch number
5. Expected execution time
6. Elapsed execution time
7. Remaining execution time

The program will display valuable information such as the current batch, the process in execution and the list of completed processes. There will also be a global timer and the execution of the program will end whenever there are no more remaining batches to execute.

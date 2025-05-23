# First Come First Served

First Come First Served is a commonly used algorithm that prioritizes the order of arrival of the processes, which means that the first
process will be executed first, this algorithm should not be confuesd with a FIFO algorithm or structure because the first executed
process might not always be the first fully executed since interruptions can occur during processing time.

## Program Functionality
For this simulation, memory may contain up to 5 processes, including the process in execution. If there are more than 5 non-resolved processes in the system, the queue will continue to pass them to the memory whenever a process is completed.

Processes will be executed sequentially as FCFS indicates, Interruptions and Errors can happen whenever the user presses I or E respectively. If a process is interrupted it will be sent again to the end of the memory queue; on the otehr hand if a process suffers an error it will be inmediately terminated and will mark an "Error" result.

Each process will have valuable control information, which will be randomly generated by the simulation, such as:
1. Process ID
2. Operation (basic arithmetic)
3. Result
4. Status
5. Expected execution time
6. Elapsed execution time
7. Remaining execution time

The program will display some other valuable information such as the remaining tasks and a global timer which will end simultaneously to the end of the simulation.

# Simple Paging

Paging is a memory management scheme that eliminates the need for a contiguous allocation of physical memory. The process of retrieving 
processes in the form of pages from the secondary storage into the main memory is known as paging. The basic purpose of paging is to 
separate each procedure into pages. Additionally, frames will be used to split the main memory. This scheme permits the physical address 
space of a process to be non–contiguous.

In paging, the physical memory is divided into fixed-size blocks called page frames, which are the same size as the pages used by the 
process. The process’s logical address space is also divided into fixed-size blocks called pages, which are the same size as the page 
frames. When a process requests memory, the operating system allocates one or more page frames to the process and maps the process’s 
logical pages to the physical page frames.

In simple paging only a single process can be stored into a page even if the size of it is not fully used, this can led to internal
fragmentation leaving unusable memory.

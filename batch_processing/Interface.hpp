#ifndef INTERFACE_HPP
#define INTERFACE_HPP

#include <iostream>
#include <string>
#include <sstream>
#include <vector>

#include "Process.hpp"

#define MIN_HEIGHT 6

class Interface {
    private:
        std::vector<Process> batchContent, completedTasks;
        Process currentTask;
        int currentBatch, remainingBatches, elapsedTime;
        int tableHeight;

        int calculateTableHeight();

        std::string formatString(std::string, int);

        std::string showHeaders();

    public:
        Interface();
        Interface(std::vector<Process>, Process, std::vector<Process>);

        std::string showInterface();
};

#endif
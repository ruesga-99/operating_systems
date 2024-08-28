#ifndef INTERFACE_HPP
#define INTERFACE_HPP

#include <iostream>
#include <string>
#include <sstream>
#include <vector>

#include "Process.hpp"

class Interface {
    private:
        std::vector<Process> batchContent, completedTasks;
        std::vector<std::string> currentTask;
        int currentBatch, remainingBatches, elapsedTime;
        int tableHeight;

        int calculateTableHeight();

        std::string formatString(std::string, int);

        std::string showHeaders();

    public:
        Interface();
        Interface(std::vector<Process>, std::vector<std::string>, std::vector<Process>);

        std::string showInterface();
};

#endif
#include "Interface.hpp"
using namespace std;

Interface::Interface() : batchCount(0), remainingBatches(0), elapsedTime(0){
}

Interface::Interface(vector<Process> batchContent, vector<string> currentTask, vector<Process> completedTasks, int remainingBatches, int elapsedTime, int batchCount) :
    batchContent(batchContent), currentTask(currentTask), completedTasks(completedTasks), remainingBatches(remainingBatches), elapsedTime(elapsedTime), batchCount(batchCount) {
}

int Interface::calculateTableHeight () {
    return (max(batchContent.size(), completedTasks.size()) > currentTask.size())
            ? max(batchContent.size(), completedTasks.size()) : currentTask.size();
}

string Interface::formatString (string s, int length) {
    if (s.length() == length) {
        return s;
    }

    int difference = abs(static_cast<int>(s.length()) - length);

    if (s.length() > length) {
        s = s.substr(0, length);
    } else {
        s.append(difference, ' ');
    }

    return s;
}

string Interface::showInterface (int remainingT) {
    tableHeight = calculateTableHeight();

    stringstream fullInterface;

    fullInterface << showHeaders();


    // Filling table content
    for (int i(0); i < tableHeight; i++) {
        // Vector 1: batchContent
        if (i < batchContent.size()) {
            fullInterface << formatString(to_string(batchContent[i].getPid()),13)  << " | ";
            fullInterface << formatString(to_string(batchContent[i].getMaxT()), 13) << " | ";
            fullInterface << formatString(to_string(remainingT), 14) << " | ";
        } else {
            // Fill table with empty spaces
            fullInterface << formatString("", 13) << " | ";
            fullInterface << formatString("", 13) << " | ";
            fullInterface << formatString("", 14) << " | ";
        }

        // Vector 2: currentTask
        if (i + 1 < currentTask.size()) {
            fullInterface << formatString(currentTask[i + 1], 28) << " | ";
        } else {
            // Fill table with empty spaces
            fullInterface << formatString("", 28) << " | ";
        }

        // Vector 3: completedTasks
        if (i < completedTasks.size()) {
            fullInterface << formatString(to_string(completedTasks[i].getPid()), 5) << " | ";
            fullInterface << formatString(completedTasks[i].getOperator(), 25) << " | ";
            fullInterface << formatString(completedTasks[i].getResult(), 15) << " | ";
            fullInterface << formatString(to_string(completedTasks[i].getBatch()), 8) << "\n";
        } else {
            // Fill table with empty spaces
            fullInterface << formatString("", 5) << " | ";
            fullInterface << formatString("", 25) << " | ";
            fullInterface << formatString("", 15) << " | ";
            fullInterface << formatString("", 8) << "\n";
        }
    }

    fullInterface << "--------------+---------------+----------------+------------------------------+-------+---------------------------+-----------------+--------" << endl;

    fullInterface << "\nPENDING BATCHES: " << remainingBatches << endl;
    fullInterface << "TIME KEEPER: " << elapsedTime << " sec " << endl;

    return fullInterface.str();
}

string Interface::showHeaders () {
    stringstream haeder;

    haeder << "-----------------------------------------------+------------------------------+-------------------------------------------------------------- \n";
    haeder << formatString("CURRENT BATCH: " + to_string(batchCount), 46) << " | " << formatString("TASK INFORMATION", 28) << " | "
           << formatString("COMPLETED TASKS", 51) << "\n";
    haeder << "-----------------------------------------------+------------------------------+-------------------------------------------------------------- \n";
    haeder << formatString("PID", 13) << " | " << formatString("MAX TIME", 13) << " | " << formatString("REMAINING TIME", 14) << " | "<<formatString("PID: " + currentTask[0], 28)
           << " | " << formatString("PID", 5) << " | "<< formatString("OPERATION", 25) << " | " << formatString("RESULT", 15) << " | "
           << formatString("BATCH #", 8) << "\n";
    haeder << "------------------------------+----------------+------------------------------+-------+---------------------------+-----------------+------- \n";

    return haeder.str();
}

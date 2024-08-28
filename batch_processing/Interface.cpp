#include "Interface.hpp"
using namespace std;

Interface::Interface() : currentBatch(0), remainingBatches(0), elapsedTime(0){
}

Interface::Interface(vector<Process> batchContent, vector<string> currentTask, vector<Process> completedTasks) :
    batchContent(batchContent), currentTask(currentTask), completedTasks(completedTasks) {
}

int Interface::calculateTableHeight () {
    /*
    return (max(batchContent.size(), completedTasks.size()) > currentTask.size()) 
            ? max(batchContent.size(), completedTasks.size()) : currentTask.size(); */

    return max(batchContent.size(), completedTasks.size(), currentTask.size());
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

string Interface::showInterface () {
    tableHeight = calculateTableHeight();

    stringstream fullInterface;
    
    fullInterface << showHeaders();

    
    // Filling table content
    for (int i(0); i < tableHeight; i++) {
        fullInterface << formatString(batchContent[i].getName(), 25) << " | ";
        fullInterface << formatString(to_string(batchContent[i].getMaxT()), 13) << " | ";

        fullInterface << formatString(currentTask[i+1], 31) << " | ";

        fullInterface << formatString(to_string(completedTasks[i].getPid()), 5) << " | ";
        fullInterface << formatString(to_string(completedTasks[i].getOp()), 25) << " | ";
        fullInterface << formatString(to_string(completedTasks[i].getResult()), 15) << " | ";
        fullInterface << formatString(to_string(completedTasks[i].getBatch()), 8) << "\n";
    }
    
    
    for (int i(0); i < tableHeight; i++) {
        fullInterface << formatString(".", 25) << " | ";
        fullInterface << formatString(".", 13) << " | ";

        fullInterface << formatString(".", 31) << " | ";

        fullInterface << formatString(".", 5) << " | ";
        fullInterface << formatString(".", 25) << " | ";
        fullInterface << formatString(".", 15) << " | ";
        fullInterface << formatString(".", 8) << "\n";
    }

    fullInterface << "--------------------------+---------------+---------------------------------+-------+---------------------------+-----------------+----------" << endl;

    fullInterface << "\nPENDING BATCHES: " << remainingBatches << endl;
    fullInterface << "TIME KEEPER: " << elapsedTime << " sec " << endl;

    return fullInterface.str();
}

string Interface::showHeaders () {
    stringstream haeder;

    haeder << "------------------------------------------+---------------------------------+---------------------------------------------------------------- \n";
    haeder << formatString("CURRENT BATCH: " + to_string(currentBatch), 41) << " | " << formatString("TASK INFORMATION", 31) << " | " 
           << formatString("COMPLETED TASKS", 51) << "\n";
    haeder << "------------------------------------------+---------------------------------+---------------------------------------------------------------- \n";
    haeder << formatString("NAME", 25) << " | " << formatString("MAX TIME", 13) << " | " << formatString("PID: " /*+ currentTask[0]*/, 31)
           << " | " << formatString("PID", 5) << " | "<< formatString("OPERATION", 25) << " | " << formatString("RESULT", 15) << " | " 
           << formatString("BATCH #", 8) << "\n";
    haeder << "--------------------------+---------------+---------------------------------+-------+---------------------------+-----------------+---------- \n";

    return haeder.str();
}
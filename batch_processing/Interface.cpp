#include "Interface.hpp"
using namespace std;

Interface::Interface() : currentBatch(0), remainingBatches(0), elapsedTime(0){
}

Interface::Interface(vector<Process> batchContent, Process currentTask, vector<Process> completedTasks) :
    batchContent(batchContent), currentTask(currentTask), completedTasks(completedTasks) {
}

int Interface::calculateTableHeight () {
    return (max(batchContent.size(), completedTasks.size()) > MIN_HEIGHT) 
            ? max(batchContent.size(), completedTasks.size()) : MIN_HEIGHT;
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

    fullInterface << "\n\nPENDING BATCHES: " << remainingBatches << endl;
    fullInterface << "TIME KEEPER: " << elapsedTime << " sec " << endl;

    return fullInterface.str();
}

string Interface::showHeaders () {
    stringstream haeder;

    haeder << "------------------------------------------+---------------------------------+--------------------------------------------------- \n";
    haeder << formatString("CURRENT BATCH: " + to_string(currentBatch), 41) << " | " << formatString("TASK INFORMATION", 31) << " | " 
           << formatString("COMPLETED TASKS", 51) << "\n";
    haeder << "------------------------------------------+---------------------------------+--------------------------------------------------- \n";
    haeder << formatString("NAME", 25) << " | " << formatString("MAX TIME", 13) << " | " << formatString("PID: " + to_string(currentTask.getPid()), 31)
           << " | " << formatString("OPERATION", 25) << " | " << formatString("RESULT", 15) << "\n";
    haeder << "--------------------------+---------------+---------------------------------+---------------------------+----------------------- \n";

    return haeder.str();
}
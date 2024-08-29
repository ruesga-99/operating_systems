#include "Process.hpp"
using namespace std;

Process::Process() {

}

Process::Process (string name, unsigned id, unsigned maxT, unsigned op, unsigned batch, int a, int b) 
    : name(name), id(id), maxT(maxT), op(op), batch(batch), a(a), b(b), remainingT(maxT), elapsedT(0) {

}

string Process::getName() {
    return this->name;
}

unsigned Process::getPid() {
    return this->id;
}

unsigned Process::getBatch() {
    return this->batch;
}

unsigned Process::getMaxT() {
    return this->maxT;
}

unsigned Process::getRemainingT() {
    return this->remainingT;
}

unsigned Process::getElapsedT() {
    return this->elapsedT;
}

int Process::getResult() {
    return calculateResult(a, b);
}

string Process::getOp() {
    stringstream operation;

    operation << a << " " << defineOperator() << " " << b;

    return operation.str();
}

int Process::calculateResult(int a, int b) {
    if (op == 1) {
        return a+b;
    } else if (op == 2) {
        return a-b;
    } else if (op == 3) {
        return a*b;
    } else if (op == 4) {
        return a/b;
    } else if (op == 5) {
        return a%b;
    } else {
        return 0;
    }
}

char Process::defineOperator() {
    if (op == 1) {
        return '+';
    } else if (op == 2) {
        return '-';
    } else if (op == 3) {
        return '*';
    } else if (op == 4) {
        return '/';
    } else if (op == 5) {
        return '%';
    } else {
        return ' ';
    }
}

string Process::toString() {
    stringstream details;

    details << "Name: " << name << endl;
    details << "PID: " << id << endl;
    details << "Operation: " << a << " " << defineOperator() << " " << b << endl;
    details << "Max Time: " << maxT << endl;
    details << "Elapsed Time: " << elapsedT << endl;
    details << "Remaining Time: " << remainingT << endl;

    return details.str();
}

string Process::information() {
    stringstream info;
    info << name << "\t | " << maxT;
    return info.str();
}

string Process::completedInfo(){
    stringstream details;

    details << "PID: " << id << endl;
    details << "Operation: " << a << " " << defineOperator() << " " << b << endl;
    details << "Result: " << calculateResult(a, b) << endl;
    details << "Batch N.: " << batch << endl;

    return details.str(); 
}

void Process::updateTime() {
    this->remainingT--;
    this->elapsedT++;
}

vector<string> Process::vectorizeTask() {
    vector<string> result;

    result.push_back(to_string(id));                                // Process id
    result.push_back("Name: " + name);                              // Name
    result.push_back("Operation: " + to_string(a) + " " +           // Operation
                    defineOperator() + " " + to_string(b));                       
    result.push_back("Max Time: " + to_string(maxT));               // Max Expected Time
    result.push_back("Elapsed Time: " + to_string(elapsedT));       // Elapsed Time
    result.push_back("Remaining Time: " + to_string(remainingT));   // Remaining Time

    return result;
}
#include "Process.hpp"
using namespace std;

Process::Process() {

}

Process::Process (string name, unsigned id, unsigned maxT, unsigned op, unsigned batch, float a, float b) 
    : name(name), id(id), maxT(maxT), op(op), batch(batch), a(a), b(b), remainingT(maxT), elapsedT(0) {

}

string Process::getName() {
    return this->name;
}

unsigned Process::getBatch() {
    return this->batch;
}

unsigned Process::getRemainingT() {
    return this->remainingT;
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

void Process::updateTime() {
    this->remainingT--;
    this->elapsedT++;
}
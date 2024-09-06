#include "Process.hpp"
using namespace std;

Process::Process() {

}

Process::Process (unsigned id, unsigned maxT, unsigned op, unsigned batch, int a, int b)
    : id(id), maxT(maxT), op(op), batch(batch), a(a), b(b), remainingT(maxT), elapsedT(0) {

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

int Process::getOpt() {
    return this->op;
}

bool Process::getProcessed() {
    return this->processed;
}

int Process::getA() {
    return this->a;
}

int Process::getB() {
    return this->b;
}

string Process::getResult() {
    return to_string(calculateResult(a, b));
}

string Process::getOperator() {
    stringstream operation;

    operation << a << " " << defineOperator() << " " << b;

    return operation.str();
}

void Process::setMaxT(unsigned m){
    this->maxT=m;
}

void Process::setRemainingTime(unsigned r){
    this->remainingT=r;
}

void Process::setResult(string re){
    this->result=re;
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

void Process::setProcessed(bool p){
    this->processed=p;
}

string Process::toString() {
    stringstream details;

    details << "PID: " << id << endl;
    details << "Operation: " << a << " " << defineOperator() << " " << b << endl;
    details << "Max Time: " << maxT << endl;
    details << "Elapsed Time: " << elapsedT << endl;
    details << "Remaining Time: " << remainingT << endl;

    return details.str();
}

string Process::information() {
    stringstream info;
    info << id << "\t | " << maxT;
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

int Process::updateTime() {
    this->remainingT--;
    this->elapsedT++;
    return remainingT;
}

vector<string> Process::vectorizeTask() {
    vector<string> result;

    result.push_back(to_string(id));                                // Process id
    result.push_back("Operation: " + to_string(a) + " " +           // Operation
                    defineOperator() + " " + to_string(b));
    result.push_back("Max Time: " + to_string(maxT));               // Max Expected Time
    result.push_back("Elapsed Time: " + to_string(elapsedT));       // Elapsed Time
    result.push_back("Remaining Time: " + to_string(remainingT));   // Remaining Time

    return result;
}

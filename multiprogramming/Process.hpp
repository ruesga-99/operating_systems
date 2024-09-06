#ifndef PROCESS_HPP
#define PROCESS_HPP

#include <iostream>
#include <string>
#include <sstream>
#include <vector>

class Process {
    private:
        unsigned id, maxT, elapsedT, remainingT, batch, op;
        int a, b;
        std::string result;
        bool processed;

        // Class methods
        int calculateResult(int, int);

        char defineOperator();

    public:
        Process ();
        Process (unsigned, unsigned, unsigned, unsigned, int, int);

        // Getters
        unsigned getPid();
        unsigned getMaxT();
        unsigned getElapsedT();
        unsigned getRemainingT();
        unsigned getBatch();
        bool getProcessed();
        int getOpt();
        int getA();
        int getB();
        std::string getResult();

        std::string getOperator();

        // Setters
        void setMaxT(unsigned);
        void setElapsedTime(unsigned);
        void setRemainingTime(unsigned);
        void setBatch(unsigned);
        void setProcessed(bool);
        void setA(int);
        void setB(int);
        void setResult(std::string);

        // Class Methods
        std::string toString();
        std::string information();
        std::string completedInfo();

        int updateTime();

        std::vector<std::string> vectorizeTask();
};

#endif

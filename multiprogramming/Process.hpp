#ifndef PROCESS_HPP
#define PROCESS_HPP

#include <iostream>
#include <string>
#include <sstream>
#include <vector>

class Process {
    private:
        unsigned id, maxT, elapsedT, remainingT, batch, op;
        int a, b, result;

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
        int getOpt();
        int getA();
        int getB();
        int getResult();

        std::string getOperator();

        // Setters
        void setMaxT(unsigned);
        void setElapsedTime(unsigned);
        void setRemainingTime(unsigned);
        void setBatch(unsigned);
        void setA(int);
        void setB(int);

        // Class Methods
        std::string toString();
        std::string information();
        std::string completedInfo();

        void updateTime();

        std::vector<std::string> vectorizeTask();
};

#endif

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
        std::string name;

        // Class methods
        int calculateResult(int, int);

        char defineOperator();

    public:
        Process ();
        Process (std::string, unsigned, unsigned, unsigned, unsigned, int, int);

        // Getters 
        std::string getName();
        unsigned getPid();
        unsigned getMaxT();
        unsigned getElapsedT();
        unsigned getRemainingT();
        unsigned getBatch();
        int getResult();

        std::string getOp();

        // Setters
        void setName(std::string);
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
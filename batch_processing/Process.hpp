#ifndef PROCESS_HPP
#define PROCESS_HPP

#include <iostream>
#include <string>
#include <sstream>

class Process {
    private: 
        unsigned id, maxT, elapsedT, remainingT, batch, op;
        float a, b, result;
        std::string name, opName;
        bool completed;

        // Class methods
        float calculateResult();
        

        char defineOperator();

    public:
        Process ();
        Process (std::string, unsigned, unsigned, unsigned, unsigned, float, float);

        // Getters 
        std::string getName();
        unsigned getPid();
        unsigned getMaxT();
        unsigned getElapsedT();
        unsigned getRemainingT();
        unsigned getBatch();
        unsigned getOp();
        float getA();
        float getB();
        float getResult();

        // Setters
        void setName(std::string);
        void setMaxT(unsigned);
        void setElapsedTime(unsigned);
        void setRemainingTime(unsigned);
        void setBatch(unsigned);
        void setA(float);
        void setB(float);

        // Class Methods
        std::string toString();
        std::string information();

        void updateTime();
};

#endif
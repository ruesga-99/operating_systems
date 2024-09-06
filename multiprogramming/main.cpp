#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <thread>
#include <functional>
#include <windows.h>
#include <conio.h>

#include "Process.hpp"
#include "Interface.hpp"

using namespace std;

#define TICK 1000

// Random number generator
int randomInt(int a, int b) {
    default_random_engine generator(chrono::system_clock::now().time_since_epoch().count());
	uniform_int_distribution<int> distribution(a, b);
	auto randomInt = bind(distribution, generator);

    return randomInt();
}

int checkKey(int i,Process p,vector<Process> &temp,vector<Process> &temp2){
    char key;
    if(_kbhit()){
        key=_getch();
        if(key=='e'){
            temp[i].setRemainingTime(0);
        }
        else if(key=='p'){
            system("pause");
            while(key!='c'){
                if(_kbhit()){
                    key=_getch();
                }
            }
        }
        else if(key=='i'){
            temp2.push_back(p);
            return 2;
        }
    }
    return 0;
}

// Batches related functions
Process fillProcess (unsigned batch,unsigned j) {
    unsigned id, maxT, op;
    float a, b;

    id=j;

    maxT=randomInt(5, 20);
    op = randomInt(1, 5);
    a = randomInt(-100, 100);
    do{
        b = randomInt(-100, 100);
    }while((op==4 or op==5)and b==0);

    Process temp(id, maxT, op, batch, a, b);

    return temp;
}

vector<Process> generateBatches () {
    int i(0),batch(0), n;
    unsigned j(1);
    vector<Process> tasks;

    cout << "Number of Processes: ";
    cin >> n;

    while (i < n) {
        if (i % 5 == 0) {
            batch ++;
        }
        Process temp = fillProcess(batch,j);
        tasks.push_back(temp);
        i++;
        j++;
        //std::this_thread::sleep_for(std::chrono::seconds(3));
    }

    return tasks;
}

void executeProcess (Process &temp) {
    temp.updateTime();
}

int main () {
    vector<Process> tasks = generateBatches();
    vector<Process> completed, current;

    int pendingBatches(tasks.size()/5), remainingTasks(tasks.size());
    int count(0), batch(0), timeKepper(0),it(count);

    if (tasks.size() % 5 != 0) {
        pendingBatches += 1;
    }

    system("cls");
    while (remainingTasks > 0) {
        // Update the batch number each 5 iteartions
        if (count % 5 == 0) {
            batch ++;
            pendingBatches --;

            current.clear();
            for (int i(count); i < count+5; i++) {
                if (i >= tasks.size()) {
                    break;
                }
                current.push_back(tasks[i]);
            }
        }

        Sleep(TICK);
        system("cls");
        Interface intf1(current, tasks[count].vectorizeTask(), completed, pendingBatches, timeKepper, batch);
        cout << intf1.showInterface(tasks[it++].getRemainingT());

        current.erase(current.begin());

        while (tasks[count].getRemainingT() > 0) {
            executeProcess(tasks[count]);
            if(checkKey(count,tasks[count],tasks,current)==2){
                tasks[count].setProcessed(false);
                break;
            }

            timeKepper ++;
            Sleep(TICK);
            system("cls");
            Interface intf(current, tasks[count].vectorizeTask(), completed, pendingBatches, timeKepper, batch);
            cout << intf.showInterface(tasks[count].getRemainingT());
        }
        if(tasks[count].getProcessed()==true){
            completed.push_back(tasks[count]);
        }

        count ++;
        remainingTasks--;

        Sleep(TICK);
        system("cls");
        Interface intf(current, tasks[count].vectorizeTask(), completed, pendingBatches, timeKepper, batch);
        cout << intf.showInterface(tasks[count].getRemainingT());
    }

    string pause;
    cout << "\nPresione enter para terminar ...";
    getline(cin, pause);

    return 0;
}

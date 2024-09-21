#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <functional>
#include <windows.h>

#include "Process.hpp"
#include "Interface.hpp"

using namespace std;

#define TICK 500

// Validation functions
bool isUnique(int id, vector<Process> &temp) {
    for (int i(0); i < temp.size(); i++) {
        if (id == temp[i].getPid()) {
            return false;
        }
    }
    return true;
}

bool isInteger(float num) {
    return floor(num) == num;
}

bool isValid(float t) {
    if (t <= 0 || !isInteger(t)) {
        return false;
    } else {
        return true;
    }
}

// Random number generator
int randomInt(int a, int b) {
    default_random_engine generator(chrono::system_clock::now().time_since_epoch().count());
	uniform_int_distribution<int> distribution(a, b);
	auto randomInt = bind(distribution, generator);

    return randomInt();
}

// Batches related functions
Process fillProcess (unsigned batch) {
    string name;
    unsigned id, maxT, op;
    float a, b;

    cout << "Name: "; 
    cin >> name;
    cout << "ID: ";
    cin >> id;
    cout << "Max Expected Time: ";
    cin >> maxT;

    a = randomInt(-100, 100);
    b = randomInt(-100, 100);
    op = randomInt(1, 5);

    Process temp(name, id, maxT, op, batch, a, b);

    return temp;
}

vector<Process> generateBatches () {
    int i(0), batch(0), n;
    vector<Process> tasks;

    cout << "Number of Processes: ";
    cin >> n;

    while (i < n) {
        if (i % 5 == 0) {
            batch ++;
        }
        Process temp = fillProcess(batch);
        tasks.push_back(temp);
        i++;
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
    int count(0), batch(0), timeKepper(0);

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
        cout << intf1.showInterface();
        current.erase(current.begin());

        while (tasks[count].getRemainingT() > 0) {
            executeProcess(tasks[count]);
            timeKepper ++;
            Sleep(TICK);
            system("cls");
            Interface intf(current, tasks[count].vectorizeTask(), completed, pendingBatches, timeKepper, batch);
            cout << intf.showInterface();
        }
        completed.push_back(tasks[count]);

        count ++;
        remainingTasks--;

        Sleep(TICK);
        system("cls");
        Interface intf(current, tasks[count].vectorizeTask(), completed, pendingBatches, timeKepper, batch);
        cout << intf.showInterface();
    }

    string pause;
    cout << "\nPresione enter para terminar ...";
    getline(cin, pause);

    return 0;
}  
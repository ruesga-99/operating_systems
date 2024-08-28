#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <functional>
#include <windows.h>

#include "Process.hpp"
#include "Interface.hpp"

using namespace std;

// Validation functions
bool isUnique(int id, vector<Process> &temp) {
    for (int i(0); i < temp.size(); i++) {
        if (id == temp[i].getPid()) {
            return false;
        }
    }
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
    cout << temp.toString();
}

int main () {

    vector<Process> tasks = generateBatches();
    vector<Process> completed, current;

    int pendingBatches = tasks.size() / 5;

    while (pendingBatches > 0) {
        
        int batch(0), count(0);
        for (int i(0); i < tasks.size(); i++) {    
            cout << tasks[i].information() << endl;

            while (tasks[i].getRemainingT() > 0) {
                executeProcess(tasks[i]);
            }

            count ++;
            if (count % 5 == 0) {
                batch ++;
                cout << "SE PASA AL SIGUIENTE LOTE" << endl;
                cout << "Pending Batches: " << pendingBatches << "\n\n";
                pendingBatches--;
                /*
                    - Limpiar Pantalla
                    - Imprimir de Nuevo
                */
            }
        }
    }
    cout << "Pending Batches: " << pendingBatches << "\n\n";

    return 0;
}  

/*
    // Initialize Interface with dummy data
    vector<string> currentTask; // Can be filled with task names or IDs if available
    Interface i(tasks, currentTask, completed);

    // Call showInterface() to check its output
    cout << i.showInterface() << endl;
*/
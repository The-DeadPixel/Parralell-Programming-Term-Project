/* Name: Luke Burford
 * Date: 09/14/17
 * Email: lburford@rams.colostate.edu
 */

#include <fDriver.h>
#include <iostream>
#include <ctime>
#include <ratio>
#include <chrono>
using namespace std::chrono;
using std::cout;
using std::endl;
using std::cin;
using std::cerr;

int main(int argc, char* argv[]) {
/* TEMP TESTING STEM FUNCTIONS ONLY */

/* END OF TESTING */
    high_resolution_clock::time_point start = high_resolution_clock::now();
    if(argc < 3) {
        cerr << "Missing file as argument" << endl;
        return -1;
    }
    fDriver fd = fDriver(argc);
    // process the files to be turned into lexo objects/vectors
    if(fd.read(argv) == -1)
        return -1;
    // calculate the matrix of Sim calcualtions between the files
    fd.calcMatrix();
    high_resolution_clock::time_point stop = high_resolution_clock::now();
    duration<double> durationTot = duration_cast<duration<double>>(stop - start);
//     cout << durationTot.count() << endl;
    cout << fd.numFOP << endl;
    cout << fd.numByte << endl;
    // print the results of Sim, pass in the number of files to check line length
     //fd.printDocMatrix();
    return 0;
 }

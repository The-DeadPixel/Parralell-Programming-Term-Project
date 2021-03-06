/* Updated for implimenting Parralell OMP
 * Name: Luke Burford
 * Data: 12/6/18
 * Email: lburford@rams.colostate.edu
 */ 

/* Name: Luke Burford
 * Date: 09/08/17
 * Email: lburford@rams.colostate.edu
 */

#ifndef LEXO_H_INCLUDE
#define LEXO_H_INCLUDE

#include <iostream>
#include <StemExcep.h>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <ctime>
#include <ratio>
#include <chrono>
using namespace std::chrono;
using namespace std;

extern duration<double> stemTime;

class lexo{
public:
    /* ---Functions & Methods--- */
    
    // constructor for lexo, takes the current object of StemExcep to keep the needed exception vectors
    lexo(StemExcep &se) {StemE = se;};
    // takes a string and checks it to make sure that its grammatically correct
    void checkEng(string &sIn);
    // check for punctuation in the current string
    void checkPunct(string &sIn, int pos);
    // check for digits in the current string
    void checkDig(string &sIn, int pos);
    // check for alphabetic characters in the current string
    void checkAlpha(string &sIn, int pos);
    // check words to later be sent to subString, calls StemExcep and Stem
    string checkWord(string &sIn);
    // takes in a string, and a size to substring out the portion to push into
    string subString(string &sIn, int size);
    // adds given string to the ambigous vector
    void addambVector(const string &sIn);
    // adds given string to the unambigous vector
    void addunambVector(const string &sIn);
    // adds given string to the list vector
    void addlVector(const string &sIn);
    // use the sort algorithm: sort(vec.begin(), vec.end()); to sort lexographicaly 
    void lexSort();
    /* calculates the frequency of the sorted vector by adding it to a map that contains a count for frequency
     * NOTE: used to be lexprintFreq
     */
    void lexCalcFreq();
    // add string to the freqMap to have its frequency recorded
    void addFreqMap(const string &sIn);
    // check through the special vect to remove ambigous words
    bool checkAmbigous(string sIn);
    // removes everything out of the special vector, lowecases, and stems all of them before pushing to lVect
    void clearAmb();
    /* ---Instance Variable Getters--- */
    
    /* prints the freqMap in the format: "word count\n"
     * NOTE: this is more of a debug print than a functional one (used this for the prev assignments)
     */
    const void printMap();
    // get a words frequency from the map, if it is not in the map, returns 0
    const int getMapWordCount(const string &sIn);
    /* ---Instance Variables--- */
    
    // map containing all lVect words with their word counts NOTE: in the future make enough getters to keep private
    map<string,int> freqMap; 
    
private:
    /* ---Instance Variables--- */
    
    StemExcep StemE = StemExcep();
    vector<string> lVect; // vector with all strings sorted lexographicaly
    vector<string> ambVect; // special vector for taking ambigous capitalized strings
    vector<string> unambVect; // special vector for taking ambigous capitalized strings
    bool SoS = true; // value for tracking if at the start of sentence, 0 if false, 1 if true
    bool stemTest = true;
};

#endif //LEXO_H_INCLUDE

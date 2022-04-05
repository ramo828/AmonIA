#ifndef LIBTOOLS_HPP
#define LIBTOOLS_HPP

#include <iostream>

using namespace std;

class tutils {
    private:
        void sumData(string s);
        void writeFile(string data);
        void mainPY();
        void runPY(string srcpy);
    public:
        void inData();
        string getSumData();
        void argument(int argc, char *argv[]);

};

#endif
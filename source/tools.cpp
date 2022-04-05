#include <iostream>
#include <fstream>

#include <cstring>
#include <limits.h>
#include <string.h>
#include <fstream>
#include <sys/stat.h>

#include "libtools.hpp"

using namespace std;

string n;
string n1;
string sum;
string split = ">> ";
string fileName = "input/numbersIN.txt";

void tutils::inData() {
	ofstream yaz;                                    // fayl obyektini cagir
	cout << "Nömrələri daxil edin: " << endl;        // Label
	while(n != ":cix"){                              // yazildiqda durdur
		cout << split;                               // ayirici goster
		cin >> n;                                    // nomreleri al
		n1 = n;                                      // n1 deyerine elave et
		sumData(n1);                                 // toplanan deyerler
	}
	yaz.open(fileName);                              // fayli ac
	yaz << getSumData() << endl;                     // datalari fayla yaz
}

void tutils::sumData(string s){
	if(s != ":cix")                                          // q deyeri alinmadiqda elave et
		sum.append(s+"\n");
}
string tutils::getSumData() {                                // alinan datalari geri donder
	return sum;
}

void tutils::writeFile(string data) {
	int status = mkdir(".config",0777);
	ofstream outfile;
	outfile.open(".config/contact.name");
	outfile << data;
	outfile.close();
}

void tutils::runPY(string srcpy){
	string temp = "python "+srcpy;
	system(temp.c_str());
}

void tutils::mainPY() {
	int choise;
	cout << "\t----------------\n\t[---RamoSOFT---]\n\t----------------\n";
	cout << "\t---AMONIA---" << endl;
	cout << 
	"\n\t1 - Numerator"
	"\n\t----------"
	"\n\t2 - Auto Serializer"
	"\n\t----------"
	"\n\t3 - Siyahı hazırla"
	"\n\t----------"
	"\n\t0 - Exit\n>> ";
	cin >> choise;
	switch(choise) {
		case 0: exit(0);
				break;
		case 1: runPY("pyapp/aserial.py");
				break;
		case 2: runPY("pyapp/numerator.py");
				break;
		case 3: inData();
				break;
		default:
				cout << "Bilinməyən əmr!" << endl;
				break;
	}
}

void tutils::argument(int argc, char *argv[]){
	if(argc > 1){
		if(strcmp(argv[1], "-cn") == 0){
			cout << "Yeni ad: " <<argv[2] << endl;
			writeFile(string(argv[2]));
			}
		else if(strcmp(argv[1], "-h") == 0){
			cout << "Hello" << endl;
			}

		}
	else
		mainPY();
}
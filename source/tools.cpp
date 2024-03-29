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
	ofstream yaz;					 // fayl obyektini cagir
	cout << "\t--------------------------\n"
		"\tSadə axtarış\n"
		"\tMəsələn; 830xx66 (Sadecə 055 üçün!)\n"
		"\tPrefixə görə axtarış\n"
		"\tMəsələn; [99830xx66; [55830xx66\n"
		"\tKategoriya və Prefix seçərək axtarış\n"
		"\tMəsələn; |1[55830xx66; |1[99830xx66\n"
	        "\tQeyd: Kategoriya 1dən başlayır\n"
		"\tHər yeni seriya daxil etdikcə enteri sıxın\n"
		"\tSiyahını hazırlayıb çıxmaq üçün :cix yazıb enter sıxın\n"	<< endl;
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
	"\n\t1 - Numerator (text)"
	"\n\t----------"
	"\n\t2 - Numerator (html)"
	"\n\t----------"
	"\n\t3 - Numerator (Banner)"
	"\n\t----------"
	"\n\t4 - Numerator (CSV)"
	"\n\t----------"
	"\n\t5 - Numerator (VCF)"
	"\n\t----------"
	"\n\t6 - Auto Serializer"
	"\n\t----------"
	"\n\t7 - Siyahı hazırla"
	"\n\t----------"
	"\n\t8 - AvtoMesaj"
	"\n\t----------"
	"\n\t9 - AvtoMesaj Incə ayarlar"
	"\n\t----------"
	"\n\t0 - Exit\n>> ";
	cin >> choise;
	switch(choise) {
		case 0: exit(0);
				break;
		case 1: runPY("pyapp/aserial.py txt");
				break;
		case 2: runPY("pyapp/aserial.py html");
				break;
		case 3: runPY("pyapp/aserial.py html1");
				break;
		case 4: runPY("pyapp/aserial.py csv");
				break;
		case 5: runPY("pyapp/aserial.py vcf");
				break;
		case 6: runPY("pyapp/numerator.py");
				break;
		case 7: inData();
				break;
		case 8: system("java robot/Robo");
				break;
		case 9: system("java robot/setting");
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

#include <iostream>
#include <cstring>
#include <limits.h>
#include <string.h>
#include <fstream>
#include <sys/stat.h>

using namespace std;

void writeFile(string data);

int main(int argc, char *argv[]) {
	if(argc > 1){
	if(strcmp(argv[1], "-cn") == 0){
		cout << "Yeni ad: " <<argv[2] << endl;
		writeFile(string(argv[2]));
		}
	}
	else
		system("python main.py");
	return 0;
}

void writeFile(string data) {
	int status = mkdir(".config",0777);
	ofstream outfile;
	outfile.open(".config/contact.name");
	outfile << data;
	outfile.close();
}

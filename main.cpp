#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>

using namespace std;

void GoToLower(char * TestInput){
    string EachLine;
    fstream ToLowerData ("ToLowerData.txt");

    if (ToLowerData){
        while(getline(ToLowerData, EachLine)){
            transform(EachLine.begin(), EachLine.end(), EachLine.begin(), ::tolower);
            cout << EachLine << "\n";
        }
    }

}

int main(int argc, char * const argv[])
{
    char * TestInput = argv[1];
    GoToLower(TestInput);
    return 0;
}

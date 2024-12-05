#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <cmath>
#include <fstream>
#include <sstream>

using namespace std;

int main(){
    ifstream inputFile("smallinput");
    string line;

    if(inputFile.is_open()){
        while(getline(inputFile, line)){
        cout << line << endl;
        }
    }

}


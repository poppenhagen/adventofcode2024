#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <cmath>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

vector<int> split_line(string line){

    vector<int> numbers;

    stringstream ss(line);
    int num;

    while(ss >> num) {
        numbers.push_back(num);
    }
    // for (int n : numbers){  <------ SAVING BECAUSE THIS LOOP RANGE IS USEFUL
    //     cout << n << endl;
    // }
    return numbers;

};

int main(){
    ifstream inputFile("smallinput");
    string raw_input;
    vector<vector <int>> reports; 

    if(inputFile.is_open()){
            while(getline(inputFile, raw_input)){
                reports.push_back(split_line(raw_input));
            }

        }
    
    // for (int i = 0; i < size(reports); i++){ <------ FOR CHECKING REPORTS
    //     for (int n : reports[i]){
    //         cout << n << ", ";
    //     }
    //     cout << endl;
    // }
    

}


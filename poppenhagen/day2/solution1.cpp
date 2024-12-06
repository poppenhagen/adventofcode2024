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
    vector<vector <int>> safe_strings; // This is not necessary. Have a variable that's just counting the amount safe passages, not the passages themselves
    bool increasing;
    bool safe; // set this to null. Then perform checks afterwards

    if(inputFile.is_open()){
            while(getline(inputFile, raw_input)){

                to_check = split_line(raw_input);
                for (int i = 1; i < size(to_check); i++){
                    if(to_check[i-1]-to_check[i] < 0){
                        
                        increasing = false;
                    }
                    if(to_check[i-1]-to_check[i] > 0){
                        increasing = true;
                    }
                    else{
                        bool safe = false;
                    }
                }

                // safe.push_back(split_line(raw_input));
            }

        }
    
    // for (int i = 0; i < size(reports); i++){ <------ FOR CHECKING REPORTS
    //     for (int n : reports[i]){
    //         cout << n << ", ";
    //     }
    //     cout << endl;
    // }
    

}


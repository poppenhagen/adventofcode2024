#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int main() {

    int const smalln = 6;
    int const n = 1000;

    vector<int> a, b;

    for (int i=0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        a.push_back(x);
        b.push_back(y);
    };

    int similarity_score = 0;
    int multiplier = 0;

    for (int i = 0; i < n; i++) {
        multiplier = 0;
        for (int j = 0; j < n; j++) {
            if (a[i] == b[j]){
                multiplier ++;
            }
        }
        similarity_score += a[i] * multiplier;
    }
    cout << similarity_score << endl;

    
}
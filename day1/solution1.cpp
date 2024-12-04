#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int main() {

    int const n = 1000;

    vector<int> a, b;

    for (int i=0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        a.push_back(x);
        b.push_back(y);
    };
    
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int difference_sum = 0;
    cout << "difference_sum" << difference_sum << endl;
    for (int i = 0; i < n; i++){
        difference_sum += abs(a[i] - b[i]);
    }
    
    cout << difference_sum << endl;
}
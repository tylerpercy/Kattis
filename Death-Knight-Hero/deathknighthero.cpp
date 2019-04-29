#include <iostream>
#include <vector>

using namespace std;

int main() {
    
    vector<string> str;
    
    int n;
    cin >> n;
    int total = n;
    
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        str.push_back(s);
    }
    
    for (int i = 0; i < str.size(); i++) {
        bool checkNext = true;
        //printf("Iteration: %d\n", i);
        for (int j = 1; j < str[i].length() && checkNext; j++) {
            if (str[i].at(j-1) == 'C' && str[i].at(j) == 'D') {
                //cout << "removing 1 from total....." << endl;
                total--;
                checkNext = false;
            }
        }
    }
    
    cout << total << endl;
    
    return 0;
}

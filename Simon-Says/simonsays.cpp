#include <iostream>

using namespace std;

int main() {
    
    int n;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        string simon;
        getline(cin, simon, '.');
        //cout << simon << endl;
        auto check = simon.find("Simon says ");
        
        if (check != string::npos) {
            simon.erase(0,12);
            cout << simon << "." << endl;
        }
    }
    
    return 0;
}

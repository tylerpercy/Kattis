#include <iostream>
#include <string>

using namespace std;

int main() {
    
    string code = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.";
    int n;
    string input;
    
    do {
    
    cin >> n >> input;
    
    for (int i = 0; i < input.length(); i++) {
        input[i] = code[i]+n;
    }
    
    reverse(input.begin(), input.end());
    
    cout << input << endl;
        
    } while (n != 0);
    
    return 0;
}

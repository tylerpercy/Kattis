#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
    
    int n;
    cin >> n;
    
    double yeet = 0;
    double time;
    double value;
    vector<double> total;
    vector<double> timeVector;
    vector<double> valueVector;
    
    
    for (int i = 0; i < n; i++) {
        cin >> time >> value;
        timeVector.push_back(time);
        valueVector.push_back(value);
    }
    
    for (int i = 1; i < n; i++) {
        double yote =
            ((((valueVector[i-1] + valueVector[i]) / 2) * (timeVector[i] - timeVector[i-1])) / 1000);
        total.push_back(yote);
        //cout << yote << endl;
    }
    
    for (double val : total) {
        yeet += val;
    }
    
    if (yeet - (int)yeet > 0.0) {
        cout << fixed << setprecision(5) << yeet << endl;
    } else {
        cout << yeet << endl;
    }
    
    return 0;
}

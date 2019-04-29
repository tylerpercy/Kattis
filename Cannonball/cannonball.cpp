#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int main() {
    
    int n;
    cin >> n;
    vector<string> answers;
    
    for (int i = 0; i < n; i++) {
        double velocity, theta, distance, lowerBound, upperBound;
        cin >> velocity >> theta >> distance >> lowerBound >> upperBound;
        
        double x = velocity * distance * cos(theta);
        double y = (velocity * distance * sin(theta)) - (.5*(9.81)*((distance)*(distance)));
        
        if (x == distance) {
            if (y > lowerBound + 1 && y < upperBound - 1) {
                answers.push_back("Safe");
            }
        } else {
            answers.push_back("Not Safe");
        }
    }
    
    //cout << answers.size();
    
    for (int i = 0; i < answers.size(); i++) {
        cout << answers[i] << endl;
    }
    
    return 0;
}

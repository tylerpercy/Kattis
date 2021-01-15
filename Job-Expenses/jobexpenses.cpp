#include <iostream>

using namespace std;

int main()
{
    int n;
    int total = 0;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (x < 0) {
            total += -x;
        }
    }

    cout << total << endl;

    return 0;
}
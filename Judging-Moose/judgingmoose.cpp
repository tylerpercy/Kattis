#include <iostream>

using namespace std;

int main()
{
    int num1, num2;
    cin >> num1 >> num2; // 2 3

    if (num1 == num2 && num1 > 0 && num2 > 0)
    {
        int sum = num1 + num2;
        cout << "Even " << sum;
    }
    else if (num1 > num2)
    {
        int doubled = num1 * 2;
        cout << "Odd " << doubled;
    }
    else if (num2 > num1)
    {
        int doubled = num2 * 2;
        cout << "Odd " << doubled;
    }
    else if (num1 == 0 && num2 == 0)
    {
        cout << "Not a moose";
    }


    return 0;
}
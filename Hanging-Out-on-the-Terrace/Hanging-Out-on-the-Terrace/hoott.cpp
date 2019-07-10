// hoott.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>

using namespace std;

int main()
{
	int rejectCounter = 0;
	int currentPeople = 0;
	int n, c;
	cin >> n >> c;

	for (int i = 0; i < c; i++) {

		string s;
		int a;
		cin >> s >> a;

		if (s == "enter") {
			if (currentPeople + a > n) {
				rejectCounter++;
			} else {
				currentPeople += a;
			}
		} else {
			currentPeople -= a;
		}
	}

	cout << rejectCounter << endl;

	return 0;
}




// Harshad.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>

using namespace std;

int harshad(int);

int main() {
	int n;
	cin >> n;

	cout << harshad(n) << endl;

	return 0;
}

int harshad(int n) {
	int sum = 0;
	for (int temp = n; temp > 0; temp /= 10) {
		sum += temp % 10;
	}

	if (n % sum == 0) {
		return n;
	} else {
		n += 1;
		 return harshad(n);
	}

}

// Kemija.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	string s;
	getline(cin, s);
	string w;
	int i = 0;
	while (i < s.size()) {

		switch (s[i]) {
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u':
			i += 2;
		default:
			w.push_back(s[i++]);
		}
	}

	cout << w << endl;

	return 0;
}

	



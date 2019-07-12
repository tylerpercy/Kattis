
#include <iostream>
#include <string>

using namespace std;

int getLargest(int, int, int);

int main()
{
	int x;
	cin >> x;

	string adrian = "ABC";
	string bruno = "BABC";
	string goran = "CCAABB";

	int aScore = 0;
	int bScore = 0;
	int gScore = 0;

	string c;
	cin >> c;

	for (int i = 0; i < x; i++) {
		if (adrian.length() < c.length()) {
			adrian.append(adrian);
		}
		if (bruno.length() < c.length()) {
			bruno.append(bruno);
		}
		if (goran.length() < c.length()) {
			goran.append(goran);
		}
	}

	for (int i = 0; i < x; i++) {
		if (adrian[i] == c[i]) {
			aScore++;
		}
		if (bruno[i] == c[i]) {
			bScore++;
		}
		if (goran[i] == c[i]) {
			gScore++;
		}
	}

	int max = getLargest(aScore, bScore, gScore);
	cout << max << endl;

	if (aScore == max) cout << "Adrian\n";
	if (bScore == max) cout << "Bruno\n";
	if (gScore == max) cout << "Goran\n";

	return 0;

}

int getLargest(int a, int b, int g) {
	int max = (a < b) ? b : a;
	return ((max < g) ? g : max);
	
}


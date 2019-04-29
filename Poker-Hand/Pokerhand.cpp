#include <iostream>
#include <map>

using namespace std;

int main()
{

  map<char, int> m;
  int ans = 0;

  for (int i = 0; i < 5; i++)
  {
     char r, s;
     cin >> r >> s;
     m[r]++; 
     ans = max(ans, m[r]);
  }

  cout << ans << endl;

  return 0;
}

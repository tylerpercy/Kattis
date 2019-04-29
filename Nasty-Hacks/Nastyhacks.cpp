#include <iostream>

using namespace std;

int main()
{
   int n;
   cin >> n;

   for (int i = 0; i < n; i++)
   {
       int a, b, c;
       cin >> a >> b >> c;
       
       //int ans = max(a, b-c);
       if (a < b-c)
          cout << "advertise" << endl;
       else if (a == b-c)
          cout << "does not matter" << endl;
       else
          cout << "do not advertise" << endl;
   }

  return 0;
}

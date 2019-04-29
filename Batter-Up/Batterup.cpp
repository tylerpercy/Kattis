#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
   int n;
   double counter = 0;
   cin >> n;
   double bat[n];

   for (int i = 0; i < n; i++)   
   {
       int val;
       cin >> val;
       bat[i] = val;
   }

   double sum = 0;

   for (int i = 0; i < n; i++)
   {
       if (bat[i] != -1)
       {
          sum+= bat[i];
          counter++;
       }
   }

  // cout << sum << " " << counter << endl;

   double ans = sum/counter;
   cout << fixed << setprecision(4) << ans << endl;

   return 0;
}

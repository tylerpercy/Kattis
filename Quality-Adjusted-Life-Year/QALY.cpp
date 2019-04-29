#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
   int n;
   double ans = 0;
   cin >> n;
   for (int i = 0; i < n; i++)
   {
      double x, y;
      cin >> x >> y;
      ans += x*y;
   }

   cout << fixed << setprecision(3) << ans;

   return 0;
}

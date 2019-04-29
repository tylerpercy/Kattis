#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
   int n;
   cin >> n;

   for (int i = 0; i < n; i++)
   {
      double b, p;
      cin >> b >> p;
     
      double ans1 = 60/(p/(b-1));
      double ans2 = 60/(p/b);
      double ans3 = 60/(p/(b+1));
      cout << fixed << setprecision(4) << 
      ans1 << " " << ans2 << " " << ans3 << endl;
   }


   return 0;
}

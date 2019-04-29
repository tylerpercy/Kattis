#include <iostream>

using namespace std;

bool checkPossible(double a, double b, double c)
{
   if (a+b == c)
      return true;
   else if (a-b == c || b-a == c)
      return true;
   else if (a*b == c)
      return true;
   else if (a/b == c || b/a == c)
      return true;
   else
      return false;
}

int main()
{
   int n;
   cin >> n;
   
   for (int i = 0; i < n; i++)
   {
       double a, b, c;
       cin >> a >> b >> c;
       
       bool ans = checkPossible(a, b, c);

       ans == true ? cout << "Possible" << endl : cout << "Impossible" << endl;      
   }

   return 0;
}

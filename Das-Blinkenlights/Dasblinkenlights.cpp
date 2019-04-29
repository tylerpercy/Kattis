#include <iostream>

using namespace std;

int main()
{
   bool ans = false;
   int a, b, c;
   cin >> a >> b >> c;

   int max = (a < b) ? a : b;
   
   do
   {
      if (max % a == 0 && max % b == 0)
      {
         break;
      }
      else
         max++;

   } while (true);

   if (max <= c)
      cout << "yes" << endl;
   else
      cout << "no" << endl;


   return 0;
}

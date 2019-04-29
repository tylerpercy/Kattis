#include <iostream>

using namespace std;

int main()
{
   string s;
   cin >> s;

   double ws, lc, uc, sy;

   for (int i = 0; i < s.length(); i++)
   {
       if (islower(s[i]))
          lc++;
       else if (isupper(s[i]))
          uc++;
       else if (s[i] == '_')
          ws++;
       else
          sy++;
   }

   double wsAns = ws / s.length();
   double lcAns = lc / s.length();
   double ucAns = uc / s.length();
   double sAns = sy / s.length();

   cout << wsAns << endl << lcAns << endl << ucAns << endl << sAns << endl; 


   return 0;
}

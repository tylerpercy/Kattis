#include <iostream>

using namespace std;

string detectHiss(string s)
{
   for (int i = 0; i < s.length(); i++)
   {
      if (s[i] == 's')
      {
         if (s[i] == s[i+1])
         {
            return "hiss";
         }
      }
   }

   return "no hiss";
}

int main()
{
   string s;
   cin >> s;

   cout << detectHiss(s) << endl;

   return 0;
}

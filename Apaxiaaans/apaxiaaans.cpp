#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
   string s;
   cin >> s;
   
   for (int i = 0; i < s.length(); i++)
   {
       if (s[i] == s[i+1])
       {
           s.replace(i, 1, " ");
       }
   
    //   cout << s << endl;
   }

  // cout << s << endl;

   s.erase(remove(s.begin(), s.end(), ' '), s.end());
   
   cout << s << endl;


   return 0;
}

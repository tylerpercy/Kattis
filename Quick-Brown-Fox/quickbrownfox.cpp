#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
   int n;
   cin >> n;
  // char alphabet[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
  //                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
   
   string alphabet = "abcdefghijklmnopqrstuvwxyz";
   int counter;
   vector<char> common;

   cin.get();
   for (int i = 0; i < n; i++)
   {
       counter = 0;
       bool found[26] = {false};
       string s;
       getline(cin, s);
      // cout << s << endl;

       set_intersection(s[0], s[s.length()], alphabet[0], alphabet[alphabet.length()], back_inserter(common));
      
       string ans = "missing ";
       for (int j = 0; j < 26; j++)
       {
           if (found[j] == false)
           {
              ans += common[j];
           }
       }

       if (counter == 0)
          ans = "pangram";

       cout << ans << endl;
   }
  
   return 0;
}

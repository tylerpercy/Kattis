#include <iostream>
#include <vector>
#include <map>
#include <regex>

using namespace std;

int main()
{
   string rec;
   int n;
   int wscount = 0;

   cin >> n;
   cin.get();
   getline(cin, rec);

   for (int i = 0; i < rec.length(); i++)
       if (rec[i] == ' ' || rec[i] == '\n')
          wscount++;

   cout << wscount << endl;
   for (int i = 0; i < n; i++)
   {
       vector<string> v;
       string s;
       do
       {
          getline(cin, s);
          auto found = s.find_last_of(' ');
          string sound = s.substr(found+1);
          v.push_back(sound);
       } while (s != "what does the fox say?");

       v.pop_back();
       for (vector<string>::iterator it = v.begin(); it != v.end(); it++)
       {    
           string a;
           for (int j = 0; j < wscount; j++)
           { 
              a = *it;
              auto f = rec.find(a);
              if (f != string::npos)
                 rec.erase(f, a.length()+1);               
           }         
       }

       cout << rec << endl;
   }


   return 0;
}

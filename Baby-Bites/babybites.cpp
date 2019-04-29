#include <iostream>
#include <string>

using namespace std;

int main()
{
   int n;
   cin >> n;

   int counter = 0;
   char arr[n];
   bool check[n] = {false};
   
   for (int i = 0; i < n; i++)
      arr[i] = i - '0';

   for (int i = 0; i < n; i++)
   {
      string s;
      cin >> s;
      cout << arr[i] << s << endl;
      if (s == "mumble" || stoi(s) == arr[i])
      {
         check[i] = true;
      }  
   }

   for (int i = 0; i < n; i++)
      if (check[i] = true)
         counter++;

   counter == n ? cout << "makes sense" : cout << "something is fishy";


   return 0;
}

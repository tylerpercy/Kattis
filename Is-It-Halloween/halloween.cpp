#include <iostream>

using namespace std;

int main()
{
   string s;
   int i;

   cin >> s >> i;

   if ((s == "OCT" && i == 31) || (s == "DEC" && i == 25))
   {
      cout << "yup" << endl;
   }
   else
      cout << "nope" << endl;   


   return 0;
}

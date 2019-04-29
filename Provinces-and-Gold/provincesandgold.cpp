#include <iostream>

using namespace std;

int main()
{
   int c, s, g;
   cin >> g >> s >> c;
   int sum = (g*3)+(s*2)+c;
   
   switch (sum)
   {
      case 0:
      case 1:
         cout << "Copper" << endl;
      break;
      case 2:
         cout << "Estate or Copper" << endl;
      break;
      case 3:
      case 4:
         cout << "Estate or Silver" << endl;
      break;
      case 5:
         cout << "Duchy or Silver" << endl;
      break;
      case 6:
      case 7:
         cout << "Duchy or Gold" << endl;
      break;
      default:
         cout << "Province or Gold" << endl;
      break;
   }

   return 0;
}

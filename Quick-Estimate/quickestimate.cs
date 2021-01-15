using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication3
{
    class Program
    {
        static void Main(string[] args)
        {
            int input = Convert.ToInt32(Console.ReadLine());
            string[] tempArr = new string[input];
            if (input <= 100 && input >= 1)
            {
                for(int i = 0; i < input; i ++)
                {
                    tempArr[i] = Console.ReadLine();
                }

                foreach (string str in tempArr)
                {
                    char[] temp = str.ToCharArray();
                    Console.WriteLine(temp.Length);

                }
                Console.ReadKey();
            }
            
        }
    }
}
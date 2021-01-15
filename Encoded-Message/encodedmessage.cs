using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication5
{
    class Program
    {
        static void Main(string[] args)
        {
            int amt = Convert.ToInt32(Console.ReadLine());
            string[] strTemp = new string[amt];

            for (int i = 0; i < amt; i++)
            {
                int m = 0;
                char[] input = Console.ReadLine().ToCharArray();
                int lgth = (int)(Math.Sqrt(input.Length));
                char[,] foo = new char[lgth, lgth];
                for(int j = 0; j < lgth; j++)
                {
                    for (int k = 0; k < lgth; k++)
                    {
                        foo[j, k] = input[m];
                        m++;
                    }
                    
                }

                for (int j = (lgth - 1); j >= 0; j--)
                {
                    for (int k = 0; k < lgth; k++)
                    {
                        strTemp[i] += foo[k, j];
                    }
                } 
                          
            }
            foreach(string str in strTemp)
            {
                Console.WriteLine(str);
            }
            Console.ReadKey();
        }
    }
}

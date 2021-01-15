using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PET
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] total = new int[5];
            int[] lines = new int[5] { 1, 2, 3, 4, 5 };
            string[] string1 = Console.ReadLine().Split(' ');
            string[] string2 = Console.ReadLine().Split(' ');
            string[] string3 = Console.ReadLine().Split(' ');
            string[] string4 = Console.ReadLine().Split(' ');
            string[] string5 = Console.ReadLine().Split(' ');

            int[,] intArr = new int[5, 4];

            for (int j = 0; j <4; j++)
            {
                intArr[0, j] = Convert.ToInt32(string1[j]);
            }
            for (int j = 0; j < 4; j++)
            {
                intArr[1, j] = Convert.ToInt32(string2[j]);
            }

            for (int j = 0; j < 4; j++)
            {
                intArr[2, j] = Convert.ToInt32(string3[j]);
            }

            for (int j = 0; j < 4; j++)
            {
                intArr[3, j] = Convert.ToInt32(string4[j]);
            }

            for (int j = 0; j < 4; j++)
            {
                intArr[4, j] = Convert.ToInt32(string5[j]);
            }

            for(int i = 0; i < 5; i++)
            {
                for (int j = 0; j < 4;j++)
                {
                    total[i] += intArr[i,j];
                }
            }

            Array.Sort(total, lines);
            Console.WriteLine(lines[4] + " " + total[4]);

            Console.ReadKey();



        }
    }
}

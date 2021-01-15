using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication9
{
    class Program
    {
        static int days;

        static void Main(string[] args)
        {
            string input = Console.ReadLine().ToUpper();

            for (int i = 0; i < input.Length; i+=3)
            {
                if (input[i] != 'P')
                {
                    input.Replace(input[0], 'P');
                    days++;
                }
            }
            for (int i = 1; i < input.Length; i += 3)
            {
                if (input[i] != 'E')
                {
                    input.Replace(input[0], 'E');
                    days++;
                }
                
            }
            for (int i = 2; i < input.Length; i += 3)
            {
                if (input[i] != 'R')
                {
                    input.Replace(input[0], 'R');
                    days++;
                }
            }

            Console.WriteLine(days);
            Console.ReadKey();
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace hai
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();
            string[] split = input.Split(' ');

           int r1 = Convert.ToInt32(split[0]);
           int s = Convert.ToInt32(split[1]);

            int final = (s * 2) - r1;

            Console.WriteLine(final);

        }
    }
}
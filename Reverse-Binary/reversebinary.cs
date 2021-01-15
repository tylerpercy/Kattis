using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication7
{
    class Program
    {
        static void Main(string[] args)
        {
            int input = Convert.ToInt32(Console.ReadLine());
            string binary = Convert.ToString(input, 2);
            //binary.Reverse();
            string foo = "";
            for (int i = binary.Length - 1; i >= 0; i--)
            {foo += binary[i];}
            int noo = Convert.ToInt32(foo, 2);
                       Console.WriteLine(noo);
            Console.ReadLine();

        }
    }
}
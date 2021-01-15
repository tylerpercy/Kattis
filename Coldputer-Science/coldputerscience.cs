using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace thing
{
    class Program
    {
        static void Main(string[] args)
        {
            int input = Convert.ToInt32(Console.ReadLine());
            string days = Console.ReadLine();
            string[] indivDays = days.Split('-');

            Console.WriteLine(indivDays.Length - 1);
            Console.ReadLine();
        }
    }
}

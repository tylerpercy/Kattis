using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    class Program
    {
        static void Main(string[] args)
        {
            var inputs = Convert.ToInt32(Console.ReadLine());
            int[] array = new int[inputs];

            for (int i = 0; i < inputs; i++)
            {               
                var number = Convert.ToInt32(Console.ReadLine());
                array[i] = number;
            }

            foreach (int number in array)
            {
                Console.WriteLine(number % 2 == 0 ? "{0} is even" : "{0} is odd", number);
            }

            Console.ReadKey();
        }
    }
}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication14
{
    class Program
    {
        static void Main(string[] args)
        {
            var list = new List<double>();

            string[] input = Console.ReadLine().Split(' ');

            double matches = Convert.ToDouble(input[0]);
            double l = Convert.ToDouble(input[1]);
            double w = Convert.ToDouble(input[2]);

            double max = Math.Sqrt((l * l) + (w * w));

            for (int i = 0; i < matches; i++)
            {
                string inputLength = Console.ReadLine();
                double matchLength = Convert.ToDouble(inputLength);

                list.Add(matchLength);
            }

            Console.Clear();

            foreach (double number in list)
            {
                if (number > max)
                    Console.WriteLine("NE");
                else
                    Console.WriteLine("DA");
            }

            Console.ReadKey();
        }
    }
}
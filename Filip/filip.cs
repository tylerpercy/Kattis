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
            string[] input = Console.ReadLine().Split(' ');

            var num1 = input[0].ToCharArray();
            var num2 = input[1].ToCharArray();

            int[] intArray1 = Array.ConvertAll(num1, c => (int)Char.GetNumericValue(c));
            int[] intArray2 = Array.ConvertAll(num2, c => (int)Char.GetNumericValue(c));

            Array.Reverse(intArray1);
            Array.Reverse(intArray2);

            var reverse1 = string.Join("", intArray1.Select(x => x.ToString()).ToArray());
            var reverse2 = string.Join("", intArray2.Select(x => x.ToString()).ToArray());

            int final1 = Convert.ToInt32(reverse1);
            int final2 = Convert.ToInt32(reverse2);

            if (final1 > final2)
                Console.WriteLine(final1);
            else
                Console.WriteLine(final2);

            Console.ReadKey();
        }
    }
}

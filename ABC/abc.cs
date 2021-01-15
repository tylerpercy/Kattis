using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ABC
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] numbers = Console.ReadLine().Split(' ');
            char[] letters = Console.ReadLine().ToCharArray();
            int[] num = new int[3];
            for(int i = 0; i <3; i++)
            {
                num[i] = Convert.ToInt32(numbers[i]);
                if (num[i] > 100)
                {
                    Environment.Exit(0);
                }
            }

            Array.Sort(num);

            for (int i = 0; i < 3; i++)
            {
                    if (letters[i] == 'C')
                    {
                        Console.Write(num[2]);
                    }
                    else if (letters[i] == 'B')
                    {
                        Console.Write(num[1]);
                    }
                    else
                    {
                        Console.Write(num[0]);
                    }
                    if (i != 2)
                    {
                        Console.Write(" ");
                    }
                

            }


            Console.ReadKey();


        }
    }
}
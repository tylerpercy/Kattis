using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp7
{
    class Program
    {
        static void Main(string[] args)
        {
            bool unique = true;

            string[] sentence = Console.ReadLine().Split(' ');
            List<string> list = new List<string>();

            for (int i = 0; i < sentence.Length; i++)
            {

                if (list.Contains(sentence[i]))
                {
                    unique = false;
                    break;
                }                                               

                list.Add(sentence[i]);
            }

            if (unique)
                Console.WriteLine("yes");
            else
                Console.WriteLine("no");

                Console.ReadKey();
        }
    }
}
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
            string carrots = Console.ReadLine();
            string[] charArray = new string[1]; charArray = carrots.Split(' ');
            Console.WriteLine(charArray[1]);
            Console.ReadLine();
        }
    }
}
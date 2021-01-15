using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication8
{
    class Program
    {
        static void Main(string[] args)
        {
            string cards = Console.ReadLine();
            int points=0;
            int Ts = 0;
            int Cs = 0;
            int Gs = 0;
            int difpoints = 0;
            for (int i = 0; i <= cards.Length - 1; i++)
            {
                if (cards[i] == 'T')
                {Ts++;}
                if (cards[i] == 'C')
                { Cs++; }
                if (cards[i] == 'G')
                { Gs++; }

            }
            
            if (Ts > 0 & Cs > 0 & Gs > 0)
            {
                int[] nums = new int[] { Ts, Cs, Gs };
                int low = nums.Min();
                difpoints=low * 7 ;
            }
            
            
            points = (Ts *Ts) + (Cs*Cs) + (Gs *Gs) + difpoints;
            Console.WriteLine(points);
            Console.ReadLine();


        }
    }
}

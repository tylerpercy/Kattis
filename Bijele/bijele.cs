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
            const int king = 1;
            const int queen = 1;
            const int rook = 2;
            const int bishop = 2;
            const int knight = 2;
            const int pawn = 8;

            string[] pieces = Console.ReadLine().Split(' ');

            int needKing = 0;
            int needQueen = 0;
            int needRook = 0;
            int needBishop = 0;
            int needKnight = 0;
            int needPawn = 0;

            Int32.TryParse(pieces[0], out needKing);
            Int32.TryParse(pieces[1], out needQueen);
            Int32.TryParse(pieces[2], out needRook);
            Int32.TryParse(pieces[3], out needBishop);
            Int32.TryParse(pieces[4], out needKnight);
            Int32.TryParse(pieces[5], out needPawn);

            if (needKing != king)
            {
                if (needKing < king)
                {
                    needKing = 1;
                    Console.Write("{0} ", needKing);
                }
                else if (needKing > king)
                {
                    needKing = (king - needKing);
                    Console.Write("{0} ", needKing);
                }
            }
            else
            {
                needKing = 0;
                Console.Write("{0} ", needKing);
            }
            if (needQueen != queen)
            {
                if (needQueen < queen)
                {
                    needQueen = 1;
                    Console.Write("{0} ", needQueen);
                }
                else if (needQueen > queen)
                {
                    needQueen = (queen - needQueen);
                    Console.Write("{0} ", needQueen);
                }
            }
            else
            {
                needQueen = 0;
                Console.Write("{0} ", needQueen);
            }
            if (needRook != rook)
            {
                if (needRook < rook)
                {
                    needRook = (rook - needRook);
                    Console.Write("{0} ", needRook);
                }
                else if (needRook > rook)
                {
                    needRook = (needRook - rook);
                    Console.Write("-{0} ", needRook);
                }
            }
            else
            {
                needRook = 0;
                Console.Write("{0} ", needRook);
            }
            if (needBishop != bishop)
            {
                if (needBishop < bishop)
                {
                    needBishop = (bishop - needBishop);
                    Console.Write("{0} ", needBishop);
                }
                else if (needBishop > bishop)
                {
                    needBishop = (needBishop - bishop);
                    Console.Write("-{0} ", needBishop);
                }
            }
            else
            {
                needBishop = 0;
                Console.Write("{0} ", needBishop);
            }
            if (needKnight != knight)
            {
                if (needKnight < knight)
                {
                    needKnight = (knight - needKnight);
                    Console.Write("{0} ", needKnight);
                }
                else if (needKnight > knight)
                {
                    needKnight = (needKnight - knight);
                    Console.Write("-{0} ", needKnight);
                }
            }
            else
            {
                needKnight = 0;
                Console.Write("{0} ", needKnight);
            }
            if (needPawn != pawn)
            {
                if (needPawn < pawn)
                {
                    needPawn = (pawn - needPawn);
                    Console.Write("{0} ", needPawn);
                }
                else if (needPawn > pawn)
                {
                    needPawn = (needPawn - pawn);
                    Console.Write("-{0} ", needPawn);
                }
            }
            else
            {
                needPawn = 0;
                Console.Write("{0} ", needPawn);
            }

            Console.ReadKey();
        }
    }
}
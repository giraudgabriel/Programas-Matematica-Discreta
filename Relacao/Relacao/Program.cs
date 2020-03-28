using System;
using System.Collections.Generic;

namespace Relacao
{
    class Program
    {
        static void Main(string[] args)
        {
            string conjuntoA;
            string conjuntoB;
            Console.WriteLine("-------Gabriel Fernandes Giraud -1º Semestre BD ------- \n \n");
            Console.WriteLine("-------Programa sobre relação cartesiana entre os conjuntos A e B------- \n \n");

            Console.WriteLine("Digite os valores do conjunto A, separados por ';' \n");

            conjuntoA = Console.ReadLine();

            Console.WriteLine("Digite os valores do conjunto B, separados por ';' \n");

            conjuntoB = Console.ReadLine();
            Console.WriteLine("\n");

            var A = conjuntoA.Split(';');

            var B = conjuntoB.Split(';');

            var relacao = new List<string>();

            for (int i = 0; i < A.Length; i++)
            {
                if (A.Length > B.Length)
                {
                    for (int j = 0; j < B.Length; j++)
                    {
                        if(A[i]!=null && B[j]!=null)
                        relacao.Add($"<{A[i]};{B[j]}>");
                    }
                }
                else
                {
                    for (int j = 0; j < A.Length; j++)
                    {
                        if (A[i] != null && B[j] != null)
                        relacao.Add($"<{A[i]};{B[j]}>");
                    }
                }
            }

            relacao.ForEach(r => { Console.WriteLine(r); });
            Console.ReadKey();
        }
    }
}

programa
{
	
	//Gabnel Fernandes Giraud - 1ªSemestre BD
	//Programa para Fazer União entre Dois Vetores
	funcao inicio()
	{
		inteiro v1[20], v2[20], v3[40], uniao = 0

		para(inteiro j = 0 ; j < 20 ; j++)
		{	
			escreva("Digite um valor para o vetor 1:\n")
			leia(v1[j])
			escreva("Digite um valor para o vetor 2:\n")
			leia(v2[j])
			se(v1[j] == v2[j])
				{
					se(contemNumero(v1[j],v3,20) == falso)
					{
						v3[uniao] = v2[j]
						uniao++
					}
				}
				senao
				{
				   se(contemNumero(v1[j],v3,20) == falso)
					{
						v3[uniao] = v1[j]
						uniao++
					}
					se(contemNumero(v2[j],v3,20) == falso)
					{
						v3[uniao] = v2[j]
						uniao++
					}
				}			
		}
		limpa()
		para(inteiro i = 0 ; i < uniao ; i++)
		{
			escreva(v3[i],"\n")
		}
	}

	funcao logico contemNumero(inteiro numero,inteiro vetor[], inteiro qtd)
	{
		para(inteiro l = 0 ; l < qtd; l++)
		{
			se(vetor[l] == numero)
			{
				retorne verdadeiro
			}
		}
		retorne falso
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 84; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {v1, 8, 10, 2}-{v2, 8, 18, 2}-{v3, 8, 26, 2};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
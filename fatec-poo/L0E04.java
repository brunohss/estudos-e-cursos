/* Nome Bruno Henrique dos Santos Silva N  3 - ADS 20/03/2022
 * 
 * L0E04.java
 * 
 *4) Escreva um programa em Java para
ler uma matriz D de dimensão N x M,
onde N e M não poderem ser menores que um. Gerar os elementos
aleatoriamente. O usuário deve informar a dimensão (linha e coluna) e um
valor máximo para elementos aleatórios. O programa efetuar todas as
validações. Lembre-se de aproveitar os recursos da linguagem Java para
facilitar as validações
 * 
 * 
 */

import java.util.Random;
import java.util.Scanner;

public class L0E04 {
	
	
	public static void main (String[] args) {
		
		Random rand = new Random();
		Scanner leia = new Scanner ( System.in );
		
		
		int x,y,r ;
		do{
			System.out.println("Digite o tamanho da linha da matrix: ");
			 x = leia.nextInt();
			
			}	while( x< 0||x>=20);
			do{
			System.out.println("Digite o tamanho da coluna da matrix: ");
			 y = leia.nextInt();
			
			}	while( x< 0||x>=20);
			
			System.out.println("Digite o numero maximo dos numeros randomicos: ");
			 r = leia.nextInt();
		
		int[][] a = new int[x][y];
		
		for ( int i = 0 ; i < x ; i++ ) {
			
			for ( int j = 0 ; j < y ; j++ ) {
				
				//System.out.print("Elemento " + i + " x " + j + ": ");
				a[i][j] = rand.nextInt(r);
			}
		}
		
		
		System.out.println("\n");
		
		for ( int i = 0 ; i < x ; i++ ) {
			
			for ( int j = 0 ; j < y ; j++ ) {
				
				System.out.print ( a[i][j] + "\t");
			}
			
			System.out.println ();
		}
	}
}


/* Nome Bruno Henrique dos Santos Silva N  3 - ADS 20/03/2022
 * 
 * L0E03.java
 * 
 *3) Escreva um programa em Java para
ler uma matriz C quadrada de dimensão N,
onde N é menor ou igual a 20 e imprimir seus elementos. O usuário deve informar o
número o tamanho da matriz quadrada (dimensão) e os elementos podem ser gerados
aleatoriamente (menor que 100).
 * 
 * 
 */

import java.util.Random;
import java.util.Scanner;

public class L0E03 {
	
	
	public static void main (String[] args) {
		
		Random rand = new Random();
		Scanner leia = new Scanner ( System.in );
		
		
		int x ;
		do{
			System.out.println("Digite o tamanho da matrix quadrada: ");
			 x = leia.nextInt();
			
			}	while( x< 0||x>=20);
		
		int[][] a = new int[x][x];
		
		for ( int i = 0 ; i < x ; i++ ) {
			
			for ( int j = 0 ; j < x ; j++ ) {
				
				//System.out.print("Elemento " + i + " x " + j + ": ");
				a[i][j] = rand.nextInt(100);
			}
		}
		
		
		System.out.println("\n");
		
		for ( int i = 0 ; i < x ; i++ ) {
			
			for ( int j = 0 ; j < x ; j++ ) {
				
				System.out.print ( a[i][j] + "\t");
			}
			
			System.out.println ();
		}
	}
}


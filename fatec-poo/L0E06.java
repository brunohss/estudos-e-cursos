/* Nome Bruno Henrique dos Santos Silva N  3 - ADS 20/03/2022
 * 
 * L0E06.java
 * 
 *6) Escreva um programa em Java para gerar aleatoriamente (menor que 25)
uma matriz
N x M de dimensão definidas pelo usuário. Solicitar ao usuário
um valor. Imprimir a matriz gerada. Informar se o valor digitado existe na
matriz, indicando a posição (linha X coluna) e no final a quantidade de
ocorrências
 * 
 * 
 */

import java.util.Random;
import java.util.Scanner;

public class L0E06 {
	
	
	public static void main (String[] args) {
		Random rand = new Random();
		Scanner leia = new Scanner ( System.in );
		
		
		int x,y,r ;
		do{
			System.out.println("Digite o tamanho da linha das matrix: ");
			 x = leia.nextInt();
			
			}	while( x< 0||x>=20);
			do{
			System.out.println("Digite o tamanho da coluna das matrix: ");
			 y = leia.nextInt();
			
			}	while( x< 0||x>=20);
			
			System.out.println("Digite o numero maximo dos numeros randomicos: ");
			 r = leia.nextInt();
		
		int[][] a = new int[x][y];
		int[][] b = new int[x][y];
		for ( int i = 0 ; i < x ; i++ ) {
			
			for ( int j = 0 ; j < y ; j++ ) {
				
				//System.out.print("Elemento " + i + " x " + j + ": ");
				a[i][j] = rand.nextInt(r);
				b[i][j] = rand.nextInt(r);
			}
		}
		
		
		System.out.println("\n Matrix A :\n");
		
		for ( int i = 0 ; i < x ; i++ ) {
			
			for ( int j = 0 ; j < y ; j++ ) {
				
				System.out.print ( a[i][j] + "\t");
			}
			
			System.out.println ();
		};
				
		System.out.println ("\n Matrix B :\n");		
				
				
		for ( int i = 0 ; i < x ; i++ ) {
			
			for ( int j = 0 ; j < y ; j++ ) {
				
				System.out.print ( b[i][j] + "\t");
			}
			
			System.out.println ();
		};
		
		System.out.println ("\n Matrix A  + B :\n");		
				
				
		for ( int i = 0 ; i < x ; i++ ) {
			
			for ( int j = 0 ; j < y ; j++ ) {
				
				System.out.print ( b[i][j] + a[i][j] + "\t");
			}
			
			System.out.println ();
		}
		
		
		
	}
}


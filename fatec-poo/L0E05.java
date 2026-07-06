/* Nome Bruno Henrique dos Santos Silva N  3 - ADS 20/03/2022
 * 
 * L0E05.java
 * 
 *5) Escreva um programa em Java para
ler 2 matrizes N x M (definido pelo usuário) e
calcular a soma entre elas gerando uma terceira matriz.
 * 
 * 
 */

import java.util.Random;
import java.util.Scanner;

public class L0E05 {
	
	
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


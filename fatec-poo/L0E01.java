/* Nome Bruno Henrique dos Santos Silva N  3 - ADS 20/03/2022
 *
 * L0E01.java
 *
 * 1) Escreva um programa em Java para
ler uma matriz A de 4 linhas por 5 colunas e
imprimir seus elementos.
 *
 *
 */

import java.util.Scanner;

public class L0E01 {
    public static void main(String[] args) {

        Scanner leia = new Scanner ( System.in );

        int[][] a = new int[4][5];

        System.out.println("Entre com os elementos da matriz A");

        for ( int i = 0 ; i < 4 ; i++ ) {

            for ( int j = 0 ; j < 5 ; j++ ) {

                System.out.print("Elemento " + i + " x " + j + ": ");
                a[i][j] = leia.nextInt();
            }
        }


        System.out.println("\n");

        for ( int i = 0 ; i < 4 ; i++ ) {

            for ( int j = 0 ; j < 5 ; j++ ) {

                System.out.print ( a[i][j] + "\t");
            }

            System.out.println ();
        }
    }
}


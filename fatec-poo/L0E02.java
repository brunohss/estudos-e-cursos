/* Nome Bruno Henrique dos Santos Silva N  3 - ADS 20/03/2022
 *
 * L0E02.java
 *
 * 2) Escreva um programa em Java para
geral aleatoriamente os elementos
(menor que 100) de uma matriz B de 6 linha por 3 colunas, imprimir a matriz
gerada e imprimir a matriz em ordem invertida.
 *
 *
 */

import java.util.Random;

public class L0E02 {


    public static void main (String[] args) {

        Random rand = new Random();

        int[][] a = new int[4][5];

        //System.out.println("Entre com os elementos da matriz A");

        for ( int i = 0 ; i < 4 ; i++ ) {

            for ( int j = 0 ; j < 5 ; j++ ) {

                //System.out.print("Elemento " + i + " x " + j + ": ");
                a[i][j] = rand.nextInt(100);
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


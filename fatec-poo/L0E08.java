/* Nome Bruno Henrique dos Santos Silva N  3 - ADS 20/03/2022
 *
 * L0E08.java
 *
 *8) Escreva um programa em Java para gerar uma matriz F (N x M).
 * Criar os vetores IMPAR e PAR com a quantidade de elementos (ímpares / pares) da matriz.
 * Imprimir a matriz e os vetores. Validar para caso não haja uma das duas possibilidades
 *  (sem elementos pares ou ímpares).
 *
 */

import java.util.Random;
import java.util.Scanner;

public class L0E08 {


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


        int[][] a = new int[x][y];

        for ( int i = 0 ; i < x ; i++ ) {

            for ( int j = 0 ; j < y ; j++ ) {
                int n = rand.nextInt(50);
                if(j%2==0){ a[i][j] = 2*rand.nextInt(50)+1;
                }else{a[i][j] = 2*rand.nextInt(50);

                }
                //System.ou a[i][j] =t.print("Elemento " + i + " x " + j + ": ");

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


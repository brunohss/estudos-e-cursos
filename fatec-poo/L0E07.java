/* Nome Bruno Henrique dos Santos Silva N  3 - ADS 20/03/2022
 *
 * L0E07.java
 *
 *8) Escreva um programa em Java para gerar uma matriz F (N x M). Criar os
vetores IMPAR e PAR com a quantidade de elementos (ímpares / pares) da matriz.
* Imprimir a matriz e os vetores. Validar para caso não haja uma das
duas possibilidades (sem elementos pares ou ímpares)
 *
 */

import java.util.Random;
import java.util.Scanner;

public class L0E07 {


    public static void main (String[] args) {

        Random rand = new Random();
        Scanner leia = new Scanner ( System.in );

        int[]   comp={100,0,0,0,0,0};
        int     x,
                y;
        do{
            System.out.println("Digite o tamanho da linha da matrix: ");
            x = leia.nextInt();

        }	while( x< 0||x>=20);
        do{
            System.out.println("Digite o tamanho da coluna da matrix: ");
            y = leia.nextInt();

        }	while( x< 0||x>=20);



        int[][] a = new int[x][y];

        for ( int i = 0 ; i < x ; i++ ) {

            for ( int j = 0 ; j < y ; j++ ) {

                //System.out.print("Elemento " + i + " x " + j + ": ");
                a[i][j] = rand.nextInt(100);
                if(a[i][j]>=comp[3]){
                    comp[3]=a[i][j];
                    comp[4]=i+1;
                    comp[5]=j+1;
                }
                if(a[i][j]<=comp[0]){
                    comp[0]=a[i][j];
                    comp[1]=i+1;
                    comp[2]=j+1;
                }

            }
        }


        System.out.println("\n");

        for ( int i = 0 ; i < x ; i++ ) {

            for ( int j = 0 ; j < y ; j++ ) {

                System.out.print ( a[i][j] + "\t");
            }

            System.out.println ();
            }
        System.out.print("O maior numero desta matrix é " + comp[0] + " , esta na linha " + comp[1] + " e na coluna: " + comp[2]+ " ;") ;
        System.out.print("\nO menor numero desta matrix é " + comp[3] + " , esta na linha " + comp[4] + " e na coluna: " + comp[5]+ " .");

    }

}


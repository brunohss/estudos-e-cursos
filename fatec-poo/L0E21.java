/* Nome Bruno Henrique dos Santos Silva N  3 - ADS 20/03/2022
 *5
 * L0E21.java
 *
 *21) Escreva um programa em Java para gerar uma matriz (N x M) e outra (N x P).
 * Gerar uma terceira matriz (N x (M+P)), sendo que para cada linha concatenar suas respectivas
 *  colunas e apresentar as três matrizes.


 *
 */

import java.util.Random;
import java.util.Scanner;

public class L0E21 {


    public static void main(String[] args) {

        Random rand = new Random();
        Scanner leia = new Scanner(System.in);


        int x, y, z;

        System.out.println("Digite o tamanho da linha das matrix: ");
        x = leia.nextInt();
        System.out.println("Digite o tamanho da coluna da matrix A: ");
        y = leia.nextInt();


        System.out.println("Digite o tamanho da coluna da matrix B:");
        z = leia.nextInt();

        int[][] a = new int[x][y];
        int[][] b = new int[x][z];
        int[][] c = new int[x][y + z];

        for (int i = 0; i < x; i++) {

            for (int j = 0; j < y; j++) {

                //System.out.print("Elemento " + i + " x " + j + ": ");
                a[i][j] = rand.nextInt(100);

            }
        }

        for (int i = 0; i < x; i++) {

            for (int j = 0; j < z; j++) {

                //System.out.print("Elemento " + i + " x " + j + ": ");
                b[i][j] = rand.nextInt(100);

            }
        }



        for (int i = 0; i < x; i++) {
           if(z>=y) {
               for (int j = 0; j < z; j++) for (int k = 0; k < x; k++) c[i][j] += a[i][k] * b[k][j];
           }
           else{
               for (int j = 0; j < z; j++) for (int k = 0; k < x; k++) c[i][j] += a[i][k] * b[k][j];
           }
        }



        System.out.println ("\n Matriz A :\n");

        for ( int i = 0 ; i < x ; i++ ) {

            for ( int j = 0 ; j < y ; j++ ) {

                System.out.print ( a[i][j] + "\t");
            }

            System.out.println ();
        }

        System.out.println ("\n Matriz B :\n");


        for ( int i = 0 ; i < x ; i++ ) {

            for ( int j = 0 ; j < z ; j++ ) {

                System.out.print ( b[i][j] + "\t");
            }

            System.out.println ();
        }

        System.out.println ("\n Matriz C :\n");


        for ( int i = 0 ; i < x ; i++ ) {
            if(y<z){for ( int j = 0 ; j < z ; j++ ) {

                System.out.print ( c[i][j] + "\t");
            }

            System.out.println ();
        }else{

                for (int j = 0; j < z; j++) {

                        System.out.print(c[i][j] + "\t");
                    }

                    System.out.println ();
                }
            }
        }


    }


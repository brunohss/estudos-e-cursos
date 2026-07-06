/* Nome Bruno Henrique dos Santos Silva N  3 - ADS 20/03/2022
 *5
 * L0E20.java
 *
 *20) Escreva um programa em Java para gerar uma matriz quadrada T de dimensão N.
 *  Imprimir os elementos da “ampulheta”.

 *
 */

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class L0E20 {


    public static void main(String[] args) {
        Random rand = new Random();
        Scanner leia = new Scanner(System.in);

        ArrayList<String> saida;
        saida = new ArrayList();
        ArrayList<String> saida1;
        saida1 = new ArrayList();
        int x, y;
        System.out.println("Digite o tamanho da matrix quadrada: ");
        x = leia.nextInt();


        System.out.println("Digite o tamanho da dimensão da matrix: ");
        y = leia.nextInt();


        int[][][] a = new int[y][x][x];
        for (int c = 0; c < y; c++) {
            for (int i = 0; i < x; i++) {

                for (int j = 0; j < x; j++) {

                    //System.out.print("Elemento " + i + " x " + j + ": ");
                    a[c][i][j] = rand.nextInt(100);
                }
            }
        }


        System.out.println("\n");
        for (int c = 0; c < y; c++) {


            for (int i = 0; i < x; i++) {

                for (int j = 0; j < x; j++) {
                    System.out.print(a[c][i][j] + "\t");
                    //linha + coluna = dimensão + 1

                    if (i < j) {
                        if (i + j < x - 1) {
                            saida.add(String.valueOf(a[c][i][j]));
                        }
                    }
                    if (i > j) {
                        if (i + j > x - 1) {
                            saida1.add(String.valueOf(a[c][i][j]));
                        }
                    }

                }
                System.out.println();
            }
            System.out.println("\n");
        }
        System.out.println("Os elementos da parte superior da ampulheta: " + saida);
        System.out.println("Os elementos da da parte inferior da ampulheta: " + saida1);
        System.out.println("Os elementos da  ampulheta: " + saida + saida1);
    }

}


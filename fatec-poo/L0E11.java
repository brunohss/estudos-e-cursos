/* Nome Bruno Henrique dos Santos Silva N  3 - ADS 20/03/2022
 *
 * L0E11.java
 *
 *1) Escreva um programa em Java para gerar uma matriz quadrada K de dimensão N.
Imprimir os elementos da abaixo da diagonal principal (inclusa).

 *
 */

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class L0E11 {


    public static void main(String[] args) {
        Random rand = new Random();
        Scanner leia = new Scanner(System.in);

        ArrayList<String> saida;
        saida = new ArrayList<String>();
        int x, y;
        do {
            System.out.println("Digite o tamanho da matrix quadrada: ");
            x = leia.nextInt();

        } while (x < 0 || x >= 20);
        do {
            System.out.println("Digite o tamanho da dimensão da matrix: ");
            y = leia.nextInt();

        } while (x < 0 || x >= 20);




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
                    System.out.print ( a[c][i][j] + "\t");
                    //linha + coluna = dimensão + 1
                    if(i>=j){
                        saida.add(String.valueOf(a[c][i][j]));
                    }
                }
                System.out.println ();
            }
            System.out.println ("\n");
        }
        System.out.println("Os elementos da diagonal abaixo da principal sao: " + saida);
    }
}


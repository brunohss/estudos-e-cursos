#include <stdio.h>

int main() {
    int tamanho, i, j, espacos;

    // Solicita ao usuário o tamanho da pirâmide
    printf("Digite o tamanho da piramide: ");
    scanf("%d", &tamanho);

    // Verifica se o tamanho é válido
    if (tamanho <= 0) {
        printf("O tamanho deve ser um numero positivo.\n");
        return 1;
    }

    // Gera a pirâmide2
    for (i = 1; i <= tamanho; i++) {
        // Imprime os espaços à esquerda
        for (espacos = 0; espacos < tamanho - i; espacos++) {
            printf(" ");
        }
        // Imprime os caracteres '#'
        for (j = 0; j < (2 * i - 1); j++) {
            printf("#");
        }
        printf("\n"); // Próxima linha
    }

    return 0;
}

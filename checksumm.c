#include <stdio.h>

unsigned short calculateChecksum(unsigned short data[], int n) {
    unsigned int sum = 0;

    for (int i = 0; i < n; i++) {
        sum += data[i];

        if (sum >> 16) {
            sum = (sum & 0xFFFF) + 1;
        }
    }

    return ~sum & 0xFFFF;
}

int main() {
    int n;
    printf("Enter the number of data words: ");
    scanf("%d", &n);

    unsigned short data[n];
    printf("Enter %d data words (in hexadecimal, e.g. 0x1234):\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%hx", &data[i])
    }

    unsigned short checksum = calculateChecksum(data, n);
    printf("\nCalculated Checksum (Sender side): 0x%04X\n", checksum);

    printf("\n--- Receiver Side Verification ---\n");
    printf("Enter the received %d data words:\n", n);
    unsigned short recvData[n];
    for (int i = 0; i < n; i++) {
        scanf("%hx", &recvData[i]);
    }

    unsigned int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += recvData[i];
        if (sum >> 16) {
            sum = (sum & 0xFFFF) + 1;
        }
    }
    sum += checksum;
    if (sum >> 16) {
        sum = (sum & 0xFFFF) + 1;
    }

    if ((sum & 0xFFFF) == 0xFFFF) {
        printf("\n No Error: Data received correctly.\n");
    } else {
        printf("\n Error detected in received data!\n");
    }

    return 0;
}

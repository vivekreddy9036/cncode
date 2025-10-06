#include <stdio.h>

// Function to calculate checksum
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
    printf("Enter %d data words (hexadecimal, e.g. 0x1234):\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%hx", &data[i]);
    }

    unsigned short checksum = calculateChecksum(data, n);
    printf("\nCalculated Checksum (Sender side): 0x%04X\n", checksum);

    printf("\n--- Receiver Side Verification ---\n");

    unsigned short recvData[n];
    for (int i = 0; i < n; i++) {
        recvData[i] = data[i];
    }

    recvData[0] ^= 0x000F;  
    printf("Simulating error: Modified first data word.\n");

    //verify
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

    // (b) Check result
    if ((sum & 0xFFFF) == 0xFFFF) {
        printf("No Error: Data received correctly.\n");
    } else {
        printf(" Error detected in received data!\n");
    }

    return 0;
}

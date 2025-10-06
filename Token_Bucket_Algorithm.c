#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>  // for sleep()

int main() {
    int bucketSize, tokenRate, packetSize, nPackets;
    int tokens = 0;   // current number of tokens in the bucket

    // Step 1: Input parameters
    printf("Enter bucket capacity (in tokens): ");
    scanf("%d", &bucketSize);

    printf("Enter token arrival rate (tokens per second): ");
    scanf("%d", &tokenRate);

    printf("Enter number of packets to be sent: ");
    scanf("%d", &nPackets);

    int packets[nPackets];
    printf("Enter packet sizes (in tokens needed for each packet):\n");
    for (int i = 0; i < nPackets; i++) {
        scanf("%d", &packets[i]);
    }

    printf("\n--- Token Bucket Simulation ---\n");

    for (int i = 0; i < nPackets; i++) {
        // Step 2: Add tokens periodically (simulate time passing)
        sleep(1);  // simulate 1 second interval
        tokens += tokenRate;

        // ensure tokens do not exceed bucket capacity
        if (tokens > bucketSize)
            tokens = bucketSize;

        printf("\nPacket %d of size %d arrived. Tokens available = %d\n",
               i + 1, packets[i], tokens);

        // Step 3: Check if enough tokens are available
        if (tokens >= packets[i]) {
            tokens -= packets[i];  // consume tokens
            printf(" Packet %d sent. Remaining tokens = %d\n", i + 1, tokens);
        } else {
            // Step 4: Packet dropped
            printf(" Packet %d dropped (insufficient tokens).\n", i + 1);
        }
    }

    return 0;
}

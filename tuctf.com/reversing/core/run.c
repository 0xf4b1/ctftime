#include <stdio.h>  // prints
#include <stdlib.h> // malloc
#include <string.h> // strcmp
#include <unistd.h> // read
#include <fcntl.h>  // open
#include <unistd.h> // close
#include <time.h>   // time

#define FLAG_LEN 64
char flag[FLAG_LEN];

void xor(char *str, int len) {
	for (int i = 0; i < len; i++) {
		str[i] = str[i] ^ 1;
	}
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 20);
    setvbuf(stdin, NULL, _IONBF, 20);

	// Read the flag
	memset(flag, 0, FLAG_LEN);
	printf("> ");
	int len = read(0, flag, FLAG_LEN);

	xor(flag, len);

	char buf[32];
	read(0, buf, 128);

    return 0;
}

#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "subtract.h"

#include "key.h"

#define NAME "swh2"

int private_subtract(int a, int b) {
	return a - b;
}

int subtract(int a, int b, const char *key) {
	if(strcmp(key, KEY)) {
		fprintf(stderr, "%s: Illegal operation.\n", NAME);
		exit(EXIT_FAILURE);
	}
	return private_subtract(a, b);
}

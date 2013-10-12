#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "add.h"

#include "key.h"

#define NAME "swh1"

int private_add(int a, int b) {
	return a + b;
}

int add(int a, int b, const char *key) {
	if(strcmp(key, KEY)) {
		fprintf(stderr, "%s: Illegal operation.\n", NAME);
		exit(EXIT_FAILURE);
	}
	return private_add(a, b);
}

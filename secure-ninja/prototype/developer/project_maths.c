#include <stdlib.h>
#include <stdio.h>
#include <getopt.h>

#include "../swh1/add.h"
#include "../swh2/subtract.h"
#include "keys.h"

#define OPTLIST "i:a:s:"

int main(int argc, char *argv[]) {
	int x = 0;
	int opt;
	while((opt = getopt(argc, argv, OPTLIST)) != -1) {
		switch(opt) {
			case 'i': x = atoi(optarg); break;
			case 'a': x = add(x, atoi(optarg), SWH_swh1_KEY); break;
			case 's': x = subtract(x, atoi(optarg), SWH_swh2_KEY); break;
			default: return EXIT_FAILURE;
		}
		printf("%d\n", x);
	}
}

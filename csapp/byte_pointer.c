#include <stdio.h>

typedef unsigned char *byte_pointer;

void show_bytes(byte_pointer start, size_t len) {
        int i;
        for (i = 0; i < len; i++)
                printf(" %.2x", start[i]);
        printf("\n");
}

void show_int(int x) {
        show_bytes((byte_pointer) &x, sizeof(int));
}

void show_float(float x) {
        show_bytes((byte_pointer) &x, sizeof(float));
}

void show_pointer(void *x) {
        show_bytes((byte_pointer) &x, sizeof(void *));
}

void main() {
        show_int(12);
        show_int(122);
        show_int(1111);
        show_int(1344);
        show_int(123123);
        show_int(2934293);

        show_float(1.000);
        show_float(48423.121);

        int i = 190;
        void* p_i = &i;
        show_pointer(p_i);

        char c = 'u';
        void* p_c = &c;
        show_pointer(p_c);
}

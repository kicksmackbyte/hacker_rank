#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char* ltrim(char*);
char* rtrim(char*);
int len(char*);

int parse_int(char*);

/*
 * Complete the 'extraLongFactorials' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

int LL_BITS = 256;

int len(char* s) {
    int length = 0;
    while(s[length] != 0) {
        ++length;
    }

    return length;
}

int eq(char* a, char* b) {
    int i = 1;
    while(a[i] == b[i]){
        ++i;
    }

    return i == LL_BITS ? 1 : 0;
}

char* pad(char* s) {
    int length = len(s);
    char* new_s = calloc(LL_BITS, sizeof(char*));
    int size_diff = LL_BITS - length;

    for(int i = 0; i < size_diff; ++i) {
        new_s[i] = '0';
    }

    for(int i = 0; i < length; ++i) {
        new_s[size_diff + i] = s[i];
    }

    return new_s;
}

char* trim(char* s) {
    int start = 0;
    while(s[start] == '0') {
        ++start;
    }

    char* new_s = calloc(LL_BITS-start, sizeof(char*));

    for(int i = 0; i < LL_BITS-start; ++i) {
        new_s[i] = s[start+i];
    }

    return new_s;
}

char itoa(int i) {
    char result = i + '0';
    return result;
}

char* add(char* x, char* y) {
    char* padded_x = pad(x);
    char* padded_y = pad(y);
    char* result = pad("");

    int carry = 0;
    for(int i = LL_BITS-1; i >= 0; --i) {
        char x_bit = padded_x[i];
        char y_bit = padded_y[i];

        int sum = (x_bit-'0') + (y_bit-'0') + carry;
        if(sum > 9) {
            carry = 1;
            sum = sum % 10;
        }
        else {
            carry = 0;
        }

        result[i] = sum + '0';
    }

    return result;
}

char* sub(char* x, char* y) {
    char* padded_x = pad(x);
    char* padded_y = pad(y);
    char* result = pad("");

    int borrow = 0;
    for(int i = LL_BITS-1; i >= 0; --i) {
        char x_bit = padded_x[i];
        char y_bit = padded_y[i];

        int diff = (x_bit-'0') - (y_bit-'0') - borrow;
        if(diff < 0) {
            borrow = 1;
            diff = 9;
        }
        else {
            borrow = 0;
        }

        result[i] = diff + '0';
    }

    return result;
}

void plusplus(char** i) {
    *i = add(*i, "1");
}

int gt(char* x, char* y) {
    int result = 0;

    for(int i = 0; (i < LL_BITS) && (result == 0); ++i) {
        int x_bit = x[i]-'0';
        int y_bit = y[i]-'0';

        if(x_bit > y_bit) {
            result = 1;
            break;
        }
    }

    return result;
}

char* mul(char* x, char* y) {
    char* result = pad("");
    char* stop = pad(x);

    for(char* i = pad(""); strcmp(i, stop) != 0; plusplus(&i)) {
        result = add(result, y);
    }

    return result;
}

char* extraLongFactorials(char* n) {
    char* stop = pad("1");

    if(strcmp(n, stop)) {
        char* factorial = mul(n, extraLongFactorials(sub(n, "1")));
        return factorial;
    }
    else {
        return stop;
    }
}

int main()
{
    //int n = parse_int(ltrim(rtrim(readline())));

    //char* fact = extraLongFactorials(5);
    //char* diff = sub("17", "2");
    //int length = len("12345");
    //printf("%d\n", length);

    //char* padded = pad("12345");
    //printf("%s\n", padded);

    //char* sum = add("8", "4");
    //printf("%s\n", sum);

    //char* diff = sub("452", "123");
    //printf("%s\n", diff);

    //char* product = mul("3", "4");
    //printf("%s\n", product);

    char* n = pad("100");
    char* fact = extraLongFactorials(n);
    printf("%s\n", trim(fact));

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;

    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) {
            break;
        }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') {
            break;
        }

        alloc_length <<= 1;

        data = realloc(data, alloc_length);

        if (!data) {
            data = '\0';

            break;
        }
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';

        data = realloc(data, data_length);

        if (!data) {
            data = '\0';
        }
    } else {
        data = realloc(data, data_length + 1);

        if (!data) {
            data = '\0';
        } else {
            data[data_length] = '\0';
        }
    }

    return data;
}

char* ltrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    while (*str != '\0' && isspace(*str)) {
        str++;
    }

    return str;
}

char* rtrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    char* end = str + strlen(str) - 1;

    while (end >= str && isspace(*end)) {
        end--;
    }

    *(end + 1) = '\0';

    return str;
}

int parse_int(char* str) {
    char* endptr;
    int value = strtol(str, &endptr, 10);

    if (endptr == str || *endptr != '\0') {
        exit(EXIT_FAILURE);
    }

    return value;
}

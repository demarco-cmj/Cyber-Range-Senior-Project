#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* This is a function that will never be called. Why? Well, it is just here to
    pad out where things are in memory, so you can ignore it */
float useless_function(int loop, float number) {
    for (int i = 0; i < loop; i++)
    {
        number = number / 2;
    }
    return number;
}


/* break_me is where the buffer overflow will occur. It takes what the
    user inputted, copies the input into a buffer, and in real life it would
    check it aginst correct passwords but since we don't want any password to
    work, we won't do that */
int break_me (char *input) {
    int placeholder = 20;
    /* Here, we set up the string_buffer to accept at most 16 chars */
    char string_buffer[16];

    /* This is what causes the buffer overflow. strcpy will copy every char in
        input into string_buffer, even if the space allocated to string_buffer
        is less than what is in input. This will cause memory not assigned to
        string_buffer to be overwritten causing issues. The exploit was later
        updated with strncpy that won't copy all of input if it is too big, and
        something similar is used in newer languages like Python by default,
        thus this program being in C */
    strcpy (string_buffer, input);

    /* Just some code to pad this function out. */
    if (placeholder == 20) {
        placeholder--;
    } else if (placeholder > 20) {
        placeholder = placeholder - placeholder % 20 - 1;
    } else {
        return 1;
    }

    /* Make sure we only return false */
    return 0;
}

/* Here, we take the user input, it to break_me to get "verified," and if
    we get back a 1, then we will print "Overflow Occured!" and "Failed" if 0
    is returned */

int main (int argc, char *argv[]) {
    /* If no password was given at start time, return 0 */
    if (argc < 2) {
        return 0;
    }
    
    /* If break_me returns 1, print that overflow has occured. This is where
    	you want to get into. Otherwise, the program will print "Failed" */
    if (break_me (argv[1])) {
        printf("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n");
        printf(" What are you doing in here?\n");
        printf("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n");
    } else {
        printf ("\nFailed\n");
    }
}

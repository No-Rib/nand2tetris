// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.


(INIT)
// initialize counter of 16bit blocks
    @8192
    D=A
    @R0
    M=D

// initialize pointer to 16bit block
    @SCREEN
    D=A
    @R1
    M=D

// scan a char
    @KBD
    D=M

// goto: if key is pressed
    @KDLOOP
    D;JNE

// goto: if key is not pressed
    @KULOOP
    D;JEQ


// logic: if key is pressed

(KDLOOP)

// move to screen mem
    @R1
    A=M

// paint it black
    M=-1
    
// decrement the counter
    @R0
    M=M-1

// break loop when all is black
    @INIT
    M;JEQ

// move to next 16bit block
    @R1
    M=M+1

    @KDLOOP
    0;JMP


(KULOOP)

// move to screen mem
    @R1
    A=M

// paint it white
    M=0

// decrement the counter
    @R0
    M=M-1

// break the loop when all is white
    @INIT
    M;JEQ

// move to next 16bit block
    @R1
    M=M+1

    @KULOOP
    0;JMP



"""Constants used by VM translator."""

"""Command codes."""
C_ARITHMETICS = 0
C_CALL = 1
C_FUNCTION = 2
C_GOTO = 3
C_IF = 4
C_LABEL = 5
C_POP = 6
C_PUSH = 7
C_RETURN = 8


"""Segment names."""
S_ARG    = 'argument'
S_CONST  = 'constant'
S_LOCAL  = 'local'
S_PTR    = 'pointer'
S_STATIC = 'static'
S_TEMP   = 'temp'
S_THAT   = 'that'
S_THIS   = 'this'

DLXassembler
============

A python assembler for the DLX instruction set.

Recursive Decent Parser
```
G = (T, N, P, S) where  
T = {  
        .asciiz, .align, .word, .double, .space, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x,  
         y, z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8,  
         9  
    },  
N = {<Outline>, <RomanNumeral>, <CapitalLetter>, <ArabicNumeral>, <LowercaseLetter>, <Level1>, <Level2>, <Level3>, <Level4>},  
P = {  
    
    <label>
    
    <OctalNumber> ::= 0<OctalValue>
    <OctalValue> ::= <OctalDigit><OctalValue> | λ
    
    <HexNumber> ::= 0x<HexValue>
    <HexValue> ::=  <DecimalDigit><HexValue> | <HexCharacter><HexValue> | λ
    
    <DecimalNumber> ::= <NonZeroDecimalDigit><DecimalValue>
    <DecimalValue> ::= <DecimalDigit><DecimalValue> | λ
    
    <OctalDigit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7
    <NonZeroDecimalDigit> ::= 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
    <DecimalDigit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
    <HexCharacter> ::= a | b | c | d | e | f | A | B | C | D | E | F
},  
S = <Outline>
```
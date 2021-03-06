LIST P=PIC18F458,F=INHX32,N=0,ST=OFF,R=HEX
#include p18f458.inc
    CONFIG OSC=XT,OSCS=OFF
    CONFIG WDT= OFF,BOR=ON
    CONFIG BORV=45,PWRT=ON
    CONFIG  LVP = OFF            
    
R0 EQU 0x07
R1 EQU 0x08
R2 EQU 0x09 
Rr EQU 0x0A
RL EQU 0x0B
Rl EQU 0x0C
	
    	ORG 0
	;PORT B & D0,D1 AS OUTPUTS 
	CLRF TRISB 
	CLRF TRISC 

	BSF PORTC , 4
	BSF PORTC , 5
	
L3	MOVLW 0x00    ; 00000000	
	MOVWF RL
L1	MOVLW 0x00   ; 00000000	
	MOVWF R0
	MOVLW 0x0A   ; 00000000	
	MOVWF Rr
	MOVLW 0x0A   ; 00000000	
	MOVWF Rl	
	;START COUNTING 

	;right  on , left off 
L2	MOVF R0 ,W 
	MOVWF PORTC
	BSF PORTC , 4
	BCF PORTC , 5
	INCF R0,F
	CALL DELAY
	
	MOVF RL ,W 
	MOVWF PORTC
	BSF PORTC , 5
	BCF PORTC , 4
	CALL DELAY
	DECF Rr,F
	BNZ L2
	INCF RL,F
	CALL DELAY
	DECF Rl,F
	BZ L3
	GOTO L1
	
	

DELAY	MOVLW D'200'
	MOVWF R1	
D1	MOVLW D'250'
	MOVWF R2
D2 	NOP
	NOP
	DECF R2,F
	BNZ D2		
	DECF R1,F
	BNZ D1
	RETURN

SECDELAY CALL DELAY
	 CALL DELAY
	 CALL DELAY
	 CALL DELAY
	RETURN
    END
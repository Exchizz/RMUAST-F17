/****************************************************************************
# FroboScout Safety Controller firmware
# Copyright (c) 2015, Kjeld Jensen <kjen@mmmi.sdu.dk> <kj@kjen.dk>
# All rights reserved.
****************************************************************************/
/* includes */
#include <stdlib.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include "nano_def.h"

/* defines */
/* #define INT0_CNT_TOP	249 */ /* corresponds on an interrupt0 each 1ms */
#define INT1_1MS_CNT 2000 /* 1ms */

/* variables */
volatile unsigned char t1ms;

/***************************************************************************/
void timer_1ms_init(void)
{
	/* timer 0 interrupt init (each 1ms) */
	t1ms = 0;
	/* TIMSK0 = BV(OCIE0A);  */
	/* TCCR0A = BV(CS00) | BV(CS01) | BV(WGM01); */ /* clk/64, TOS is defined as OCR0A */  
	/* OCR0A = INT0_CNT_TOP; */

	TIMSK1 = BV(OCIE1A); 
	TCCR1B = BV(CS11) | BV(WGM12); /* clk/8, Clear Timer on Compare Match (OCR1A) */  
	OCR1A = INT1_1MS_CNT;
}
/***************************************************************************/
ISR (TIMER1_COMPA_vect)
{
	t1ms++;
}
/***************************************************************************/


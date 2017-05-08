/****************************************************************************
# Copyright (c) 2015, Kjeld Jensen <kjeld@cetus.dk>
# All rights reserved.
****************************************************************************/

/* includes */
#include <stdlib.h>
#include <avr/interrupt.h>
#include <avr/wdt.h>
#include "nano_def.h"
#include "timer.h"
#include "scheduler.h"
#include "reset.h"
#include "protocol.h"

/***************************************************************************/
int main(void)
{
	save_reset_cause(); /* determine the cause of the startup */
	timer_1ms_init(); /* initialize the 1ms timer */
	sei(); /* enable interrupts */

	task_init(); /* initialize all tasks */
	/* wdt_enable (WDTO_15MS); */ /* enable watchdog reset at approx 15 ms (ref. p.58) */

	for (;;) /* go into an endless loop */
	{
		if (t1ms != 0) /* if the interrupt has timed out after 10ms */
		{
			t1ms --;
			task_update(); /* run the scheduler */
		}
		else
			task_idle();
	}
	return 0; /* just for the principle as we never get here */
}
/***************************************************************************/

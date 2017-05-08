/****************************************************************************
# Copyright (c) 2015, Kjeld Jensen <kjeld@cetus.dk>
# All rights reserved.
****************************************************************************/
/* includes */
#include <avr/wdt.h>
#include "nano_def.h"
#include "scheduler.h"
#include "led_rgy.h"
#include "buttons.h"
#include "adc.h"
#include "protocol.h"

/* defines */
/*typedef struct{
   unsigned char a[16];
} string; */

/* variables */
static unsigned short t1ms_cnt;
char link_state;
char user_state;

/***************************************************************************/
void task_init(void)
{
	/* string s; */

	link_state = LINK_STATE_STARTUP;
	user_state = USER_STATE_STARTUP;
	t1ms_cnt = 0;

	button_init();

	led_rgy_init();
	led_red_set(1);
	led_yellow_set(-1);
	led_green_set(-1);

	adc_init();

	proto_init();
	proto_send_boot();

	link_state = LINK_STATE_OFFLINE;
	user_state = USER_STATE_IDLE;
}
/***************************************************************************/
void task_idle(void)
{
	proto_update();
}
/***************************************************************************/
void task_5ms(void)
{
	/* wdt_reset(); */ /* reset watchdog */
}
/***************************************************************************/
void task_10ms(void)
{
}
/***************************************************************************/
void task_20ms(void)
{
}
/***************************************************************************/
void task_50ms(void)
{
	proto_send_controls();
}
/***************************************************************************/
void task_100ms(void)
{
	button_update();
}
/***************************************************************************/
void task_200ms(void)
{
	led_rgy_update();
	if (but_enter_state == BUTTON_STATE_LONG_RELEASE)
		but_enter_state = BUTTON_STATE_OFF;
	if (but_enter_state == BUTTON_STATE_SHORT_RELEASE)
		but_enter_state = BUTTON_STATE_OFF;
	if (but_exit_state == BUTTON_STATE_LONG_RELEASE)
		but_exit_state = BUTTON_STATE_OFF;
	if (but_exit_state == BUTTON_STATE_SHORT_RELEASE)
		but_exit_state = BUTTON_STATE_OFF;
}
/***************************************************************************/
void task_update(void)
{
	t1ms_cnt++;
	if (t1ms_cnt == 10000)
		t1ms_cnt = 0;
	
	if (t1ms_cnt % 5 == 0) /* each 5 ms */
	{
		task_5ms();

		if (t1ms_cnt % 10 == 0) /* each 10 ms */
		{
			task_10ms();
		}
		if (t1ms_cnt % 20 == 0) /* each 20 ms */
		{
			task_20ms();
		}
		if (t1ms_cnt % 50 == 0) /* each 50 ms */
		{
			task_50ms();
		}

		if (t1ms_cnt % 100 == 0) /* each 100 ms */
		{
			task_100ms();
		}

		if (t1ms_cnt % 200 == 0) /* each 200 ms */
		{
			task_200ms();
		}
	}
}
/***************************************************************************/


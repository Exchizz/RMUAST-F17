/****************************************************************************
# Copyright (c) 2015, Kjeld Jensen <kjeld@cetus.dk>
# All rights reserved.
****************************************************************************/

/* defines */
#define LINK_STATE_STARTUP		0
#define LINK_STATE_OFFLINE		1
#define LINK_STATE_ONLINE		2

#define USER_STATE_STARTUP		0
#define USER_STATE_IDLE			1
#define USER_STATE_MANUAL		2
#define USER_STATE_AUTO			3
#define USER_STATE_MENU			4

/* variables */
extern char link_state;
extern char user_state;

/* function prototypes */
void task_init(void);
void task_update(void);
void task_idle(void);
void task_5ms(void);
void task_10ms(void);
void task_20ms(void);
void task_50ms(void);
void task_100ms(void);
void task_200ms(void);

/***************************************************************************/


/*
 * led.h
 *
 *  Created on: Apr 14, 2016
 *      Author: exchizz
 */
#include "at90can_def.h"
#ifndef LED_H_
#define LED_H_

//extern QueueHandle_t Queue_Uart_Tx;
//extern QueueHandle_t Queue_Uart_Rx;

void led_init();
void is_alive_task(uint8_t my_state);

#endif /* LED_H_ */

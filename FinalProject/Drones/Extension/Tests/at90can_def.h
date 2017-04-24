/*
 * at90can_def.h
 *
 *  Created on: Apr 14, 2016
 *      Author: exchizz
 */
#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdint.h>
#include <stdbool.h>


#ifndef AT90CAN_DEF_H_
#define AT90CAN_DEF_H_


#define WIFI_BOARD 1

#define INT0_CNT_TOP	125//249 /* corresponds on an interrupt0 each 1ms */

#define BV(bit) (1<<bit) /* return bit value for a bit */

#define PB_OUT( ddr, bit)		ddr |= BV(bit) /* set port bit as output */
#define PB_IN( ddr, bit) ddr &= ~BV(bit) /* set port bit as input */
#define PB_HIGH( port, bit)		port |= BV(bit) /* set port bit high */
#define PB_LOW( port, bit)		port &= ~BV(bit) /* set port bit low */
#define PB_FLIP( port, bit)		port ^= BV(bit) /* flip port bit */


/* LED defines */
#define INT_LED_INIT_YELLOW		PB_OUT (DDRG,DDE3) /* set LED bit as output */
#define INT_LED_ON_YELLOW			PB_LOW (PORTG,PE3) /* turn LED on */
#define INT_LED_OFF_YELLOW			PB_HIGH (PORTG,PE3) /* turn LED off */


#endif /* AT90CAN_DEF_H_ */

#include "led.h"
#include "at90can_def.h"

int main(){
	led_init();
	INT_LED_ON_YELLOW;
	while(1);

return 0;
}

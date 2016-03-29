MODULES = AccelGyroMag ADC AHRS Barometer GPS LED2 Servo RCInput AccelCalibration

all:
	for dir in $(MODULES); do \
	cd $$dir; \
	($(MAKE) ); \
	cd ..; \
	done
	
clean:
	for dir in $(MODULES); do \
	cd $$dir; \
	($(MAKE) clean); \
	cd ..; \
	done

CXX ?= g++
NAVIO = ../../Navio
INCLUDES = -I ../..

all:
	$(CXX) $(INCLUDES) $(NAVIO)/LSM9DS1.cpp $(NAVIO)/MPU9250.cpp $(NAVIO)/Util.cpp AccelCalibration.cpp -o AccelCalibration

clean:
	rm -f AccelCalibration

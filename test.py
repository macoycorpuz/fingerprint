class flowsensor:
    global count, flowTotal, flowTotally

    count=0
    flowTotal=0
    flowTotally=0

    def init(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        global count, flowTotal, flowTotally, start_counter

        while self._running:
            #start_counter = 1
            flowTotal = (count * 2.25)
            count=0
            flowTotally=flowTotal+flowTotally

            '''if (flowTotally>=250):
                GPIO.output(VALVE1, GPIO.HIGH) #Close Irrigation Solenoid Valve
                GPIO.output(PUMPIRR, GPIO.HIGH) #Close Irrigation Pump
            '''
            sleep(0.1)
FlowSense = flowsensor()
FlowSenseThread = Thread(target=FlowSense.run)
FlowSenseThread.start()
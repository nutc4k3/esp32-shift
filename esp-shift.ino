#include <SPI.h>

#include "shift.pb.h"


#include "pb_common.h"
#include "pb.h"
#include "pb_decode.h"

#define LATCH 13
#define MAX_BYTES 128
#define NUM_REGISTERS 2
#define NUM_BITS (NUM_REGISTERS * 8)

uint8_t states[NUM_BITS];
uint8_t curPos = 0;
uint8_t bstate[NUM_REGISTERS];

SPIClass * vspi = NULL;
static const int spiClk = 10000000; // 10 MHz


// ProtoBuf Part
CmdMsg message = CmdMsg_init_default;
uint8_t buffer[MAX_BYTES];
uint16_t numBytes = 0;

// Code

void setup() {
  Serial.begin(115200);
  Serial.println("Initializing SPI");
  vspi = new SPIClass(VSPI);
  vspi->begin();

  // put your setup code here, to run once:
  pinMode(LATCH, OUTPUT);
  clear();
}

void clear() {
  for (int i = 0; i < NUM_BITS; i++) {
    states[i] = HIGH;
  }
}

void updatebstates() {
  for (int i = 0; i < NUM_REGISTERS; i++) {
    bstate[i] = 0;
  }
  for (int i = 0; i < NUM_BITS; i++) {
    int s = i / 8;
    int o = i % 8;
    bstate[s] |= states[i] * (1 << o);
  }
}

void updateByte(uint8_t num, uint8_t val) {
  for (int i = 0; i < 8; i++) {
    states[num*8+i] = val & (1 << i) ? LOW : HIGH;
  }
}

void update() {
  updatebstates();
  vspi->beginTransaction(SPISettings(spiClk, MSBFIRST, SPI_MODE0));
  // Since is shifted, use reverse order
  for (int i = NUM_REGISTERS-1; i >= 0; i--) {
    vspi->transfer(bstate[i]);
  }
  vspi->endTransaction();
}

void latch() {
  digitalWrite(LATCH, HIGH);
  delayMicroseconds(1);
  digitalWrite(LATCH, LOW);
  delayMicroseconds(1);
}

void CmdReset() {
  clear();
  Serial.println("( OK) All bits reset");
}

void CmdSetPin(uint8_t *data) {
  uint8_t pin = data[0];
  uint8_t val = data[1] ? LOW : HIGH;

  if (pin >= NUM_BITS) {
    Serial.println("( ERR) Pin number cannot be higher than NUM_BITS");
    return;
  }

  states[pin] = val;
  Serial.print("( OK) Pin ");
  Serial.print(pin);
  Serial.print(" state set to ");
  Serial.println(val);
}

void CmdSetByte(uint8_t *data) {
  uint8_t numByte = data[0];
  uint8_t val = data[1];

  if (numByte >= NUM_REGISTERS) {
    Serial.println("( ERR) Byte number cannot be higher than NUM_REGISTERS");
    return;
  }

  updateByte(numByte, val);
  Serial.print("( OK) Byte ");
  Serial.print(numByte);
  Serial.print(" state set to ");
  Serial.println(val, BIN);
}

void CmdHealthCheck() {
  Serial.println("( OK) Health Check OK");
}

void processPayload() {
  pb_istream_t stream = pb_istream_from_buffer(buffer, numBytes);
  if (!pb_decode(&stream, CmdMsg_fields, &message)) {
    Serial.println("( ERR) Error parsing message");
    return;
  }

  switch (message.cmd) {
    case CmdMsg_Command_HealthCheck:  return CmdHealthCheck();
    case CmdMsg_Command_SetPin:
      if (message.data.size == 2) {
        return CmdSetPin(message.data.bytes);
      }
      Serial.println("( ERR) Expected 2 bytes for SetPin");
      break;
    case CmdMsg_Command_SetByte:
      if (message.data.size == 2) {
        return CmdSetByte(message.data.bytes);
      }
      Serial.println("( ERR) Expected 2 bytes for SetByte");
      break;
    case CmdMsg_Command_Reset: return CmdReset();
  }
}

void receivePayload() {
  int n = Serial.available();
  if (n >= 2) {
    buffer[0] = Serial.read();
    buffer[1] = Serial.read();

    numBytes = *((uint16_t*) buffer);

    if (numBytes >= MAX_BYTES) {
      Serial.print("( ERR) Wanted to receive ");
      Serial.print(numBytes);
      Serial.print("bytes. But max is MAX_BYTES");
      return;
    }

    for (int i = 0; i < numBytes; i++) {
      buffer[i] = Serial.read();
    }

    processPayload();
  }
}

void loop() {
  receivePayload();
  update();
  latch();
  delay(1);
}

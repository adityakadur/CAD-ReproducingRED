# CAD-ReproducingRED
Team project for ECE6110- CAD. Trying to reproduce results in the Tuning RED paper using NS3

uint8_t opcode 

Extra Data
Opcode: 00000000

Primary request
Opcode: 00000001

Secondary request
Opcode: 00000010

Primary response
Opcode: 00000011

Secondary response
Opcode: 00000100 (maybe not required)

uint32_t Size is determined by probability distriution.

First byte of every packet contains the opcode. 
1. If the opcode is 0, ignore the data. 
2. If the opcode is 1 or 2, read the next 4 bytes to find out response size. Create BulkSendApp to send that many bytes back to the same port.
3. If the opcode is 3 or 4, increment the resp_bytes counter in new-send-application.



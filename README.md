# CAD-ReproducingRED
Team project for ECE6110- CAD. Trying to reproduce results in the Tuning RED paper using NS3

uint8_t opcode 

Extra Data
Opcode: 00000000

Request
Opcode: 00000001


uint32_t Size is determined by probability distriution.

First byte of every packet contains the opcode. 
1. If the opcode is 0, ignore the data. 
2. If the opcode is 1, read the next 4 bytes to find out response size. Create BulkSendApp to send that many bytes back to the same port.


TO-DO

1. Change new-send-application constructor to set m_maxBytes and resp_size



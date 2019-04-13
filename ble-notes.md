# ble-notes

FE:51:0A:AA:D1:AA
E5:0C:D5:30:71:2F


* temperature + humidity is service handle 23

raw
0x
020106030[20AA]0EFF
00[1501]00[2502][49][fe510aaad1aa] [00][temp][00][humidity][battery][mac]
-more stuff-

```bash
gatttool -b FE:51:0A:AA:D1:AA --char-read -a 0x0021
20 aa
gatttool -b FE:51:0A:AA:D1:AA --char-read -a 0x0023
001406002701  #temp+humitidty!
gatttool -b FE:51:0A:AA:D1:AA --char-read -a 0x0026
01  #sampling enabled
gatttool -b FE:51:0A:AA:D1:AA --char-read -a 0x0028
ff  #sample rate in 100ths of a second
gatttool -b FE:51:0A:AA:D1:AA --char-read -a 0x001f
49 #hex battery %


gatttool -b FE:51:0A:AA:D1:AA --char-read -u 0x2a19
49 #hex battery %
gatttool -b FE:51:0A:AA:D1:AA --char-read -u 0xaa21
001406002701  #temp+humitidty!
gatttool -b FE:51:0A:AA:D1:AA --char-read -u 0xaa22
01  #sampling enabled
gatttool -b FE:51:0A:AA:D1:AA --char-read -u 0x0023
ff  #sample rate in 100ths of a second

gatttool -b FE:51:0A:AA:D1:AA --char-read -u 0x0024
gatttool -b FE:51:0A:AA:D1:AA --char-read -u 0x0025
gatttool -b FE:51:0A:AA:D1:AA --char-read -u 0x0026
gatttool -b FE:51:0A:AA:D1:AA --char-read -u 0x0027
gatttool -b FE:51:0A:AA:D1:AA --char-read -u 0x0028

gatttool -b FE:51:0A:AA:D1:AA --char-read -u 0x2902
# firmawre-related? 4 handles (0x000d 0x0020 0x0024 0x0036) returned all with 0 value



```

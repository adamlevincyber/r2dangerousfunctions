# r2dangerousfunctions
This is a r2/radare2 script that will find and print dangerous functions and their respective memory locations inside of a binary. It will also print the xrefs to where they are being called.

OpenBTS.bin was an example binary that I used in the development of this r2pipe script due to it's questionable function calls.

Usage: `python3 r2dangerousfunctions.py`

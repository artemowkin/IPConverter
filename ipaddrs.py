"""Console IP address converter app

Examples
--------

$ python3 ipaddrs.py
Hello! I'm an IP addresses converter!
IP Address: 192.168.1.1
> digit
192.168.1.1
> binary
11000000101010000000000100000001
> exit

"""


class IPAddr:

    """Simple IP converter

    Properties
    ----------
    digit : str
        Return IP address in digit format

    binary : str
        Return IP address in binary format


    Examples
    --------

    >>> ipaddr = IPAddr('192.168.1.1')
    >>> ipaddr.digit
    '192.168.1.1'
    >>> ipaddr.binary
    '11000000101010000000000100000001'

    """

    def __init__(self, addr: str) -> None:
        if not isinstance(addr, str):
            raise ValueError("`addr` attribute must be a string")

        if not '.' in addr:
            raise ValueError("`addr` must be an IP address")

        self._addr = addr
        self._binary_addr = None

    @property
    def digit(self) -> str:
        """Return IP address in digit format: XXXX.XXXX.XXXX.XXXX"""
        return self._addr

    @property
    def binary(self) -> str:
        """Return IP address in 32 bit binary format"""
        if not self._binary_addr:
            # Split by dot: 192.168.1.1 wil be [192, 168, 1, 1]
            octets = list(map(int, self._addr.split('.')))
            # [192, 168, 1, 1] wil be
            # ['11000000', '10101000', '0000001', '0000001']
            binary_octets = [
                bin(octet)[2:].rjust(8, '0') for octet in octets
            ]
            self._binary_addr = ''.join(binary_octets)

        return self._binary_addr


if __name__ == '__main__':
    print("Hello! I'm an IP addresses converter!")
    ipaddr = IPAddr(input('IP Address: '))
    while True:
        command = input('> ')
        if command.lower() == 'binary':
            print(ipaddr.binary)
        elif command.lower() == 'digit':
            print(ipaddr.digit)
        elif command.lower() == 'exit':
            break
        else:
            print("Unexpected command. Try again.")

    print("Goodbye!")



def get_cp932_chars(include_cyrillic=False):
    # cp932 code
    # see https://uic.jp/charset/show/cp932/

    all_list = []

    # one byte characters
    for i in range(0xa1, 0xf0):
        all_list.append([i])

    # two bytes characters
    ranges_2bytes = [
        (0x8100, 0x8400),
        (0x849f, 0xa000),
        (0xe000, 0xeb00),
        (0xfa00, 0xfd00)
    ]
    if include_cyrillic:
        ranges.append((0x8440, 0x8492))
    
    for r in ranges_2bytes:
        for i in range(r[0], r[1]):
            upper,lower = divmod(i, 0x100)
            all_list.append([upper,lower])

    cp932_chars = set()

    for x in all_list:
        try:
            chr = bytes(x).decode('cp932')
            cp932_chars.add(chr)
        except:
            pass

    #print(len(char_list))    
    return cp932_chars

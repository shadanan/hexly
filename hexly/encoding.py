from dataclasses import dataclass


@dataclass
class Encoding:
    name: str
    code: dict[int, str]

    def __getitem__(self, key: int) -> str:
        return self.code[key]

    def __contains__(self, key: int) -> bool:
        return key in self.code


ASCII = Encoding(
    name="ASCII",
    code={i: chr(i) for i in range(32, 127)},
)

IBM437 = Encoding(
    name="IBM437",
    code={
        i + 0x1: v
        for i, v in enumerate(
            r"""☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼"""
            r""" !"#$%&'()*+,-./0123456789:;<=>?"""
            r"""@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_"""
            r"""`abcdefghijklmnopqrstuvwxyz{|}~⌂"""
            r"""ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜ¢£¥₧ƒ"""
            r"""áíóúñÑªº¿⌐¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐"""
            r"""└┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀"""
            r"""αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡÷≈°∙·√ⁿ²■"""
        )
    },
)

IBM850 = Encoding(
    name="IBM850",
    code={
        i + 0x1: v
        for i, v in enumerate(
            r"""☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼"""
            r""" !"#$%&'()*+,-./0123456789:;<=>?"""
            r"""@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_"""
            r"""`abcdefghijklmnopqrstuvwxyz{|}~⌂"""
            r"""ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜø£Ø×ƒ"""
            r"""áíóúñÑªº¿®¬½¼¡«»░▒▓│┤ÁÂÀ©╣║╗╝¢¥┐"""
            r"""└┴┬├─┼ãÃ╚╔╩╦╠═╬¤ðÐÊËÈıÍÎÏ┘┌█▄¦Ì▀"""
            r"""ÓßÔÒõÕµþÞÚÛÙýÝ¯´­±‗¾¶§÷¸°¨·¹³²■"""
        )
    },
)

WINDOWS_1252 = Encoding(
    name="Windows-1252",
    code={
        i + 0x20: v
        for i, v in enumerate(
            r""" !"#$%&'()*+,-./0123456789:;<=>?"""
            r"""@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_"""
            r"""`abcdefghijklmnopqrstuvwxyz{|}~"""
        )
    }
    | {0x80: r"€", 0x8E: r"Ž", 0x9E: r"ž", 0x9F: r"Ÿ"}
    | {i + 0x82: v for i, v in enumerate(r"‚ƒ„…†‡ˆ‰Š‹Œ")}
    | {i + 0x91: v for i, v in enumerate(r"‘’“”•–—˜™š›œ")}
    | {
        i + 0xA1: v
        for i, v in enumerate(
            r"""¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏ"""
            r"""ÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"""
        )
    },
)

HEXLY = Encoding(
    name="HEXLY",
    code=dict(
        enumerate(
            r"""ø☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼"""
            r"""␣!"#$%&'()*+,-./0123456789:;<=>?"""
            r"""@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_"""
            r"""`abcdefghijklmnopqrstuvwxyz{|}~⌂"""
            r"""ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜ¢£¥₧ƒ"""
            r"""áíóúñÑªº¿⌐¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐"""
            r"""└┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀"""
            r"""αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡÷≈°∙·√ⁿ²■⍽"""
        )
    ),
)

from linuxinfo.rpi import decode, RPiInfo

def test_decode():
    data = [
        (
            decode(0xa020a0),
            RPiInfo(type='CM3', processor='BCM2837', memory='1GB', revision=0, manufacturer='Sony UK', flag='new-style revision'),
        ),  # compute module 3
        (
            decode(0xa22042),
            RPiInfo(type='2B', processor='BCM2837', memory='1GB', revision=2, manufacturer='Embest', flag='new-style revision'),
        ),  # Pi2B
        (
            decode(0xc03111),
            RPiInfo(type='4B', processor='BCM2711', memory='4GB', revision=1, manufacturer='Sony UK', flag='new-style revision'),
        )  # Pi4B
    ]

    for (d, r) in data:
        assert d == r, f"Error on {d} == {r}"

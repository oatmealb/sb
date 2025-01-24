from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en") as sb:
    url = "https://www.nepremicnine.net/oglasi-oddaja/juzna-primorska/koper/koper/"
    sb.activate_cdp_mode(url)
    sb.sleep(2.5)
    t=sb.get_text('.property-section')
$('.property-section')
    .remove('script')
    .remove('style')
    .remove('.jd-ekskluziva')
    .toString()

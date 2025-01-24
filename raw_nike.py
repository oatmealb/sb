from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en", ad_block=True) as sb:
    url = "https://www.nike.com/"
    sb.activate_cdp_mode(url)
    sb.sleep(2.5)
    t=sb.find_element('body')
    # t=sb.find_element('.property-section')
    print(f'.prop: {t}')
    print(f'.prop.text: {t.text}')
    t=sb.remove_attributes('script')
    print(f'.prop WOO script: {t}')
    print(f'.prop WOO script.text: {t.text}')
    t=sb.remove_attributes('style')
    t=sb.remove_attributes('.jd-ekskluziva')


    # sb.cdp.gui_click_element('div[data-testid="user-tools-container"]')
    # sb.sleep(1.5)
    # search = "Nike Air Force 1"
    # sb.cdp.press_keys('input[type="search"]', search)
    # sb.sleep(4)
    # elements = sb.cdp.select_all('ul[data-testid*="products"] figure .details')
    # if elements:
    #     print('**** Found results for "%s": ****' % search)
    # for element in elements:
    #     print("* " + element.text)


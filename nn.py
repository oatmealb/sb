from seleniumbase import SB
import psycopg2,os
from psycopg2.extras import Json, execute_values
from datetime import datetime, timezone
db_config = {
    'dbname': os.getenv('DB_NAME', 're'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'postgres'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432')
}
try:
    conn = psycopg2.connect(**db_config)
except psycopg2.Error as e:
    print(f"Database connection failed: {e}")
    raise SystemExit(e)
def _sleep():
  return SB.sleep(random.uniform(1.9,3))
def insert2(data: dict, conn, now) -> None:
    with conn.cursor() as cur:
        nep_net_source_id=1
        cur.execute("""
            INSERT INTO scrapes_listings_html (
                source_id,
                html,
                scraped_at
            ) VALUES (%s, %s,%s)
        """, (nep_net_source_id, data, now))
    conn.commit()
def insert(data: dict, conn, now,url) -> None:
    with conn.cursor() as cur:
        nep_net_source_id=1
        district_id,city_id=1,2
        listing_type_id=1
        property_type_id=1
        cur.execute("""
            INSERT INTO scrapes_listings_html (
                source_id,
                html,
                scraped_at,
                scraped_url,
                district_id,
                city_id
            ) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)
        """, (nep_net_source_id, data, now,url,district_id,city_id, listing_type_id, property_type_id))
    conn.commit()

BASE_URL=os.getenv("BASE_URL")
ptype=os.getenv("PTYPE")
ltype=os.getenv("LTYPE")
division_path=os.getenv("DIVISION_URL_PATH")
url = f"{BASE_URL}/{ltype}/{division_path}/{ptype}/"

now=datetime.now(timezone.utc)
def get_and_insert_cur_page(sb):
    _sleep(sb)
    sb.remove_elements('style')
    sb.remove_elements('.midad')
    sb.remove_elements('.line')
    sb.remove_elements('.jd-ekskluziva')
    sb.remove_elements('.labels-left')
    e=sb.find_element('.property-section')
    insert(e.text,conn,now,sb.get_current_url())

    _sleep(sb)
    sb.cdp.scroll_down(amount=random.randint(50,400))
    _sleep(sb)
    sb.cdp.scroll_to_top()
    _sleep(sb)
with SB(uc=True, test=True, locale_code="en") as sb:
    sb.activate_cdp_mode(url)
    # sb.inspect_html()
    _sleep(sb)
    sb.cdp.scroll_down(amount=random.randint(50,400))

    get_and_insert_cur_page(sb)
    next_page_btn='.paging_next'
    while sb.cdp.is_element_visible(next_page_btn):
        print(f'next')
        sb.cdp.gui_click_element(next_page_btn)
        get_and_insert_cur_page(sb)

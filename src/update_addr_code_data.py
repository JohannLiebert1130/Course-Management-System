from src.common.ChineseIDValidator.addr_code_crawler import AddressCode

if __name__ == '__main__':
    url = 'http://www.mca.gov.cn/article/sj/xzqh//1980/'
    AddressCode.save_addr_code_to_json(base_url=url, old=False)
    AddressCode.save_addr_code_to_json(file_name='1995_addr_codes.json',old=True)

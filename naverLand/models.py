from typing import List
import requests
import webScrap
import dataProcessing

class GuScraper(webScrap.Work):

    cityNo : str
    
    def request(self):
        url = f'https://new.land.naver.com/api/regions/list?cortarNo={self.cityNo}'
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2NDE4MjMwNTEsImV4cCI6MTY0MTgzMzg1MX0.G2LIx6IATbC1JDuGaK10mllYmb061biA6viyofkZiso',
            'Connection': 'keep-alive',
            
            'Host': 'new.land.naver.com',

            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        return requests.get(url=url, headers=headers).json() 

class GuScrapers(webScrap.Works):

    works : List[GuScraper]

class GuScraperProcessor(dataProcessing.Modeling):

    def process(self, init_data=None):
        # init_data = {'seoul': '1100000000', 'gyung-gi': '4100000000'}
        return [GuScraper(cityNo=i) for i in init_data.values()]


class DongScraper(webScrap.Work):

    guNo : str

    def request(self): 
        url = f'https://new.land.naver.com/api/regions/list?cortarNo={self.guNo}'
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2NDE4MjMwNTEsImV4cCI6MTY0MTgzMzg1MX0.G2LIx6IATbC1JDuGaK10mllYmb061biA6viyofkZiso',
            'Connection': 'keep-alive',

            'Host': 'new.land.naver.com',

            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        return requests.get(url, headers=headers).json()


class DongScrapers(webScrap.Works):

    works : List[DongScraper]

class DongScraperProcessor(dataProcessing.Modeling):

    def process(self, init_data=None):
        gu_list = [guInfo.get('cortarNo') for guInfo in init_data.get('regionList')]
        return [DongScraper(guNo=i) for i in gu_list]

class ComplexScraper(webScrap.Work):

    dongNo: str

    def request(self): 
        url = f'https://new.land.naver.com/api/regions/complexes?cortarNo={self.dongNo}&realEstateType=APT&order='
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2NDE4MjMwNTEsImV4cCI6MTY0MTgzMzg1MX0.G2LIx6IATbC1JDuGaK10mllYmb061biA6viyofkZiso',
            'Connection': 'keep-alive',

            'Host': 'new.land.naver.com',

            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        return requests.get(url, headers=headers).json()

class ComplexScrapers(webScrap.Works):

    works: List[ComplexScraper]

class ComplexScraperProcessor(dataProcessing.Modeling):

    def process(self, init_data=None):
        dong_list = [dongInfo.get('cortarNo') for dongInfo in init_data.get('regionList')]
        return [ComplexScraper(dongNo=i) for i in dong_list]

class ArticleScraper(webScrap.Work):

    complexNo: str
    tradeType: str

    def request(self): 

        url = f'https://new.land.naver.com/api/articles/complex/{self.complexNo}?realEstateType=APT&tradeType={self.tradeType}&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page=1&complexNo={self.complexNo}&buildingNos=&areaNos=&type=list&order=rank'
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2NTQxODI5NDIsImV4cCI6MTY1NDE5Mzc0Mn0.qH5BpVq1KtIcdeNWa1c5rxe6OA3y1q6s7HfB6Zowkbo',
            'Connection': 'keep-alive',

            'Host': 'new.land.naver.com',
            'Referer': 'https://new.land.naver.com/complexes/137413?ms=37.5038337,127.0508535,16&a=APT&b=A1&e=RETAIL',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        return requests.get(url, headers=headers).json()

class ArticleScrapers(webScrap.Works):

    works: List[ArticleScraper]

class ArticleScraperProcessor(dataProcessing.Modeling):
    
    def process(self, init_data=None):
        complex_list = [complexInfo.get('complexNo') for complexInfo in init_data.get('complexList')]
        return [ArticleScraper(complexNo=i, tradeType='A1') for i in complex_list]


class ArticleInfoScraper(webScrap.Work):

    articleNo: str

    def request(self):
        url = f'https://new.land.naver.com/api/articles/{self.articleNo}?complexNo='
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2NDE4MjMwNTEsImV4cCI6MTY0MTgzMzg1MX0.G2LIx6IATbC1JDuGaK10mllYmb061biA6viyofkZiso',
            'Connection': 'keep-alive',
            'Cookie': 'NNB=XDAEADAWTN2V6; NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; ASID=d3cfd3330000017b6b53b7920000006c; nx_ssl=2; _ga=GA1.2.1641582590.1602312031; _ga_7VKFYR6RV1=GS1.1.1640622961.64.0.1640622961.60; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.ipaddress_city=1100000000; landHomeFlashUseYn=N; nhn.realestate.article.trade_type_cd=A1; realestate.beta.lastclick.cortar=1168010300; REALESTATE=Tue%20Jan%2011%202022%2000%3A10%3A43%20GMT%2B0900%20(KST); wcs_bt=4f99b5681ce60:1641827444',
            'Host': 'new.land.naver.com',
            'Referer': 'https://new.land.naver.com/complexes/8928?ms=37.496437,127.07371950000001,17&a=APT&b=A1:B1&e=RETAIL',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        return requests.get(url, headers=headers).json()

class ArticleInfoScrapers(webScrap.Works):

    works: List[ArticleInfoScraper]


class ArticleInfoScraperProcessor(dataProcessing.Modeling):
    
    def process(self, init_data=None):
        articleNo_list = [articleInfo.get('articleNo') for articleInfo in init_data.get('articleList')]
        return [ArticleInfoScraper(articleNo=i) for i in articleNo_list]


class ComplexPriceScraper(webScrap.Work):

    hscpNo: str
    ptpNo: str

    def request(self):

        url = f'https://new.land.naver.com/api/complexes/{self.hscpNo}/prices?complexNo={self.hscpNo}&year=5&tradeType=A1&areaNo={self.ptpNo}&type=chart'
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2NDI0MzM3MDAsImV4cCI6MTY0MjQ0NDUwMH0.0E_bLezMEZWh-H_YEXWAU3gwjpUiyc-NPS_9Dbx_BRw',
            'Connection': 'keep-alive',
            'Host': 'new.land.naver.com',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }
        return requests.get(url, headers=headers).json()

class ComplexPriceScrapers(webScrap.Works):

    works: List[ComplexPriceScraper]


class ComplexPriceScraperProcessor(dataProcessing.Modeling):
    
    def process(self, init_data=None):
        return list(set([ComplexPriceScraper(**init_data.get('articleDetail'))]))

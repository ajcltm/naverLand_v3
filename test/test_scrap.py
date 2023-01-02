import unittest
import shutil
import pickle
import dataProcessing

from naverLand import scraperFactories, utils, config

def make_file(dir, data):
    with open(dir, mode='wb') as fw:
        pickle.dump(data, fw)

class Print_data(dataProcessing.Modeling):

    def process(self, init_data=None):
        print(init_data)

@unittest.skip("")
class Test_1_gu_scrap(unittest.TestCase):

    def setUp(self) -> None:
        self.dir = config.dir_gu
        utils.make_dir(self.dir)

    def tearDown(self) -> None:
        Print_data(folder_path=self.dir).process_all()
        shutil.rmtree(self.dir)

    def test_1_scrap(self):
        gu_scrapers = scraperFactories.get_gu_scrapers()
        gu_scrapers.do_work(folder_path=self.dir, type='pickle')
    
@unittest.skip("")
class Test_2_dong_scrap(unittest.TestCase):

    def setUp(self) -> None:
        self.pre_dir = config.dir_gu
        self.dir = config.dir_dong
        utils.make_dir(self.dir)
        
        utils.make_dir(self.pre_dir)
        sample_data ={
                'regionList': 
                [
                    {'cortarNo': '1168000000', 'centerLat': 37.517408, 'centerLon': 127.047313, 'cortarName': '강남구', 'cortarType': 'dvsn'},
                    {'cortarNo': '1174000000', 'centerLat': 37.530126, 'centerLon': 127.123771, 'cortarName': '강동구', 'cortarType': 'dvsn'}
                ]
            } 
        make_file(self.pre_dir.joinpath('.pickle'), sample_data)

    def tearDown(self) -> None:
        Print_data(folder_path=self.dir).process_all()
        shutil.rmtree(self.dir)
        shutil.rmtree(self.pre_dir)

    def test_1_scrap(self):
        dong_scrapers = scraperFactories.get_dong_scrapers()
        dong_scrapers.do_work(folder_path=self.dir, type='pickle')

@unittest.skip("")
class Test_3_complex_scrap(unittest.TestCase):

    def setUp(self) -> None:
        self.pre_dir = config.dir_dong
        self.dir = config.dir_complex
        utils.make_dir(self.dir)
        
        utils.make_dir(self.pre_dir)
        sample_data = [
            {'regionList': [
                {'cortarNo': '1168011400', 'centerLat': 37.487485, 'centerLon': 127.081638, 'cortarName': '일원동', 'cortarType': 'sec'}, 
                {'cortarNo': '1168011200', 'centerLat': 37.4766, 'centerLon': 127.101, 'cortarName': '자곡동', 'cortarType': 'sec'}, 
                {'cortarNo': '1168010400', 'centerLat': 37.525492, 'centerLon': 127.05235, 'cortarName': '청담동', 'cortarType': 'sec'}
                ]
            } 
        ]
        make_file(self.pre_dir.joinpath('gu_some1.pickle'), sample_data[0])

    def tearDown(self) -> None:
        Print_data(folder_path=self.dir).process_all()
        shutil.rmtree(self.dir)
        shutil.rmtree(self.pre_dir)

    def test_1_scrap(self):
        complex_scrapers = scraperFactories.get_complex_scrapers()
        complex_scrapers.do_work(folder_path=self.dir, type='pickle')

@unittest.skip("")
class Test_4_article_scrap(unittest.TestCase):

    def setUp(self) -> None:
        self.pre_dir = config.dir_complex
        self.dir = config.dir_article
        utils.make_dir(self.dir)
        
        utils.make_dir(self.pre_dir)
        sample_data = {'complexList': [
    {'complexNo': '151006', 'complexName': 'J&M하우스(도시형)', 'cortarNo': '1168010400', 'realEstateTypeCode': 'APT', 'realEstateTypeName': '아파트', 'detailAddress': '26-35', 'latitude': 37.51941, 'longitude': 127.044033, 'totalHouseholdCount': 12, 'totalBuildingCount': 1, 'highFloor': 4, 'lowFloor': 4, 'useApproveYmd': '20120725', 'dealCount': 0, 'leaseCount': 0, 'rentCount': 0, 'shortTermRentCount': 0, 'cortarAddress': '서울시 강남구 청담동'},
    {'complexNo': '16502', 'complexName': 'LG', 'cortarNo': '1168010400', 'realEstateTypeCode': 'APT', 'realEstateTypeName': '아파트', 'detailAddress': '104-2', 'latitude': 37.528287, 'longitude': 127.048213, 'totalHouseholdCount': 11, 'totalBuildingCount': 1, 'highFloor': 6, 'lowFloor': 6, 'useApproveYmd': '19980504', 'dealCount': 0, 'leaseCount': 0, 'rentCount': 0, 'shortTermRentCount': 0, 'cortarAddress': '서울시 강남구 청담동'}, 
    {'complexNo': '135644', 'complexName': 'PH129', 'cortarNo': '1168010400', 'realEstateTypeCode': 'APT', 'realEstateTypeName': '아파트', 'detailAddress': '129', 'latitude': 37.526054, 'longitude': 127.054312, 'totalHouseholdCount': 29, 'totalBuildingCount': 1, 'highFloor': 20, 'lowFloor': 18, 'useApproveYmd': '20200812', 'dealCount': 11, 'leaseCount': 1, 'rentCount': 4, 'shortTermRentCount': 0, 'cortarAddress': '서울시 강남구 청담동'}, 
    {'complexNo': '123601', 'complexName': 'T.S.', 'cortarNo': '1168010400', 'realEstateTypeCode': 'APT', 'realEstateTypeName': '아파트', 'detailAddress': '115-5', 'latitude': 37.527971, 'longitude': 127.047144, 'totalHouseholdCount': 8, 'totalBuildingCount': 1, 'highFloor': 4, 'lowFloor': 4, 'useApproveYmd': '19980703', 'dealCount': 0, 'leaseCount': 0, 'rentCount': 0, 'shortTermRentCount': 0, 'cortarAddress': '서울시 강남구 청담동'}, 
    {'complexNo': '104069', 'complexName': '강변상지리츠빌', 'cortarNo': '1168010400', 'realEstateTypeCode': 'APT', 'realEstateTypeName': '아파트', 'detailAddress': '106-17', 'latitude': 37.528007, 'longitude': 127.050603, 'totalHouseholdCount': 12, 'totalBuildingCount': 1, 'highFloor': 13, 'lowFloor': 13, 'useApproveYmd': '20010630', 'dealCount': 0, 'leaseCount': 0, 'rentCount': 4, 'shortTermRentCount': 0, 'cortarAddress': '서울시 강남구 청담동'}, 
    {'complexNo': '1000', 'complexName': '건영', 'cortarNo': '1168010400', 'realEstateTypeCode': 'APT', 'realEstateTypeName': '아파트', 'detailAddress': '108', 'latitude': 37.527524, 'longitude': 127.052159, 'totalHouseholdCount': 240, 'totalBuildingCount': 2, 'highFloor': 19, 'lowFloor': 14, 'useApproveYmd': '19940905', 'dealCount': 10, 'leaseCount': 1, 'rentCount': 5, 'shortTermRentCount': 6, 'cortarAddress': '서울시 강남구 청담동'}, 
    {'complexNo': '101483', 'complexName': '골든아트빌(주상복합)', 'cortarNo': '1168010400', 'realEstateTypeCode': 'APT', 'realEstateTypeName': '아파트', 'detailAddress': '28-13', 'latitude': 37.519941, 'longitude': 127.047006, 'totalHouseholdCount': 19, 'totalBuildingCount': 1, 'highFloor': 8, 'lowFloor': 8, 'useApproveYmd': '20000601', 'dealCount': 2, 'leaseCount': 2, 'rentCount': 0, 'shortTermRentCount': 0, 'cortarAddress': '서울시 강남구 청담동'}, 
    {'complexNo': '3063', 'complexName': '구산', 'cortarNo': '1168010400', 'realEstateTypeCode': 'APT', 'realEstateTypeName': '아파트', 'detailAddress': '128-1', 'latitude': 37.52668, 'longitude': 127.05395, 'totalHouseholdCount': 37, 'totalBuildingCount': 1, 'highFloor': 9, 'lowFloor': 5, 'useApproveYmd': '19931126', 'dealCount': 0, 'leaseCount': 7, 'rentCount': 8, 'shortTermRentCount': 0, 'cortarAddress': '서울시 강남구 청담동'}
]
}
        make_file(self.pre_dir.joinpath('dong_some.pickle'), sample_data)

    def tearDown(self) -> None:
        Print_data(folder_path=self.dir).process_all()
        shutil.rmtree(self.dir)
        shutil.rmtree(self.pre_dir)

    def test_1_scrap(self):
        article_scrapers= scraperFactories.get_article_scrapers()
        article_scrapers.do_work(folder_path=self.dir, type='pickle')

@unittest.skip("")
class Test_5_article_scrap(unittest.TestCase):

    def setUp(self) -> None:
        self.pre_dir = config.dir_article
        self.dir = config.dir_articleInfo
        utils.make_dir(self.dir)
        
        utils.make_dir(self.pre_dir)
        sample_data = {
            'isMoreData': True, 
            'articleList': [
                {
                    'articleNo': '2246711070', 
                    'articleName': 'PH129', 
                    'articleStatus': 'R0', 
                    'realEstateTypeCode': 'APT', 
                    'realEstateTypeName': '아파트',
                    'articleRealEstateTypeCode': 'A01', 
                    'articleRealEstateTypeName': '아파트', 
                    'tradeTypeCode': 'A1', 
                    'tradeTypeName': '매매', 
                    'verificationTypeCode': 'TEL', 
                    'floorInfo': '16/20', 
                    'priceChangeState': 'SAME', 
                    'isPriceModification': False, 
                    'dealOrWarrantPrc': '145억', 
                    'areaName': '332', 
                    'area1': 332, 
                    'area2': 273, 
                    'direction': '남향', 
                    'articleConfirmYmd': '20221227', 
                    'representativeImgUrl': '/20221227_279/land_naver_1672107016009hjn8i_JPEG/2021090414384332317_28017_ws.jpg', 
                    'representativeImgTypeCode': '10', 
                    'representativeImgThumb': 'f130_98', 
                    'siteImageCount': 0, 
                    'articleFeatureDesc': '현존 고급빌라 넘버원', 
                    'tagList': ['4년이내', '대형평수', '방네개이상', '화장실네개이상'], 
                    'buildingName': '1동', 
                    'sameAddrCnt': 4, 
                    'sameAddrDirectCnt': 0, 
                    'sameAddrMaxPrc': '145억', 
                    'sameAddrMinPrc': '145억', 
                    'cpid': 'hkdotcom', 
                    'cpName': '한경부동산', 
                    'cpPcArticleUrl': 'https://realestate.hankyung.com/naver-listing?UID=2246711070', 
                    'cpPcArticleBridgeUrl': '', 
                    'cpPcArticleLinkUseAtArticleTitleYn': False, 
                    'cpPcArticleLinkUseAtCpNameYn': True, 
                    'cpMobileArticleUrl': '', 
                    'cpMobileArticleLinkUseAtArticleTitleYn': False, 
                    'cpMobileArticleLinkUseAtCpNameYn': False, 
                    'latitude': '37.525889', 
                    'longitude': '127.05415', 
                    'isLocationShow': False, 
                    'realtorName': '청담윌부동산중개법인(주)', 
                    'realtorId': 'm5158033', 
                    'tradeCheckedByOwner': False, 
                    'isDirectTrade': False, 
                    'isInterest': False, 
                    'isComplex': True, 
                    'detailAddress': '', 
                    'detailAddressYn': 'N'
                }
            ]
            }
        make_file(self.pre_dir.joinpath('complex_some.pickle'), sample_data)

    def tearDown(self) -> None:
        Print_data(folder_path=self.dir).process_all()
        shutil.rmtree(self.dir)
        shutil.rmtree(self.pre_dir)

    def test_1_scrap(self):
        articleInfo_scrapers= scraperFactories.get_articleInfo_scrapers()
        articleInfo_scrapers.do_work(folder_path=self.dir, type='pickle')

class Test_6_article_scrap(unittest.TestCase):

    def setUp(self) -> None:
        self.pre_dir = config.dir_articleInfo
        self.dir = config.dir_complexPrice
        utils.make_dir(self.dir)
        sample_data = {
            'articleDetail': {'articleNo': '2246711070', 'articleName': 'PH129 1동', 'articleSubName': '', 'cpId': 'hkdotcom', 'cortarNo': '1168010400', 'hscpNo': '135644', 'ptpNo': '1', 'ptpName': '332', 'tradeBuildingTypeCode': 'APT'}
            }
        utils.make_dir(self.pre_dir)
        make_file(self.pre_dir.joinpath('article_some.pickle'), sample_data)

    def tearDown(self) -> None:
        Print_data(folder_path=self.dir).process_all()
        shutil.rmtree(self.dir)
        shutil.rmtree(self.pre_dir)

    def test_1_scrap(self):
        complexPrice_scrapers= scraperFactories.get_complexPrice_scrapers()
        complexPrice_scrapers.do_work(folder_path=self.dir, type='pickle')

if __name__ == '__main__':
    unittest.main()
    
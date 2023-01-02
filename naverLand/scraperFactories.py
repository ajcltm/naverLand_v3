import dataProcessing

from naverLand import models, config

def get_gu_scrapers():
    cities = {'seoul': '1100000000', 'gyung-gi': '4100000000'}
    scraper_list = models.GuScraperProcessor().process_all(cities)
    return models.GuScrapers(works = scraper_list)

def get_dong_scrapers():
    scraper_list = models.DongScraperProcessor(folder_path=config.dir_gu, apply=True, dim_down=True).process_all()
    return models.DongScrapers(works = scraper_list)

def get_complex_scrapers():
    scraper_list = models.ComplexScraperProcessor(folder_path=config.dir_dong, apply=True, dim_down=True).process_all()
    return models.ComplexScrapers(works = scraper_list)

def get_article_scrapers():
    scraper_list = models.ArticleScraperProcessor(folder_path=config.dir_complex, apply=True, dim_down=True).process_all()
    return models.ArticleScrapers(works = scraper_list)

def get_articleInfo_scrapers():
    scraper_list = models.ArticleInfoScraperProcessor(folder_path=config.dir_article, apply=True, dim_down=True).process_all()
    return models.ArticleInfoScrapers(works = scraper_list)

def get_complexPrice_scrapers():
    scraper_list = models.ComplexPriceScraperProcessor(folder_path=config.dir_articleInfo, apply=True, dim_down=True).process_all()
    return models.ComplexPriceScrapers(works = scraper_list)
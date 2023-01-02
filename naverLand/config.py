from pathlib import Path

current_project = '221230'
dir_main = Path('F:').joinpath('data', 'naverLand')
dir_current_project = dir_main.joinpath(current_project)
dir_gu = dir_current_project.joinpath('0. gu')
dir_dong = dir_current_project.joinpath('1. dong')
dir_complex = dir_current_project.joinpath('3. complex')
dir_article = dir_current_project.joinpath('4. article')
dir_articleInfo = dir_current_project.joinpath('5. articleInfo')
dir_complexPrice = dir_current_project.joinpath('6. complexPrice')
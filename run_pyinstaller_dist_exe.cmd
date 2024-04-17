.venv\Scripts\activate.bat ^
    && pyinstaller --clean ^
            --onedir ^
            --contents-directory . ^
            --paths src/antlr_gen ^
            --add-data "conf/def_macros.txt:conf" ^
            --noconfirm ^
            src/main.py ^
    && cd dist/main ^
    && main.exe C:\Lab_Data\pyinstaller_demo\input\myfile.c
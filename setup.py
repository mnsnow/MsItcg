import cx_Freeze

executables = [cx_Freeze.Executable("itcg.py")]

cx_Freeze.setup(
    name = 'MS_ITCG',
    options = {"build_exe":{"packages":["pygame"],"include_files":["static","action.py","button.py","card_database_filter.py","card_database.py","card.py","display.py","game_functions.py","grid.py","player2.py","README.md","requirements.txt","rules.txt","settings.py","user_deck_list_string.txt","user.py"]}},

    description = "Maplestory Itcg Alpha -- 1.0",
    executables = executables


)




#

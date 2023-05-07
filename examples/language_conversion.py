import oopmultilang


"""
Define a class<Lang> instance object dedicated to ui function description in the global.

In the argument passed in param<include>:

1. ``"./lang/en_us.lang as en_us"``: Expression using the full-form kind.
2. ``"./lang/zh_cn.lang"``: Expression using the short-form kind. The file name "zh_cn" will be used as the name of the 
language associated with this language dictionary.
"""
ui_alt_lang = oopmultilang.LangSwitcher(
    include=(
    "./lang/en_us.lang as en_us",
    "./lang/zh_cn.lang"
),
    load_mode=oopmultilang.LoadMode.REALTIME
)


def main():
    """
    Use the object-oriented paradigm conversion method to obtain the "en_us" native word whose universal word is
    "UI.login".
    """
    ui_login_alt_english = ui_alt_lang.universal.UI.login.en_us  # user login

    """
    First set the default target language to "en_us", then use the string conversion method to obtain the "en_us" native 
    word whose universal word is "UI.login".
    """
    ui_alt_lang.default_lang(target_lang="en_us")
    ui_login_alt_english = ui_alt_lang.universal.UI.login  # user login

    """
    Use the string conversion method to obtain the "zh_cn" native word whose "en_us" native word is "user login".
    """
    ui_login_alt_chinese = ui_alt_lang.str("user login", "en_us", "zh_cn")  # 用户登录

    """
    First set the default source language to "en_us", and the default target language to "the universal word".
    And then use the string conversion method obtain the universal word whose "en_us" native word is "user login".
    Finally, use the built-in eval function to execute the statement using the object-oriented paradigm conversion 
    method to obtain the "zh_cn" native word whose universal word is "UI.login".
    """
    ui_alt_lang.default_lang(source_lang="en_us", target_lang=None)
    ui_login_alt_chinese = eval("lang_obj.universal.{}.zh_cn".format(ui_alt_lang.str("user login")))  # UI.login -> 用户登录

    """
    Try to use the string conversion method to obtain the "en_us" native word whose universal word is non-existent 
    "UI.title", catch the exception and print out the word being converted that caused the error to occur.
    """
    try:
        ui_title_alt_english = ui_alt_lang.str("UI.title", None, "en_us")
    except oopmultilang.LangDictSearchError as error:
        if error.type == oopmultilang.LangDictSearchError.UNIVERSAL_WORD_EXIST_ERROR:
            print(f"{error.word} is not a universal word.")

    """
    Try to use the string conversion method to obtain the "en_us" native word whose "zh_cn" native word is non-existent 
    "界面标题", catch the exception and print out message that the word does not exist in the corresponding language 
    dictionary.
    """
    try:
        ui_title_alt_english = ui_alt_lang.str("界面标题", "zh_cn", "en_us")
    except oopmultilang.LangDictSearchError as error:
        print(f"{error.word} is not in {error.position} dictionary.")


if __name__ == "__main__":
    main()

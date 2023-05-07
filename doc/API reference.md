## LoadMode

An enumeration representing two loading modes.

| **Enum** | Description                                                  |
| -------- | ------------------------------------------------------------ |
| REALTIME | Static data files are read for each conversion.              |
| ONETIME  | Static data files are only read once when the object is instantiated for the first time. |



## LangSwitcher

A working class for language conversion.

### Constructor

```python
LangSwitcher(include, load_mode)
```

| Parameter | Type     | Default           | Description                                                  |
| --------- | -------- | ----------------- | ------------------------------------------------------------ |
| include   | tuple    | ()                | A tuple of expressions which are importing language dictionaries.<br>There are two forms of this expression, for example: <br>1. full: `"./en_us.lang as en_us"`<br>2. short: `"./en_us.lang"`<br>Note that when using the short form, the name of the associated language will be the name of the file. |
| load_mode | LoadMode | LoadMode.REALTIME | The option for loading mode.                                 |

> The detail of the data format supported by imported language dictionaries is in [doc](https://github.com/leoweyr/Python-OOPMultilang/blob/main/doc/data%20standard.md#supportdataformat).

### Default setting

```
LangSwitcher().default_lang(source_lang, target_lang)
```

| Parameter   | Type   | Default | Description                                                 |
| ----------- | ------ | ------- | ----------------------------------------------------------- |
| source_lang | string | ""      | The option for the default source language to convert from. |
| target_lang | string | ""      | The option for the default target language to convert to.   |

> `None` represents it is the universal word, not a specific language.

### Conversion

> The description of the universal word and the native word is in [doc](https://github.com/leoweyr/Python-OOPMultilang/blob/main/doc/data%20standard.md).

#### LangSwitcher().str(word, source_lang, target_lang)

String conversion method.

| Parameter   | Type   | Default | Description                          |
| ----------- | ------ | ------- | ------------------------------------ |
| word        | string |         | A word to be converted.              |
| source_lang | string | ""      | The source language to convert from. |
| target_lang | string | ""      | The target language to convert to.   |

> `""` represents it is the default language set in `LangSwitcher().default_lang()`.

#### LangSwitcher().universal

Object-oriented paradigm conversion method, only supports converting a universal word into other native word.

There are two syntax statements: 

```python
# Pure object-oriented paradigm suffix.
LangSwitcher().universal.*

# End of suffix with the target language to convert to.
LangSwitcher().universal.*.target_lang

# `*` represents a specific universal word.
```

> For the difference between two methods in practical application, please see [example](https://github.com/leoweyr/Python-OOPMultilang/tree/main/examples).



## LangDictSearchError

An exception class thrown when language conversion error occurs.

### Attributes

<table>
    <tr>
    	<td><code>LangDictSearchError().type</code></td>
        <td>Return the type of error reason.</br>● LangDictSearchError.UNIVERSAL_WORD_EXIST_ERROR</br>● LangDictSearchError.SOURCE_LANG_DICT_MATCH_ERROR</br>●  LangDictSearchError.TARGET_LANG_DICT_MATCH_ERROR</td>
    </tr>
    <tr>
    	<td><code>LangDictSearchError().word</code></td>
        <td>Return the word being converted that caused the error to occur.</td>
    </tr>
    <tr>
    	<td><code>LangDictSearchError().position</code></td>
        <td>Return the name of language associated with language dictionary which caused the error to occur.</td>
    </tr>
</table>

# UTF-8中の日本語文字(っぽいもの)を判定するもの

## これはなに?

UTF-8中の日本語の判別方法ですが、ひらがなやカタカナはいいとして漢字については中国語と日本語を区別するのがむずかしそうです。
そこで、今回は簡易的にcp932コードに含まれているものを日本語と識別することにしました。
試行錯誤の結果、以下のようにしました。

- 0x8f以下は対象外(英語圏の文字)
- ギリシャ文字は日本語テキストでも数学の記号として使われていることが多いので対象
- キリル文字は対象外

正確な方法ではありませんが、おおよその傾向をつかむにはこの程度でいいかなと思います。

## 使い方例

huggingface transformersのxlm-roberta-baseモデルの語彙から日本語っぽいものを抽出してみます。

```python
from transformers import AutoTokenizer
from japanese_char_checker import JapaneseCharChecker

checker = JapaneseCharChecker(remove_chars=['▁', '#'])

model = 'xlm-roberta-base'

tokenizer = AutoTokenizer.from_pretrained(model)
vocab = tokenizer.get_vocab().keys()
vocab_ja = [k for k in vocab if checker.fullmatch(k)]
print(len(vocab_ja))
```

なぜかはよく分かっていないけれど、色々とフルパスで指定しないと動かない。

# 単語-読みファイルの作成
単語-読みファイルを手で作る。

- `vim word.yomi`

# 音素ファイルの作成
単語-読みファイルを元に、音素ファイルを自動生成する。

- `iconv -f utf8 -t eucjp word.yomi | ~/julius/julius-4.4.2.1/gramtools/yomi2voca/yomi2voca.pl | iconv -f eucjp -t utf8 > word.phone`

# 文法ファイルの作成
音素ファイルを元に、文法ファイルを手で作る。

- `cp word.phone word.voca`
- `vim word.voca`: phoneをひな形に作ると楽。
- `vim word.grammar`: 頑張って作る。
- `~/julius/julius-4.4.2.1/gramtools/mkdfa/mkdfa.pl ~/julius/dict/word`:/julius/dict/はword.yomi等があるディレクトリまでのパスに変更。

# 動作
`~/julius/julius-4.4.2.1/julius/julius -C ~/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -nostrip -gram ~/julius/dict/word -input mic`

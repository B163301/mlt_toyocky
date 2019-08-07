#!/bin/sh

~/julius/julius-4.4.2.1/julius/julius -C ~/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -gram ~/julius/dict/word -module > /dev/null &
echo $! #プロセスIDを出力
sleep 2 #2秒間スリープ

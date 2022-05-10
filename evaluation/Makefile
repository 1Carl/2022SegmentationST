LANG=mon
ARCH=transformer

resultc:
	python evaluate.py --guess ../${ARCH}/${LANG}.tsv --gold ../data/${LANG}.word.dev.tsv --out ../${ARCH}/resultjson/${LANG}.json --category || python evaluate.py --guess ../${ARCH}/${LANG}.tsv --gold ../data/${LANG}.word.dev.tsv --out ../${ARCH}/resultjson/${LANG}.json
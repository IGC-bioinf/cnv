#!/bin/bash
echo "Usage: bash run_cnvkit.sh /path/to/bam/dir /path/to/bed /path/to/ref"
mkdir cnvkit_pipeline_TSOne_Exp
cd cnvkit_pipeline_TSOne_Exp
bam_num=$(ls $1/*.bam | grep -v trio | wc -l)
count=0
for i in $(ls $1/*.bam | grep -v trio)
do
	count=$((count+1))
	echo "File" $count '/' $bam_num "in progress..."
	filename=$(basename -- "$i")
	filename="${filename%.*}"
	cnvkit.py batch $i --n -m hybrid --segment-method hmm-germline  --targets $2 --fasta $3 --output-reference $filename.cnn -p 8 --output-dir cnvkit_$filename --scatter --diagram
	mkdir -p cnvkit_$filename
	cd cnvkit_$filename
	cnvkit.py segmetrics -s $filename.cn{s,r} --ci > $filename.segmetrics.cns
	cnvkit.py call $filename.segmetrics.cns --filter ci -o $filename.calls.cns
	cnvkit.py gainloss $filename.cnr -s $filename.calls.cns > $filename.final_stat.txt
	cnvkit.py gainloss $filename.cnr -s $filename.calls.cns -m 3 | tail -n+2 | cut -f1 | sort > $filename.segment-gainloss.txt
	cnvkit.py gainloss $filename.cnr -m 3 | tail -n+2 | cut -f1 | sort >  $filename.ratio-gainloss.txt
	comm -12 $filename.segment-gainloss.txt $filename.ratio-gainloss.txt > $filename.trusted-gainloss.txt
	cnvkit.py scatter -s $filename.cn{s,r}
	cd ../
	rm $filename.cnn
done

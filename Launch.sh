Ref=/storage/analysis/Databases/Ref/GRCh37_only_chr.fna
Path=$(pwd)

# Oksana
#Rscript /storage/analysis/progs/ClinCNV/clinCNV.R --normal $Path/ClinCNV/ex_oks_84.cov --bed $Path/gc_genes_annotated.150bp_chunks.exome_oksana.bed --out $Path/ClinCNV/ClinResult_ON_84 --numberOfThreads 19 --minimumNumOfElemsInCluster 25
#Rscript /storage/analysis/progs/ClinCNV/clinCNV.R --out $Path/ClinCNV/ClinResult_OFF_84 --normalOfftarget $Path/ClinCNV/ex_oks_84_off.cov --bedOfftarget $Path/gcAnnotated.offtarget_chunks.exome_oksana.bed --numberOfThreads 18 --minimumNumOfElemsInCluster 18
#
#Rscript /storage/analysis/progs/ClinCNV/clinCNV.R --normal $Path/ClinCNV/ex_oks_84.cov --bed $Path/gc_genes_annotated.150bp_chunks.exome_oksana.bed --out $Path/ClinCNV/ClinResult_BOTH_84 --normalOfftarget $Path/ClinCNV/ex_oks_84_off.cov --bedOfftarget $Path/gcAnnotated.offtarget_chunks.exome_oksana.bed --numberOfThreads 18 --minimumNumOfElemsInCluster 20 



# Larissa
#Rscript /storage/analysis/progs/ClinCNV/clinCNV.R --normal $Path/ClinCNV/ex_lar_32.cov --bed $Path/gc_genes_annotated.150bp_chunks.exome_larissa.bed --out $Path/ClinCNV/ClinResult_BOTH_32 --normalOfftarget $Path/ClinCNV/ex_lar_32_off.cov --bedOfftarget $Path/gcAnnotated.offtarget_chunks.exome_oksana.bed --numberOfThreads 18 --minimumNumOfElemsInCluster 15 
#Rscript /storage/analysis/progs/ClinCNV/clinCNV.R --normal $Path/ClinCNV/ex_lar_32.cov --bed $Path/gc_genes_annotated.150bp_chunks.exome_larissa_in_cov.bed --out $Path/ClinCNV/ClinResult_ON_32 --numberOfThreads 18 --minimumNumOfElemsInCluster 15


#file="ex_Exp_96"
#BedName="TSOneExpanded"
#num=96

# Exp
#Rscript /storage/analysis/progs/ClinCNV/clinCNV.R --normal $Path/ClinCNV/${file}.cov --bed $Path/gc_genes_annotated.150bp_chunks.$BedName.bed --out $Path/ClinCNV/ClinResult_BOTH_$num --normalOfftarget $Path/ClinCNV/${file}_off.cov --bedOfftarget $Path/gcAnnotated.offtarget_chunks.$BedName.bed --numberOfThreads 18 --minimumNumOfElemsInCluster 18 
#Rscript /storage/analysis/progs/ClinCNV/clinCNV.R --normal $Path/ClinCNV/${file}.adj.cov --bed $Path/gc_genes_annotated.150bp_chunks.$BedName.Sadj.bed --out $Path/ClinCNV/ClinResult_BOTH_$num --normalOfftarget $Path/ClinCNV/${file}_off.cov --bedOfftarget $Path/gcAnnotated.offtarget_chunks.$BedName.bed --numberOfThreads 18 --minimumNumOfElemsInCluster 18 
#Rscript /storage/analysis/progs/ClinCNV/clinCNV.R --normal $Path/ClinCNV/${file}.adj.cov --bed $Path/gc_genes_annotated.150bp_chunks.${BedName}.Sadj.bed --out $Path/ClinCNV/ClinResult_ON_$num --numberOfThreads 19 --minimumNumOfElemsInCluster 18
#Rscript /storage/analysis/progs/ClinCNV/clinCNV.R --out $Path/ClinCNV/ClinResult_OFF_$num --normalOfftarget $Path/ClinCNV/${file}_off.cov --bedOfftarget $Path/gcAnnotated.offtarget_chunks.$BedName.bed --numberOfThreads 18 --minimumNumOfElemsInCluster 18

file="ex_Full_167"
BedName="exome_oksana"
num=167

# Full exome
#Rscript /storage/analysis/progs/ClinCNV/clinCNV.R --normal $Path/ClinCNV/${file}.cov --bed $Path/gc_genes_annotated.150bp_chunks.$BedName.bed --out $Path/ClinCNV/ClinResult_BOTH_$num --normalOfftarget $Path/ClinCNV/${file}_off.cov --bedOfftarget $Path/gcAnnotated.offtarget_chunks.$BedName.bed --numberOfThreads 19 --minimumNumOfElemsInCluster 30 
Rscript /storage/analysis/progs/ClinCNV/clinCNV.R --normal $Path/ClinCNV/${file}.cov --bed $Path/gc_genes_annotated.150bp_chunks.$BedName.bed --out $Path/ClinCNV/ClinResult_BOTH_$num --normalOfftarget $Path/ClinCNV/${file}_off.cov --bedOfftarget $Path/gcAnnotated.offtarget_chunks.$BedName.bed --numberOfThreads 19 --minimumNumOfElemsInCluster 30 
Rscript /storage/analysis/progs/ClinCNV/clinCNV.R --normal $Path/ClinCNV/${file}.cov --bed $Path/gc_genes_annotated.150bp_chunks.${BedName}.bed --out $Path/ClinCNV/ClinResult_ON_$num --numberOfThreads 19 --minimumNumOfElemsInCluster 30
Rscript /storage/analysis/progs/ClinCNV/clinCNV.R --out $Path/ClinCNV/ClinResult_OFF_$num --normalOfftarget $Path/ClinCNV/${file}_off.cov --bedOfftarget $Path/gcAnnotated.offtarget_chunks.$BedName.bed --numberOfThreads 19 --minimumNumOfElemsInCluster 30




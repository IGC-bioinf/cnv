#Path_to="/storage/analysis/oksana_exome/date/reports/" # change date 

IDS, = glob_wildcards("bam/{id}.bam")
BedName = "TSOneExpanded"
BedName = "exome_oksana"

rule all:
    input: expand("ClinCNV/on-target/{id}.cov", id=IDS), expand("ClinCNV/off-target/{id}_off.cov", id=IDS)

rule cov:
        input: "bam/{id}.bam"
        output: "ClinCNV/on-target/{id}.cov"
        shell: "/storage/analysis/progs/ngs-bits/bin/BedCoverage -bam {input} -in ./gc_genes_annotated.150bp_chunks."+BedName+".bed -min_mapq 5 -decimals 4 > {output}"
#        shell: "/storage/analysis/progs/ngs-bits/bin/BedCoverage -bam {input} -in ./gc_genes_annotated.150bp_chunks."+BedName+".S.bed -min_mapq 5 -decimals 4 > {output}"

rule cov_off:
        input: "bam/{id}.bam"
        output: "ClinCNV/off-target/{id}_off.cov"
        shell: "/storage/analysis/progs/ngs-bits/bin/BedCoverage -bam {input} -in ./offtarget_chunks."+BedName+".bed -min_mapq 5 -decimals 4 > {output}"
#        shell: "/storage/analysis/progs/ngs-bits/bin/BedCoverage -bam {input} -in ./offtarget_chunks."+BedName+".S.bed -min_mapq 5 -decimals 4 > {output}"


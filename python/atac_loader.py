import os
from pybedtools import BedTool

ATAC_peaks_regions  = BedTool('../islet_ATAC_peaks/GSE76268_RAW/GSM1978246_ACFQ363beta2_summits.bed.gz')
ATAC_peaks_regions = ATAC_peaks_regions.sequence(fi=os.path.expanduser('~/Desktop/genomes/hg19/chr1.fa.gz.bgz'))

print open(ATAC_peaks_regions.seqfn, "r").read()[0]

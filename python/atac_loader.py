import os
from pybedtools import BedTool
from pyfaidx import Fasta
import ggplot as gg
import pandas as pd

ATAC_peaks_regions  = BedTool('../islet_ATAC_peaks/GSE76268_RAW/GSM1978246_ACFQ363beta2_.bed.gz')

genome = Fasta(os.path.expanduser('~/Desktop/genomes/hg19/chr1.fa.gz.bgz'))
print genome.get_seq( 'chr1',
                      int(ATAC_peaks_regions[100][1]),
                      int(ATAC_peaks_regions[100][2]) )

ATAC_peaks_regions_pd = pd.DataFrame(columns = ["start", "end"],
                                     index = [i[0] for i in ATAC_peaks_regions])

ATAC_peaks_regions_pd["start"] = [int(i[1]) for i in ATAC_peaks_regions]
ATAC_peaks_regions_pd["end"]   = [int(i[2]) for i in ATAC_peaks_regions]
ATAC_peaks_regions_pd["length"]  = ATAC_peaks_regions_pd["start"]-ATAC_peaks_regions_pd["end"]
ATAC_peaks_regions_pd.head()
p = gg.ggplot(data = ATAC_peaks_regions_pd, aesthetics=gg.aes(x="start", y="length")) + gg.geom_point()
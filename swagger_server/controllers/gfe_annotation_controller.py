from Bio import SeqIO
from BioSQL import BioSeqDatabase
from seqann.sequence_annotation import BioSeqAnn
from pygfe.pygfe import pyGFE
from seqann.gfe import GFE


def gfeAnnotation_post(sequence, locus, gene):
    kir = gene
    sequence = sequence['sequence']
    server = BioSeqDatabase.open_database(driver="pymysql", user="root",
                                          passwd="my-secret-pw", host="0.0.0.0",
                                          db="bioseqdb", port=3306)
    gfe = GFE()
    if kir:
        seqann = BioSeqAnn(server=server, kir=kir)
    else:
        seqann = BioSeqAnn(server=server)
    annotation = seqann.annotate(sequence, locus)
    return {
        'annotation': annotation
    }

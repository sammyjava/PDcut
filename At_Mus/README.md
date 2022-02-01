## OrthoFinder run on mouse Cilia proteins and Arabidopsis

This directory contains OrthoFinder orthogroups containing orthologous mouse and Arabidopsis proteins where the mouse protein list was 
provided by Mathieu in the file `Cilia_proteome.xlsx` on the sciebo share.

The output orthogroups mostly have 0 At proteins or 0 mouse proteins. The `-nonzero` suffix is on files that contain only orthgroups with at least 
1 At and 1 mouse protein.

- `Orthogroups.GeneCount-nonzero.tsv` contains the gene counts
- `Orthogroups-nonzero.tsv` contains the actual orthogroups

Note that the EMBL gene identifiers are used for the mouse genes. I used a lookup Python routine `ensemble-fasta.py` to query EMBL for the ID
corresponding to a given UniProt identifier, and then queried the protein FASTA for that EMBL ID.

If you'd like to look up a mouse gene from the EMBL ID, simply enter it at the top of [https://www.ebi.ac.uk/](url). For example, if you enter ENSMUSP00000100033.2,
you'll find that that mouse gene is H4c4, UniProt P62806.

There are 927 orthogroups containing the Cilia_proteome genes for mouse.

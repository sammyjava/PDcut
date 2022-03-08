# PDcut routines

## reformat-pho
This routine reformats the orthogroups in the `N0.tsv` file into a tab-delimited row format with only protein names.
For example, if you ran OrthoFinder in the At_Mus directory (containing the FASTAs), you'll get the following file:
```
At_Mus/OrthoFinder/Results_Feb01/Phylogenetic_Hierarchical_Orthogroups/N0.tsv
```
In this case, run reformat-pho as follows:
```
$ cd At_Mus/OrthoFinder/Results_Feb01/
$ ../../../reformat-pho > pho.tsv
```
This will create a file `pho.tsv` which contains the orthogroup identifiers, e.g.
```
HOG     OG      Gene Tree Parent Clade  Arabidopsis_thaliana.TAIR10.pep.all     Mus_musculus-Cilia_proteome
N0.HOG0000000   OG0000000       n0      AT5G09950.2     AT5G09950.3     AT5G09950.1     AT4G33170.1     AT1G16480.1 ...
```
Note that the top lines of this file are *very long* because they contain large At orthogroups. Groups that contain Mus genes are further down in the file.

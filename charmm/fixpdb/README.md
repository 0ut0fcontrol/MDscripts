# fixpdb
A script to fix PDB format to CHARMM input format.
see [A Beginner's Guide to CHARMM](../ref/A_Beginner_s_Guide_to_CHARMM.pdf)

example:        
    ```
        gawk -f fixpdb.awk segid=prot chainID=A <2ARC.pdb >protein.pdb
    ```

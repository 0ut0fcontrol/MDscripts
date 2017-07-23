# this script need gawk to run
BEGIN {FIELDWIDTHS=" 6 5 1 4 1 3 1 1 4 1 3 8 8 8 6 6 6 4 2 2"}
{
	if ($1 == "HEADER")
		print "REMARK" substr($0, 7, 69)
	if ($1 != "ATOM  " && $1 != "HETATM") # Note, two spaces after ATOM
		endif
	else if ($5 != " " && $5 != "A")
		endif
	else if ($6 == resname || $8 == chainID || ($8 == " " && $1 != "HETATM"))
	{
	#	atomno++
		if ($6 == "HOH")
		{ 	$4 = " OH2"
			$6 = "TIP"
			$7 = "3"
		}
		if ($1 == "HETATM")
			$1 = "ATOM  " # Two spaces after ATOM
		if ($6 == "HIS")
			$6 = "HSD"
		if ($6 == "ILE" && $4 == " CD1")
			$4 = " CD "
		if ($4 == " OXT" || $4 == "OCT1")
			$4 = " OT1"
		if ($4 == "OCT2")
			$4 = " OT2"
		printf "%6s",$1
		printf "%5d", atomno
		printf "%1s", " "
		printf "%4s", $4
		printf "%1s", " "
		printf "%3s", $6
		printf "%1s", $7
		printf "%1s", " "
		printf "%4s", $9
		printf "%4s", "    " # Four spaces
		printf "%8s", $12
		printf "%8s", $13
		printf "%8s", $14
		printf "%6s", $15
		printf "%6s", $16
		printf "%6s", "      " # Six spaces
		printf "%4s", "    "
                printf "%2s\n", $19
	}
        atomno++
}
END {printf "%3s\n", "END"}

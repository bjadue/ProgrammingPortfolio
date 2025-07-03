#beware of the whatif
#made by Brandon Jadue, in part from
#https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/rename-computer?view=powershell-7.5

Write-Output "PLEASE create a txt file containing the computer names separated by commas: `n[oldcomputer,newcomputer,oldcomputer2,newcomputer2...]`n"
Write-Output "Refer to 'data_example.txt'"

$targetFile = Read-Host "Input the file location for TXT file"
$rawText = Get-Content "$targetFile" -Raw
$entries = $rawText -split ','
for($checkNum=0;$checkNum -le [int]($entries.length - 1);$checkNum++){
	$lessThan16 = $true
	$curEntryLength = [int]($entries[$checkNum].length)
	
	if ($curEntryLength -gt 16){
	$lessThan16 = $false
	Write-Host "WARNING: `n"$entries[$checkNum]"is longer than 16 chars. `nThis can cause issues with Azure AD, SQL, etc.." -ForegroundColor Red
	$16response = Read-Host "Type [n] to cancel this process and close the script, otherwise press enter"
		if($16response = "n"){
			exit 1
		}else{
			Write-Host "Continuing..."
		}
	}
}

$creds = get-credential
$oldcompInt = 0
$newcompInt = 1

for($comp=0;$comp -le [int]($entries.length/2);$comp++){
	$renameParams = @{
	    ComputerName = "$entries["$oldcompInt"]"
	    NewName = "$entries["$newcompInt"]"
	    DomainCredential = $creds
	    Force = $true
	    PassThru = $true
	    Restart = $true
	}
	rename-computer @renameParams
	$oldcompInt++
	$oldcompInt++
	$newcompInt++
	$newcompInt++
}
Write-Output "done. ciao"
exit 0

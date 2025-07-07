#written by Brandon Jadue, in part from
#https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/rename-computer?view=powershell-7.5

$lessThan15 = $true
$15response = "y"
#default variables regarding the target name being above 15 characters
write-output "Please note that target PC must already be added to the domain.`n"
$target = Read-Host "Please enter host name of target PC"
$nombre = Read-Host "Please enter new host name of target PC"

if ($nombre.length -gt 15){
	$lessThan15 = $false
	Write-Host "WARNING: `nNew host name of target PC is longer than 15 characters. This can cause issues with Azure AD, SQL, etc.." -ForegroundColor Red
	$15response = Read-Host "Would you like to continue with the process? (CAN CAUSE ISSUES) [y/n]" -ForegroundColor Yellow
}

if ($15response -eq "n"){
	$nombre = Read-Host "Please enter new host name of target PC [15>= characters]"
}

$creds = get-credential
$renameParams = @{
    ComputerName = "$target"
    NewName = "$nombre"
    DomainCredential = $creds
    Force = $true
    PassThru = $true
    Restart = $true
}
#run cmdlet with the pre-defined parameters
rename-computer @renameParams
exit 0
